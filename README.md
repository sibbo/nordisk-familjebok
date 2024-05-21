# Linking editions of Nordisk Familjebok with Wikidata

0. Make sure you meet the requirements in `requirements.txt`.

1. `scraper.ipynb`: Downloading (scraping) the first and second editions of the text, as well as some post processing.

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
    "e2_key": "", # corresponding entryid in second edition from linking
    "e4_key": "", # corresponding entryid in fourth edition from linking (not implemented)
    "cross_ref_key": "", # the key to the cross reference
    "latitude": None, # latitude from wikidata linking
    "longitude": None, # longitude from wikidata linking
}
```
4. `postprocessing.ipynb`: performs post processing on the json files. Removes unordered entries and adds cross references.

5. `location_classifier.ipynb`: classifies entries as locations and non-locations. Written to be run in Google Colab, since it requires a lot of computing power.

6. `sentence_embeddings.ipynb`: creates sentence embeddings for the entries in both editions. Also written to be run in Google Colab, since creating embeddings requires a lot of computing power. 

Instructions:

    * Create a copy of the notebook in Google Colab
    * Move your json files to a Google Drive folder
    * Change the file path in the pd.read_json() functions
    * Run the notebook
    * Download the vectors (if the cell for downloading doesn't work, go into the file system on the left and download from there)

7. `qdrant.ipynb` and `linker.ipynb`: adds the json files (payload) and the corresponding sentence embeddings to a qdrant database, and then links entries between editions.

8. `wiki_searcher.ipynb`:

9. `visualization.ipynb`: