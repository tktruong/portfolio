/** Description: An example of SQL queries I write in my work in healthcare.
(Details have been obscured and ids are fake)

PREP:
In this example, stakeholders requested a list of active patients
with DSM diagnoses with psychotic features within past 6 months--something not
clearly defined in the encoding. After obtaining a csv list of qualifying
diagnoses from clinicians, I imported the file into python to parse the data into
ICD10 code to write the temp table.

**/

CREATE TABLE #dx (code varchar(10))
INSERT INTO #dx values ('F20.0')
INSERT INTO #dx values ('F20.1')
INSERT INTO #dx values ('F20.2')
INSERT INTO #dx values ('F20.3')
INSERT INTO #dx values ('F20.5')
INSERT INTO #dx values ('F20.81')
INSERT INTO #dx values ('F20.89')
INSERT INTO #dx values ('F20.9')
INSERT INTO #dx values ('F21')
INSERT INTO #dx values ('F22')
INSERT INTO #dx values ('F23')
INSERT INTO #dx values ('F24')
INSERT INTO #dx values ('F25.0')
INSERT INTO #dx values ('F25.1')
INSERT INTO #dx values ('F25.8')
INSERT INTO #dx values ('F25.9')
INSERT INTO #dx values ('F28')
INSERT INTO #dx values ('F29')
INSERT INTO #dx values ('F30.10')
INSERT INTO #dx values ('F30.11')
INSERT INTO #dx values ('F30.12')
INSERT INTO #dx values ('F30.13')
INSERT INTO #dx values ('F30.2')
INSERT INTO #dx values ('F30.3')
INSERT INTO #dx values ('F30.4')
INSERT INTO #dx values ('F30.8')
INSERT INTO #dx values ('F30.9')
INSERT INTO #dx values ('F31.0')
--there were 212 diagnoses actually but I didn't include them in this example


SELECT
   p.last_name,
   p.first_name,
	 --truncate the MRN to remove leading zeros
   SUBSTRING(pat.med_rec_nbr, PATINDEX('%[^0 ]%', pat.med_rec_nbr + ''), LEN(pat.med_rec_nbr)) AS [med_rec_nbr],
   -- dates are stored as varchars in this database unfortunately
   CONVERT(Date, pp.eff_date, 101) AS 'eff_date', --patient open date
	 pp.program_name, --which behavioral health program does the patient belong to?
	 pp.provider_name, --who is their clinician?
   --string of all Dx codes with psychotic features separated by ,
	 pdx.dx_codes AS 'Dx codes with Psychotic Features',
   --string of all Dx descriptions with psychotic features separated by ;
	 pdx.dx_descriptions AS 'Dx descriptions'
FROM
   patient_provider AS pp
   INNER JOIN
      person AS p
      ON pp.person_id = p.person_id
   INNER JOIN
      patient AS pat
      ON p.person_id = pat.person_id
   INNER JOIN
  	(SELECT pdx1.person_id,
      --combine distinct code rows into one string separated by commas
      (SELECT DISTINCT diagnosis_code_id + ', '
        FROM patient_diagnosis pdx2
        WHERE pdx2.person_id = pdx1.person_id
        -- only use dx from last 6 months
        AND create_timestamp BETWEEN DATEADD(MONTH, -6, GETDATE()) AND GETDATE()
        AND diagnosis_code_id IN (SELECT code FROM #dx)
        FOR XML PATH('') ) AS dx_codes,
        --combine distinct code description rows into one string separated by ;
        -- some descriptions have commas so ; is better
      (SELECT DISTINCT description + '; '
        FROM patient_diagnosis pdx3
        WHERE pdx3.person_id = pdx1.person_id
        AND create_timestamp BETWEEN DATEADD(MONTH, -6, GETDATE()) AND GETDATE()
        AND diagnosis_code_id IN (SELECT code FROM #dx)
        FOR XML PATH('') ) as dx_descriptions
      FROM patient_diagnosis AS pdx1
      WHERE pdx1.diagnosis_code_id IN #dx
      AND pdx1.create_timestamp BETWEEN DATEADD(MONTH, -6, GETDATE()) AND GETDATE()
      GROUP BY person_id) AS pdx
  	  ON p.person_id = pdx.person_id
WHERE
   pp.practice_id = '1111'
   AND patient_status.practice_id = '1111'
   AND pat.practice_id = '1111'
	 -- only include those without an expiration date aka active
   AND pp.exp_date = 0
   -- exclude dummy test patients
   AND p.last_name NOT LIKE 'Testpatient%'
ORDER BY
   pp.program_name DESC;
