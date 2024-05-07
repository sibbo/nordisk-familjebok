# Linking editions of Nordisk Familjebok with Wikidata

1. `scraper.ipynb`: Downloading (scraping) the first and second editions of the text

2. `entry_classifier.ipynb`: Creates a logistic regression model for entry classification. First annotates training data and then trains the model.

3. `segmenter.ipynb`: Segments the text into headword and text, gives unique ids to all entries and creates initial json files.
```
item = {
    "headword": "Paris",
    "entryid": "e{edition_nbr}_{entry_nbr}_{volume}_{page_nbr}_{page_entry_nbr}",
    "text": "<b>Paris</b> [franskt utt. pari], Frankrikes hufvudstad, näst London Europas folkrikaste stad ...",
    "classifier_type": 0, # 0 = bold, 1 = index, 2 = regression
    "class": 0, # 0 = default, 1 = location
    "qid": "0", # QID, unique identifier used in Wikidata
    "second_edition_key": "", # corresponding entryid in second edition from linking
    "fourth_edition_key": "", # corresponding entryid in fourth edition from linking (not implemented)
    "is_cross_ref": "", # if the entry is a cross reference
    "cross_ref_key": "", # the key to the cross reference
    "latitude": None, # latitude from wikidata linking
    "longitude": None, # longitude from wikidata linking
}
```
4.