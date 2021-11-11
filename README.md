# Analysis of gender representation UK's leading newspapers 
## Project Milestone 2

## Abstract 

Gender representation in most work-related domains has for a long time been largely dominated by men. But as women and gender minorities' rights and voices have gained awareness and freedom in the last decades, we want to analyze how this evolution translates in the newspapers, more precisely in the UK. In this project, we aim to study how differently are women represented in English newspapers compared to men, its evolution over the last five years, as well as the representation of gender minorities. The first aspect to consider is the proportion of quotes written by each gender. Then, we will determine the distribution of genders per subject, which we can find by performing some unsupervised pattern matching to classify the subjects of articles. Via this analysis we hope to extract some interesting information and raise awareness over women and gender minorities' representation.

## Research questions 

- Over time span 2015-2020, which newspapers have the most/least equally distributed author gender?
- How are gender minorities represented in terms of proportions of authors ?
- Which subjects are more present in women/gender minorities quotations?
- Which subjects are more present in men quotations?
- Which subjects have seen their author gender proportion rise the most during the time span 2015-2020?
- How does the gender proportion in general in the UK compare with the one of India (or another country, to be determined) ?

## Additional dataset

 In order to get the gender information for each quotation's speaker, we used the speaker_attribute.parquet dataset provided by the teaching staff, and the labels of wikidata speakers. At first we tried to loop over the quotes and for each speaker add the corresponding label, but we found that this method was extremely costly in terms of time. We later found that by creating dictionaries with all genders we were able to do this operation in a much more efficient way (seconds instead of hours!). We managed to add a gender a nationality information for each quote.
 
 ## Methods
 
 We plan to use an unsupervised pattern matching algorithm in order to classify the subjects of the quotes. We could use term frequency-inverse document frequency (also called tf-idf) in order to represent the quotes in vectorial space, and then apply K-means to this data, with a fixed k corresponding to the number of subjects we plan to have.
 
 ## Proposed timeline
 
 - by November 20th : extract information about distribution of genders for all years, and for each newspaper.
 - by November 30th : test different machine learning algorithm to find the best one and fit it to our model, extract the different categories of our quotes.
 - by December 6th : extract information about gender distribution depending on the subject.
 - by December 12th : compare the information we got until here with another country (India?).
 - by December 17th (Milestone 3) : Fix remaining errors, clean up our analysis and present our findings.
 
 ## Organization within the team
 
 We do most of the work simultaneously as a team but we will try to divide the tasks as following :
 
 - Lorena Egger: Analysis of gender distribution and evolution in our time span, extraction of observed patterns.
 - Marie Knoepfel: Find a machine learning algorithm to classify our quotes and fit it to our model.
 - Moritz Waldleben: interpret information of the model fitting and add a subject information for each quote, analyze distribution of genders regarding that information.
 - Paloma Cito: Comparison with quotes from Indian newspapers, analysis of the differences observed.

