---
aid: openai
url: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/apis.yml
apis:
  - aid: openai:openai-assistants-api
    name: OpenAI Assistants API
    tags:
      - Assistants
    score: 1329
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/assistants/overview
    properties:
      - url: https://platform.openai.com/docs/assistants/overview
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/assistants
        type: Documentation
      - url: openapi/assistants-openapi-original.yml
        type: OpenAPI
    description: The Assistants API allows you to build AI assistants within your own applications. An Assistant has instructions and can leverage models, tools, and knowledge to respond to user queries. The Assistants API currently supports three types of tools - Code Interpreter, Retrieval, and Function calling. In the future, we plan to release more OpenAI-built tools, and allow you to provide your own tools on our platform.
  - aid: openai:openai-audio-api
    name: OpenAI Audio API
    tags:
      - Audio
    score: 128
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/text-to-speech
    properties:
      - url: https://platform.openai.com/docs/guides/text-to-speech
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/audio
        type: Documentation
      - url: https://platform.openai.com/docs/guides/speech-to-text
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/audio/
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/voice-agents/
        type: Documentation
      - url: openapi/audio-openapi-original.yml
        type: OpenAPI
      - url: openapi/openai-audio-openapi.yml
        type: OpenAPI
      - url: json-ld/openai-context.jsonld
        type: JSONLD
    description: The Audio API provides two speech to text endpoints, transcriptions and translations, based on our state-of-the-art open source large-v2 Whisper model.
  - aid: openai:openai-chat-api
    name: OpenAI Chat API
    tags:
      - Chat
    score: 149
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/chat
    properties:
      - url: https://platform.openai.com/docs/api-reference/chat
        type: Documentation
      - url: openapi/chat-openapi-original.yml
        type: OpenAPI
      - url: openapi/openai-chat-completions-openapi.yml
        type: OpenAPI
      - url: json-schema/openai-chat-completion-schema.json
        type: JSONSchema
      - url: json-ld/openai-context.jsonld
        type: JSONLD
    description: Given a list of messages comprising a conversation, the model will return a response., providing an AI chat interface you can use to engage with users.
  - aid: openai:openai-chat-completions-api
    name: OpenAI Chat Completions API
    tags:
      - Chat
      - Completions
    score: 281
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/chat
    properties:
      - url: https://platform.openai.com/docs/api-reference/chat
        type: Documentation
      - url: properties/openai-chat-completions-api-openapi.yml
        type: OpenAPI
      - url: openapi/openai-chat-completions-openapi.yml
        type: OpenAPI
      - url: json-schema/openai-chat-completion-schema.json
        type: JSONSchema
      - url: json-ld/openai-context.jsonld
        type: JSONLD
    description: Chat models take a list of messages as input and return a model-generated message as output. Although the chat format is designed to make multi-turn conversations easy, it's just as useful for single-turn tasks without any conversation.
  - aid: openai:openai-embeddings-api
    name: OpenAI Embeddings API
    tags:
      - Embedding
      - Embeddings
      - Inputs
      - Representing
      - Text
      - Vectors
    score: 112
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/embeddings
    properties:
      - url: https://platform.openai.com/docs/guides/embeddings
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/embeddings
        type: Documentation
      - url: openapi/embeddings-openapi-original.yml
        type: OpenAPI
      - url: openapi/openai-embeddings-openapi.yml
        type: OpenAPI
      - url: json-schema/openai-embedding-schema.json
        type: JSONSchema
      - url: json-ld/openai-context.jsonld
        type: JSONLD
    description: Learn how to turn text into numbers, unlocking use cases like search. OpenAI's text embeddings measure the relatedness of text strings.
  - aid: openai:openai-files-api
    name: OpenAI Files API
    tags:
      - AI
      - Artificial Intelligence
      - Files
    score: 894
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/files
    properties:
      - url: https://platform.openai.com/docs/api-reference/files
        type: Documentation
      - url: openapi/files-openapi-original.yml
        type: OpenAPI
    description: Files are used to upload documents that can be used with features like Assistants and Fine-tuning. Upload a file that can be used across various endpoints. The size of all the files uploaded by one organization can be up to 100 GB.
  - aid: openai:openai-fine-tuning-api
    name: OpenAI Fine Tuning API
    tags:
      - Fine Tune
      - Fine Tuning
    score: 492
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/fine-tuning
    properties:
      - url: https://platform.openai.com/docs/guides/fine-tuning
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/fine-tuning
        type: Documentation
      - url: openapi/fine-tuning-openapi-original.yml
        type: OpenAPI
    description: Manage fine-tuning jobs to tailor a model to your specific training data. Creates a fine-tuning job which begins the process of creating a new model from a given dataset.Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.
  - aid: openai:openai-images-api
    name: OpenAI Images API
    tags:
      - Images
    score: 120
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/guides/images
    properties:
      - url: https://platform.openai.com/docs/guides/images
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/images
        type: Documentation
      - url: https://platform.openai.com/docs/guides/image-generation
        type: Documentation
      - url: https://platform.openai.com/docs/guides/images-vision
        type: Documentation
      - url: openapi/images-openapi-original.yml
        type: OpenAPI
      - url: openapi/openai-images-openapi.yml
        type: OpenAPI
      - url: json-ld/openai-context.jsonld
        type: JSONLD
    description: Learn how to generate or manipulate images with DALL_E in the API. The Images API provides three methods for interacting with images - creating images from scratch based on a text prompt, creating edited versions of images by having the model replace some areas of a pre-existing image, based on a new text prompt, Creating variations of an existing image.
  - aid: openai:openai-models-api
    name: OpenAI Models API
    tags:
      - Large Language Models
      - Models
    score: 201
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/models
    properties:
      - url: https://platform.openai.com/docs/models
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/models
        type: Documentation
      - url: openapi/models-openapi-original.yml
        type: OpenAPI
    description: List and describe the various models available in the API. You can refer to the Models documentation to understand what models are available and the differences between them.
  - aid: openai:openai-threads-api
    name: OpenAI Threads API
    tags:
      - Assistants
      - Threads
    score: 1861
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages
    properties:
      - url: https://platform.openai.com/docs/assistants/how-it-works/managing-threads-and-messages
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/threads
        type: Documentation
      - url: openapi/threads-openapi-original.yml
        type: OpenAPI
    description: Create threads that assistants can interact with.
  - aid: openai:openai-responses-api
    name: OpenAI Responses API
    tags:
      - Agents
      - Responses
      - Text Generation
    score: 150
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/responses
    properties:
      - url: https://platform.openai.com/docs/api-reference/responses
        type: Documentation
      - url: https://platform.openai.com/docs/guides/text
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/deep-research/
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/conversation-state/
        type: Documentation
    description: The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs into a single streamlined interface, supporting text and image inputs, text outputs, and built-in tools like web search, file search, computer use, and code interpreter. Recommended for all new projects.
  - aid: openai:openai-moderations-api
    name: OpenAI Moderations API
    tags:
      - Content Safety
      - Moderation
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/moderations
    properties:
      - url: https://platform.openai.com/docs/api-reference/moderations
        type: Documentation
      - url: https://platform.openai.com/docs/guides/moderation
        type: Documentation
    description: The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including harassment, hate speech, sexual content, self-harm, violence, and illicit content. The moderation endpoint is free to use and supports the omni-moderation-latest model for multi-modal inputs.
  - aid: openai:openai-batch-api
    name: OpenAI Batch API
    tags:
      - Async
      - Batch
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/batch
    properties:
      - url: https://platform.openai.com/docs/api-reference/batch
        type: Documentation
      - url: https://platform.openai.com/docs/guides/batch
        type: Documentation
    description: The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports /v1/responses, /v1/chat/completions, /v1/embeddings, /v1/completions, and /v1/moderations endpoints. A single batch may include up to 50,000 requests with a batch input file size up to 200 MB.
  - aid: openai:openai-vector-stores-api
    name: OpenAI Vector Stores API
    tags:
      - Retrieval
      - Search
      - Vector Stores
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/vector-stores
    properties:
      - url: https://platform.openai.com/docs/api-reference/vector-stores
        type: Documentation
      - url: https://platform.openai.com/docs/guides/retrieval
        type: Documentation
    description: Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a file to a vector store it is automatically chunked, embedded, and indexed. You can query a vector store using natural language to retrieve relevant chunks with similarity scores.
  - aid: openai:openai-uploads-api
    name: OpenAI Uploads API
    tags:
      - Files
      - Uploads
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/uploads
    properties:
      - url: https://platform.openai.com/docs/api-reference/uploads
        type: Documentation
    description: The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in total and expires after an hour. Once you complete the Upload, a File object is created that can be used across the platform.
  - aid: openai:openai-realtime-api
    name: OpenAI Realtime API
    tags:
      - Audio
      - Realtime
      - Streaming
      - Voice
    score: 150
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/realtime
    properties:
      - url: https://platform.openai.com/docs/api-reference/realtime
        type: Documentation
      - url: https://platform.openai.com/docs/guides/realtime
        type: Documentation
      - url: https://platform.openai.com/docs/guides/realtime-webrtc
        type: Documentation
      - url: https://platform.openai.com/docs/guides/realtime-server-controls
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/realtime-conversations/
        type: Documentation
    description: The Realtime API enables low-latency, bidirectional communication with models that natively support speech-to-speech interactions as well as multimodal inputs (audio, images, and text) and outputs (audio and text). It supports WebRTC, WebSocket, and SIP connection methods for real-time voice agents and conversational interfaces.
  - aid: openai:openai-evals-api
    name: OpenAI Evals API
    tags:
      - Evals
      - Evaluation
      - Testing
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/evals
    properties:
      - url: https://platform.openai.com/docs/api-reference/evals
        type: Documentation
      - url: https://platform.openai.com/docs/guides/evals
        type: Documentation
    description: The Evals API allows you to programmatically configure and run evaluations to test model outputs against your expectations. Evaluations ensure model responses meet style and content criteria you specify, and are essential for building reliable LLM applications, especially when upgrading or trying new models.
  - aid: openai:openai-completions-api
    name: OpenAI Completions API
    tags:
      - Completions
      - Legacy
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/completions
    properties:
      - url: https://platform.openai.com/docs/api-reference/completions
        type: Documentation
      - url: openapi/completions-openapi-original.yml
        type: OpenAPI
    description: The legacy Completions API endpoint provides a freeform text completion interface using a text prompt. Unlike the Chat Completions endpoint which uses a list of messages, the Completions API input is a freeform text string called a prompt. This endpoint received its last update in July 2023.
  - aid: openai:openai-videos-api
    name: OpenAI Videos API
    tags:
      - Sora
      - Video Generation
      - Videos
    score: 150
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/videos
    properties:
      - url: https://platform.openai.com/docs/api-reference/videos
        type: Documentation
      - url: https://platform.openai.com/docs/guides/video-generation
        type: Documentation
    description: The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from a text prompt, checking video status, downloading finished MP4 files, listing videos with pagination, and deleting videos from storage. Supported models include sora-2 and sora-2-pro.
  - aid: openai:openai-conversations-api
    name: OpenAI Conversations API
    tags:
      - Conversations
      - State Management
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/conversations/create
    properties:
      - url: https://platform.openai.com/docs/api-reference/conversations/create
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/conversation-state/
        type: Documentation
    description: The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a created_at timestamp, and metadata. Because conversations are stateful, managing context across conversations is handled automatically, and the /responses/compact endpoint can shrink context for long-running conversations.
  - aid: openai:openai-containers-api
    name: OpenAI Containers API
    tags:
      - Code Interpreter
      - Containers
      - Sandbox
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/containers
    properties:
      - url: https://platform.openai.com/docs/api-reference/containers
        type: Documentation
      - url: https://platform.openai.com/docs/api-reference/container-files
        type: Documentation
      - url: https://developers.openai.com/api/docs/guides/tools-code-interpreter/
        type: Documentation
    description: The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers can be created explicitly or auto-managed, with configurable memory limits of 1g, 4g, 16g, or 64g. Container files can be uploaded, listed, retrieved, and downloaded. Containers expire after 20 minutes of inactivity.
  - aid: openai:openai-chatkit-api
    name: OpenAI ChatKit API
    tags:
      - Agents
      - Chat
      - ChatKit
    score: 100
    baseURL: https://api.openai.com
    humanURL: https://platform.openai.com/docs/api-reference/chatkit
    properties:
      - url: https://platform.openai.com/docs/api-reference/chatkit
        type: Documentation
      - url: https://platform.openai.com/docs/guides/chatkit
        type: Documentation
    description: ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants, research companions, support agents, and more. ChatKit sessions include resolved feature configuration for automatic thread titling, file upload, and history settings. Threads have statuses including active, locked, and closed.
name: OpenAI
tags:
  - AI
  - Artificial Intelligence
  - Large Language Models
  - T1
type: Contract
score: 308
access: 3rd-Party
common:
  - url: https://platform.openai.com/docs/overview
    name: Overview - OpenAI API
    type: Portal
    description: 'null'
  - url: https://platform.openai.com/docs/quickstart
    name: Developer quickstart - OpenAI API
    type: GettingStarted
    description: 'null'
  - url: https://platform.openai.com/docs/libraries
    name: Libraries - OpenAI API
    type: SDKs
    description: 'null'
  - url: https://community.openai.com/categories
    name: Categories - OpenAI Developer Community
    type: Forums
    description: 'null'
  - url: https://platform.openai.com/docs/guides/rate-limits
    name: Rate limits - OpenAI API
    type: RateLimits
    description: 'null'
  - url: https://platform.openai.com/docs/deprecations
    name: Deprecations - OpenAI API
    type: Deprecations
    description: 'null'
  - url: https://openai.com/policies/
    name: Terms & policies | OpenAI
    type: TermsOfService
    description: 'null'
  - url: https://openai.com/policies/terms-of-use/
    name: Terms of use | OpenAI
    type: TermsOfService
    description: 'null'
  - url: https://openai.com/policies/privacy-policy/
    name: Privacy policy | OpenAI
    type: PrivacyPolicy
    description: 'null'
  - url: https://platform.openai.com/docs/overview
    name: Overview - OpenAI API
    type: Documentation
    description: 'null'
  - url: https://help.openai.com/en
    name: OpenAI Help Center
    type: Support
    description: 'null'
  - url: https://status.openai.com/
    name: OpenAI Status
    type: Status
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/authentication
    name: API Reference - OpenAI API
    type: Authentication
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/webhook_events/response
    name: API Reference - OpenAI API
    type: Webhooks
    description: 'null'
  - url: properties/openai-openapi
    name: OpenAPI
    type: OpenAPI
  - url: json-schema/openai-chat-completion-schema.json
    name: Chat Completion JSON Schema
    type: JSONSchema
    description: 'null'
  - url: json-schema/openai-embedding-schema.json
    name: Embedding JSON Schema
    type: JSONSchema
    description: 'null'
  - url: json-ld/openai-context.jsonld
    name: OpenAI JSON-LD Context
    type: JSONLD
    description: 'null'
  - url: https://github.com/openai
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://openai.com/api/pricing/
    data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 0
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Access to GPT5
          - name: Real-time data from the web with search
          - name: Limited access to file uploads, data analysis, image generation, and voice mode
          - name: Code edits with the ChatGPT desktop app for macOS
          - name: Use custom GPTs
        description: Explore how AI can help with everyday tasks
      - id: plus
        name: Plus
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $20.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Extended access to GPT5, our flagship model
          - name: Extended limits on messaging, file uploads, data analysis, and image generation
          - name: Standard and advanced voice mode with video and screensharing
          - name: Access to ChatGPT agent
          - name: Create and use projects, tasks, and custom GPTs
          - name: Limited access to Sora video generation
          - name: Opportunities to test new features
        description: Level up productivity and creativity with expanded access
      - id: pro
        name: Pro
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $200.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Unlimited access to GPT5
          - name: Access to GPT5 pro, which uses more compute for the best answers to the hardest questions
          - name: Unlimited access to advanced voice, with higher limits for video and screensharing
          - name: Access to OpenAI o3pro, which uses more compute for the best answers to the hardest questions
          - name: Extended access to ChatGPT agent
          - name: Extended access to Sora video generation
          - name: Access to research preview of Codex agent
        description: Get the best of OpenAI with the highest level of access
      - id: team
        name: Team
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: $25.00
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Unlimited GPT5 messages, with generous access to GPT5 thinking, and access to GPT5 proplus the flexibility to add credits as needed
          - name: A secure, dedicated workspace with essential admin controls, SAML SSO, and MFA
          - name: Team data is excluded from training by default, with encryption at rest and in transit. Learn more`
          - name: Support for compliance with GDPR, CCPA, and other privacy laws. Aligned with CSA STAR` and SOC 2 Type 2 Trust Services Criteria.
          - name: Connectors to apps for more personalized answersGoogle Drive, SharePoint, GitHub, Notion, and more
          - name: Business features like data analysis, record mode, canvas, projects, tasks, custom workspace GPTs, and deep research
          - name: Includes access to Codex and ChatGPT agent for reasoning and taking action across your documents, tools, and codebases
        description: A secure, collaborative workspace for startups and growing teams
      - id: enterprise
        name: Enterprise
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Contact
            metric: user
            timeFrame: month
            description: User based pricing.
        elements:
          - name: Expanded context window that supports longer inputs and larger files
          - name: Enterprise-level security and controls, including SCIM, user analytics, domain verification, and role-based access controls
          - name: Advanced data privacy with custom data retention policies, encryption at rest and in transit, and no training on your business data by default. Learn more`
          - name: Support for data residency in seven regions
          - name: 24/7 priority support, SLAs, custom legal terms, and access to AI advisors for eligible customers
          - name: Built for scale with volume discounts, invoicing and ACH billing, and support for unlimited users
        description: Enterprise-grade AI, security, and support at scale
    name: Plans
    type: Plans
    description: This is the description of the plans for general OpenAI usage.
  - url: https://openai.com/api/pricing/
    data:
      - id: gpt-5
        name: GPT-5
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 1.25
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.125
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 10
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: The best model for coding and agentic tasks across industries.
      - id: gpt-5-mini
        name: GPT-5 mini
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.25
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.025
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 2
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: A faster, cheaper version of GPT-5 for well-defined tasks.
      - id: gpt-5-nano
        name: GPT-5 nano
        type: Flagship
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.05
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.005
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 0.4
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
        description: The fastest, cheapest version of GPT-5great for summarization and classification tasks.
      - id: gpt-4-1
        name: GPT-4.1
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 3
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.75
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 12
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 25
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: gpt-4-1-mini
        name: GPT-4.1 mini
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.8
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.2
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 3.2
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 5
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: gpt-4-1-nano
        name: GPT-4.1 nano
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.2
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 0.05
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 0.8
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 1.5
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
      - id: o4-mini
        name: o4-mini
        type: Fine-Tuning
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 4
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Cached Input
            price: 1
            metric: token
            timeFrame: usage
            description: Cached input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 16
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Training
            price: 100
            metric: token
            timeFrame: usage
            description: Training token usage-based pricing.
        description: No description.
    name: Pricing
    type: Pricing
    description: this is the pricing for API usage across different models.
  - url: https://openai.com/api/pricing/
    data:
      - name: Free
        description: User must be in an allowed geography.
      - name: Tier 1
        description: "$5 paid\t$100 / month"
      - name: Tier 2
        description: "$50 paid and 7+ days since first successful payment\t$500 / month"
      - name: Tier 3
        description: "$100 paid and 7+ days since first successful payment\t$1,000 / month"
      - name: Tier 4
        description: "$250 paid and 14+ days since first successful payment\t$5,000 / month"
      - name: Tier 5
        description: "$1,000 paid and 30+ days since first successful payment\t$200,000 / month"
    name: Tiers
    type: Tiers
    description: This is the description of the plans for general OpenAI usage.
  - url: https://example.com/rate-limits
    data:
      - name: GPT-5 Token Limits
        type: Model
        limit: 800000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-5 model.
        userMultiplied: false
      - name: GPT-5 Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-5 model.
        userMultiplied: false
      - name: GPT-5 Batch Queue Limits
        type: Model
        limit: 100000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-5 model.
        userMultiplied: false
      - name: GPT-5 Mini Token Limits
        type: Model
        limit: 4000000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-5 Mini model.
        userMultiplied: false
      - name: GPT-5 Mini Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-5 Mini model.
        userMultiplied: false
      - name: GPT-5 Mini Batch Queue Limits
        type: Model
        limit: 40000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-5 Mini model.
        userMultiplied: false
      - name: GPT-5 Nano Token Limits
        type: Model
        limit: 4000000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-5 Nano model.
        userMultiplied: false
      - name: GPT-5 Nano Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-5 Nano model.
        userMultiplied: false
      - name: GPT-5 Nano Batch Queue Limits
        type: Model
        limit: 40000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-5 Nano model.
        userMultiplied: false
      - name: GPT-4.1 Token Limits
        type: Model
        limit: 800000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-4.1 model.
        userMultiplied: false
      - name: GPT-4.1 Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-4.1 model.
        userMultiplied: false
      - name: GPT-4.1 Batch Queue Limits
        type: Model
        limit: 100000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-4.1 model.
        userMultiplied: false
      - name: GPT-4.1 Mini Token Limits
        type: Model
        limit: 4000000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-4.1 Mini model.
        userMultiplied: false
      - name: GPT-4.1 Mini Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-4.1 Mini model.
        userMultiplied: false
      - name: GPT-4.1 Mini Batch Queue Limits
        type: Model
        limit: 40000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-4.1 Mini model.
        userMultiplied: false
      - name: GPT-4.1 Nano  Token Limits
        type: Model
        limit: 4000000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The token limits for the GPT-4.1 Nano  model.
        userMultiplied: false
      - name: GPT-4.1 Nano  Request Limits
        type: Model
        limit: 5000
        metric: request
        domains:
          - api.openai.com
        timeframe: minute
        description: The request limits for the GPT-4.1 Nano  model.
        userMultiplied: false
      - name: GPT-4.1 Nano  Batch Queue Limits
        type: Model
        limit: 40000000
        metric: tokens
        domains:
          - api.openai.com
        timeframe: day
        description: The batch queue token limits for the GPT-4.1 Nano  model.
        userMultiplied: false
    name: Rate Limits
    type: RateLimits
    description: The rate limits for this API.
  - url: https://status.openai.com/
    name: OpenAI Status
    type: StatusPage
  - url: https://platform.openai.com/api-keys
    type: API Keys
  - url: https://platform.openai.com/signup
    name: Sign Up
    type: Signup
    description: 'null'
  - url: https://platform.openai.com/login
    name: Login
    type: Login
    description: 'null'
  - url: https://developers.openai.com/changelog/
    name: Developer Changelog
    type: ChangeLog
    description: 'null'
  - url: https://developers.openai.com/blog/
    name: OpenAI Developer Blog
    type: Blog
    description: 'null'
  - url: https://cookbook.openai.com/
    name: OpenAI Cookbook
    type: Cookbook
    description: 'null'
  - url: https://platform.openai.com/docs/guides/safety-best-practices
    name: Safety Best Practices
    type: SafetyBestPractices
    description: 'null'
  - url: https://platform.openai.com/docs/guides/production-best-practices
    name: Production Best Practices
    type: BestPractices
    description: 'null'
  - url: https://openai.com/security-and-privacy/
    name: Security and Privacy
    type: Security
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/administration
    name: Administration API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/audit-logs
    name: Audit Logs API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/usage
    name: Usage API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/guides/function-calling
    name: Function Calling Guide
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/guides/structured-outputs
    name: Structured Outputs Guide
    type: Documentation
    description: 'null'
  - url: https://github.com/openai/openai-openapi
    name: OpenAI OpenAPI Specification
    type: GitHubRepository
    description: 'null'
  - url: https://github.com/openai/openai-python
    name: OpenAI Python SDK
    type: GitHubRepository
    description: 'null'
  - url: https://github.com/openai/openai-node
    name: OpenAI Node SDK
    type: GitHubRepository
    description: 'null'
  - url: https://openai.com/policies/service-terms/
    name: Service Terms
    type: TermsOfService
    description: 'null'
  - url: https://platform.openai.com/docs/guides/webhooks
    name: Webhooks Guide
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/webhook-events
    name: Webhook Events API Reference
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/api/docs/guides/deep-research/
    name: Deep Research Guide
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/api/docs/guides/voice-agents/
    name: Voice Agents Guide
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/api/docs/guides/code-generation/
    name: Code Generation Guide
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/guides/images-vision
    name: Images and Vision Guide
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/api/docs/guides/conversation-state/
    name: Conversation State Guide
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/api/docs/guides/migrate-to-responses/
    name: Migrate to Responses API Guide
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/containers
    name: Containers API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/container-files
    name: Container Files API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/chatkit
    name: ChatKit API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/videos
    name: Videos API Reference
    type: Documentation
    description: 'null'
  - url: https://platform.openai.com/docs/api-reference/conversations/create
    name: Conversations API Reference
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/
    name: OpenAI for Developers
    type: Portal
    description: 'null'
  - url: https://developers.openai.com/api/reference/
    name: OpenAI API Reference
    type: Documentation
    description: 'null'
  - url: https://developers.openai.com/codex
    name: OpenAI Codex
    type: Documentation
    description: 'null'
  - url: https://github.com/openai/chatkit-js
    name: OpenAI ChatKit JS SDK
    type: GitHubRepository
    description: 'null'
  - type: SpectralRules
    url: rules/openai-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/openai-vocabulary.yaml
  - type: Features
    url: https://platform.openai.com/docs/overview
    data:
      - GPT-5.5 flagship model at $5/$30 per MTok input/output
      - GPT-5.5 Pro for highest reasoning at $30/$180 per MTok
      - GPT-5.4 mid-tier balanced model at $2.50/$15 per MTok
      - GPT-5.4 Mini at $0.75/$4.50 per MTok
      - GPT-5.4 Nano cheapest model at $0.20/$1.25 per MTok
      - GPT Realtime 1.5 for low-latency voice with separate audio pricing
      - Cached input at ~10x discount vs uncached
      - Batch API at 50% discount on input and output
      - Flex tier for reduced cost / lower priority workloads
      - Vision, tool use, structured outputs, and function calling
      - Six usage tiers (Free + Tier 1-5) with automatic spend-based advancement
      - 'Five rate limit metrics: RPM, RPD, TPM, TPD, IPM'
      - Per-model rate ceilings; X-RateLimit-* headers on every response
      - Project-level API keys for cost allocation
      - Cost Tracking API and per-project hard spend limits
      - Regional data residency with 10% uplift
    sources:
      - https://developers.openai.com/api/docs/pricing
      - https://platform.openai.com/docs/guides/rate-limits
    updated: '2026-05-04'
  - type: UseCases
    url: https://openai.com/api/
    data:
      - name: Conversational AI
        description: Build chatbots, virtual assistants, and customer support agents using Chat Completions or Responses API.
      - name: Content Generation
        description: Generate marketing copy, articles, product descriptions, and creative writing with controllable tone and style.
      - name: Code Generation
        description: Automate code writing, debugging, refactoring, and documentation generation across programming languages.
      - name: Document Analysis
        description: Extract, summarize, and answer questions from uploaded documents using Assistants with file search.
      - name: Voice Agents
        description: Build real-time voice-based AI agents for customer service, sales, and interactive experiences.
      - name: Semantic Search
        description: Implement intelligent search using embeddings and vector stores for knowledge bases and document retrieval.
      - name: Content Moderation
        description: Automatically classify and filter harmful content across text and images using the Moderations API.
      - name: Data Extraction
        description: Extract structured data from unstructured text using function calling and structured outputs.
  - type: Integrations
    url: https://platform.openai.com/docs/libraries
    data:
      - name: Python SDK
        description: Official Python client library for accessing all OpenAI API endpoints with async support and streaming.
      - name: Node.js SDK
        description: Official TypeScript and JavaScript client library for server-side and edge runtime OpenAI API integration.
      - name: Microsoft Azure OpenAI
        description: Run OpenAI models on Azure infrastructure with enterprise security, compliance, and regional data residency.
      - name: LangChain
        description: Framework integration for building LLM-powered applications with chains, agents, and retrieval-augmented generation.
      - name: Vercel AI SDK
        description: Integration with Vercel AI SDK for building streaming AI-powered web applications with React and Next.js.
      - name: Zapier
        description: No-code automation integration connecting OpenAI to thousands of apps for automated AI-powered workflows.
created: '2024-04-14'
modified: '2026-05-04'
position: Consuming
description: APIs for accessing OpenAI's artificial intelligence models including GPT, DALL-E, Whisper, and Embeddings.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
image: https://openai.com/favicon.ico
---
