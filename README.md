arealm
======

steps to generate final output

starting from arealm shapefiles from  http://www2.census.gov/geo/tiger/TIGER2013/AREALM/

```shell
for i in *shp; do ogr2ogr -f GeoJSON "$i.json" "$i"; done
for i in fixed/*; do ~/packages/shputils/shape-gn-matchr.py --shp_name_keys=FULLNAME --allowed_gn_classes=S,H,L,T,V --fallback_allowed_gn_classes=P --dbname=gis $i gn-$(basename $i); done
for i in gn-matched/gn-fixed-tl_2013_*; do /home/blackmad/packages/shputils/dissolve-shapes.py -f qs_gn_id -c FULLNAME:first,MTFCC:uniq,AREAID -i $i -o dissolved-$(basename $i); done
```

