---
aid: google-gemini
url: https://raw.githubusercontent.com/api-evangelist/google-gemini/refs/heads/main/apis.yml
apis:
- name: Gemini API
  description: Generate content using Google's Gemini models with text, image, audio, and video inputs.
  image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
  humanURL: https://ai.google.dev/
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Audio Understanding
  - Chat
  - Image Understanding
  - Multimodal
  - Structured Output
  - Text Generation
  - Video Understanding
  properties:
  - type: Documentation
    url: https://ai.google.dev/docs
  - type: OpenAPI
    url: openapi/google-gemini-api-openapi.yml
  - type: OpenAPI
    url: https://generativelanguage.googleapis.com/$discovery/rest?version=v1beta
  - type: JSON Schema
    url: json-schema/google-gemini-generate-content-schema.json
  - type: JSON-LD Context
    url: json-ld/google-gemini-context.jsonld
  - type: Getting Started
    url: https://ai.google.dev/tutorials/get_started_web
  - type: API Keys
    url: https://aistudio.google.com/app/apikey
  - type: Pricing
    url: https://ai.google.dev/pricing
  - type: Rate Limits
    url: https://ai.google.dev/docs/rate_limits
  - type: Models
    url: https://ai.google.dev/models
  - type: API Reference
    url: https://ai.google.dev/api
  - type: Quickstart
    url: https://ai.google.dev/gemini-api/docs/quickstart
  - type: Change Log
    url: https://ai.google.dev/gemini-api/docs/changelog
  - type: SDKs
    url: https://ai.google.dev/gemini-api/docs/libraries
  - type: OpenAI Compatibility
    url: https://ai.google.dev/gemini-api/docs/openai
  - type: Safety Settings
    url: https://ai.google.dev/gemini-api/docs/safety-settings
  - type: Structured Output
    url: https://ai.google.dev/gemini-api/docs/structured-output
  - type: Token Counting
    url: https://ai.google.dev/gemini-api/docs/tokens
- name: Gemini Pro API
  description: Advanced reasoning and complex task handling.
  baseURL: https://generativelanguage.googleapis.com/v1beta/models/gemini-pro
  tags:
  - Reasoning
  - Text Generation
  properties:
  - type: Documentation
    url: https://ai.google.dev/models/gemini
- name: Gemini Pro Vision API
  description: Multimodal understanding of text and images.
  baseURL: https://generativelanguage.googleapis.com/v1beta/models/gemini-pro-vision
  tags:
  - Image Understanding
  - Multimodal
  - Vision
  properties:
  - type: Documentation
    url: https://ai.google.dev/tutorials/prompting_with_media
- name: Gemini Ultra API
  description: Most capable model for highly complex tasks.
  baseURL: https://generativelanguage.googleapis.com/v1beta/models/gemini-ultra
  tags:
  - Advanced AI
  - Complex Tasks
  properties:
  - type: Documentation
    url: https://ai.google.dev/models/gemini
- name: Gemini Embedding API
  description: Generate text embedding vectors for semantic search, classification, clustering, and retrieval tasks using the gemini-embedding-001 model.
  humanURL: https://ai.google.dev/gemini-api/docs/embeddings
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Embeddings
  - Retrieval
  - Semantic Search
  - Text Similarity
  properties:
  - type: Documentation
    url: https://ai.google.dev/gemini-api/docs/embeddings
- name: Gemini Live API
  description: Low-latency real-time voice and video interactions with Gemini using WebSockets for streaming multimodal input and output.
  humanURL: https://ai.google.dev/gemini-api/docs/live
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Multimodal
  - Real-Time
  - Streaming
  - Video
  - Voice
  - WebSockets
  properties:
  - type: Documentation
    url: https://ai.google.dev/gemini-api/docs/live
- name: Gemini Context Caching API
  description: Cache input tokens for repeated use across multiple requests to reduce costs and improve latency for large context workloads.
  humanURL: https://ai.google.dev/gemini-api/docs/caching
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Caching
  - Cost Optimization
  - Performance
  properties:
  - type: Documentation
    url: https://ai.google.dev/gemini-api/docs/caching
  - type: API Reference
    url: https://ai.google.dev/api/caching
- name: Gemini Fine-Tuning API
  description: Customize Gemini model behavior for specific tasks using supervised fine-tuning with your own training data.
  humanURL: https://ai.google.dev/gemini-api/docs/model-tuning
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Fine-Tuning
  - Model Customization
  - Supervised Learning
  properties:
  - type: Documentation
    url: https://ai.google.dev/gemini-api/docs/model-tuning
  - type: API Reference
    url: https://ai.google.dev/api/tuning
- name: Gemini Interactions API
  description: Unified interface for interacting with Gemini models and agents providing a consistent way to manage multi-turn conversations and tool use.
  humanURL: https://ai.google.dev/gemini-api/docs/interactions
  baseURL: https://generativelanguage.googleapis.com
  tags:
  - Agents
  - Interactions
  - Multi-Turn
  - Tool Use
  properties:
  - type: Documentation
    url: https://ai.google.dev/gemini-api/docs/interactions
- name: Vertex AI Gemini API
  description: Enterprise-grade access to Gemini models through Google Cloud Vertex AI with advanced features including grounding, safety filters, and regional endpoints.
  humanURL: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference
  baseURL: https://aiplatform.googleapis.com
  tags:
  - Enterprise
  - Generative AI
  - Google Cloud
  - Vertex AI
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference
  - type: API Reference
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest
  - type: Quickstart
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstart
  - type: OpenAI Compatibility
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/openai
  - type: Models
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models
  - type: Release Notes
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes
  - type: Pricing
    url: https://cloud.google.com/vertex-ai/pricing
- name: Vertex AI Imagen API
  description: Generate and edit images using Google Imagen models on Vertex AI for high-quality image creation from text prompts.
  humanURL: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview
  baseURL: https://aiplatform.googleapis.com
  tags:
  - Google Cloud
  - Image Generation
  - Imagen
  - Text-To-Image
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/overview
  - type: API Reference
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api
- name: Vertex AI Gemini Live API
  description: Enterprise real-time multimodal streaming API on Vertex AI for building low-latency voice and video AI agents.
  humanURL: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api
  baseURL: https://aiplatform.googleapis.com
  tags:
  - Enterprise
  - Real-Time
  - Streaming
  - Vertex AI
  - Video
  - Voice
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/live-api
  - type: API Reference
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/multimodal-live
- name: Vertex AI Text Embeddings API
  description: Generate text embeddings for semantic search and classification tasks using Google embedding models on Vertex AI.
  humanURL: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings
  baseURL: https://aiplatform.googleapis.com
  tags:
  - Embeddings
  - Semantic Search
  - Text Similarity
  - Vertex AI
  properties:
  - type: Documentation
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings
  - type: API Reference
    url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api
- name: Firebase AI Logic API
  description: Access Gemini API capabilities through Firebase SDKs for mobile and web applications with built-in security and authentication.
  humanURL: https://firebase.google.com/docs/ai-logic
  baseURL: https://firebaseml.googleapis.com
  tags:
  - Client-Side
  - Firebase
  - Mobile
  - Web
  properties:
  - type: Documentation
    url: https://firebase.google.com/docs/ai-logic
  - type: Getting Started
    url: https://firebase.google.com/docs/ai-logic/get-started
  - type: Models
    url: https://firebase.google.com/docs/ai-logic/models
name: Google Gemini
tags:
- Agentic AI
- Artificial Intelligence
- Code Generation
- Embeddings
- Generative AI
- Image Generation
- LLM
- Machine Learning
- Multimodal
type: Contract
image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google's multimodal AI model APIs for text, image, audio, and video understanding.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

