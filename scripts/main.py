import pandas as pd

def main():
    df = pd.read_csv('states.csv')
    print (df)
    import pandas as pd
    print(df.describe())
    df.info()
    
import geopandas as gpd

gdf = gpd.read_file("africa_countries.geojson")
print(gdf.shape)
print(gdf.head())