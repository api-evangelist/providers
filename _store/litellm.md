---
aid: litellm
name: LiteLLM
segments:
  - Gateways
description: LiteLLM is an open-source Python SDK and proxy server providing a unified OpenAI-compatible interface to 100+ LLM providers.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Gateways
created: '2026-03-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/litellm/refs/heads/master/apis.yml
specificationVersion: '0.19'
apis:
  - aid: litellm:chat-completions-api
    name: LiteLLM Chat Completions API
    description: Provides an OpenAI-compatible /chat/completions endpoint that routes requests to 100+ LLM providers with unified request and response formatting, streaming support, cost tracking, and load balancing.
    humanURL: https://docs.litellm.ai/docs/completion
    tags:
      - AI
      - Chat
      - Completions
      - LLM
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/completion
      - type: GettingStarted
        url: https://docs.litellm.ai/docs/proxy/quick_start
  - aid: litellm:completions-api
    name: LiteLLM Completions API
    description: Provides an OpenAI-compatible /completions endpoint for text completion requests routed through the LiteLLM proxy to supported LLM providers.
    humanURL: https://docs.litellm.ai/docs/text_completion
    tags:
      - Completions
      - LLM
      - Text
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/text_completion
  - aid: litellm:responses-api
    name: LiteLLM Responses API
    description: Provides an OpenAI-compatible /responses endpoint supporting the Responses API specification, including conversation history compression via /responses/compact.
    humanURL: https://docs.litellm.ai/docs/response_api
    tags:
      - AI
      - LLM
      - Responses
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/response_api
  - aid: litellm:embeddings-api
    name: LiteLLM Embeddings API
    description: Provides an OpenAI-compatible /embeddings endpoint for generating text embeddings across multiple providers including OpenAI, Cohere, HuggingFace, and Bedrock with unified formatting.
    humanURL: https://docs.litellm.ai/docs/embedding/supported_embedding
    tags:
      - AI
      - Embeddings
      - Vectors
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/embedding/supported_embedding
  - aid: litellm:image-generation-api
    name: LiteLLM Image Generation API
    description: Provides OpenAI-compatible /images/generations, /images/edits, and /images/variations endpoints for image generation and manipulation routed through the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/image_generation
    tags:
      - AI
      - Generation
      - Images
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/image_generation
  - aid: litellm:audio-api
    name: LiteLLM Audio API
    description: Provides OpenAI-compatible /audio/transcriptions and /audio/speech endpoints for audio transcription and text-to-speech conversion across supported providers.
    humanURL: https://docs.litellm.ai/docs/audio_transcription
    tags:
      - AI
      - Audio
      - Speech
      - Transcription
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/audio_transcription
  - aid: litellm:moderations-api
    name: LiteLLM Moderations API
    description: Provides an OpenAI-compatible /moderations endpoint for content moderation across supported providers through the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/moderation
    tags:
      - Content
      - Moderation
      - Safety
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/moderation
  - aid: litellm:batches-api
    name: LiteLLM Batches API
    description: Provides an OpenAI-compatible /batches endpoint for batch processing operations, enabling bulk request handling across LLM providers.
    humanURL: https://docs.litellm.ai/docs/batches
    tags:
      - Batches
      - Bulk
      - Processing
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/batches
  - aid: litellm:files-api
    name: LiteLLM Files API
    description: Provides an OpenAI-compatible /files endpoint for file management operations used in conjunction with fine-tuning and batch processing.
    humanURL: https://docs.litellm.ai/docs/files_endpoints
    tags:
      - Files
      - Management
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/files_endpoints
  - aid: litellm:fine-tuning-api
    name: LiteLLM Fine-Tuning API
    description: Provides an OpenAI-compatible /fine_tuning endpoint for model fine-tuning operations across supported providers through the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/fine_tuning
    tags:
      - Fine-Tuning
      - Models
      - Training
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/fine_tuning
  - aid: litellm:rerank-api
    name: LiteLLM Rerank API
    description: Provides a /rerank endpoint for document reranking operations, supporting providers like Cohere through the LiteLLM proxy with a unified interface.
    humanURL: https://docs.litellm.ai/docs/rerank
    tags:
      - Relevance
      - Rerank
      - Search
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/rerank
  - aid: litellm:vector-stores-api
    name: LiteLLM Vector Stores API
    description: Provides /vector_stores endpoints for creating and managing vector stores, file operations within vector stores, and search functionality for retrieval-augmented generation (RAG) use cases.
    humanURL: https://docs.litellm.ai/docs/vector_stores/create
    tags:
      - RAG
      - Search
      - Storage
      - Vectors
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/vector_stores/create
  - aid: litellm:messages-api
    name: LiteLLM Anthropic Messages API
    description: Provides Anthropic-compatible /v1/messages and /v1/messages/count_tokens endpoints for native Anthropic API format support through the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/anthropic_unified/
    tags:
      - AI
      - Anthropic
      - Messages
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/anthropic_unified/
  - aid: litellm:realtime-api
    name: LiteLLM Realtime API
    description: Provides /realtime WebSocket endpoints for real-time model interactions with load balancing and guardrails support across providers.
    humanURL: https://docs.litellm.ai/docs/realtime
    tags:
      - Realtime
      - Streaming
      - WebSocket
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/realtime
  - aid: litellm:mcp-api
    name: LiteLLM MCP API
    description: Provides /mcp endpoints for Model Context Protocol (MCP) integration, enabling LLMs to interact with external tools and APIs through OpenAPI specifications.
    humanURL: https://docs.litellm.ai/docs/mcp
    tags:
      - MCP
      - Protocols
      - Tools
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/mcp
  - aid: litellm:ocr-api
    name: LiteLLM OCR API
    description: Provides an /ocr endpoint for optical character recognition, enabling text extraction from images through supported providers via the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/ocr
    tags:
      - Images
      - OCR
      - Text Extraction
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/ocr
  - aid: litellm:guardrails-api
    name: LiteLLM Guardrails API
    description: Provides /guardrails/apply_guardrail endpoint for applying configured content filtering and safety guardrails to LLM requests and responses.
    humanURL: https://docs.litellm.ai/docs/apply_guardrail
    tags:
      - Content Filtering
      - Guardrails
      - Safety
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/apply_guardrail
  - aid: litellm:evals-api
    name: LiteLLM Evals API
    description: Provides /evals endpoints for the Evaluations API, enabling measurement and benchmarking of model performance through the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/evals_api
    tags:
      - Benchmarks
      - Evaluations
      - Performance
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/evals_api
  - aid: litellm:a2a-api
    name: LiteLLM A2A Agent Gateway API
    description: Provides /a2a endpoints for the Agent-to-Agent (A2A) gateway, enabling agent registration, publishing, and inter-agent communication.
    humanURL: https://docs.litellm.ai/docs/a2a
    tags:
      - A2A
      - Agents
      - Gateway
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/a2a
  - aid: litellm:videos-api
    name: LiteLLM Videos API
    description: Provides /videos endpoints for video generation and handling through supported providers like RunwayML via the LiteLLM proxy.
    humanURL: https://docs.litellm.ai/docs/videos
    tags:
      - AI
      - Generation
      - Videos
    properties:
      - type: Documentation
        url: https://docs.litellm.ai/docs/videos
common:
  - type: Portal
    url: https://www.litellm.ai/
  - type: Documentation
    url: https://docs.litellm.ai/docs/
  - type: GettingStarted
    url: https://docs.litellm.ai/docs/proxy/quick_start
  - type: GitHubOrg
    url: https://github.com/BerriAI/litellm
  - type: Blog
    url: https://docs.litellm.ai/blog
  - type: ChangeLog
    url: https://www.litellm.ai/changelog
  - type: ReleaseNotes
    url: https://docs.litellm.ai/release_notes
  - type: Status
    url: https://status.litellm.ai/
  - type: Support
    url: https://www.litellm.ai/support
  - type: Pricing
    url: https://docs.litellm.ai/docs/enterprise
  - type: Dashboard
    url: https://admin.litellm.ai/
  - type: Providers
    url: https://docs.litellm.ai/docs/providers
  - type: Models
    url: https://models.litellm.ai/
  - type: Configuration
    url: https://docs.litellm.ai/docs/proxy/configs
  - type: Authentication
    url: https://docs.litellm.ai/docs/set_keys
  - type: Guardrails
    url: https://docs.litellm.ai/docs/apply_guardrail
  - type: Enterprise
    url: https://docs.litellm.ai/docs/proxy/enterprise
  - type: ReleaseCycle
    url: https://docs.litellm.ai/docs/proxy/release_cycle
  - type: SSO
    url: https://docs.litellm.ai/docs/proxy/admin_ui_sso
  - type: Docker
    url: https://docs.litellm.ai/docs/proxy/docker_quick_start
  - type: PyPI
    url: https://pypi.org/project/litellm/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
