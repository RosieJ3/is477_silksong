# Data Dictionary

## Gaia_Single_Match.csv
| Column name | Desc|
| ----| ----|
|source_id | unique identifier for the object in the Gaia Data set|
|ra | The right ascension for each object|
|ra_error | error associated with the right ascension|
|dec| The declination of the object|
|dec_error | error for the declination| 
|source_id| source id for the astrophysical object|
|teff_gspphot| estimated effective temperature from GSP-phot|
|spectraltype_esphs| Estimated stellar type|
|lum_flame| Stellar luminosity in solar luminosities|
|mass_flame| Solar mass of the object|

## gaia_double_stars_nonull.csv & gaia2.csv

| Column name | Desc|
| --------| ----|
|-|index column|
|SOURCE_ID| unique source id|
|ra| right ascension|
|ra_error | right ascension error|
|dec | declination|
|dec_error | declination error|
|period | orbital period of the binary system|
|eccentricity| eccentricity of the binary system (parameter describing difference from circular orbit)
|center_of_mass_velocity| velocity of the system through space|
|temperature_ratio | ration between the two objects in the system|

##  sdss_single.csv & sdss_binary_match.csv

| Column name | Desc|
| --------| ----|
|specObjID| SDSS unique object id|
|z| redshift|
|class | primary spectroscopic classification (galaxy,star,quasar,etc.)|
|subClass| more detailed classification|
|type| photometric type/ morphology|
|ra| right ascension |
|dec| declination|
|dered_u| redshift adjusted u band magnitude|
|dered_g| redshift adjusted g band magnitude|
|dered_r| redshift adjusted r band magnitude|
|dered_i| redshift adjusted i band magnitude|
|dered_z| redshift adjusted z band magnitude|


