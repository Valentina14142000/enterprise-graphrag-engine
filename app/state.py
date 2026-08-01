from typing import List, TypedDict


class GraphRAGState(TypedDict):
  query: str
  vector_context: List[str]
  graph_context: List[str]
  combined_context: str
  generation: str
  faithfulness_score: float