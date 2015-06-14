# -*- coding: utf-8 -*-

from os import path, listdir
import json

json_dir = path.abspath('../jsonIncidents2015')
files = listdir(json_dir)

def convert2geojson(filepath, filename):
    output = { 'type': 'FeatureCollection', 'features': [] }
    with open(filepath, 'r') as f:
        incidents = json.loads(f.read())

    for i in incidents:
        try:
            incident = i.get("incident")
            new_incident = {}
            new_incident["type"] = "Feature"
            new_incident["geometry"] = {
                "type": "Point",
                "coordinates": [
                    float(incident["lng"]),
                    float(incident["lat"])
                ]
            }

            # add properties
            new_incident["properties"] = {}
            for p in incident:
                new_incident["properties"][p] = incident[p]

            output['features'].append(new_incident)
        except TypeError:
            continue

    output_dir = 'geojson'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    (root, ext) = os.path.splitext(filename)
    new_filename = output_dir + '/' + root + '.geojson'

    with open(new_filename, 'w') as outfile:
        json.dump(output, outfile)

# grab all .json files within directory
# for each file, do the stuff below and append to output features

for filename in files:
    if ".json" in filename:
        convert2geojson(path.join(json_dir, filename), filename)
