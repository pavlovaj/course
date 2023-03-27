import xml.etree.ElementTree as etree


tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('res.txt', 'w') as f:
    for source in root.iter('source'):
            f.write(source.text + ' ')
