---
aid: qubrid-ai
name: Qubrid AI
description: Qubrid AI is a cloud platform that provides GPU-accelerated infrastructure and AI services for enterprise developers. Their developer platform offers OpenAI-compatible inference endpoints, GPU compute provisioning, model fine-tuning, and retrieval-augmented generation capabilities, all running on NVIDIA GPU infrastructure.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Cloud Computing
  - GPU
  - Inference
  - Large Language Models
  - Machine Learning
  - NVIDIA
  - Serverless
url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qubrid-ai:inference
    name: Qubrid AI Inference API
    description: The Qubrid AI Inference API provides a single, OpenAI-compatible endpoint for orchestrating 40+ open-source models running on NVIDIA GPU infrastructure. By abstracting hardware orchestration through TensorRT-LLM and Triton Inference Server, the API allows enterprise developers to run inference on models without managing underlying infrastructure.
    humanURL: https://docs.platform.qubrid.com
    baseURL: https://platform.qubrid.com/api/v1
    tags:
      - Artificial Intelligence
      - Inference
      - Large Language Models
      - Machine Learning
      - NVIDIA
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.platform.qubrid.com
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/openapi/qubrid-ai-inference-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-schema/qubrid-ai-inference-schema.json
  - aid: qubrid-ai:compute
    name: Qubrid AI Compute API
    description: The Qubrid AI Compute API provides programmatic access to GPU cloud infrastructure including NVIDIA H100, H200, and B200 accelerators. Developers can provision and manage GPU instances for AI and machine learning workloads through API calls.
    humanURL: https://docs.platform.qubrid.com
    baseURL: https://platform.qubrid.com/api/v1
    tags:
      - Cloud Computing
      - GPU
      - NVIDIA
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.platform.qubrid.com
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/openapi/qubrid-ai-compute-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-schema/qubrid-ai-compute-schema.json
  - aid: qubrid-ai:fine-tuning
    name: Qubrid AI Fine-Tuning API
    description: The Qubrid AI Fine-Tuning API enables developers and enterprises to customize open-source AI models using their own data. The API provides endpoints for uploading training datasets, configuring fine-tuning parameters, launching training jobs on GPU infrastructure, and retrieving fine-tuned model artifacts.
    humanURL: https://docs.platform.qubrid.com
    baseURL: https://platform.qubrid.com/api/v1
    tags:
      - Artificial Intelligence
      - Fine-Tuning
      - Machine Learning
      - Model Training
    properties:
      - type: Documentation
        url: https://docs.platform.qubrid.com
      - type: Documentation
        url: https://docs.platform.qubrid.com/Fine%20Tuning
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/openapi/qubrid-ai-fine-tuning-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-schema/qubrid-ai-fine-tuning-schema.json
  - aid: qubrid-ai:rag
    name: Qubrid AI RAG API
    description: The Qubrid AI RAG API provides retrieval-augmented generation capabilities that allow developers to upload departmental or enterprise data and query it using large language models. The API handles document ingestion, embedding generation, vector storage, and context-aware retrieval to ground model responses in organizational knowledge.
    humanURL: https://docs.platform.qubrid.com
    baseURL: https://platform.qubrid.com/api/v1
    tags:
      - Artificial Intelligence
      - RAG
      - Retrieval Augmented Generation
      - Search
      - Knowledge Management
    properties:
      - type: Documentation
        url: https://docs.platform.qubrid.com
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/openapi/qubrid-ai-rag-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-schema/qubrid-ai-rag-schema.json
common:
  - type: Portal
    url: https://platform.qubrid.com
  - type: Documentation
    url: https://docs.platform.qubrid.com
  - type: Website
    url: https://qubrid.com
  - type: Login
    url: https://platform.qubrid.com/login
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-ld/qubrid-ai-context.jsonld
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
