import pandas as pd
import numpy as np


## binary


gaia2 = pd.read_csv("gaia2.csv")
df5 = pd.read_csv("sdss_binary_match.csv")

ra = gaia2["ra"]
rae = gaia2["ra_error"]
dec = gaia2["dec"]
dece = gaia2["dec_error"]

## iterate through gaia and sdss , check sdss coords within range of gaia coords and collect corresponding IDs

id_match_gaia = []
id_match_sdss = []

for i in range(len(df5)):
    df_match = df5[ (df5["ra"] >= ra[i] - rae[i]) & (df5["ra"] <= ra[i] + rae[i]) & 
                    (df5["dec"] >= dec[i] - dece[i]) & (df5["dec"] <= dec[i] + dece[i])]
    id_match_sdss.append(list(df_match["specObjID"]))
    id_match_gaia.append([gaia2["SOURCE_ID"].iloc[i] for _ in range(len(df_match))])


## select rows with corresponding IDs

id_match_df = pd.DataFrame()

for i in range(len(id_match_gaia)):

    cs = id_match_sdss[i]
    cg = id_match_gaia[i]

    if not cs:
        continue
    if not cg:
        continue

    sdss_data = df5[df5["specObjID"].isin(cs)]
    sdss_data["gaia_id_match"] = cg

    id_match_df = pd.concat([id_match_df, sdss_data], ignore_index = True)



## single


s_single = pd.read_csv("sdss_single.csv")
g_single = pd.read_csv("gaia_single_match.csv")

ra2 = s_single["ra"]
dec2 = s_single["dec"]
err = 0.089

g_match_id = []
s_match_id = []

for i in range(len(s_single)):
    df_match = s_single[ (s_single["ra"] >= ra2[i] - err) & (s_single["ra"] <= ra2[i] + err) & 
                    (s_single["dec"] >= dec2[i] - err) & (s_single["dec"] <= dec2[i] + err)]
    s_match_id.append(list(df_match["specObjID"]))
    g_match_id.append([g_single["source_id"].iloc[i] for _ in range(len(df_match))])


id_match_df2 = pd.DataFrame()

for i in range(len(g_match_id)):

    cs = s_match_id[i]
    cg = g_match_id[i]

    if not cs:
        continue
    if not cg:
        continue

    sdss_data = s_single[s_single["specObjID"].isin(cs)]
    sdss_data["gaia_id_match"] = cg

    id_match_df2 = pd.concat([id_match_df2, sdss_data], ignore_index = True)

id_match2_nodup = id_match_df2.drop_duplicates(subset = ["ra", "dec"])


## match closest objects by coordinates


match_mult = id_match_df.copy() ## has all SDSS data and corresponding gaia IDs
match_single = id_match2_nodup.copy() ## has all SDSS data and corresponding gaia IDs

g_mult = match_mult["gaia_id_match"].unique()
g_mult_data = gaia2[gaia2["SOURCE_ID"].isin(g_mult)] ## gaia data for multiple-star source IDs matched with SDSS
g_mult_data = g_mult_data.drop_duplicates(subset = ["SOURCE_ID"], ignore_index = True)

gsingle = match_single["gaia_id_match"].unique()
g_single_data = g_single[g_single["source_id"].isin(gsingle)] ## gaia data for single-star source IDs matched with SDSS
g_single_data = g_single_data.drop_duplicates(subset = ["source_id"], ignore_index = True)


## multiple stars closest

closest = 0

sdss_mult_closest = pd.DataFrame()

for i in range(len(g_mult_data)):

    cg_id = g_mult_data["SOURCE_ID"].iloc[i]
    cg = g_mult_data.iloc[i]
    cs = match_mult[match_mult["gaia_id_match"] == cg_id].reset_index()

    # for j in range(len(cs)):
    #     e_ra = cs["ra"].iloc[j] - cg["ra"]
    #     e_dec = cs["dec"].iloc[j] - cg["dec"]
    #     e_tot = abs(e_ra + e_dec)
        
    #     if e_tot < error:
    #         error = e_tot
    #         closest = j

    errs = abs( (cs["ra"] - cg["ra"]) + (cs["dec"] - cg["dec"]) )
    closest = errs.index[errs == min(errs)]

    s_closest = cs.iloc[closest]

    sdss_mult_closest = pd.concat([sdss_mult_closest, s_closest], ignore_index = True)


sdss_mult_closest = sdss_mult_closest[sdss_mult_closest["type"] == 6.0] 
## select stars only, source https://skyserver.sdss.org/dr18/MoreTools/browser with PhotoObjAll table selected


## single


closest = 0

sdss_single_closest = pd.DataFrame()

for i in range(len(g_single_data)):

    cg_id = g_single_data["source_id"].iloc[i]
    cg = g_single_data.iloc[i]
    cs = match_single[match_single["gaia_id_match"] == cg_id].reset_index()

    errs = abs( (cs["ra"] - cg["ra"]) + (cs["dec"] - cg["dec"]) )
    closest = errs.index[errs == min(errs)]
    print(closest)

    s_closest = cs.loc[closest]

    sdss_single_closest = pd.concat([sdss_single_closest, s_closest], ignore_index = True)


## get resulting tables

g_single_data.to_csv(path_or_buf = "gaia_single_data.csv")
g_mult_data.to_csv(path_or_buf = "gaia_multiple_data.csv")
sdss_single_closest.to_csv(path_or_buf = "sdss_single_closest.csv")
sdss_mult_closest.to_csv(path_or_buf = "sdss_multiple_closest.csv")
