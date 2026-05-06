---
aid: kaito
name: KAITO
description: KAITO (Kubernetes AI Toolchain Operator) is an open-source operator suite that automates LLM model inference, fine-tuning, and Retrieval Augmented Generation (RAG) engine deployment in Kubernetes clusters. It simplifies the process of deploying large AI models through optimized preset configurations and integrates with Karpenter for GPU node auto-provisioning.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - GPU
  - Inference
  - Kubernetes
  - LLM
  - Machine Learning
  - Open Source
  - Operator
  - RAG
url: https://raw.githubusercontent.com/api-evangelist/kaito/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kaito:rag-engine
    name: KAITO RAGEngine API
    description: RAGEngine exposes endpoints for managing retrieval-augmented generation services with embedded vector databases, including document indexing, retrieval, and chat completion endpoints.
    humanURL: https://kaito-project.github.io/kaito/docs/rag
    tags:
      - AI
      - RAG
      - Vector Database
      - Inference
    properties:
      - type: Documentation
        url: https://kaito-project.github.io/kaito/docs/rag
      - type: GitHub
        url: https://github.com/kaito-project/kaito
common:
  - type: Website
    url: https://kaito-project.github.io/kaito/
  - type: Documentation
    url: https://kaito-project.github.io/kaito/docs/
  - type: Installation
    url: https://kaito-project.github.io/kaito/docs/installation
  - type: Getting Started
    url: https://kaito-project.github.io/kaito/docs/quick-start
  - type: GitHub Organization
    url: https://github.com/kaito-project
  - type: Source Code
    url: https://github.com/kaito-project/kaito
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
