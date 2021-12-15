---
layout: post
title:  "Our data story"
date:   2021-12-03 16:46:57 +0100
categories: jekyll update
---

# Gender representation in UK newspapers (to update)

## Abstract

Add catchy fact we found here

## Introduction

(to modify) Gender representation in most work-related domains has for a long time been largely dominated by men. But in the last decades, women and gender minorities' rights and voices have gained awareness and freedom. We want to analyze how this evolution translates in the newspapers, more precisely in the UK. In this project, we aim to study how differently women are represented in English newspapers compared to men, its evolution over the last five years, as well as the representation of gender minorities. The first aspect to consider is the proportion of quotes depending on the gender. Then, we will determine the distribution of genders per subject, which we can find by performing some unsupervised pattern matching to classify the subjects of articles. We will consider other attributes as well, like the occupation. Via this analysis we hope to extract some interesting information and raise awareness over women and gender minorities' representation.
+ support, article on data set

## Gender representation
Distribution of genders on most read UK newspapers 
- Percentages of each gender in UK (internet source)

- Most unfair/fair newspaper years distribution difference (Q1)
{% include fig_counts_uk_2019.html %}
{% include fig_counts_other_uk_2019.html %}
- General plot of all newspapers (Q1) {% include fig_perc_female_uk.html %}


Detailed view on gender minorities
{% include fig_perc_other_uk.html %}
- Intro on gender minorities representation in UK (internet source)
- All newspapers percentage of gender minorities authors (Q2)

Comparison with other countries
- Percentages of each gender in UK + other countries (internet source)
- General plot of all newspapers (Q1)

## Topics analysis

We will now analyze further the gender distribution in the press by studying the distribution of genders based on the topics describing each quotation.
We will focus solely on the UK newspapers for this analysis.
In order to extract these topics, we used  [Empath](https://hci.stanford.edu/publications/2016/ethan/empath-chi-2016.pdf), a tool created by researchers at Stanford University. This tool uses a combination of deep learning and crowdsourcing to analyze text over 200 pre-existing categories, and lets us easily add new categories. 

To see which subjects are most popular, we keep only the 10 most popular topics for each gender and year. We get the following distribution for males in 2020 : 
{% include fig_topics_males_2020.html %}
For females : 
{% include fig_topics_females_2020.html %}
And for the gender minorities : 
{% include fig_topics_others_2020.html %}

We see that the most popular topics are highly similar between the genders, but the order is different : the highest scored topic for men is business, while for women it is positive emotion and for the gender minorities it is optimism. 
This result is in line with the fact that in our society, there is a pressure on women to perform a certain likability and to come accross as nice and non-aggressive, while men do not undergo the same thing and can be more direct in their speech.



- Study of subject that gender minorities talk about (Q3)
- Study of subject that women talk about (Q3)
- Study of subject that men talk about (Q3)

- Proportion of gender in most popular topics (emphasis)

- General plot of subject changes through the years for each gender (Q3)

- Most talked about subjects in general (Q4)
- Most cited quote 2020 minorities/women/men (if interesting)
- Other easy to show interesting feature we found
- me too, short analysis

## Conclusion
- summary of obvious facts and if our analysis was meaningful
- our conclusion on women in minorities in the press
