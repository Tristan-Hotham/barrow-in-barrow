"""r/dataisbeautiful collage for barrow-in-barrow: is_there_a_barrow_in_barrow.png (2400 x 3000).
Every number is read from results/summary.csv or counted from results/places_scored.csv and data/raw/scheduled_barrows.csv.
Run: python3 collage.py  (BARROW=/path/to/barrow-in-barrow)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
BARROW = os.environ.get("BARROW", "/home/claude/repo-barrow")
import numpy as np, pandas as pd
from house import *
from matplotlib.lines import Line2D

SM = pd.read_csv(os.path.join(BARROW, "results/summary.csv")).set_index("el")
P = pd.read_csv(os.path.join(BARROW, "results/places_scored.csv"))
B = pd.read_csv(os.path.join(BARROW, "data/raw/scheduled_barrows.csv"))
C = counties_km()
E = C[C.nation == "England"]

MOUND, YES, NO, HILL = "#8A6A4E", "#C2412D", "#2F4B7C", "#9C9483"
bg = P[P.element == "berg"].copy()
bg["x"], bg["y"] = to_km(bg.Longitude.values, bg.Latitude.values)
gl = bg[bg.glossed_burial_mound]
n_gl, n_gl0 = len(gl), int((gl.n2 == 0).sum())
barrow_grove = int(((P.element == "bearu") & P.PlaceName.str.startswith("Barrow")).sum())
r = SM.loc["berg"]

fig = new_fig()
words(fig, 0.045, 0.972, [("Is there a", FG), ("barrow", MOUND)])
words(fig, 0.045, 0.924, [("in", FG), ("Barrow?", NO)])
fig.text(0.045, 0.862, f"Old English beorg meant a mound or a rounded hill, and gives us the word barrow. Here are the\n"
         f"{len(bg)} English places named from it, against all {len(B):,} scheduled burial mounds in England.",
         family=SER, fontsize=14.5, color=FG, va="top", linespacing=1.15)

ax = fig.add_axes([0.0, 0.25, 0.6, 0.575]); ax.set_facecolor(BGC)
E.plot(ax=ax, color=LAND, edgecolor=BGC, linewidth=0.5, zorder=0)
ax.scatter(B.Easting / 1e3, B.Northing / 1e3, s=2.2, color=MOUND, alpha=.55, lw=0, zorder=1, rasterized=True)
has = bg.n2 > 0
ax.scatter(bg.x[has], bg.y[has], s=46, color=YES, edgecolor="white", lw=.8, zorder=3)
ax.scatter(bg.x[~has], bg.y[~has], s=40, facecolor="white", edgecolor=NO, lw=1.5, zorder=3)
ax.set_xlim(125, 660); ax.set_ylim(5, 665); ax.set_aspect(1); ax.axis("off")


def note(txt, xy, xyt, ha="left"):
    ax.annotate(txt, xy=xy, xytext=xyt, family=MONO, fontsize=10.2, color=FG, ha=ha, va="center", zorder=8,
                arrowprops=dict(arrowstyle="-", color=FG, lw=.8), path_effects=halo(3))


rut = bg[(bg.PlaceName == "Barrow")].iloc[0]
note(f"Barrow, Rutland: glossed\n'burial mound', {int(rut.n2)} barrows\nwithin 2 km", (rut.x, rut.y), (250, 330), ha="center")
for name, xyt, ha in [("Barrow upon Humber", (250, 470), "center")]:
    q = bg[bg.PlaceName == name].iloc[0]
    note(f"{name}:\n{int(q.n2)} within 2 km", (q.x, q.y), xyt, ha)
note("Dorset and Wiltshire:\nthick with barrows", (395, 105), (470, 35), ha="left")

# key
fig.text(0.62, 0.8, "THE KEY", family=MONO, fontsize=11, color=MUT)
keys = [(dict(marker="o", ms=9, color=YES, mec="white"), "beorg place with a scheduled\nbarrow within 2 km"),
        (dict(marker="o", ms=8.5, mfc="white", mec=NO, mew=1.5, color=NO), "beorg place with none"),
        (dict(marker="o", ms=4, color=MOUND, alpha=.7), "scheduled barrow, tumulus\nor round cairn")]
yy = 0.772
for kw, t in keys:
    fig.lines.append(Line2D([0.635], [yy], transform=fig.transFigure, ls="none", **kw))
    fig.text(0.655, yy, t, family=MONO, fontsize=10.5, color=FG, va="center", linespacing=1.15)
    yy -= 0.034

d, h = SM.loc["dun"], SM.loc["hyll"]
items = [
    (f"{r.ratio2:.2f}×", YES,
     f"as many barrows within 2 km of beorg places as\nexpected locally. Places named dūn, 'hill', get\n{d.ratio2:.2f}×, and hyll {h.ratio2:.2f}×. So beorg mostly meant 'hill'."),
    (f"{n_gl0} of {n_gl}", NO,
     f"beorg names that the Key to English Place-Names\nglosses as 'burial mound' have no scheduled\nbarrow within 2 km."),
    (f"{r.any2:.0f}%", MOUND,
     f"of beorg places have any barrow within 2 km.\nOld Norse haugr, 'mound', gets just\n{SM.loc['haugr'].obs2:.0f} barrows where {SM.loc['haugr'].exp2:.0f} were expected."),
    (f"{barrow_grove}", "#4F7A3A",
     f"places called Barrow come not from beorg\nbut from bearu, 'grove'."),
]
headlines(fig, [0.62, 0.25, 0.37, 0.43], items, big=36, step=0.25, sub_off=0.093)

# bottom strip: ratio by element with 95% intervals
label(fig, 0.045, 0.232, "BARROWS WITHIN 2 KM, AGAINST LOCAL EXPECTATION, BY PLACE-NAME ELEMENT (95% INTERVAL)")
a = fig.add_axes([0.2, 0.078, 0.74, 0.135]); a.set_facecolor(BGC)
order = SM.sort_values("ratio2").index
for i, el in enumerate(order):
    s = SM.loc[el]; c = {"berg": YES, "bearu": "#4F7A3A", "haugr": MOUND}.get(el, HILL)
    a.plot([s.lo2, s.hi2], [i, i], color=c, lw=2.4, alpha=.45, solid_capstyle="round")
    a.plot(s.ratio2, i, "o", ms=9, color=c, mec="white", mew=1)
    a.text(s.hi2 + 0.04, i, f"{s.ratio2:.2f}", family=MONO, fontsize=9.6, color=MUT, va="center")
    lab = s.label.replace("beorg/berg", "beorg")
    fig.text(0.19, 0.078 + 0.135 * (i + .5) / len(order), lab, family=SER, fontsize=11.5, ha="right", va="center",
             color=FG, weight=600 if el == "berg" else 400)
a.axvline(1, color=FG, lw=.8, ls=(0, (3, 3)))
a.text(1.0, len(order) - .35, "as many as expected ", family=MONO, fontsize=9.6, color=MUT, ha="right", va="bottom")
a.set_ylim(-.5, len(order) - .5); a.set_xlim(0, 2.6)
a.set_yticks([]); a.tick_params(axis="x", labelsize=9.6, colors=MUT, length=0)
for t in a.get_xticklabels(): t.set_family(MONO)
for sp in a.spines.values(): sp.set_visible(False)
a.grid(axis="x", color="#DDD6C8", lw=.6); a.set_axisbelow(True)

footer(fig, "Data: Key to English Place-Names (Institute for Name-Studies, University of Nottingham); National Heritage List for England\n"
       "© Historic England (OGL v3, contains OS data © Crown copyright); counties ONS (OGL v3). Expected counts scale the barrows within\n"
       "30 km by area. Scheduled mounds are survivors. Analysis and chart: Tristan Hotham, with Python and matplotlib.")
fig.savefig(os.path.join(HERE, "is_there_a_barrow_in_barrow.png"), dpi=200, facecolor=BGC)
print("written", len(bg), len(B), n_gl, n_gl0, barrow_grove, r.ratio2, r.any2)
