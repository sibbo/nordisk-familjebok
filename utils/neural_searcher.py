from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('KBLab/sentence-bert-swedish-cased', device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

    def vector_search(self, vector, threshold: float, search_limit: int):
        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            limit=search_limit, 
            score_threshold=threshold
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads

    def string_search(self, text: str, threshold: float):
        # Convert text query into vector
        vector = self.model.encode(text).tolist() 
        return self.vector_search(vector, threshold=threshold) # This does not work