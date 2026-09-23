# System Architecture

## Goal

The goal of this project is to build a system that allows a user
to ask natural-language questions about sensor-network data.

## Initial Architecture

Sensor data is assumed to already exist in PostgreSQL.

The RAG system will use two retrieval mechanisms:

1. SQL retrieval for structured numerical and temporal queries.
2. Vector retrieval for semantic information such as events,
   anomalies, and generated summaries.

An LLM will combine the retrieved information and generate
the final natural-language response.

## High-Level Architecture

PostgreSQL
    |
    +---- Structured Data
    |
    +---- Semantic Documents
              |
              +---- Embeddings
              |
              +---- pgvector
                     |
                     v
                 RAG Layer
                     |
                  Router
                 /      \
               SQL     Vector
                 \      /
                   LLM
                    |
                 Response
