\# Endee Agentic RAG Project



\## Overview



This project implements Semantic Search, RAG, and Agentic AI workflow using Endee vector database.



\## Problem



Keyword search cannot understand meaning.



We need semantic search using vectors.



\## Solution



User → Agent → Embedding → Endee → Search → Context → LLM → Answer



\## Tech



Endee

Ollama

Sentence Transformers

Streamlit

Docker



\## Agentic Workflow



Agent decides action



if greeting → reply



if search → RAG



else → RAG



\## Endee Usage



Store embeddings



Search embeddings



Return metadata



Used in RAG pipeline



\## Setup



Fork Endee repo



Clone repo



Create project



Run:



docker compose up --build



Pull model:



ollama pull orca-mini



Insert data:



python ingest.py



Open:



localhost:8501

