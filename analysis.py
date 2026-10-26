"""Is there a barrow in Barrow? KEPN place-names by element against Historic England scheduled barrows.
Inputs: data/raw/kepn_<element>.csv (KEPN advanced search by element, exported as CSV from kepn.nottingham.ac.uk;
not redistributed here) and data/raw/scheduled_barrows.csv (NHLE scheduled monuments whose names match
barrow|tumul|burial mound|round cairn|bowl cairn). Output: results/summary.csv and results/places_scored_full.csv."""
import pandas as pd, numpy as np, json
from pyproj import Transformer
from scipy.spatial import cKDTree
tr=Transformer.from_crs(4326,27700,always_xy=True)
sm=pd.read_csv('data/raw/scheduled_barrows.csv')
T=cKDTree(sm[['Easting','Northing']].values)
G={'berg':'beorg/berg (mound, hill)','hlaw':'hlāw (mound, hill)','haugr':'haugr (ON mound)','dun':'dūn (hill)','hyll':'hyll (hill)','hoh':'hōh (hill-spur)','burh':'burh (fort)','bearu':'bearu (grove)'}
rows=[]
for k in G:
    d=pd.read_csv(f'data/raw/kepn_{k}.csv').dropna(subset=['Latitude','Longitude']).drop_duplicates(['PlaceName','Latitude','Longitude'])
    x,y=tr.transform(d.Longitude.values,d.Latitude.values); d['x']=x; d['y']=y; d['el']=k
    rows.append(d)
D=pd.concat(rows,ignore_index=True)
D=D[(D.x>0)&(D.x<700000)&(D.y>0)&(D.y<700000)]
P=D[['x','y']].values
for r in [1000,2000,3000]:
    D[f'n{r//1000}']=[len(i) for i in T.query_ball_point(P,r)]
R=30000
D['nR']=[len(i) for i in T.query_ball_point(P,R)]
for r in [1,2,3]:
    D[f'exp{r}']=D.nR*(r*1000)**2/R**2
D['burial']=D.Etymology.str.contains('burial',case=False,na=False)
out=[]
for k,g in D.groupby('el'):
    o={'el':k,'label':G[k],'n':len(g)}
    for r in [1,2,3]:
        o[f'obs{r}']=g[f'n{r}'].sum(); o[f'exp{r}']=g[f'exp{r}'].sum(); o[f'ratio{r}']=o[f'obs{r}']/o[f'exp{r}']
        o[f'any{r}']=100*(g[f'n{r}']>0).mean()
    # bootstrap CI of ratio2
    rng=np.random.default_rng(1); bs=[]
    for _ in range(2000):
        s=g.sample(len(g),replace=True,random_state=rng.integers(1e9)); bs.append(s.n2.sum()/s.exp2.sum())
    o['lo2'],o['hi2']=np.percentile(bs,[2.5,97.5])
    out.append(o)
O=pd.DataFrame(out).sort_values('ratio2',ascending=False)
pd.set_option('display.width',250)
print(O.round(2).to_string())
b=D[D.el=='berg']
print('berg burial-gloss',b.burial.sum(), 'ratio2', b[b.burial].n2.sum()/b[b.burial].exp2.sum(), 'non', b[~b.burial].n2.sum()/b[~b.burial].exp2.sum())
D.to_csv('results/places_scored_full.csv',index=False)
O.to_csv('results/summary.csv',index=False)
