#!/usr/bin/env python3

import xml.etree.ElementTree as ET

tree = ET.parse("uzivatele.xml")
root = tree.getroot()

csv = open("output.csv", "w")

for element in root:
    element_data = []
    for subelement in element:
        element_data.append(subelement.text)
    csv.write(",".join(element_data) + "\n")

csv.close()