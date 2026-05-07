import pandas as pd
import numpy as np
from astropy.table import Table

t = Table.read("gaia_again.vot")
t_df = t.to_pandas()
t_df2 = t_df[["SOURCE_ID", "ra", "ra_error", "dec", "dec_error", "period",
              "eccentricity", "center_of_mass_velocity", 
              "temperature_ratio"]]

t_df2.to_csv(path_or_buf = "gaia2.csv")