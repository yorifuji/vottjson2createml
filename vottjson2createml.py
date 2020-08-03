
'''

Convert from VoTT JSON to Create ML Annotation JSON Format.

# Create ML Annotation JSON Format

[
    {
        "image":"image1.jpg",
        "annotations": [
            {
                "label": "cat",
                "coordinates": {
                    "x": 100,
                    "y": 100,
                    "width": 200,
                    "height": 200
                }
            }
        ]
    },
    {
        "image":"image2.jpg",
        ...
]

'''

import json
vott_json = json.load(open("./project1-export.json", "r"))

createml_json = []
for asset in vott_json["assets"].values():
    image_json = {
        "image": asset["asset"]["name"],
        "annotations": []
    }
    for region in asset["regions"]:
        annotation = {
            "label": region["tags"][0],
            "coordinates": {
                "x": int(region["boundingBox"]["left"]) + int(region["boundingBox"]["width"])/2,
                "y": int(region["boundingBox"]["top"]) + int(region["boundingBox"]["height"])/2,
                "width": int(region["boundingBox"]["width"]),
                "height": int(region["boundingBox"]["height"])
            }
        }
        image_json["annotations"].append(annotation)
    createml_json.append(image_json)

print(json.dumps(createml_json, indent=2))


