# Analysis of gender representation in UK's leading newspapers 
## Project Milestone 2

## Abstract
Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender minorities' rights and voices have gained awareness and freedom. We want to analyze how this evolution translates in the newspapers, more precisely in the UK. In this project, we aim to study how differently women are represented in English newspapers compared to men, its evolution over the last five years, as well as the representation of gender minorities. The first aspect to consider is the proportion of quotes depending on the gender. Then, we will determine the distribution of genders per subject, which we can find by performing some unsupervised pattern matching to classify the subjects of articles. We will consider other attributes as well, like the occupation. Via this analysis we hope to extract some interesting information and raise awareness over women and gender minorities' representation.

## Research questions
- Over time span 2015-2020, which newspapers have the most/least equally distributed author gender?
- How are gender minorities represented in terms of proportions of authors?
- Which subjects are more present in women/gender minorities quotations?
- Which subjects are more present in men quotations?
- Which subjects have seen their author gender proportion rise the most during the time span 2015-2020?
- How does the gender proportion in general in the UK compare with the one of India (or another country, to be determined)?

## Additional dataset
In order to get the gender, nationality and occupation information for each quotation's speaker, we used the speaker_attribute.parquet dataset provided by the teaching staff, and the labels of wikidata speakers. At first we tried to loop over the quotes and for each speaker add the corresponding label, but we found that this method was extremely costly in terms of time. We later found that by using dictionaries we were able to do this operation in a much more efficient way (seconds instead of hours!). Indeed, we created a first dictionary linking the qids present in the speakers attributes dataframe and their corresponding label text, then one dictionary per attribute (gender, nationality and occupation) wich links each speakers qid to the qid of the concerned attribute. Hence we managed to add gender, nationality and occupation information for each quote's author.
 
## Methods 
First, we need to reduce the size of the dataset as it is too large to handle for our analysis. We proceed by eliminating rows with a 'None' speaker, and by removing columns 'probas' and 'phase' which are not relevant for us. To do a first exploration, we decided to select only quotes that come from the three most popular newspapers in the UK (based on a study in an article). To do this, we select exclusively the quotes that have the url of one of the newspapers in their url.
 
Next, we want to expand our data and add additional information about our speakers. For this, we need to choose one of the qids for each speaker as most of them have several aliases. We decided to pick the first alias of the list, as it the most probable alias for the speaker. We load the speaker data, clean it (by only keeping the columns that interest us and removing None genders) and use it to create dictionaries mapping speaker qid and their attributes. Next we map the cleaned quotation datagram with these dictionaries and add our new columns (gender, nationality and occupation). Finally we do some sanity check to make sure there are no abnormalities left.
 
For the next part, we plan to use an unsupervised pattern matching algorithm in order to classify the subjects of the quotes. We could use term frequency-inverse document frequency (also called tf-idf) in order to represent the quotes in vectorial space, and then apply K-means to this data, with a fixed k corresponding to the number of subjects we plan to have.
 
Finally, we plan on using visualisation and statistical tools to extract information from the comparison of resulting data.
 
## Proposed timeline
- by November 20th : Extract information about distribution of genders for all years, and for more (around 10) newspaper.
- by November 30th : Test different machine learning algorithm to find the best one and fit it to our model, extract the different categories of our quotes.
- by December 6th : Extract information about gender distribution depending on the subject.
- by December 12th : Compare the information we got until here with another country (India?).
- by December 17th (Milestone 3) : Fix remaining errors, clean up our analysis and present our findings.
 
## Organization within the team 
We do most of the work simultaneously as a team but we will try to divide the tasks as following:
 
- Lorena Egger: Analysis of gender distribution and evolution in our time span, extraction of observed patterns.
- Marie Knoepfel: Find a machine learning algorithm to classify our quotes and fit it to our model.
- Moritz Waldleben: Interpret information of the model fitting and add a subject information for each quote, analyze distribution of genders regarding that information.
- Paloma Cito: Comparison with quotes from Indian newspapers, analysis of the differences observed.

--------------------------------------------- MILESTON 3 -----------------------------------------------------
1. Choisir x pays, 10-15 newspapers par pays, et distributions de genres par pays 
2. Refaire datasets pour chaque année, séparés pour chaque pays (2020-uk,2020-us,etc)
3. Voir statistiques de chaque dataset
4. Faire analyses indépendantes des catégories
5. Finaliser algorithme de classification
6. Créer dataset pour train l’algo (random quotes de chaque pays et années)
7. Le train sur un dataset assez grand, décider les catégories finales et les ajouter comme colonne aux dataframes
8. Prédire les catégories avec le model pour tous les autres datasets 
9. Faire analyses par rapport aux catégories
10. Faire le data story final
11. Clean le notebook et tout mettre ensemble
12. Update readme

1. Country choices: 5 countries with a large population and from different continents
https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language
- United States, North america, english as primary language, population: 328,239,523
- United Kingdom, Europe, english as primary language, population: 66,040,229
- Australia, Oceania, english as primary language, population: 25,795,700
- India, Asia, used as lingua franca, mostly and widely spoken, educational, commerce, and government, population: 1,247,540,000
- Nigeria, Africa, english as primary language, used as lingua franca, population:182,202,000

  Newspapers choices: 10-15 per countries with largest circulation
- United States: https://en.wikipedia.org/wiki/List_of_newspapers_in_the_United_States
     USA Today
     The Wall Street Journal
     The New York Times
     New York Post
     Los Angeles Times
     The Washington Post
     Star Tribune
     Newsday
     Chicago Tribune
     The Boston Globe
- United Kingdom: https://en.wikipedia.org/wiki/List_of_newspapers_in_the_United_Kingdom_by_circulation
     Metro
     The Sun
     Daily Mail
     Evening Standard
     Daily Mirror
     The Times
     The Daily Telegraph
     Daily Express
     Daily Star
     i
     Financial Times
     The Guardian
     Daily Record
     City A.M.
- Australia: https://en.wikipedia.org/wiki/List_of_newspapers_in_Australia_by_circulation
     The Australian Financial Review
     The Australian
     The Canberra Times
     Daily Telegraph
     The Sydney Morning Herald
     Northern Territory News
     The Courier-Mail
     The Advertiser
     The Mercury
     The Age
     Herald Sun
     The West Australian
- India: https://en.wikipedia.org/wiki/List_of_newspapers_in_India_by_circulation (only in english)
     The Times of India
     The Hindu
     Hindustan Times
     The Economic Times
     The Telegraph
- Nigeria: https://answersafrica.com/top-10-nigerian-newspapers-most-read-online.html
     Vanguard
     The Punch
     The Nation online
     Sahara Reporters
     Sun News
     THISDAY
     Nigeria Tribune
     The Guardian
     National Mirror
     Leadership
     
     
     
