---
name: ChatGPT
description: OpenAI's ChatGPT API for conversational AI and language model interactions.
image: https://openai.com/content/images/2023/05/openai-avatar.png
url: https://platform.openai.com/docs/api-reference
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Contract
access: 3rd-Party
apis:
  - name: ChatGPT API
    description: API for accessing OpenAI's ChatGPT language models for chat completions and conversations.
    image: https://openai.com/content/images/2023/05/openai-avatar.png
    humanURL: https://platform.openai.com/docs/guides/chat
    baseURL: https://api.openai.com/v1
    tags:
      - Artificial Intelligence
      - Chatbot
      - Conversational AI
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
      - type: RateLimits
        url: https://platform.openai.com/docs/guides/rate-limits
      - type: TermsOfService
        url: https://openai.com/terms
      - type: PrivacyPolicy
        url: https://openai.com/privacy
      - type: StatusPage
        url: https://status.openai.com
      - type: Support
        url: https://help.openai.com
      - type: GitHubOrganization
        url: https://github.com/openai
      - type: GettingStarted
        url: https://platform.openai.com/docs/quickstart
      - type: ChangeLog
        url: https://platform.openai.com/docs/changelog
      - type: Blog
        url: https://openai.com/blog
      - type: SDK
        url: https://developers.openai.com/api/docs/libraries/
      - type: Security
        url: https://openai.com/business-data/
      - type: Models
        url: https://platform.openai.com/docs/models
      - type: SignUp
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
      - Conversational AI
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
        url: json-ld/chatgpt-responses-context.jsonld
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
      - Creative AI
      - DALL-E
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
      - Trust And Safety
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
      - WebSocket
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
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
  - name: OpenAI
    email: support@openai.com
    url: https://openai.com
common:
  - type: Portal
    url: https://platform.openai.com
  - type: Documentation
    url: https://platform.openai.com/docs/api-reference
  - type: GettingStarted
    url: https://platform.openai.com/docs/quickstart
  - type: Authentication
    url: https://platform.openai.com/docs/api-reference/authentication
  - type: Pricing
    url: https://openai.com/pricing
  - type: RateLimits
    url: https://platform.openai.com/docs/guides/rate-limits
  - type: ChangeLog
    url: https://platform.openai.com/docs/changelog
  - type: Blog
    url: https://openai.com/blog
  - type: StatusPage
    url: https://status.openai.com
  - type: Support
    url: https://help.openai.com
  - type: GitHubOrganization
    url: https://github.com/openai
  - type: SDK
    url: https://developers.openai.com/api/docs/libraries/
  - type: CodeExamples
    url: https://cookbook.openai.com/
  - type: OpenAPI
    url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
  - type: TermsOfService
    url: https://openai.com/terms
  - type: PrivacyPolicy
    url: https://openai.com/privacy
  - type: Security
    url: https://openai.com/business-data/
  - type: Models
    url: https://platform.openai.com/docs/models
  - type: SignUp
    url: https://platform.openai.com/signup
  - type: Login
    url: https://platform.openai.com/login
  - type: Features
    data:
      - name: Chat Completions
        description: Generate conversational responses using GPT models with support for text, function calling, structured outputs, vision inputs, and streaming.
      - name: Responses API
        description: Next-generation API with built-in tools for web search, file search, computer use, and code interpreter supporting agentic workflows.
      - name: Embeddings
        description: Generate vector representations of text for search, clustering, classification, and recommendation use cases.
      - name: Image Generation
        description: Create and edit images from text prompts using DALL-E and GPT Image models.
      - name: Audio and Speech
        description: Text-to-speech generation, speech transcription, and translation using Whisper and other audio models.
      - name: Content Moderation
        description: Classify text and images to detect potentially harmful content across safety categories.
      - name: Fine-Tuning
        description: Customize OpenAI models on your own training data for domain-specific performance improvements.
      - name: Batch Processing
        description: Send asynchronous groups of requests at lower cost with higher rate limits.
      - name: Realtime Communication
        description: Ultra-low latency multimodal communication over WebRTC, WebSocket, and SIP.
      - name: Vector Stores
        description: Manage collections of processed files for retrieval-augmented generation with the file search tool.
  - type: UseCases
    data:
      - name: Customer Support Automation
        description: Build AI-powered chatbots and support agents that handle customer inquiries, troubleshoot issues, and escalate complex cases.
      - name: Content Generation
        description: Generate marketing copy, blog posts, product descriptions, and creative content at scale.
      - name: Code Assistance
        description: Help developers write, review, debug, and explain code across multiple programming languages.
      - name: Data Analysis
        description: Extract insights from unstructured text, summarize documents, and perform sentiment analysis.
      - name: Multimodal Applications
        description: Build applications that process text, images, and audio inputs together for richer user experiences.
      - name: Agentic Workflows
        description: Create autonomous AI agents that use tools, search the web, and execute multi-step tasks.
  - type: Integrations
    data:
      - name: Microsoft Azure OpenAI
        description: Deploy OpenAI models on Azure infrastructure with enterprise security, compliance, and regional availability.
      - name: LangChain
        description: Build LLM-powered applications using the LangChain framework with OpenAI model providers.
      - name: Zapier
        description: Connect ChatGPT to thousands of apps for automated workflows without code.
      - name: Slack
        description: Integrate ChatGPT into Slack workspaces for team collaboration and AI-assisted communication.
tags:
  - Agents
  - AI
  - ChatGPT
  - Embeddings
  - Fine-Tuning
  - GPT-4
  - GPT-5
  - Language Model
  - OpenAI
  - Realtime
---
