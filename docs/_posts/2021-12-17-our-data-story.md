---
layout: post
title:  "Breaking News : Gender Inequality in the Press"
date:   2021-12-17 16:46:57 +0100
categories: jekyll update
---

"A study on how different genders are represented in newspapers, in terms of proportions, quote themes and comparison between English-speaking countries throughout the years 2015-2020."

Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender minorities' rights and voices have gained awareness and freedom. How does this evolution translate in the newspapers? How differently women and gender minorities are represented in English newspapers compared to men?

This exploration has been conducted using the Quotebank dataset (add link), a corpus of speaker-attributed quotations extracted from millions of English news articles from the web between AUgust 2008 and April 2020. In order to get more information on authors of the quotations, a Wikidata set of speaker attributes (addlink) was used.

## Gender Representation

### Distribution of genders in the most read newspapers in the United Kingdom

In the United Kingdom, the population consists of about 49% of women and 51% of men. But this equality is not as well represented in most newspapers. With a selection of 14 newspapers, each dealing with different themes, a significant disparity in the genres of authors can be seen without exceptions. Women are underrepresented.

{% include fig_counts_uk_2019.html %} 
_The equality of men and women in the population is not represented. The difference holds for any newspaper from the tabloids to more serious daily journals._


{% include fig_perc_female_uk.html %} 

{% include fig_perc_female_uk.html %}
_This disparity remains more or less constant throughout the 5-year span with an average between … and ….. Females are best represented in **Daily Mail** and **Daily Star** which are both tabloid newspapers._

 Overall it is difficult to establish a link between certain types of newspapers and how they represent women. There seems to be a general state of mind of the publisher in each journal which is not necessarily related to their content.



### Detailed view on gender minorities

But Women are not the only gender underrepresented. The Quotebank also represent gender minorities as non-binary, transgender or genderfluid individuals. Statistics for the representation of those gender minorities are extremely hard to get. They either don’t exist yet or are misled due to a part of the society being still sceptical about the possibility of identify differently than male or female. A survey conducted in 2011 by the Equality and Human Rights Commission estimates that they consist between “0.1-2% [of the general population] depending on the inclusion criteria and geographic location."
https://doi.org/10.1016/j.ecl.2019.01.001

{% include fig_counts_other_uk_2019.html %} ((Knowing that these minorities consist of approximatively 2% of the population, it is more difficult to assess if they are really underrepresented in the press.))

{% include fig_perc_other_uk.html %} ((As for the representation of women throughout the 5 years span, the representation stays constant))



We don't know if gender minorities are underrepresented. the percentage fluctuates from 0.05 -0.8 % which corresponds their distrubution in the population (See section ... in the data_preprocessing notebook.).


In the end, men still represent the majority in any news type from the finance to the tabloids.


### Comparison with other countries
* Percentages of each gender in UK + other countries (internet source)
* General plot of all newspapers (Q1)
* 


## Topics analysis
In order to further analyze the gender distribution in the press, it is interesting to study the distribution of genders based on the topics they talk about the most. The focus is solely on the UK newspapers for this more in depth analysis.
To perform topic analysis, we used  [Empath](https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf), a tool created by researchers at Stanford University in 2016. It uses a combination of deep learning and crowdsourcing to analyze text over 200 pre-existing categories and output the most probable topics the text is about.


*What is the distribution of genders in topics? *

TODO : Include pie charts

In the following analysis we will keep in mind that the male gender is overly represented, hence the topic analysis will be more precise. In the contrary, gender-diverse numbers are almost none, which will have as consequence that our analysis for this gender cannot be extended to other cases. 

*What does each gender talk about?*
TODO : Most cited quote 2019 minorities/women/men

10 most popular topics per gender : 

<img src=”/docs/_includes/word_cloud.png”>

Most popular topics are highly similar between genders, but the relative importance is different : the highest topic score for men is **business**, while for women it is **positive emotion** and for gender-diverse individuals it is **optimism**. 
This result is in line with the tendency of our society to put pressure on women to be **likeable** and come across as nice and non-aggressive, while men do not undergo the same social phenomenon and tend to be more **direct** in their speech.
Concerning gender-diverse individuals, we can notice the predominance of an **emotional** lexical, tending to show that they talk more about personal experiences than facts on general news.

*What’s the evolution of topics per gender throughout the past 5 years ?*

{% include evolution_male.html %}
TODO : Male analysis
For men, there was no significant evolution, all trending topics stay at a similar level of relevance throughout the years.

{% include evolution_female.html %}
TODO : Female analysis
For women, it appears that ‘business’ and ‘negative emotion’ are the topics that had the most positive evolution.  In general we see an evolution in all topics, which could be explained by the fact that more women write and are cited in the press now compared to a few years ago.

{% include evolution_diverse.html %}
TODO : Gender-diverse analysis
For gender-diverse, we get some odd shapes which can be explained by our lack of data as there are very few (#number) gender-diverse authors of quotes.


## Conclusion
- summary of obvious facts and if our analysis was meaningful
- our conclusion on women in minorities in the press



## Lexicon

[**Non-binary** or **genderqueer** people](https://en.wikipedia.org/wiki/Non-binary_gender)  may identify themselves as an intermediate or third gender that is neither male nor female. 
[**Transgender male**](https://en.wikipedia.org/wiki/Trans_man) is a man who was assigned female at birth.
[**Transgender female**](https://en.wikipedia.org/wiki/Trans_woman) is a woman who was assigned male at birth. 
[**Genderfluid** people](https://en.wikipedia.org/wiki/Non-binary_gender) often express a desire to remain flexible about their gender identity rather than committing to a single definition.
[**Intersex** people](https://en.wikipedia.org/wiki/Intersex) are individuals born with any of several sex characteristics that, according to the Office of the United Nations High Commissioner for Human Rights, “do not fit typical binary notions of male or female bodies”.
[**Cisgender** people](https://en.wikipedia.org/wiki/Cisgender) have the same gender identity as their sex assigned at birth. 
