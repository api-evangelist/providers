---
aid: jina-ai
name: Jina AI
description: Jina AI provides Search Foundation APIs for AI-powered applications, offering embeddings, reranking, and web reading capabilities. Their Reader API converts URLs to LLM-friendly input by simply adding r.jina.ai in front.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Embeddings
  - Machine Learning
  - Reranking
  - Search
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/jina-ai/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: jina-ai:embeddings-api
    name: Jina AI Embeddings API
    description: Generate high-quality embeddings from text, images, or code using Jina AI's state-of-the-art embedding models.
    humanURL: https://jina.ai/embeddings/
    baseURL: https://api.jina.ai/v1
    tags:
      - Embeddings
      - Multimodal
      - Text
    properties:
      - type: Documentation
        url: https://docs.jina.ai/
      - type: OpenAPI
        url: openapi/jina-ai-embeddings-openapi.yml
  - aid: jina-ai:reader-api
    name: Jina AI Reader API
    description: Convert a URL to LLM-friendly input by simply adding r.jina.ai in front. Also supports search-based reading via s.jina.ai.
    humanURL: https://jina.ai/reader/
    baseURL: https://r.jina.ai
    tags:
      - Content Extraction
      - LLM
      - Web Reading
    properties:
      - type: Documentation
        url: https://jina.ai/reader/
      - type: OpenAPI
        url: openapi/jina-ai-reader-openapi.yml
  - aid: jina-ai:reranker-api
    name: Jina AI Reranker API
    description: Re-rank search results by relevance using Jina AI's reranker models to improve the quality of retrieved documents.
    humanURL: https://jina.ai/reranker/
    baseURL: https://api.jina.ai/v1
    tags:
      - Relevance
      - Reranking
      - Search
    properties:
      - type: Documentation
        url: https://docs.jina.ai/
      - type: OpenAPI
        url: openapi/jina-ai-reranker-openapi.yml
common:
  - type: Website
    url: https://jina.ai
  - type: Portal
    url: https://jina.ai/api-dashboard/
  - type: Documentation
    url: https://docs.jina.ai/
  - type: Getting Started
    url: https://docs.jina.ai/
  - type: GitHub Organization
    url: https://github.com/jina-ai
  - type: Sign Up
    url: https://jina.ai/api-dashboard/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
