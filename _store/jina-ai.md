---
aid: jina-ai
url: https://raw.githubusercontent.com/api-evangelist/jina-ai/refs/heads/main/apis.yml
apis:
- aid: jina-ai:embeddings-api
  name: Jina AI Embeddings API
  description: Generate high-quality embeddings from text, images, or code using Jina AI's state-of-the-art embedding models.
  humanURL: https://jina.ai/embeddings/
  tags:
  - Embeddings
  - Multimodal
  - Text
  properties:
  - type: Documentation
    url: https://docs.jina.ai/
- aid: jina-ai:reader-api
  name: Jina AI Reader API
  description: Convert a URL to LLM-friendly input by simply adding r.jina.ai in front. Also supports search-based reading via s.jina.ai.
  humanURL: https://jina.ai/reader/
  tags:
  - Content Extraction
  - LLM
  - Web Reading
  properties:
  - type: Documentation
    url: https://jina.ai/reader/
- aid: jina-ai:reranker-api
  name: Jina AI Reranker API
  description: Re-rank search results by relevance using Jina AI's reranker models to improve the quality of retrieved documents.
  humanURL: https://jina.ai/reranker/
  tags:
  - Relevance
  - Reranking
  - Search
  properties:
  - type: Documentation
    url: https://docs.jina.ai/
name: Jina AI
tags:
- AI
- Embeddings
- Machine Learning
- Reranking
- Search
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-07'
position: Consumer
description: Jina AI provides Search Foundation APIs for AI-powered applications, offering embeddings, reranking, and web reading capabilities. Their Reader API converts URLs to LLM-friendly input by simply adding r.jina.ai in front.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

