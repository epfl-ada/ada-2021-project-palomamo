---
layout: post
title:  "Our data story"
date:   2021-12-03 16:46:57 +0100
categories: jekyll update
---

# Gender representation in the press
"A study on how different genders are represented in newspapers, in terms of proportions, quote themes and comparison between English-speaking countries throughout the years 2015-2020."

Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender minorities' rights and voices have gained awareness and freedom. How does this evolution translates in the newspapers? How differently women and gender minorities are represented in English newspapers compared to men?

This exploration has been conducted using the Quotebank dataset (add link), a corpus of speaker-attributed quotations extratced from millions of English news articles.


## Gender distribution

### Distribution of genders in the most read newspapers in the United Kingdom

In the United Kingdom, the population consists of about 49% of women and 51% of men. But this equality is not as well represented in most newspapers. With a selection of 14 newspapers, each dealing with different themes, a significant disparity in the genres of authors can be seen without exceptions. Women are underrepresented.

{% include fig_counts_uk_2019.html %} ((From a newspaper like the Daily Telegraph with the most data collected to the Times, the inequality holds.))

{fig no occurence} ((When taking into the impact of a quote, i.e the numbers of citation of this quotes in numerous newspapers, the gap even seems to grow. (to check with plot))

{% include fig_perc_female_uk.html %} ((This disparity remains more or less constant throughout the 5 years span with an average between … and …., ))

(After computing the mean for each journal) Women are best represented  in The Sun or Metro which are both considered as tabloid. 

In the end, men still represent the majority in any news type from the finance to the tabloids.


### Detailed view on gender minorities

But Women are not the only gender underrepresented. The Quotebank also represent gender minorities as non-binary, transgender or genderfluid individual. Statistics for the representation of those gender minorities are extremely hard to get. They either don’t exist yet or are misled due to a part of the society being still sceptical about the possibility of identified differently than male or female. A survey conducted in 2011 by the Equality and Human Rights Commision estimates that they consist of 2% of the population in the United Kingdom.

{% include fig_counts_other_uk_2019.html %} ((Knowing that these minorities consist of les approximatively 2% of the population, it is more difficult to asses if they are really underrepresented in the press.))

{% include fig_perc_other_uk.html %} ((As for the representation of women throughout the 5 years span, the representation stays constant))

### Comparison with other countries
* Percentages of each gender in UK + other countries (internet source)
* General plot of all newspapers (Q1)
* 


## Topics analysis

We will now analyze further the gender distribution in the press by studying the distribution of genders based on the topics describing each quotation.
We will focus solely on the UK newspapers for this analysis.
In order to extract these topics, we used  [Empath](https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf), a tool created by researchers at Stanford University. This tool uses a combination of deep learning and crowdsourcing to analyze text over 200 pre-existing categories, and lets us easily add new categories. 

To see which subjects are most popular, only the 10 most popular topics for each gender are kept.
{% include distribution_allyears.html %}

A better undestanding of the trending topics can be achieved with this cloud visualization : 
![Word cloud](/docs/_includes/word_cloud.png)

It is clear that the most popular topics are highly similar between the genders, but the relative importance is different : the highest scored topic for men is business, while for women it is positive emotion and for the gender minorities it is optimism. 
This result is in line with the fact (TODO other word) that in our society, there is a pressure on women to perform a certain likability and to come accross as nice and non-aggressive, while men do not undergo the same social phenomenon and tend be more direct in their speech.

Trending topics are obviously not the same throughout the years, as external events happen the topics covered in the press constantly evolve. Here is a graph depicting the evolution of the most trending topics by gender : 
{% include evolution_male.html %}
{% include evolution_female.html %}
{% include evolution_diverse.html %}

For men, there was no significant evolution, all trending topics stay at a similar level of relevance throughout the years.
For women, it appears that ‘business’ and ‘negative emotion’ are the topics that had the most positive evolution.  In general we see an evolution in all topics, which could be explained by the fact that more women write and are cited in the press now compared to a few years ago.
For gender-diverse, we get some odd shapes which can be explained by our lack of data as there are very few (#number) gender-diverse authors of quotes.


A topic that has had a lot of press in the previous years is the #metoo movement.  This movement is “a social movement against sexual abuse and sexual harassment where people publicize allegations of sex crimes” (Wikipedia). 
This movement first started in 2005 at a small scale, then following the widespread sexual-abuse allegations against Harvey Weinstein in 2017, the hashtag exploded on social media.  
A further analysis on the data shows the following evolution of the #metoo topic throughout the years :

PLOT 


- Most cited quote 2020 minorities/women/men (if interesting)
- Other easy to show interesting feature we found
- me too, short analysis

## Conclusion
- summary of obvious facts and if our analysis was meaningful
- our conclusion on women in minorities in the press
