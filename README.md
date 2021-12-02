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

## Project Milestone 3

## Guideline
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

## 1. 
### Country choices: 5 countries with a large population and from different continents
https://en.wikipedia.org/wiki/List_of_countries_and_territories_where_English_is_an_official_language
- United States, North america, english as primary language, population: 328,239,523
- United Kingdom, Europe, english as primary language, population: 66,040,229
- Australia, Oceania, english as primary language, population: 25,795,700
- India, Asia, used as lingua franca, mostly and widely spoken, educational, commerce, and government, population: 1,247,540,000
- Nigeria, Africa, english as primary language, used as lingua franca, population:182,202,000

### Newspapers choices: 10-15 per countries with largest circulation
- United States: https://en.wikipedia.org/wiki/List_of_newspapers_in_the_United_States
     - USA Today, https://www.usatoday.com
     - The Wall Street Journal, https://www.wsj.com
     - The New York Times, https://www.nytimes.com
     - New York Post, https://nypost.com
     - Los Angeles Times, https://www.latimes.com
     - The Washington Post, https://www.washingtonpost.com
     - Star Tribune, https://www.startribune.com
     - Newsday, https://www.newsday.com
     - Chicago Tribune, https://www.chicagotribune.com
     - The Boston Globe, https://www.bostonglobe.com
- United Kingdom: https://en.wikipedia.org/wiki/List_of_newspapers_in_the_United_Kingdom_by_circulation
     - Metro, https://metro.co.uk
     - The Sun, https://www.thesun.co.uk
     - Daily Mail, https://www.dailymail.co.uk
     - Evening Standard, https://www.standard.co.uk
     - Daily Mirror, https://www.mirror.co.uk
     - The Times, https://www.thetimes.co.uk
     - The Daily Telegraph, https://www.telegraph.co.uk
     - Daily Express, https://www.express.co.uk
     - Daily Star, https://www.dailystar.co.uk
     - i, https://inews.co.uk
     - Financial Times, https://www.ft.com
     - The Guardian, https://www.theguardian.com
     - Daily Record, https://www.dailyrecord.co.uk
     - City A.M., https://www.cityam.com
- Australia: https://en.wikipedia.org/wiki/List_of_newspapers_in_Australia_by_circulation
     - The Australian Financial Review, https://www.afr.com
     - The Australian, https://www.theaustralian.com.au
     - The Canberra Times, https://www.canberratimes.com.au
     - Daily Telegraph, https://www.dailytelegraph.com.au
     - The Sydney Morning Herald, https://www.smh.com.au
     - Northern Territory News, https://www.ntnews.com.au
     - The Courier-Mail, https://www.couriermail.com.au
     - The Advertiser, https://www.adelaidenow.com.au
     - The Mercury, https://www.themercury.com.au
     - The Age, https://www.theage.com.au
     - Herald Sun, https://www.heraldsun.com.au
     - The West Australian, https://thewest.com.au
- India: https://en.wikipedia.org/wiki/List_of_newspapers_in_India_by_circulation (only in english)
     - The Times of India, https://timesofindia.indiatimes.com
     - The Hindu, https://www.thehindu.com
     - Hindustan Times, https://www.hindustantimes.com
     - The Economic Times, https://economictimes.indiatimes.com
     - The Telegraph, https://www.telegraphindia.com
- Nigeria: https://answersafrica.com/top-10-nigerian-newspapers-most-read-online.html
     - Vanguard, https://www.vanguardngr.com
     - The Punch, https://punchng.com
     - The Nation online, https://thenationonlineng.net
     - Sahara Reporters, http://saharareporters.com
     - Sun News, https://www.sunnewsonline.com
     - THISDAY, https://www.thisdaylive.com
     - Nigeria Tribune, https://tribuneonlineng.com
     - The Guardian, https://guardian.ng
     - National Mirror, https://www.latestnigeriannews.com
     - Leadership, https://leadership.ng/nga/
     
     
     
