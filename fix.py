#!/usr/bin/python

import csv
import json

abbrMap = {}
for l in csv.reader(open('feature_name_types.csv')):
  abbr = l[2]
  exp = l[1]
  abbrMap[abbr] = exp

import sys
import re
collection = json.load(open(sys.argv[1]))
newFeatures = []

for f in collection['features']:
  name = f['properties']['FULLNAME']
  if name:
    for k, v in abbrMap.items():
      name = re.sub(r'\b%s\b' % k, v, name)
    f['properties']['FULLNAME'] = name
    newFeatures.append(f)

collection['features'] = newFeatures

json.dump(collection, open('fixed-%s' % sys.argv[1], 'w'))

