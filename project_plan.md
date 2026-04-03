project plan

## Overview
In our project, we aim to compare features of single stars vs stars in multiple star systems using features such as age, mass, color, temperature, and location on sky. Researching this question will help us understand any broad trends in how these stellar populations are different (and, if they don't differ significantly, that's important information as well). 

We will be using data from the Gaia mission (https://gea.esac.esa.int/archive/) and the Sloan Digital Sky Survey (https://www.sdss4.org/dr17/data_access/tools/). 

## Team
We plan on alternating modules so that we have an equal share of the work, while we both get to work with both of the data sets we are going to use along with any additional data sets we plan on using in the future. 

Erika will work on
- Data Lifecycle
- Ethical Data handling 
- Data inegration
- Data Cleaning
- Reproducibility and provenance

Rosie will work on 
- Files Storage and organization
- Data collection and aquisition
- Data quality
- Workflow automation and provannce
- Metadata and data documentation

## Research Question
What are the differences between single stars and multiple-star systems in the Milky Way? How do these populations differ in source magnitude and location on sky?

## Datasets
Our first dataset will utilize data from the Gaia mission's Data Release 3. The Gaia mission (https://en.wikipedia.org/wiki/Gaia_(spacecraft)) was a space observatory that gathered data on about 1 billion objects, aiming to create the "largest and most precise 3D space catalog ever made". Analysis on Gaia's data continues, with a Data Release 4 planned for later this year.

Our second dataset will utilize data from the Sloan Digital Sky Survey Data Release 18. SDSS (https://en.wikipedia.org/wiki/Sloan_Digital_Sky_Survey , https://www.sdss.org/dr18/mwm/about/) focuses on spectroscopic data from about 5 million objects, largely at low galactic latitudes.

We will be combining these datasets to compare star features and cross-reference information (for instance, if certain data for a star is not available in Gaia, it might be available in SDSS). Our integration variable will be specific sources (individual stars) that are available in both datasets. Previous work has integrated Gaia and SDSS data (for example: https://iopscience.iop.org/article/10.3847/1538-4365/ab8d27), so we may reference existing methods for cross-matching.

We will limit our dataset to 50,000 observations, ideally 25,000 single stars and 25,000 stars in multiple-star systems.

## Timeline
- 8 March: get some data from each dataset and look at it (informally)
- 10 March: submit project plan 
- 7 April: status report; by this date we will hopefully have gathered our data and collected its metadata, copyright / usage info, etc. possibly also done data cleaning so it’s ready for analysis
- 14 April: roughly half of the required modules finished (first three from each teammate's list of modules to work on); pulled any additional star data if necessary, inspected and cleaned
- 21 April: datasets integrated into one
- 28 April: analysis complete (single vs multiple stars compared)
- 3 May: project finished (writeup complete and submitted)

## Constraints
- Size of data sets (processing challenge)
- Spatial coverage: SDSS is mostly focused on low-latitude galactic objects while Gaia explored the entire sky, so the datasets don’t completely overlap
- We could look at when each data set was first gathered so we can see any temporal differences
- Gaia multiple-star data doesn’t seem to have data on the individual stars like we want (at least the acceleration_astro doesn’t), we may need to look elsewhere in the archive or in SDSS if those stars are present and have data

## Gaps
- Cannot Find Documentation on what datatables exist within SDSS DR18
- We have not yet learned about workflow automation
