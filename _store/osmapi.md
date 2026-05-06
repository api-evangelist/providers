---
aid: osmapi
name: osmAPI
description: osmAPI is a unified AI gateway that routes requests to OpenAI, Anthropic, Google, and 14+ LLM providers through a single API. Drop-in compatible with the OpenAI SDK, it provides smart routing, streaming, function calling, web search, response healing, embeddings, audio, and realtime endpoints.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Anthropic
  - Gateway
  - LLM
  - OpenAI
  - Routing
url: https://raw.githubusercontent.com/api-evangelist/osmapi/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: osmapi:osmapi-chat-completions-api
    name: osmAPI Chat Completions API
    description: OpenAI-compatible chat completions endpoint with smart routing, streaming, function calling, web search, and response healing across multiple LLM providers.
    humanURL: https://docs.osmapi.com/v1_chat_completions
    baseURL: https://api.osmapi.com/v1
    tags:
      - AI
      - Chat
      - LLM
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.osmapi.com/v1_chat_completions
      - type: OpenAPI
        url: openapi/osmapi-chat-completions-openapi.yml
  - aid: osmapi:osmapi-anthropic-messages-api
    name: osmAPI Anthropic Messages API
    description: Anthropic-compatible messages endpoint supporting system prompts, extended thinking, tool use, and streaming through osmAPI's gateway.
    humanURL: https://docs.osmapi.com/v1_messages
    baseURL: https://api.osmapi.com/v1
    tags:
      - AI
      - Anthropic
      - Messages
      - Tool Use
    properties:
      - type: Documentation
        url: https://docs.osmapi.com/v1_messages
      - type: OpenAPI
        url: openapi/osmapi-anthropic-messages-openapi.yml
  - aid: osmapi:osmapi-models-api
    name: osmAPI Models API
    description: Endpoint for listing available AI models with pricing, context length, capabilities, and provider details.
    humanURL: https://docs.osmapi.com/v1_models
    baseURL: https://api.osmapi.com/v1
    tags:
      - AI
      - Models
    properties:
      - type: Documentation
        url: https://docs.osmapi.com/v1_models
      - type: OpenAPI
        url: openapi/osmapi-models-openapi.yml
  - aid: osmapi:osmapi-health-api
    name: osmAPI Health API
    description: Health check endpoint reporting service status and dependency connectivity.
    humanURL: https://docs.osmapi.com/health
    baseURL: https://api.osmapi.com
    tags:
      - Health
      - Status
    properties:
      - type: Documentation
        url: https://docs.osmapi.com/health
      - type: OpenAPI
        url: openapi/osmapi-health-openapi.yml
common:
  - type: Portal
    url: https://www.osmapi.com/
  - type: Documentation
    url: https://docs.osmapi.com/
  - type: Dashboard
    url: https://app.osmapi.com/
  - type: Authentication
    url: https://docs.osmapi.com/features/api-keys
  - type: RateLimits
    url: https://docs.osmapi.com/resources/rate-limits
  - type: Routing
    url: https://docs.osmapi.com/features/routing
  - type: Caching
    url: https://docs.osmapi.com/features/caching
  - type: Pricing
    url: https://docs.osmapi.com/features/cost-breakdown
  - type: JSONLDContext
    url: json-ld/osmapi-context.jsonld
  - type: JSONSchema
    url: json-schema/osmapi-chat-completion-schema.json
  - type: JSONSchema
    url: json-schema/osmapi-model-schema.json
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
