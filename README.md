# Pandas-Project

## Hypothesis: La población con más muertes por ataque de tiburón son los surferos australianos.

Steps: 

## 1. Let's look at what data we have (columns and type) and how many data elements (shape)
--> I dropped repeated columns

## 2. Null values. Let's see at column lvek the number of nulls.
--> I dropped last two columns as most of the elements are null. 

## 3. Let's look at data inside the columns we want to use to validate our hypothesis. Country / Activity / Fatal
--> how many different values we have (using set)

## 4. I uniformed Activity column merging categories into 5 broader cats: surfing, swimming, fishing, diving and other 
## 5. I uniformed Fatal into yes/No with no being everything not explicetely recorded as Y
## 6. Filtering new data set with only columns needed to validate hypothesis (Case Number, Country, Year)
## 7. Adding new uniformed columns for activity and is fatal
## 8. Creating new colum concatenating country and activity to isolate Australian surfers
## 9. Retrieveing count of country activity attacks (Using value_counts)

##               AUSTRALIAN SURFERS ARE NOT THE MOST AFFECTED POPULATION BY SHARK ATTACKS (US SURFERS ARE). IF WE ONLY LOOK AT FATAL ATTACKS US SURFERS ARE STILL THE MOST AFFACTED
