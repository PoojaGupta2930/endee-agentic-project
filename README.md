# Endee Agentic RAG Project

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-green.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This project implements **Semantic Search, Retrieval-Augmented Generation (RAG), and Agentic AI workflow** using the Endee vector database.  
It allows users to ask questions and get AI-generated answers enhanced with **vector search context**.

---

## Problem

Traditional keyword search **cannot understand the meaning** of queries.  
We need semantic search using vector embeddings to provide **accurate and context-aware results**.

---

## Solution

**Workflow:**  
User → Agent → Embedding → Endee → Search → Context → LLM → Answer


The agent decides the next action:  

- **Greeting** → reply directly  
- **Search request** → perform RAG with context  
- **Otherwise** → default to RAG

---

## Tech Stack

- **Endee** – Vector database for embeddings  
- **Ollama** – LLM generation engine  
- **Sentence Transformers** – Create vector embeddings  
- **Streamlit** – Frontend user interface  
- **FastAPI** – Backend API for vector search  
- **Docker** – Containerization for easy setup  

---

## Agentic Workflow

1. Agent analyzes user input.  
2. If greeting → reply.  
3. If search → RAG.  
4. Else → default to RAG.  

---

## Endee Usage

- Store embeddings for documents  
- Search embeddings for semantic similarity  
- Return metadata  
- Used in RAG pipeline to provide context to LLM

---

## Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/PoojaGupta2930/endee-agentic-project.git
cd endee-agentic-project

