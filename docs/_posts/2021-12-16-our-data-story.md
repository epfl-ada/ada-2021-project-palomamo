---
layout: post
title:  "Breaking News : Gender Inequality in the Press"
date:   2021-12-03 16:46:57 +0100
categories: jekyll update
--- 
_"A study on how different genders are represented in newspapers, in terms of proportions, quote themes and comparison between English-speaking countries throughout the years 2015-2020."_

Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender diverse individuals' rights and voices have gained awareness and freedom. How does this evolution translate in the newspapers? How differently women and gender minorities are represented in English newspapers compared to men?

This exploration has been conducted using the [Quotebank dataset](https://github.com/epfl-dlab/Quotebank), a corpus of speaker-attributed quotations extracted from millions of English news articles from the web between August 2008 and April 2020. In order to get more informations on authors of the quotations, a Wikidata set of speaker attributes (addlink) was used.

## Gender Representation

### Distribution of genders in the most read newspapers in the United Kingdom

In the United Kingdom, the population consists of about 49% of women and 51% of men. But this equality is not as well represented in most newspapers. With a selection of 14 newspapers, each dealing with different themes, a significant disparity in the genres of authors can be seen without exceptions. Women are underrepresented.

{% include counts_male_female_uk_2019.html %} 
_The equality of men and women in the population is not represented. The difference holds for any newspaper from the tabloids to more serious daily journals._

{% include perc_female_uk_allyears.html %}
{% include perc_female_uk_means.html %}
_This disparity remains more or less constant throughout the 5-year span with an average between 13%   and 37%. Females are best represented in **Daily Mail** and **Daily Star** which are both tabloid newspapers._

Overall it is difficult to establish a link between certain types of newspapers and how they represent women. There seems to be a general tendency for the publisher in each journal which is not necessarily related to their content.

*But are women the only gender underrepresented?*


### Detailed view on gender minorities
The Quotebank also represent gender diverse individuals such as non-binary, transgender or genderfluid individuals (see Lexicon for more details)(add link to lexicon if possible). Statistics for the representation of those gender minorities are extremely hard to get. They either don’t exist yet or are misled due to a part of the society being still sceptical about the existence of other genders than cisgender male and female. A survey conducted in 2011 by the Equality and Human Rights Commission estimates that they consist between “0.1-2% [of the general population](https://doi.org/10.1016/j.ecl.2019.01.001) depending on the inclusion criteria and geographic location."


{% include counts_other_uk_2019.html %} 
_Knowing that these minorities consist of a fraction between 0.1% and 2% of the population, it is more difficult to assess if they are really underrepresented in the press. For the selection of newspapers the representation stays constant throughout the 5-year span and the average fluctuates between 0.05 and 0.8% which corresponds to the reality._

*Can these first conclusions be extended to some other countries with a completely different cultural background?*

### Comparison with other countries

The United States, India and Nigeria are all English-speaking countries located on different continents.

{% include perc_female_countries_means.html %}
{% include perc_other_countries_means.html %}

_As before, a time independence is observed and no conclusion can be issued between the gender representation and the types of newspaper. However an interesting new observation can be made. The averages over the 5-year span, let it be for women or gender minorities' representation, differ among countries._

This can be justified by their history and their consideration for women and gender diverse individuals.
Nigeria still does not recognize [LGBT rights](https://en.wikipedia.org/wiki/LGBT_rights_in_Nigeria) and women face numerous [inequalities and difficulties](https://en.wikipedia.org/wiki/Women_in_Nigeria) compared to men. This is well represented here with the lowest proportion of female (<10%) and gender diverse individuals(<0.1%). The disparity becomes even greater than in a European country like the United Kingdom, with an average above 30% for some newspapers,  where people can be seen as more open minded and understanding on the question of gender diversity. That being said, inequalities are still present everywhere. A similar analysis can be made for India where the situation for [women](https://en.wikipedia.org/wiki/Women_in_India) gender diverse individuals can also be full of difficulties and unfairness.

{% include perc_female_countries_allyears.html %}
_A small evolution can be observed only for the United Sates and the United Kingdom._

Finally a certain progression is shown which demonstrate a certain gain in awareness and freedom in women and gender diverse individuals' rights and voices. But this also reveal how slow the process can be depending on the countries and their society as it has been discussed before.

## Topics analysis
In order to further analyze the gender distribution in the press, it is interesting to study the distribution of genders based on the topics they talk about the most. The focus is solely on the UK newspapers for this more in depth analysis.
To perform topic analysis, we used  [Empath](https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf), a tool created by researchers at Stanford University in 2016. It uses a combination of deep learning and crowdsourcing to analyze text over 200 pre-existing categories and output the most probable topics the text is about.


*What is the distribution of genders in topics? *

{% include proportion_gender.html %}


In the following analysis we will keep in mind that the male gender is overly represented, hence the topic analysis will be more precise. In the contrary, gender-diverse numbers are almost none, which will have as consequence that our analysis for this gender cannot be extended to other cases. 

*What does each gender talk about?*

Here are the most cited quote of early 2020 per gender : 

Male : "make it impossible for me to do my job." William Barr, male, 07/02/2020
Female : "work to become financially independent." Duchess of Sussex, female, 08/01/2020
Gender-diverse : "They are standing for us, and I am immensely proud of them," Rose McGowan, non-binary, 05/01/2020

The 10 most popular topics per gender : 

<img src="/docs/imgs/word_cloud.png" alt="">

Most popular topics are highly similar between genders, but the relative importance is different : the highest topic score for men is **business**, while for women it is **positive emotion** and for gender-diverse individuals it is **optimism**. 
This result is in line with the tendency of our society to put pressure on women to be **likeable** and come across as nice and non-aggressive, while men do not undergo the same social phenomenon and tend to be more **direct** in their speech.
Concerning gender-diverse individuals, we can notice the predominance of an **emotional** lexical, tending to show that they talk more about personal experiences than facts on general news.

*What’s the evolution of topics per gender throughout the past 5 years ?*

{% include evolution_male.html %}
Topics percentages are generally constant, with a majority of *positive* sentiments related to *actions* and *achievements*.

{% include evolution_female.html %}
As for men, it is not possible to detect any evolution in women’s topics distribution. The *emotions* lexicon is the prevalent one here with topics related to *family and friends* and *communication*.

{% include evolution_diverse.html %}
The lack of data is the origin of the rougher edges of the graph. However, we can still notice that *negative emotions* are very high in contrast to positive ones which might be a consequence of the fact that [“LGBT respondents are less satisfied with their life than the general UK population (rating satisfaction 6.5 on average out of 10 compared with 7.7). Trans respondents had particularly low scores (around 5.4 out of 10)”](https://www.gov.uk/government/publications/national-lgbt-survey-summary-report/national-lgbt-survey-summary-report), according to an UK survey for the LGBT community in 2007.


## Conclusion

As expected, men still represent the majority of speakers in any type of newspaper. Every country studies display this inequality depending on their cultural background. The developing countries show a more important gap.
However, the time span on which the analysis has been conducted is too short to display a significant progression in the representation of women and gender diverse individuals. To really show how their voices gained awareness, it would have been necessary to use some data over multiple decades. It has been a slow process and 5 years is not sufficient to capture enough important events capable of changing people’s mind. 

(Topics conclusion)
Throughout this analysis, no real evolution was found concerning topics that each gender talked about between 2015 and early 2020. It is however possible to see different lexicons for each gender. Men are in the action and business, women talk about emotions and caring, while gender minorities share their possibly difficult life experiences.

## Limitations

The results we found in this analysis need to be taken with a grain of salt as we encountered a few limitations and had to make some assumptions:

*  The Empath tool we used for topic detection is a tool that was published in 2016 and probably developed before that, so the pre-existing categories might not be completely up to date with our data (especially for years 2017-2020, which could make us miss some newer trending topics.

*  There are very few quotes written by gender minorities, which makes it hard to draw conclusions and extrapolate the results we found for this subgroup of genders.

*  TODO talk about legal rights and how hard it is to be recognized as a gender minority in most countries? (Marie: not sure since we talked about it in the first part no, i linked some articles for india and nigeria)

## Lexicon

-[**Non-binary** or **genderqueer** people](https://en.wikipedia.org/wiki/Non-binary_gender)  may identify themselves as an intermediate or third gender that is neither male nor female. 
- [**Transgender male**](https://en.wikipedia.org/wiki/Trans_man) is a man who was assigned female at birth.
- [**Transgender female**](https://en.wikipedia.org/wiki/Trans_woman) is a woman who was assigned male at birth. 
- [**Genderfluid** people](https://en.wikipedia.org/wiki/Non-binary_gender) often express a desire to remain flexible about their gender identity rather than committing to a single definition.
- [**Intersex** people](https://en.wikipedia.org/wiki/Intersex) are individuals born with any of several sex characteristics that, according to the Office of the United Nations High Commissioner for Human Rights, “do not fit typical binary notions of male or female bodies”.
- [**Cisgender** people](https://en.wikipedia.org/wiki/Cisgender) have the same gender identity as their sex assigned at birth. 


