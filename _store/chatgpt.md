---
aid: chatgpt
url: https://raw.githubusercontent.com/api-evangelist/chatgpt/refs/heads/main/apis.yml
apis:
- name: ChatGPT API
  description: API for accessing OpenAI's ChatGPT language models for chat completions and conversations.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/guides/chat
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Chatbot
  - Conversational Ai
  - Machine Learning
  - Natural Language Processing
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/chat
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  - type: OpenAPI
    url: openapi/chatgpt-chat-completions-api-openapi.yml
  - type: JSONSchema
    url: json-schema/chatgpt-chat-completion-schema.json
  - type: JSONLD
    url: json-ld/chatgpt-context.jsonld
  - type: Authentication
    url: https://platform.openai.com/docs/api-reference/authentication
  - type: Pricing
    url: https://openai.com/pricing
  - type: Rate Limits
    url: https://platform.openai.com/docs/guides/rate-limits
  - type: Terms of Service
    url: https://openai.com/terms
  - type: Privacy Policy
    url: https://openai.com/privacy
  - type: Status
    url: https://status.openai.com
  - type: Support
    url: https://help.openai.com
  - type: GitHub
    url: https://github.com/openai
  - type: Getting Started
    url: https://platform.openai.com/docs/quickstart
  - type: Change Log
    url: https://platform.openai.com/docs/changelog
  - type: Blog
    url: https://openai.com/blog
  - type: SDKs
    url: https://developers.openai.com/api/docs/libraries/
  - type: Cookbook
    url: https://cookbook.openai.com/
  - type: Forum
    url: https://community.openai.com/
  - type: Safety
    url: https://openai.com/safety
  - type: Security
    url: https://openai.com/business-data/
  - type: Deprecations
    url: https://platform.openai.com/docs/deprecations
  - type: Models
    url: https://platform.openai.com/docs/models
  - type: Sign Up
    url: https://platform.openai.com/signup
  - type: Login
    url: https://platform.openai.com/login
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Responses API
  description: The Responses API is OpenAI's recommended API primitive for new projects, an evolution of Chat Completions with built-in tools like web search, file search, code interpreter, and support for agentic workflows.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/responses
  baseURL: https://api.openai.com/v1
  tags:
  - Agents
  - Artificial Intelligence
  - Conversational Ai
  - Responses
  - Tools
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/responses
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  - type: OpenAPI
    url: openapi/chatgpt-responses-api-openapi.yml
  - type: JSONSchema
    url: json-schema/chatgpt-response-schema.json
  - type: JSONLD
    url: json-ld/chatgpt-context.jsonld
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Embeddings API
  description: API for generating embedding vectors from input text using models like text-embedding-3-small and text-embedding-3-large, useful for search, clustering, and recommendations.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/embeddings
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Embeddings
  - Machine Learning
  - Search
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/embeddings
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Images API
  description: API for generating and editing images from text prompts using DALL-E and GPT Image models, supporting image generations, edits, and variations.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/images
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Creative Ai
  - Dall-E
  - Image Generation
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/images
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Audio API
  description: API for audio capabilities including text-to-speech generation, speech transcription, and translation using Whisper and other audio models.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/audio
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Audio
  - Speech
  - Text-To-Speech
  - Transcription
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/audio
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Moderations API
  description: API for classifying text and images to detect potentially harmful content across categories like hate, violence, and self-harm.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/moderations
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Content Safety
  - Moderation
  - Trust and Safety
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/moderations
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Fine-Tuning API
  description: API for creating and managing fine-tuning jobs to customize OpenAI models on your own training data, supporting supervised fine-tuning and direct preference optimization.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/fine-tuning
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Fine-Tuning
  - Machine Learning
  - Model Customization
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/fine-tuning
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Files API
  description: API for uploading and managing files used across OpenAI features including fine-tuning, assistants, batch processing, and vision.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/files
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Files
  - Storage
  - Uploads
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/files
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Batch API
  description: API for sending asynchronous groups of requests at lower cost with a separate pool of significantly higher rate limits, supporting chat completions, embeddings, and completions endpoints.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/batch
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Asynchronous
  - Batch Processing
  - Cost Optimization
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/batch
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Uploads API
  description: API for uploading large files in multiple parts, supporting files up to 8 GB for use with fine-tuning, assistants, and batch processing.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/uploads
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Files
  - Large Files
  - Uploads
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/uploads
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Vector Stores API
  description: API for creating and managing vector stores used by the file search tool, supporting collections of processed files for retrieval-augmented generation.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/vector-stores
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - File Search
  - Retrieval
  - Vector Stores
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/vector-stores
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Realtime API
  description: API for real-time multimodal communication with models over WebRTC, WebSocket, and SIP, supporting speech-to-speech, text, image, and audio inputs and outputs with ultra-low latency.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/realtime
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Audio
  - Realtime
  - Speech
  - Websocket
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/realtime
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
- name: OpenAI Models API
  description: API for listing and retrieving information about available OpenAI models, including details on permissions and capabilities.
  image: https://openai.com/content/images/2023/05/openai-avatar.png
  humanURL: https://platform.openai.com/docs/api-reference/models
  baseURL: https://api.openai.com/v1
  tags:
  - Artificial Intelligence
  - Models
  properties:
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference/models
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  contact:
  - type: Support
    url: https://help.openai.com
name: ChatGPT
tags:
- Agents
- Ai
- Chatgpt
- Embeddings
- Fine-Tuning
- Gpt-3.5
- Gpt-4
- Gpt-5
- Language Model
- Openai
- Realtime
type: Contract
image: https://openai.com/content/images/2023/05/openai-avatar.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OpenAI's ChatGPT API for conversational AI and language model interactions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

