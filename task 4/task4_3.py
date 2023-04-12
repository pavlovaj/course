import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

counter1 = 0
counter2 = 0
for token in root.iter('token'):
    if token.attrib['text'] == 'Может' or token.attrib['text'] == 'может':
        for g in token.iter('g'):
            if g.attrib['v'] == 'CONJ':
                counter1 += 1
            if g.attrib['v'] == 'VERB':
                counter2 += 1
print(counter1, counter2)

