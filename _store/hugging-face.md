---
aid: hugging-face
url: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/apis.yml
apis:
- name: Hugging Face Inference API
  description: Run inference on 200,000+ machine learning models with a simple HTTP request.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/api-inference/index
  baseURL: https://api-inference.huggingface.co
  tags:
  - AI
  - Inference
  - Machine Learning
  - Models
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/api-inference/index
  - type: OpenAPI
    url: https://huggingface.co/api-inference/openapi.json
  - type: OpenAPI
    url: openapi/hugging-face-inference-api.yml
  - type: Authentication
    url: https://huggingface.co/docs/api-inference/quicktour#authentication
  - type: Getting Started
    url: https://huggingface.co/docs/api-inference/quicktour
  - type: Rate Limits
    url: https://huggingface.co/docs/api-inference/en/rate-limits
  - type: FAQ
    url: https://huggingface.co/docs/api-inference/faq
  contact:
  - type: Support
    url: https://huggingface.co/support
- name: Hugging Face Hub API
  description: Programmatically interact with the Hugging Face Hub - manage models, datasets, and spaces.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/hub/api
  baseURL: https://huggingface.co/api
  tags:
  - Datasets
  - Hub
  - Models
  - Repository Management
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/hub/api
  - type: OpenAPI
    url: https://huggingface.co/.well-known/openapi.json
  - type: OpenAPI
    url: openapi/hugging-face-hub-api.yml
  - type: Python Client
    url: https://huggingface.co/docs/huggingface_hub/index
  - type: JavaScript Client
    url: https://huggingface.co/docs/huggingface.js/hub/README
  - type: Authentication
    url: https://huggingface.co/docs/hub/security-tokens
  - type: Rate Limits
    url: https://huggingface.co/docs/hub/en/rate-limits
  contact:
  - type: Support
    url: https://huggingface.co/support
- name: Hugging Face Inference Endpoints API
  description: Deploy and scale machine learning models with dedicated, secure infrastructure.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/inference-endpoints/index
  baseURL: https://api.endpoints.huggingface.cloud
  tags:
  - Deployment
  - Enterprise
  - Inference
  - Managed Service
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/inference-endpoints/api_reference
  - type: OpenAPI
    url: openapi/hugging-face-inference-endpoints-api.yml
  - type: Getting Started
    url: https://huggingface.co/docs/inference-endpoints/index
  - type: Pricing
    url: https://huggingface.co/pricing#inference-endpoints
  - type: Authentication
    url: https://huggingface.co/docs/hub/security-tokens
  contact:
  - type: Support
    url: https://huggingface.co/support
- name: Hugging Face Inference Providers API
  description: Unified proxy layer providing access to 15+ inference partners through a single OpenAI-compatible endpoint.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/inference-providers/en/index
  baseURL: https://router.huggingface.co/v1
  tags:
  - AI
  - Inference
  - OpenAI Compatible
  - Providers
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/inference-providers/en/index
  - type: OpenAPI
    url: openapi/hugging-face-inference-providers-api.yml
  - type: API Reference
    url: https://huggingface.co/docs/inference-providers/en/tasks/index
  - type: Getting Started
    url: https://huggingface.co/docs/inference-providers/en/guides/first-api-call
  - type: Pricing
    url: https://huggingface.co/docs/inference-providers/pricing
  - type: Supported Models
    url: https://huggingface.co/inference/models
  contact:
  - type: Support
    url: https://huggingface.co/support
- name: Hugging Face Dataset Viewer API
  description: Query and visualize datasets stored on the Hugging Face Hub through a lightweight REST API.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/dataset-viewer/index
  baseURL: https://datasets-server.huggingface.co
  tags:
  - Data
  - Datasets
  - Viewer
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/dataset-viewer/index
  - type: OpenAPI
    url: https://datasets-server.huggingface.co/openapi.json
  - type: OpenAPI
    url: openapi/hugging-face-dataset-viewer-api.yml
  - type: Getting Started
    url: https://huggingface.co/docs/dataset-viewer/en/quick_start
  - type: GitHub
    url: https://github.com/huggingface/dataset-viewer
  contact:
  - type: Support
    url: https://huggingface.co/support
- name: Hugging Face Text Generation Inference API
  description: High-performance toolkit for deploying and serving large language models with optimized inference.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/text-generation-inference/en/index
  baseURL: https://api-inference.huggingface.co
  tags:
  - AI
  - Inference
  - LLM
  - Text Generation
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/text-generation-inference/en/index
  - type: OpenAPI
    url: openapi/hugging-face-text-generation-inference-api.yml
  - type: API Reference
    url: https://huggingface.co/docs/text-generation-inference/en/reference/api_reference
  - type: Getting Started
    url: https://huggingface.co/docs/text-generation-inference/quicktour
  - type: Messages API
    url: https://huggingface.co/docs/text-generation-inference/en/messages_api
  - type: GitHub
    url: https://github.com/huggingface/text-generation-inference
  contact:
  - type: Support
    url: https://huggingface.co/support
name: Hugging Face
tags:
- API
type: Contract
image: https://huggingface.co/front/assets/huggingface_logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The AI community building the future with open-source machine learning models, datasets, and applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

