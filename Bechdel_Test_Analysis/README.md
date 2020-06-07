## Bechdel Test Analysis

The Bechdel Test is a concise way to examine how well films represent female characters. In order to pass the test, the film needs to have:

1) At least 2 women with names
2) They talk to each other
3) They talk to each other about something other than a man

Although this is a limiting and imprecise test, it can be shocking what films pass and do not pass the Bechdel Test. For more information: https://bechdeltest.com

As part of a group project for my Python Fundamentals for Data Science course, we sought to analyze Bechdel Test rated films in conjunction with IMDB, box office, and earnings data. I was responsible for extracting the Bechdel Test data via API and cleaning it as well as filtering the large IMDB data files in SQL. I also performed analysis on Bechdel Test ratings for films over the decades and for films of the highest paid actresses of 2017 using pandas.

### Bechdel JSON to CSV

This notebook contains code to convert the JSON from the Bechdel Test rating website into a csv file.

### Bechdel Test Over Decades

This notebook contains an analysis of ratings over the decades. Our theory was that since films are often a reflection of societal norms, we would see an increase in pass ratings in more recent decades compared to early decades. However, due to the nature of the website and the types of users submitting ratings, recent films are overrepresented compared to older films. Thus, our analysis is inconclusive.

### Forbes Highest Paid Actresses

This notebook contains an analysis of Bechdel Test ratings for films that the highest paid actresses were in. Given that these actresses earned the most, we wanted to understand how their movies fared. Again, there were limitations to the analysis because the dataset did not contain all the movies in the actresses' filmography.
