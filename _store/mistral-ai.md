---
aid: mistral-ai
name: Mistral AI
description: Mistral AI is a French artificial intelligence company that develops and provides frontier large language models and APIs for developers and enterprises. Their developer platform offers APIs for chat completions, embeddings, fine-tuning, OCR, batch processing, and agentic workflows, enabling teams to build sophisticated AI-powered applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mistral-ai/refs/heads/main/apis.yml
tags:
  - Agents
  - Artificial Intelligence
  - Batch Processing
  - Chat
  - Embeddings
  - Fine-Tuning
  - Large Language Models
  - OCR
created: '2025-03-07'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mistral-ai:chat-completions
    name: Mistral AI Chat Completions API
    description: The Mistral AI Chat Completions API enables developers to interact with Mistral's language models in a conversational manner. It supports multi-turn conversations, function calling, and JSON mode for structured outputs. The API provides access to a range of models including Mistral Large, Mistral Small, and Codestral, each optimized for different use cases from general reasoning to code generation.
    humanURL: https://docs.mistral.ai/api/endpoint/chat
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Chat
      - Completions
      - Conversational AI
      - Large Language Models
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/chat
      - type: OpenAPI
        url: openapi/mistral-ai-chat-completions-openapi.yml
  - aid: mistral-ai:embeddings
    name: Mistral AI Embeddings API
    description: The Mistral AI Embeddings API allows developers to compute document and text embeddings using Mistral's embedding models. These embeddings can be used for semantic search, clustering, classification, and retrieval augmented generation workflows. The API accepts text inputs and returns high-dimensional vector representations suitable for a variety of natural language processing tasks.
    humanURL: https://docs.mistral.ai/capabilities/embeddings
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Embeddings
      - Semantic Search
      - Vector Search
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/capabilities/embeddings
      - type: OpenAPI
        url: openapi/mistral-ai-embeddings-openapi.yml
  - aid: mistral-ai:agents
    name: Mistral AI Agents API
    description: The Mistral AI Agents API provides a dedicated framework for building agentic applications. It complements the Chat Completion API by enabling AI agents to handle complex tasks, maintain context across interactions, and coordinate multiple actions. Developers can create agents with specific configurations, tools, and instructions, making it suitable for enterprise-grade agentic platforms and multi-step workflow automation.
    humanURL: https://docs.mistral.ai/api/endpoint/agents
    baseURL: https://api.mistral.ai/v1
    tags:
      - Agentic Workflows
      - Agents
      - Artificial Intelligence
      - Automation
      - Orchestration
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/agents
      - type: OpenAPI
        url: openapi/mistral-ai-agents-openapi.yml
  - aid: mistral-ai:fine-tuning
    name: Mistral AI Fine-Tuning API
    description: The Mistral AI Fine-Tuning API allows developers to create and manage fine-tuning jobs that customize Mistral models on proprietary datasets. Users can upload training data, configure hyperparameters, and monitor job progress through the API. Fine-tuned models can then be deployed and accessed through the Chat Completions endpoint, enabling domain-specific performance improvements for enterprise applications.
    humanURL: https://docs.mistral.ai/api/endpoint/fine-tuning
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Customization
      - Fine-Tuning
      - Machine Learning
      - Model Training
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/fine-tuning
      - type: OpenAPI
        url: openapi/mistral-ai-fine-tuning-openapi.yml
  - aid: mistral-ai:ocr
    name: Mistral AI OCR API
    description: The Mistral AI OCR API provides optical character recognition capabilities powered by the mistral-ocr-latest model. It can extract text and structured content from PDF documents and images, comprehending complex document elements including media, tables, equations, and interleaved text. The API returns ordered, structured content suitable for downstream processing and retrieval augmented generation pipelines.
    humanURL: https://docs.mistral.ai/api/endpoint/ocr
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Document AI
      - OCR
      - PDF Processing
      - Text Extraction
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/ocr
      - type: OpenAPI
        url: openapi/mistral-ai-ocr-openapi.yml
  - aid: mistral-ai:models
    name: Mistral AI Models API
    description: The Mistral AI Models API provides endpoints for listing and retrieving information about available models on the Mistral platform. Developers can query which models are accessible, inspect model capabilities and metadata, and manage fine-tuned model deployments. This API serves as the foundation for model discovery and lifecycle management within the Mistral ecosystem.
    humanURL: https://docs.mistral.ai/api/endpoint/models
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Infrastructure
      - Model Management
      - Models
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/models
      - type: OpenAPI
        url: openapi/mistral-ai-models-openapi.yml
  - aid: mistral-ai:forge
    name: Mistral AI Forge API
    description: Mistral AI Forge is a model-training platform providing a unified API for the entire model lifecycle from pre-training to reinforcement learning. Forge enables enterprises to build frontier-grade AI models grounded in proprietary knowledge, supporting pre-training on large internal datasets, post-training through supervised fine-tuning with DPO and ODPO, and reinforcement learning pipelines for aligning models with internal policies. Forge is optimized for agentic workflows, allowing AI agents to programmatically schedule training jobs, optimize hyperparameters, and generate synthetic data. The platform supports both Dense and Mixture-of-Experts model architectures with serverless infrastructure.
    humanURL: https://mistral.ai/news/forge
    tags:
      - Agentic Workflows
      - Artificial Intelligence
      - Enterprise AI
      - Model Training
      - Pre-Training
      - Reinforcement Learning
    properties:
      - type: Documentation
        url: https://mistral.ai/news/forge
      - type: OpenAPI
        url: openapi/mistral-ai-forge-openapi.yml
  - aid: mistral-ai:batch
    name: Mistral AI Batch API
    description: The Mistral AI Batch API enables developers to submit large volumes of requests for asynchronous processing at reduced cost. It is designed for workloads that do not require real-time responses, such as bulk text classification, large-scale content generation, and data processing pipelines. Developers can submit batch jobs, monitor their progress, and retrieve results once processing is complete.
    humanURL: https://docs.mistral.ai/capabilities/batch
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Asynchronous
      - Batch Processing
      - Large Scale
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/capabilities/batch
      - type: OpenAPI
        url: openapi/mistral-ai-batch-openapi.yml
common:
  - type: Portal
    url: https://console.mistral.ai/
  - type: Documentation
    url: https://docs.mistral.ai/
  - type: Website
    url: https://mistral.ai/
  - type: PrivacyPolicy
    url: https://mistral.ai/terms/#privacy-policy
  - type: TermsOfService
    url: https://mistral.ai/terms/#terms-of-use
  - type: Blog
    url: https://mistral.ai/news/
  - type: Login
    url: https://console.mistral.ai/
  - type: JSON-LD
    url: json-ld/mistral-ai-context.jsonld
  - type: JSONSchema
    url: json-schema/mistral-ai-chat-completion-schema.json
  - type: JSONSchema
    url: json-schema/mistral-ai-model-schema.json
  - type: JSONSchema
    url: json-schema/mistral-ai-fine-tuning-job-schema.json
  - type: JSONSchema
    url: json-schema/mistral-ai-batch-job-schema.json
  - type: JSONSchema
    url: json-schema/mistral-ai-ocr-response-schema.json
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
