from fastapi import FastAPI
import uvicorn

# That is the file where NeuralSearcher is stored
from utils.neural_searcher import NeuralSearcher

app = FastAPI()

# Create an instance of the neural searcher
neural_searcher_e1 = NeuralSearcher(collection_name='e1')
neural_searcher_e2 = NeuralSearcher(collection_name='e2')

@app.get("/api/search")
def search_entry(q: str):
    return {
        "result_e1": neural_searcher_e1.search(text=q),
        "result_e2": neural_searcher_e2.search(text=q)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
