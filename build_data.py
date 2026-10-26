import pandas as pd, json, numpy as np
from pyproj import Transformer
back=Transformer.from_crs(27700,4326,always_xy=True)
D=pd.read_csv('results/places_scored_full.csv'); O=pd.read_csv('results/summary.csv')
sm=pd.read_csv('data/raw/scheduled_barrows.csv')
lon,lat=back.transform(sm.Easting.values,sm.Northing.values)
bar=[[round(a,4),round(b,4),int(e),n] for a,b,e,n in zip(lat,lon,sm.ListEntry,sm.Name)]
pl=[[r.PlaceName,r.el,round(r.Latitude,4),round(r.Longitude,4),int(r.n2),round(r.exp2,2),int(r.burial)] for r in D.itertuples()]
summ=O[['el','label','n','obs2','exp2','ratio2','lo2','hi2','any2','ratio1','ratio3']].round(3).to_dict('records')
json.dump({'places':pl,'summary':summ},open('data/places.json','w'),ensure_ascii=False,separators=(',',':'))
json.dump(bar,open('data/barrows.json','w'),ensure_ascii=False,separators=(',',':'))
# public tidy data (no etymology text; see KEPN)
D[['PlaceName','el','Latitude','Longitude','burial','n1','n2','n3','nR','exp1','exp2','exp3']].rename(columns={'el':'element','burial':'glossed_burial_mound','nR':'barrows_within_30km'}).round(3).to_csv('results/places_scored.csv',index=False)
b=D[D.burial & (D.el=='berg')]
print(b[['PlaceName','n2','exp2']].to_string())
