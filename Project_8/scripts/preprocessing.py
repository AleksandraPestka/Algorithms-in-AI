''' Preprocess XML file, get some information and save to CSV file.'''

import xml.etree.ElementTree as ET
import pandas as pd

def XML_to_dict(path):
    tree = ET.parse(path)
    root = tree.getroot()

    buffer = []

    for record in root:
        doc = {}
        record = record[0]
        
        # get the number of contributors and editors
        authors = [el.text for el in record.findall('author')]
        editors = [el.text for el in record.findall('editors')]
        doc['num_contrib'] = len(authors) + len(editors)

        # get the year info
        try:
            doc['year'] = int(record.find('year').text)
        except AttributeError:
            pass

        # get the number of pages
        try:
            pages = record.find('pages').text
            separator = pages.find('-')
            doc['num_pages'] =  int(pages[separator+1:]) - int(pages[:separator])

        except (AttributeError, ValueError):
            continue         

        try:
            doc['title'] = record.find('title').text
        except AttributeError:
            pass

        buffer.append(doc)

    return buffer

def dict_to_dataframe(dictionary_list):
    # keep dictionaries with all information
    buffer = []

    for item in dictionary_list:
        try:
            buffer.append([item['num_contrib'], item['year'], 
                          item['num_pages'], item['title']])
        except KeyError:
            continue

    df = pd.DataFrame(data=buffer, columns=['num_contrib', 'year', 'num_pages', 
                                            'title'])

    return df

