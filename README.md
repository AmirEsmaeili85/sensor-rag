# sensor-rag
# Sensor-RAG

A hands-on project for building a Retrieval-Augmented Generation (RAG)
system over sensor-network data.

## Architecture

The project will eventually implement:

Sensor Data
    ↓
PostgreSQL
    ↓
Hybrid Retrieval
    ├── SQL Retrieval
    └── Vector Retrieval
    ↓
LLM
    ↓
Natural Language Answer

## Current Status

### M0 — Project Initialization
- [x] GitHub repository
- [x] Local development environment
- [x] Docker Compose
- [x] PostgreSQL
- [x] pgvector

### Upcoming

- [ ] Sensor data schema
- [ ] Synthetic sensor data
- [ ] Embedding pipeline
- [ ] Vector search
- [ ] SQL retrieval
- [ ] RAG pipeline
- [ ] Query router
- [ ] Hybrid RAG
- [ ] LLM integration
- [ ] FastAPI
- [ ] Web interface

## Technologies

- Python
- PostgreSQL
- pgvector
- Docker
- Ollama
- FastAPI
