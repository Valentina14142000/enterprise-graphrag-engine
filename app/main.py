from app.graph import app_graph
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Enterprise GraphRAG Engine",
    description="Production-grade dual retrieval with automated Ragas evaluation",
    version="1.0.0",
)


class QueryRequest(BaseModel):
  query: str


@app.post("/query")
async def run_graphrag(request: QueryRequest):
  initial_state = {
      "query": request.query,
      "vector_context": [],
      "graph_context": [],
      "combined_context": "",
      "generation": "",
      "faithfulness_score": 0.0,
  }

  result = app_graph.invoke(initial_state)

  return {
      "query": result["query"],
      "generation": result["generation"],
      "faithfulness_score": result["faithfulness_score"],
  }