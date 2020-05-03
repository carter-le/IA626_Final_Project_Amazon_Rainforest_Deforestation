#IA626_Final_Project

# Deforestation and Forest Degradation in the Amazon Rainforest 

## Original Intent 

### Summary:

For this project I plan on focusing on the Amazon Rainforest. Deforestation in the Amazon is understood to have many negative short and long-term consequence. Through this project I would like to explore what data can tell us about the causes and consequences of continued deforestation and forest degradation in the Amazon. I was referred by my professor to a dataset, listed below as my primary dataset, which shows parcels of land which have been deforested. The dataset spans from 2000 to 2018. I will look at this in conjunction with datasets on the yearly fires in the Amazon Rainforest and the air quality in the region. I have not yet identified the datasets which will be optimal for this analysis for air quality, but NASA has several to choose from. For the fire data I will be using NASA’s FIRMS system data. Any past data exceeding 7 days needs to be requested, so I will make that a priority at the start of my work on this project.  



#### Datasets:

I plan on using the following dataset to make my analysis (subject to change):

- PRIMARY DATASET SOURCE: https://data.globalforestwatch.org/datasets/4160f715e12d46a98c989bdbe7e5f4d6_1/data?geometry=-61.961%2C-4.916%2C-61.613%2C-4.796&orderBy=pathrow&orderByAsc=false&selectedAttribute=shape_Area
- Dataset with data on Amazon fires: https://firms.modaps.eosdis.nasa.gov/ (NASA FIRMS system)
- NASA has several datasets related to air quality (undecided on which will be best for my analysis) 



## Gathering the data:

#### Dataset 1: PRODES Deforestation Data 

The first dataset I downloaded from Global Forest Watch and can be found 

[here]: **https://data.globalforestwatch.org/datasets/4160f715e12d46a98c989bdbe7e5f4d6_1/data?geometry=-88.744%2C-11.717%2C-33.241%2C3.579&amp;selectedAttribute=shape_Area**

According to the description of the dataset "the PRODES project monitors clear cut deforestation in the Brazilian Legal Amazon... PRODES is operated by the National Institute of Space Research (INPE) in collaboration with the Ministry of the Environment (MMA) and the Brazilian Institute of Environment and Renewable Natural Resources (IBAMA)."

The dataset shows annual deforestation in the Brazilian Legal Amazon between 2000 and 2015 (not 2018 as I had originally thought). The following are the headers and some sample data for the dataset: 

| objectid | class_name | ano  | pathrow | uf   | areameters | gfwid | globalid                               | shape_Length | shape_Area |
| -------- | ---------- | ---- | ------- | ---- | ---------- | ----- | -------------------------------------- | ------------ | ---------- |
| 1075245  | d2004_0    | 2004 | 267     | AC   | 21601.94   |       | {368D5172-0EE3-4660-8C6C-04F4C13A7995} | 732.6464     | 22365.22   |
| 1075246  | d2001_0    | 2001 | 22971   | MT   | 7180.136   |       | {7DE155E4-FE77-44A9-AB39-C5F7B10757D1} | 373.6052     | 7770.565   |
| 1075247  | d2002_0    | 2002 | 465     | AM   | 25206.52   |       | {E00B3ED7-144C-4611-8D05-A16311571CBF} | 727.397      | 25720.18   |
| 1075248  | d2013_0    | 2013 | 466     | AC   | 99922.59   |       | {C7EBA49B-433A-4E02-98EA-B5170C0C1B7E} | 2068.505     | 102586.6   |
| 1075249  | d2003_0    | 2003 | 466     | AC   | 18006.24   |       | {05C0B8F9-59B7-4419-ABB8-DE824FF91A48} | 608.5983     | 18495.04   |
| 1075250  | d2004_0    | 2004 | 167     | AC   | 43199.91   |       | {9C769F49-698F-46F1-A9D3-EC1CB44A1719} | 1222.18      | 44811.23   |
| 1075251  | d2003_0    | 2003 | 23065   | AM   | 75478.89   |       | {7F9332AC-60DD-4E1B-A0E0-3B7A3528ACC8} | 1454.777     | 77243.54   |

One of the issues I faced was the decision about what pieces of data to use and how to use them. There was no description of the attributes and what each of the columns were, specifically. This forced me to make some inferenced. It was clear that "ano" was the year based on the sample data. I then looked at "areameters", "shape_Length", and "shape_Area". I wanted to add up the total area so "areameters " and "shape_Area" both looked like they could be what I needed. Based on the sample data I could see that "areameters" and "shape_Area" were very similar but not the same. I ultimately decided to use "areameters" because the description made it clear that the data was are in meters. I felt more comfortable using this data as there was no indicator what unit of measurement "shape_Area" used. 

After having made this decision I wrote a script which would give me the total area lost per year and also the number of pieces of area lost per year. 

```python
n = 0 
totalpieceslostperyr = {}
totalsqmeterslostperyr = {}
for row in reader:
    if n > 0:
        date = row[2]
        if date in totalpieceslostperyr.keys():
            totalpieceslostperyr[date] += 1 
        else:
            totalpieceslostperyr[date] = 1 
```

The dictionary totalpieceslostperyr takes the year as a key and the value is a tally of all the pieces which have been recorded as being deforested. 

```python
        if date in totalsqmeterslostperyr.keys():
            totalsqmeterslostperyr[date] += round(float(row[5]), 0)
        else:
            totalsqmeterslostperyr[date] = round(float(row[5]),0)
    n += 1
```

The dictionary totalsqmeterslostperyr takes the year as a key and sums the total area of all the pieces which have been recorded as being deforested. 



This is a table with the results:

| Year | Total area lost (sq meters) | Total area lost (sq kilometers) | Number areas lost |
| ---- | --------------------------- | ------------------------------- | ----------------- |
| 2001 | 19488109792                 | 19488                           | 121296            |
| 2002 | 24614670605                 | 24615                           | 102037            |
| 2003 | 26103389495                 | 26103                           | 137438            |
| 2004 | 26823529075                 | 26824                           | 142009            |
| 2005 | 23664952662                 | 23665                           | 117853            |
| 2006 | 10838224777                 | 10838                           | 51234             |
| 2007 | 11448864447                 | 11449                           | 54122             |
| 2008 | 13291954529                 | 13292                           | 105167            |
| 2009 | 6565383254                  | 6565                            | 57454             |
| 2010 | 6314796051                  | 6315                            | 62254             |
| 2011 | 5699784508                  | 5700                            | 61359             |
| 2012 | 4433081757                  | 4433                            | 34999             |
| 2013 | 5385598445                  | 5386                            | 40505             |
| 2014 | 4424619910                  | 4425                            | 34109             |
| 2015 | 5266362609                  | 5266                            | 37214             |

```
# Bar chart
{{Bar-Chart}}
- a:1
- b:2
- c: 3
- a:1
- b:2
- c: 3
```