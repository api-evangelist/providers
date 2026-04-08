---
aid: hugging-face-transformers
url: https://raw.githubusercontent.com/api-evangelist/hugging-face-transformers/refs/heads/main/apis.yml
apis:
- name: Hugging Face Inference API
  description: Serverless API for running inference on thousands of models hosted on Hugging Face. Supports NLP, computer vision, audio, and multimodal tasks.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/inference-api
  baseURL: https://api-inference.huggingface.co
  tags:
  - Inference
  - Predictions
  - Serverless
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/api-inference/index
  - type: OpenAPI
    url: https://huggingface.co/api-inference/openapi.json
  - type: Authentication
    url: https://huggingface.co/docs/api-inference/quicktour#authentication
  - type: Pricing
    url: https://huggingface.co/pricing
  contact:
  - type: Support
    url: https://huggingface.co/support
  - type: Twitter
    url: https://twitter.com/huggingface
- name: Hugging Face Hub API
  description: REST API for interacting with the Hugging Face Hub - upload, download, and manage models, datasets, and spaces programmatically.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/hub/api
  baseURL: https://huggingface.co/api
  tags:
  - Datasets
  - Hub
  - Models
  - Repositories
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/huggingface_hub/index
  - type: Python Client
    url: https://huggingface.co/docs/huggingface_hub/package_reference/overview
  - type: JavaScript Client
    url: https://huggingface.co/docs/huggingface.js/index
  - type: API Reference
    url: https://huggingface.co/docs/hub/api
  contact:
  - type: GitHub
    url: https://github.com/huggingface/huggingface_hub
- name: Transformers Pipeline API
  description: High-level Python API for easy-to-use inference pipelines covering tasks like text generation, classification, translation, and more.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/transformers/main_classes/pipelines
  baseURL: https://github.com/huggingface/transformers
  tags:
  - Inference
  - Library
  - Pipelines
  - Python
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/transformers/index
  - type: GitHub Repository
    url: https://github.com/huggingface/transformers
  - type: Quick Tour
    url: https://huggingface.co/docs/transformers/quicktour
  - type: Task Guide
    url: https://huggingface.co/docs/transformers/task_summary
  - type: PyPI Package
    url: https://pypi.org/project/transformers/
  contact:
  - type: GitHub Issues
    url: https://github.com/huggingface/transformers/issues
- name: Hugging Face Spaces API
  description: API for deploying and managing machine learning applications and demos using Gradio, Streamlit, or Docker.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/spaces
  baseURL: https://huggingface.co/api/spaces
  tags:
  - Demos
  - Deployment
  - Gradio
  - Spaces
  - Streamlit
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/hub/spaces-overview
  - type: Gradio Documentation
    url: https://gradio.app/docs/
  - type: Examples
    url: https://huggingface.co/spaces
  contact:
  - type: Discord
    url: https://discord.gg/hugging-face
- name: Text Generation Inference API
  description: High-performance inference server for large language models with features like continuous batching, token streaming, and tensor parallelism.
  image: https://huggingface.co/front/assets/huggingface_logo.svg
  humanURL: https://huggingface.co/docs/text-generation-inference/index
  baseURL: https://api-inference.huggingface.co/models
  tags:
  - Inference Server
  - Llm
  - Streaming
  - Text Generation
  properties:
  - type: Documentation
    url: https://huggingface.co/docs/text-generation-inference/index
  - type: GitHub Repository
    url: https://github.com/huggingface/text-generation-inference
  - type: API Reference
    url: https://huggingface.co/docs/text-generation-inference/basic_tutorials/consuming_tgi
  - type: Supported Models
    url: https://huggingface.co/docs/text-generation-inference/supported_models
  contact:
  - type: GitHub
    url: https://github.com/huggingface/text-generation-inference/issues
name: Hugging Face Transformers
tags:
- Artificial Intelligence
- Computer Vision
- Deep Learning
- Machine Learning
- Natural Language Processing
- Nlp
- Transformers
type: Contract
image: https://huggingface.co/front/assets/huggingface_logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and resources for Hugging Face Transformers library - a state-of-the-art machine learning library for Natural Language Processing, Computer Vision, and Audio processing tasks.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

