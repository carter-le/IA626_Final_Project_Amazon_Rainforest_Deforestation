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

The first dataset I downloaded from Global Forest Watch and can be found here:

https://data.globalforestwatch.org/datasets/4160f715e12d46a98c989bdbe7e5f4d6_1/data?geometry=-88.744%2C-11.717%2C-33.241%2C3.579&amp;selectedAttribute=shape_Area

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



![geojson](/images/deforestation_per_year.JPG)


We see here that the number of pieces of land lost to deforestation follows the total area lost. 
![geojson](images/area_vs_number_areas.JPG)

Those times where the relative number of pieces of area lost is greater than the relative total area lost could indicate there is a greater number of smaller pieces of land being deforested as opposed to large areas being clear cut by large operations. To know this it would be helpful to have further information, namely, more information on how pieces of land are broken up and classified. This is important because there is big difference between small-scale cutting and large-scale clear cutting. Dealing with sustenance farmers and dealing with plantation farmers require different information, public policy, and enforcement of legislature. 



#### Dataset 2: FIRMS Data

The second dataset is historical data from NASA's active fire map and can be found here:

https://firms.modaps.eosdis.nasa.gov/

According to NASA "The Fire Information for Resource Management System (FIRMS) distributes Near Real-Time (NRT) active fire data within 3 hours of satellite observation from both the Moderate Resolution Imaging Spectroradiometer (MODIS) and the Visible Infrared Imaging Radiometer Suite (VIIRS)." This data is stored in archive and can be requested. 

At first this seemed like it would be a simple process, but the Brazilian Legal Amazon is not listed as a country on the FIRMS request for (because it is not a country, but a region - part of a country). There is an option to request data for a custom region. This custom region needs to be a polygon formatted in Well Known Text (WKT). 

To create a custom region of the Brazilian Legal Amazon and format it in WKT this we have to follow a few steps:

1. Find a shapefile of the Brazilian Legal Amazon

   A shapefile for the Legal Brazilian Amazon was found at the website of Ambdata, modeling group for biodiversity studies:

   http://www.dpi.inpe.br/Ambdata/unidades_administrativas.php

   The following image is geojson opened with the original shapefile downloaded from the Ambdata website:

![geojson](images/original_shapefile.JPG)

   

2. Reduce the number of coordinates and reformat the data

   The original dataset was large, so it was reduced without sacrificing much precision. The level of accuracy needed was far surpassed by the original data file. 

   The following script takes the original data file and reduces and reformats it: 

   ```python
   import json
   
   with open('LegalAmazonArea.json') as f:
     data = json.load(f)
   
   newMap = {"type":"Polygon","coordinates":[[]]}
   n = 0
   for point in data['features'][0]['geometry']['coordinates'][0][0]:
       if n == 0:
           firstpoint = point
       if n % 10 == 0:
           newMap['coordinates'][0].append(point)
       n+=1 
   newMap['coordinates'][0].append(firstpoint)
   
   with open('reduced_Legal_Amazon.json', 'w') as json_file:
       json.dump(newMap, json_file)
   ```

   To test this code I uploaded the file to geojson. This confirmed that the integrity of the shape had been maintained. The result is shown here in geojson: 

![geojson](images/reduce_reformatted_json.JPG)


3. Take the properly formatted and reduced dataset and convert from json to WKT 

   The following script was written to take the reduced and properly formatted json file ('reduced_Legal_Amazon.json') and output WKT:

   ```python
   import json
   
   with open('reduced_Legal_Amazon.json') as f:
       polygon = json.load(f)
   	
   from geomet import wkt
   
   print(wkt.dumps(polygon, decimals=4))
   ```

   The original dataset was reformatted in step 2 in order to be taken by wkt.dumps (the json dictionary needed to be in the format I set up for newMap).

   

4. Take the polygon in WKT, tweak the formatting manually in Notepad (or any other such application), and insert into the FIRMS request prompt

   The code shown in step 3 will print the needed WKT to the PowerShell. I copied this code into a wordpad document. 

   The following is a sample of what the code will look like:

   ```
   POLYGON ((-73.2101 -9.4058, -73.1911 -9.3673, -73.1077 -9.3079, -73.0925 -9.2620, -73.0226 -9.2263, -73.0161 -9.1844, -72.9461 -9.1077, -72.9488 -9.0260, -72.9667 -8.9795, -73.0206 -8.9128, -73.0825 -8.8405, -73.1305 -8.7703, -73.1757 -8.6884, -73.2481 -8.6860, -73.3025 -8.6304, -73.3419 -8.6161, -73.3291 -8.5029, -73.3729 -8.4670, -73.4221 -8.4074, -73.4843 -8.3908, -73.5278 -8.3566, -73.5366 -8.2777))
   ```

   

   The FIRMS request portal requires there be no spaces after the comma, so I manually completed a find and replace where **Find: ', ' and Replace: ','**

   The following is the result:

   ```wkt
   POLYGON ((-73.2101 -9.4058,-73.1911 -9.3673,-73.1077 -9.3079,-73.0925 -9.2620,-73.0226 -9.2263,-73.0161 -9.1844,-72.9461 -9.1077,-72.9488 -9.0260,-72.9667 -8.9795,-73.0206 -8.9128,-73.0825 -8.8405,-73.1305 -8.7703,-73.1757 -8.6884,-73.2481 -8.6860,-73.3025 -8.6304,-73.3419 -8.6161,-73.3291 -8.5029,-73.3729 -8.4670,-73.4221 -8.4074,-73.4843 -8.3908,-73.5278 -8.3566,-73.5366 -8.2777, -73.2101 -9.4058))
   ```

   This polygon is now ready to be inserted into the FIRMS Download Request:

   ![geojson](images/FIRMS_request.JPG)

   We know the request was successful by clicking on "show map" for your request. Mine looked the same as the geojson of the reduced and reformatted json (refer to step 2). The region on the map is shown here: 

   ![geojson](images/FIRMS_map_of_requested_data.JPG)



After a short waiting period, the data was emailed to me, and I could begin to analyze the data. 

Please note the following acknowledgement and refer to the disclaimer from the data provider:

*We acknowledge the use of data and imagery from LANCE FIRMS operated by NASA's Earth Science Data and Information System (ESDIS) with funding provided by NASA Headquarters.*

Find their disclaimer here: https://earthdata.nasa.gov/earth-observation-data/near-real-time/citation#ed-lance-disclaimer 

The following are the headers and some sample data for the dataset: 

| latitude | longitude | brightness | scan | track | acq_date  | acq_time | satellite | instrument | confidence | version | bright_t31 | frp  | daynight | type |
| -------- | --------- | ---------- | ---- | ----- | --------- | -------- | --------- | ---------- | ---------- | ------- | ---------- | ---- | -------- | ---- |
| -6.307   | -53.2359  | 306.1      | 1.1  | 1     | 7/19/2001 | 208      | Terra     | MODIS      | 67         | 6.2     | 292.9      | 6.9  | N        | 0    |
| -6.6621  | -53.5948  | 301.6      | 1.2  | 1.1   | 7/24/2001 | 226      | Terra     | MODIS      | 42         | 6.2     | 291.1      | 4.9  | N        | 0    |
| -6.5475  | -53.5348  | 305.2      | 1.3  | 1.1   | 7/28/2001 | 201      | Terra     | MODIS      | 63         | 6.2     | 292.9      | 9.7  | N        | 0    |
| -6.5358  | -53.5244  | 316.6      | 1.3  | 1.1   | 7/28/2001 | 201      | Terra     | MODIS      | 93         | 6.2     | 294.3      | 20.9 | N        | 0    |
| -6.5373  | -53.5362  | 316.3      | 1.3  | 1.1   | 7/28/2001 | 201      | Terra     | MODIS      | 93         | 6.2     | 293.4      | 20.5 | N        | 0    |
| -6.5256  | -53.5258  | 315        | 1.3  | 1.1   | 7/28/2001 | 201      | Terra     | MODIS      | 90         | 6.2     | 294        | 18.6 | N        | 0    |
| -6.5271  | -53.5376  | 313.3      | 1.3  | 1.1   | 7/28/2001 | 201      | Terra     | MODIS      | 87         | 6.2     | 293.2      | 16.6 | N        | 0    |

The following is an attribute description list provided:

| Attribute  | Short Description                     | Long Description                                             |
| ---------- | ------------------------------------- | ------------------------------------------------------------ |
| Latitude   | Latitude                              | Center of 1km fire pixel but not necessarily the actual location of the fire as one or more fires can be detected within the 1km pixel. |
| Longitude  | Longitude                             | Center of 1km fire pixel but not necessarily the actual location of the fire as one or more fires can be detected within the 1km pixel. |
| Brightness | Brightness temperature 21 (Kelvin)    | Channel 21/22 brightness temperature of the fire pixel measured in Kelvin. |
| Scan       | Along Scan pixel size                 | The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge of scan. Scan and track reflect actual pixel size. |
| Track      | Along Track pixel size                | The algorithm produces 1km fire pixels but MODIS pixels get bigger toward the edge of scan. Scan and track reflect actual pixel size. |
| Acq_Date   | Acquisition Date                      | Data of MODIS acquisition.                                   |
| Acq_Time   | Acquisition Time                      | Time of acquisition/overpass of the satellite (in UTC).      |
| Satellite  | Satellite                             | A = Aqua and T = Terra.                                      |
| Confidence | Confidence (0-100%)                   | This value is based on a collection of intermediate algorithm quantities used in the detection process. It is intended to help users gauge the quality of individual hotspot/fire pixels. Confidence estimates range between 0 and 100% and are assigned one of the three fire classes (low-confidence fire, nominal-confidence fire, or high-confidence fire). |
| Version    | Version (Collection and source)       | Version identifies the collection (e.g. MODIS Collection 6) and source of data processing: Near Real-Time (NRT suffix added to collection) or Standard Processing (collection only). "6.0NRT" - Collection 6 NRT processing. "6.0" - Collection 6 Standard processing. Find out more on [collections](https://earthdata.nasa.gov/faq/firms-faq#ed-modis-collections) and on the [differences between FIRMS data sourced from LANCE FIRMS and University of Maryland](https://earthdata.nasa.gov/faq/firms-faq#ed-firms-umd). |
| Bright_T31 | Brightness temperature 31 (Kelvin)    | Channel 31 brightness temperature of the fire pixel measured in Kelvin. |
| FRP        | Fire Radiative Power (MW - megawatts) | Depicts the pixel-integrated fire radiative power in MW (megawatts). |
| Type*      | Inferred hot spot type                | 0 = presumed vegetation fire 1 = active volcano 2 = other static land source 3 = offshore |
| DayNight   | Day or Night                          | D= Daytime fire, N= Nighttime fire                           |

I decided that I would only use fires with a confidence of 75% or above, and only look at fires which were Type 0 or 2 ("total") 

I wrote the following script to determine the total fire area for fires with confidence over 75%. I chose to break it down and determine the "vegetation" fire area per year and the "other" fire area per year as well as the total fire area per year. 

```python
import csv, time

start = time.time()
fn = 'fire_archive_M6_118818.csv'
#this was the data file FIRMS sent to me
f = open(fn,"r")
reader = csv.reader(f) 

n = 0
totalfireareaperyr = {}
totalfirevegitation = {}
totalfireotherstatic = {}
for row in reader:
    if n > 0:
        if int(row[9]) > 74:
            if row[14] == "0" or row[14] == "2":
                date = row[5][0:4]
                if date in totalfireareaperyr.keys():
                    totalfireareaperyr[date] += 1
#each row represents 1km area where there is a fire (this is the highest level of granularity that we have)
                else:
                    totalfireareaperyr[date] = 1
            if row[14] == "0":
                if date in totalfirevegitation.keys():
                    totalfirevegitation[date] += 1
                else:
                    totalfirevegitation[date] = 1
            if row[14] == "2":
                if date in totalfireotherstatic.keys():
                    totalfireotherstatic[date] +=1
                else:
                    totalfireotherstatic[date] =1
    n+=1
```

The following table shows the results:

| Year | Total (sq. km) | Vegetation (sq. km) | Other (sq. km) |
| ---- | -------------- | ------------------- | -------------- |
| 2001 | 34970          | 34697               | 273            |
| 2002 | 158984         | 156664              | 2320           |
| 2003 | 164128         | 158711              | 5417           |
| 2004 | 212025         | 202826              | 9199           |
| 2005 | 212748         | 210448              | 2300           |
| 2006 | 129032         | 128192              | 840            |
| 2007 | 213621         | 212274              | 1347           |
| 2008 | 96560          | 96393               | 167            |
| 2009 | 62338          | 62317               | 21             |
| 2010 | 182896         | 182741              | 155            |
| 2011 | 58811          | 58687               | 124            |
| 2012 | 102178         | 101918              | 260            |
| 2013 | 53824          | 53651               | 173            |
| 2014 | 83780          | 83250               | 530            |
| 2015 | 117418         | 116901              | 517            |

The following graph shows that the "other" category is a small portion of the total fire area most of the time: 
![geojson](images/fire_total_veg_other_graph.JPG)

The following is a bar graph of the total fire area (sq. km) per year: 
![geojson](images/fire_area_bar_graph.JPG)

On it's own, this data does not tell us much, other than the fact that some years saw more area affected by fires in the Brazilian Legal Amazon than others. 



## Results

The following table brings together the results of the analysis: 

| Year | Total area deforested (sq meters) | Total area deforested (sq km) | Number areas deforested | Total area lost to fire (sq km) |
| ---- | --------------------------------- | ----------------------------- | ----------------------- | ------------------------------- |
| 2001 | 19488109792                       | 19488                         | 121296                  | 98679                           |
| 2002 | 24614670605                       | 24615                         | 102037                  | 359275                          |
| 2003 | 26103389495                       | 26103                         | 137438                  | 372849                          |
| 2004 | 26823529075                       | 26824                         | 142009                  | 473707                          |
| 2005 | 23664952662                       | 23665                         | 117853                  | 473409                          |
| 2006 | 10838224777                       | 10838                         | 51234                   | 290471                          |
| 2007 | 11448864447                       | 11449                         | 54122                   | 472420                          |
| 2008 | 13291954529                       | 13292                         | 105167                  | 224074                          |
| 2009 | 6565383254                        | 6565                          | 57454                   | 159943                          |
| 2010 | 6314796051                        | 6315                          | 62254                   | 396512                          |
| 2011 | 5699784508                        | 5700                          | 61359                   | 144670                          |
| 2012 | 4433081757                        | 4433                          | 34999                   | 244328                          |
| 2013 | 5385598445                        | 5386                          | 40505                   | 138816                          |
| 2014 | 4424619910                        | 4425                          | 34109                   | 204153                          |
| 2015 | 5266362609                        | 5266                          | 37214                   | 285622                          |

These were unexpected results. The following is a graph of total area deforested and total area lost to fire:

![geojson](images/deforested_vs_fire_graph.JPG)


#### Conclusion 

It was my original thought to use this data to see the percentage of deforestation which was happening on account of fires (as opposed to logging, etc.) - I was not expecting the total square kilometers lost to fires to far exceed the total square kilometers lost to deforestation. 

There are some of the several potential reasons for these results:

- The PRODES data is not actually monitoring the whole Brazilian Legal Amazon and is therefore only representing a subset of what the FIRMS data is representing 
- The same fire is recorded in the same 1 km square more than one time (on another day or another image taken)
- The PRODES data does not look at all burned areas as being deforested ( a vegetation fire does not necessarily mean the forest was clear cut /deforested)

More research would have to be done to determine the reason for the result. Taking a deeper look could prove valuable as the PRODES data is used to make public policy in Brazil regarding deforestation laws and reduction targets. 

Although the data was not what I expected, I learned a lot through this project. In particular, I learned about shapefiles and formatting for geojson and for WKT, and how to write scrips to convert one form to the other. I also reinforced what I head learned from previous class projects about iterating through large datasets to extract information. I considered it to be a valuable project. 

