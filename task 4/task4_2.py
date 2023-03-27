import xml.etree.ElementTree as etree

tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()

with open('result.txt', 'w') as f:
    for tokens in root.iter('tokens'):
        for token in tokens.findall('token'):
            list = []
            for g in token.iter('g'):
                list.append(g.attrib['v'])
            if 'NOUN' in list and 'plur' in list:
                f.write(token.attrib['text'] + ' ')
