---
aid: hugging-face-transformers
name: Hugging Face Transformers
description: Hugging Face Transformers is an open-source machine learning library providing thousands of pretrained models and pipelines for Natural Language Processing, Computer Vision, Audio, and multimodal tasks. This index covers the Transformers library and the surrounding Hugging Face APIs that developers use to run inference, manage models, deploy demos, and serve LLMs at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Computer Vision
  - Deep Learning
  - Machine Learning
  - Natural Language Processing
  - Open Source
  - Transformers
url: https://raw.githubusercontent.com/api-evangelist/hugging-face-transformers/refs/heads/main/apis.yml
created: '2024'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hugging-face-transformers:transformers-library
    name: Hugging Face Transformers Library
    description: Open-source Python library that provides pretrained models, tokenizers, and pipelines for inference and fine-tuning across NLP, vision, audio, and multimodal tasks. The high-level pipeline API gives drop-in access to text generation, classification, translation, summarization, speech recognition, and many other tasks.
    humanURL: https://huggingface.co/docs/transformers/index
    tags:
      - Library
      - Open Source
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
      - type: Issues
        url: https://github.com/huggingface/transformers/issues
  - aid: hugging-face-transformers:inference-api
    name: Hugging Face Inference API
    description: Serverless inference API for running predictions against thousands of models hosted on the Hugging Face Hub. Supports NLP, computer vision, audio, and multimodal tasks through a unified HTTP interface.
    humanURL: https://huggingface.co/docs/api-inference/index
    baseURL: https://api-inference.huggingface.co
    tags:
      - Inference
      - Predictions
      - Serverless
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/api-inference/index
      - type: Authentication
        url: https://huggingface.co/docs/api-inference/quicktour#authentication
      - type: Pricing
        url: https://huggingface.co/pricing
  - aid: hugging-face-transformers:hub-api
    name: Hugging Face Hub API
    description: REST API for interacting with the Hugging Face Hub - upload, download, and manage models, datasets, and spaces programmatically.
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
      - type: GitHub
        url: https://github.com/huggingface/huggingface_hub
  - aid: hugging-face-transformers:spaces-api
    name: Hugging Face Spaces API
    description: API for deploying and managing machine learning applications and demos using Gradio, Streamlit, or Docker on Hugging Face Spaces.
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
  - aid: hugging-face-transformers:text-generation-inference
    name: Text Generation Inference (TGI)
    description: High-performance inference server for large language models with continuous batching, token streaming, tensor parallelism, and OpenAI-compatible chat completions endpoints.
    humanURL: https://huggingface.co/docs/text-generation-inference/index
    tags:
      - Inference Server
      - LLM
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
common:
  - type: Website
    url: https://huggingface.co
  - type: Blog
    url: https://huggingface.co/blog
  - type: Documentation
    url: https://huggingface.co/docs
  - type: Discord
    url: https://discord.gg/hugging-face
  - type: GitHub Organization
    url: https://github.com/huggingface
  - type: Twitter
    url: https://twitter.com/huggingface
  - type: LinkedIn
    url: https://www.linkedin.com/company/huggingface
  - type: YouTube
    url: https://www.youtube.com/c/HuggingFace
  - type: Terms of Service
    url: https://huggingface.co/terms-of-service
  - type: Privacy Policy
    url: https://huggingface.co/privacy
  - type: Sign Up
    url: https://huggingface.co/join
  - type: Rules
    url: https://raw.githubusercontent.com/api-evangelist/hugging-face-transformers/refs/heads/main/hugging-face-transformers-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
