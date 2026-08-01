# Enterprise GraphRAG Engine 

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangGraph](https://img.shields.io/badge/Orchestration-LangGraph-orange)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Ragas](https://img.shields.io/badge/Evaluation-Ragas-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A production-grade, state-of-the-art **Graph Retrieval-Augmented Generation (GraphRAG)** engine built with **LangGraph** and **FastAPI**. Designed for enterprise knowledge bases, this architecture combines semantic vector search with knowledge graph traversal to solve multi-hop reasoning challenges, complete with an automated evaluation loop.

---

##  System Architecture & Workflow

The application runs on a state-machine workflow orchestrated via LangGraph, ensuring strict execution boundaries and automated quality checks:

```mermaid
graph TD
    A[Incoming Query] --> B[Vector Retrieval Node]
    B --> C[Graph Traversal Node]
    C --> D[Synthesized Answer Node]
    D --> E[Ragas Evaluation Node]
    E --> F[API Response]


