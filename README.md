# Breaking News: Gender inequality in the press
A study on how different genders are represented in UK newspapers, in terms of proportions, quote themes and comparison to other countries throughout the years 2015-2020.

## Abstract
Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender diverse individuals' rights and voices have gained awareness and freedom. We want to analyze how this evolution translates in the newspapers, more precisely in the UK. In this project, we aim to study how differently women are represented in English newspapers compared to men, its evolution over the last five years, as well as the representation of gender minorities. The first aspect to consider is the proportion of quotes depending on the gender. Then, we will extract the most popular subjects deoending on genders using a machine learning tool called Empath. Via this analysis we hope to extract some interesting information and raise awareness over women and gender minorities' representation.

## Research questions
- Over time span 2015-2020, which newspapers have the most/least equally distributed author gender?
- How are gender minorities represented in terms of proportions of authors?
- How does the gender proportion in general in the UK compare with the one in the US, India and Nigeria?
- Which subjects are more present in women, men or gender minorities quotations?
- Which subjects have seen their author gender proportion rise the most during the time span 2015-2020?

## Project structure
The file structure is shown below.

    ada_project
    ├── data_preprocessinng.ipynb
    ├── gender_representation.ipynb
    ├── gender_topics.ipynb
    ├── scripts 
    ├── ├── path_defs.py
    ├── ├── newspapers.py
    ├── ├── utility_functions.py
    ├── ├── plots.py
    ├── Quotebank
    ├── Project datasets 
    ├── Filtered data
    ├── Merged data
    ├── Results
    ├── docs
    ├── README.md

Some specifications: 

- Preprocessing of the quotebank data set is done in _data_preprocessing.ipynb_ which should be run first.
- Research questions are tackled in _gender_representation.ipynb_ and _gender_topics.ipynb_. They should be looked over in this order to follow our analysis
- Data folders (_Quotebank_, _Project dataset_, _Filtered data_, _Merged data_, _Results_) are gitignored and have to be downloaded locally from our shared google drive or can be accessed directly with Google Colab.
- The _scripts_ folder provides paths to our datasets, urls for our selected newspapers and commonly used functions.
- The _docs_ folder is used to publish our related [website](https://morwald.github.io/ada_project/).

## Additional dataset
In order to get the gender, nationality and occupation information for each quotation's speaker, we used the speaker_attribute.parquet dataset provided by the teaching staff, and the labels of wikidata speakers. At first we tried to loop over the quotes and for each speaker add the corresponding label, but we found that this method was extremely costly in terms of time. We later found that by using dictionaries we were able to do this operation in a much more efficient way (seconds instead of hours!). Indeed, we created a first dictionary linking the qids present in the speakers attributes dataframe and their corresponding label text, then one dictionary per attribute (gender, nationality and occupation) wich links each speakers qid to the qid of the concerned attribute. Hence we managed to add gender, nationality and occupation information for each quote's author.
 
## Methods
First, we need to reduce the size of the dataset as it is too large to handle for our analysis. We proceed by eliminating rows with a 'None' speaker, and by removing columns 'probas' and 'phase' which are not relevant for us. To do a first exploration, we decided to select only quotes that come from 14 newspapers with th highest circulation in the UK. To do this, we select exclusively the quotes that have the url of one of the newspapers in their url.
 
Next, we want to expand our data and add additional information about our speakers. For this, we need to choose one of the qids for each speaker as most of them have several aliases. We decided to pick the first alias of the list. Since our analysis is mainly based on the gender and most-name are gender-specific, we could assume that all aliases have the same gender and it is sufficient to pick one. We load the speaker data, clean it (by only keeping the columns that interest us and removing None genders) and use it to create dictionaries mapping speaker qid and their attributes. Next we map the cleaned quotation datagram with these dictionaries and add our new columns (gender, nationality and occupation). Finally we do some sanity check to make sure there are no abnormalities left. We then to the full process again for the US, India and Nigeria with 5 newspapers each chosen similarly as for the UK.
 
For the next part, we used some visualisation and statistical tools such as hypothesis testing to ouptut a gender representation depending on time and the different newspapers. To retrieve the most popular subjects for each gender, we used a machine learning tool called **Empath**. It was created by researchers at Stanford University in 2016. It uses a combination of deep learning and crowdsourcing to analyze text over 200 pre-existing categories and output the most probable topics the text is about. Finally, some visualisation and statistical tools were needed again to extract information from the comparison of resulting data.
 

## Update from milestone 2
- More newspapers for the UK and further analysis on the US, India and Nigeria.
- The choice of the machine learning tool **Empath**.
