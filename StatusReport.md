# Progress Report




## Project Plan task update
### Rosie
We are slightly behind on our timeline as we only have 2/3 modules done based on our timeline so we will have to increase throughput in the future weeks so that we can catch up to schedule.
### Erika
We have gathered some binary star data but still need to query for single star data.


## Updated Timeline
### Rosie
By 4/21 I will aquire the data from the sdss data release 18 so that we can continue on our steps 
4/21 we will have assessed data quality and have a write up for both datasets 
4/28 will have finished workflow automation 
5/3 will have finished metadata documentation and the write up
### Erika
Same timeline. Once we figure out data acquisition by 4/21 I will use the same process to gather single star data.


## Updates on progress
### Rosie
- Started working on ethical data handling, did not realize it was one of Erika's tasks, so we switched module 2-3 so I will take Ethical Data Handling and Erika will take File Storage and Organization. The potential problems have been identified but not addressed. 

- Data collection and aquisiton has medium progress. We are having some issues collecting the sdss dr18 catalogue  data because there is no singular data set the MilkyWay Mapper (MWM) uses, as it combines several data sets to create the MWM and we cannot determine which data set to aquire to so that we can begin integration.
- Have not begun on Data quality assessment due to the issues with acquisition.

### Erika
-Gaia data has been acquired from the Gaia archive using the following query:
SELECT TOP 25000 * FROM gaiadr3.nss_two_body_orbit
This is simply the top 25000 entries in the Gaia table that deals with orbital solutions for binary star systems (https://gea.esac.esa.int/archive/documentation/GDR3/index.html).
-The file project_code.ipynb shows some basic file processing and saving to csv. This data has been uploaded to the SDSS server so source integration can be done.
-I am trying out queries and learning more about SQL to try to join the datasets. This will be done either through a single query on the SDSS server or through Python code that connects to the server (like the API usage we learned in class).


## Challenges encountered
### Rosie
Mentioned eariler, aquiring the sdss dr18 dataset for the milkyway mapper has been more difficult than expected due to the issues with it being an aggregate over several datasets. We also faced some problems with the skyserver uploads for VOtable file format and had to convert our table into csv so that we could upload it to query against.  
### Erika
Working with Rosie to try to gather SDSS data. Might need to read more about the tables and columns and how the data were gathered. The idea is to use Gaia data on objects' positions in the sky (and associated errors on these locations) to search for SDSS objects in similar positions. I've tried several queries using the WHERE command to accomplish this but have yet to succeed. 
