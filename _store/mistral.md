---
aid: mistral
name: Mistral AI
description: Mistral AI provides state-of-the-art large language models and AI APIs for developers and enterprises.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024'
modified: '2026-05-04'
specificationVersion: '0.19'
url: https://docs.mistral.ai/apis.json
apis:
  - name: Mistral AI Chat API
    description: Chat completion API for conversational AI using Mistral's language models.
    image: https://mistral.ai/images/chat-icon.png
    humanURL: https://docs.mistral.ai/api/
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Chat
      - Conversational AI
      - Large Language Models
      - NLP
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/
      - type: OpenAPI
        url: https://docs.mistral.ai/openapi.json
      - type: Authentication
        url: https://docs.mistral.ai/api/#authentication
      - type: APIEndpoint
        url: https://docs.mistral.ai/api/endpoint/chat
      - type: OpenAPI
        url: openapi/mistral-chat-openapi.yml
    contact:
      - type: Support
        url: https://docs.mistral.ai/
      - type: Email
        url: mailto:support@mistral.ai
  - name: Mistral Embeddings API
    description: Generate vector embeddings for text and code using Mistral's embedding models for retrieval, clustering, classification, and semantic search.
    image: https://mistral.ai/images/embeddings-icon.png
    humanURL: https://docs.mistral.ai/api/#embeddings
    baseURL: https://api.mistral.ai/v1
    tags:
      - Embeddings
      - Machine Learning
      - Semantic Search
      - Vector Search
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/#embeddings
      - type: Pricing
        url: https://mistral.ai/technology/#pricing
      - type: APIEndpoint
        url: https://docs.mistral.ai/api/endpoint/embeddings
      - type: OpenAPI
        url: openapi/mistral-embeddings-openapi.yml
  - name: Mistral Moderation API
    description: Content moderation and classification API for detecting potentially harmful or inappropriate content across nine safety categories including text and chat moderation.
    image: https://mistral.ai/images/moderation-icon.png
    humanURL: https://docs.mistral.ai/api/#moderation
    baseURL: https://api.mistral.ai/v1
    tags:
      - Classification
      - Compliance
      - Content Moderation
      - Safety
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/#moderation
      - type: APIEndpoint
        url: https://docs.mistral.ai/api/endpoint/classifiers
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/guardrailing
      - type: OpenAPI
        url: openapi/mistral-moderation-openapi.yml
  - name: Mistral AI Agents API
    description: Agent completions API for building AI agents that can handle complex tasks, maintain context, coordinate multiple actions, and use tools including function calling.
    humanURL: https://docs.mistral.ai/api/endpoint/agents
    baseURL: https://api.mistral.ai/v1
    tags:
      - Agents
      - Artificial Intelligence
      - Automation
      - Function Calling
      - Tools
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/agents
      - type: GettingStarted
        url: https://docs.mistral.ai/agents/agents
      - type: OpenAPI
        url: openapi/mistral-agents-openapi.yml
  - name: Mistral AI FIM API
    description: Fill-in-the-Middle code completion API powered by Codestral for generating code between a given prompt and suffix, supporting over 80 programming languages.
    humanURL: https://docs.mistral.ai/api/endpoint/fim
    baseURL: https://api.mistral.ai/v1
    tags:
      - Code Completion
      - Code Generation
      - Codestral
      - Fill in the Middle
      - Programming
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/fim
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/code_generation
      - type: OpenAPI
        url: openapi/mistral-fim-openapi.yml
  - name: Mistral AI OCR API
    description: Optical Character Recognition API that extracts text, images, tables, and structured data from documents and PDFs with support for complex layouts, LaTeX, and mathematical expressions.
    humanURL: https://docs.mistral.ai/api/endpoint/ocr
    baseURL: https://api.mistral.ai/v1
    tags:
      - Document AI
      - Document Understanding
      - OCR
      - PDF Processing
      - Text Extraction
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/ocr
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/document_ai
      - type: OpenAPI
        url: openapi/mistral-ocr-openapi.yml
  - name: Mistral AI Fine-Tuning API
    description: Fine-tuning API for customizing Mistral models on your own datasets, supporting text, vision, and classifier fine-tuning with configurable hyperparameters and integrations.
    humanURL: https://docs.mistral.ai/api/endpoint/fine-tuning
    baseURL: https://api.mistral.ai/v1
    tags:
      - Fine-Tuning
      - Machine Learning
      - Model Customization
      - Training
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/fine-tuning
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/finetuning/text_vision_finetuning
      - type: OpenAPI
        url: openapi/mistral-fine-tuning-openapi.yml
  - name: Mistral AI Files API
    description: File management API for uploading, retrieving, downloading, and deleting files used across fine-tuning, batch processing, and OCR endpoints with support for files up to 512 MB.
    humanURL: https://docs.mistral.ai/api/endpoint/files
    baseURL: https://api.mistral.ai/v1
    tags:
      - File Management
      - Files
      - Storage
      - Upload
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/files
      - type: OpenAPI
        url: openapi/mistral-files-openapi.yml
  - name: Mistral AI Models API
    description: Models management API for listing available models, retrieving model details, and managing fine-tuned models including archiving and updating.
    humanURL: https://docs.mistral.ai/api/endpoint/models
    baseURL: https://api.mistral.ai/v1
    tags:
      - Artificial Intelligence
      - Model Management
      - Models
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/models
      - type: OpenAPI
        url: openapi/mistral-models-openapi.yml
  - name: Mistral AI Batch API
    description: Batch inference API for processing up to one million requests asynchronously at reduced cost, supporting chat completions, embeddings, FIM, moderations, OCR, classifications, and audio transcriptions.
    humanURL: https://docs.mistral.ai/api/endpoint/batch
    baseURL: https://api.mistral.ai/v1
    tags:
      - Async
      - Batch Processing
      - Bulk Operations
      - Cost Optimization
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/batch
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/batch
      - type: OpenAPI
        url: openapi/mistral-batch-openapi.yml
  - name: Mistral AI Audio Transcription API
    description: Audio transcription API powered by Voxtral for converting speech to text with support for speaker diarization, word-level timestamps, context biasing, and real-time streaming across 13 languages.
    humanURL: https://docs.mistral.ai/api/endpoint/audio/transcriptions
    baseURL: https://api.mistral.ai/v1
    tags:
      - Audio
      - Diarization
      - Speech to Text
      - Transcription
      - Voxtral
    properties:
      - type: Documentation
        url: https://docs.mistral.ai/api/endpoint/audio/transcriptions
      - type: GettingStarted
        url: https://docs.mistral.ai/capabilities/audio/
      - type: OpenAPI
        url: openapi/mistral-audio-transcription-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://mistral.ai
  - type: Documentation
    url: https://docs.mistral.ai
  - type: Getting Started
    url: https://docs.mistral.ai/getting-started/
  - type: Terms of Service
    url: https://mistral.ai/terms/
  - type: Privacy Policy
    url: https://mistral.ai/privacy/
  - type: Pricing
    url: https://mistral.ai/technology/#pricing
  - type: Status
    url: https://status.mistral.ai
  - type: GitHub
    url: https://github.com/mistralai
  - type: Twitter
    url: https://twitter.com/MistralAI
  - type: LinkedIn
    url: https://www.linkedin.com/company/mistralai
  - type: Discord
    url: https://discord.gg/mistralai
  - type: Portal
    url: https://docs.mistral.ai/api
  - type: Blog
    url: https://mistral.ai/news
  - type: ChangeLog
    url: https://docs.mistral.ai/getting-started/changelog
  - type: SignUp
    url: https://console.mistral.ai
  - type: Pricing
    url: https://mistral.ai/pricing
  - type: SDKs
    url: https://docs.mistral.ai/getting-started/clients
  - type: PythonSDK
    url: https://github.com/mistralai/client-python
  - type: TypeScriptSDK
    url: https://github.com/mistralai/client-ts
  - type: GettingStarted
    url: https://docs.mistral.ai/getting-started/quickstart
  - type: JSON-LD
    url: json-ld/mistral-context.jsonld
  - type: JSONSchema
    url: json-schema/mistral-chat-completion-schema.json
  - type: JSONSchema
    url: json-schema/mistral-model-schema.json
  - type: JSONSchema
    url: json-schema/mistral-fine-tuning-job-schema.json
  - type: JSONSchema
    url: json-schema/mistral-file-schema.json
  - type: Features
    data:
      - Mistral Large 2 at $2/$6 per MTok
      - Mistral Medium 3 at $0.40/$2
      - Mistral Small 3 at $0.10/$0.30
      - Ministral 3B at $0.04/$0.04 (smallest commercial model)
      - Mistral Nemo at $0.02/$0.04 (cheapest tier)
      - Codestral at $0.30/$0.90 for code completion/FIM
      - Pixtral Large for vision
      - Mixtral 8x22B mixture-of-experts
      - La Plateforme free tier with 1 RPS
      - 'Paid tier: 10 RPS, 5M TPM'
      - OpenAI-compatible Chat Completions
      - Function calling and tool use
      - JSON mode and guided generation
      - Embed model for semantic search
      - Available on AWS Bedrock, Azure AI, Vertex AI
      - Fine-tuning service for select models
    sources:
      - https://mistral.ai/pricing
    updated: '2026-05-04'
---
