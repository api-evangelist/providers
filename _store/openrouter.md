---
aid: openrouter
url: https://raw.githubusercontent.com/api-evangelist/openrouter/refs/heads/main/apis.yml
apis:
  - aid: openrouter:openrouter
    name: OpenRouter
    tags:
      - Artificial Intelligence
      - Gateway
      - Large Language Models
      - Router
    humanURL: https://openrouter.ai/
    baseURL: https://openrouter.ai/api/v1
    properties:
      - url: https://openrouter.ai/
        type: Documentation
      - url: https://openrouter.ai/docs/api/reference/overview
        type: Documentation
      - url: https://openrouter.ai/openapi.json
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/openrouter/refs/heads/main/openapi/openrouter-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/openrouter/refs/heads/main/json-schema/openrouter-chat-message-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/openrouter/refs/heads/main/json-ld/openrouter-context.jsonld
        type: JSONLDContext
    description: OpenRouter provides unified access to hundreds of AI models through a single API endpoint. It implements the OpenAI API specification for chat completions, allowing developers to use any model with the same request and response format. Better prices, better uptime, no subscription.
  - aid: openrouter:chat-completions-api
    name: OpenRouter Chat Completions API
    tags:
      - Chat
      - Completions
      - Large Language Models
    humanURL: https://openrouter.ai/docs/api/reference/overview
    baseURL: https://openrouter.ai/api/v1
    properties:
      - url: https://openrouter.ai/docs/api/reference/overview
        type: Documentation
      - url: https://openrouter.ai/docs/api/reference/parameters
        type: Documentation
      - url: https://openrouter.ai/docs/api/reference/streaming
        type: Documentation
      - url: https://openrouter.ai/openapi.json
        type: OpenAPI
    description: The Chat Completions API is the primary endpoint for generating model responses. It supports text and image inputs, streaming via Server-Sent Events, tool and function calling, structured outputs, and provider routing across 400+ AI models from 60+ providers through a single standardized interface at /api/v1/chat/completions.
  - aid: openrouter:models-api
    name: OpenRouter Models API
    tags:
      - Discovery
      - Models
    humanURL: https://openrouter.ai/docs/api/api-reference/models/get-models
    baseURL: https://openrouter.ai/api/v1
    properties:
      - url: https://openrouter.ai/docs/api/api-reference/models/get-models
        type: Documentation
      - url: https://openrouter.ai/docs/guides/overview/models
        type: Documentation
      - url: https://openrouter.ai/openapi.json
        type: OpenAPI
    description: The Models API allows developers to list and discover all available AI models and their properties, including pricing, context lengths, supported features, and provider information. Endpoints include listing all models and listing all endpoints for a specific model.
  - aid: openrouter:generation-api
    name: OpenRouter Generation API
    tags:
      - Generation
      - Stats
      - Usage
    humanURL: https://openrouter.ai/docs/api/reference/overview
    baseURL: https://openrouter.ai/api/v1
    properties:
      - url: https://openrouter.ai/docs/api/reference/overview
        type: Documentation
      - url: https://openrouter.ai/openapi.json
        type: OpenAPI
    description: The Generation API allows querying for generation statistics and historical usage data, including token counts, cost calculations, cached token tracking, and reasoning token counts for completed requests via the /api/v1/generation endpoint.
  - aid: openrouter:keys-api
    name: OpenRouter Keys Management API
    tags:
      - API Keys
      - Management
      - Provisioning
    humanURL: https://openrouter.ai/docs/guides/overview/auth/provisioning-api-keys
    baseURL: https://openrouter.ai/api/v1
    properties:
      - url: https://openrouter.ai/docs/guides/overview/auth/provisioning-api-keys
        type: Documentation
      - url: https://openrouter.ai/docs/guides/overview/auth/management-api-keys
        type: Documentation
      - url: https://openrouter.ai/openapi.json
        type: OpenAPI
    description: The Keys Management API enables programmatic creation, rotation, and management of OpenRouter API keys. Common use cases include SaaS applications that automatically create unique keys for each customer, key rotation for security compliance, and usage monitoring with automatic key disabling when limits are exceeded.
name: OpenRouter
tags:
  - Artificial Intelligence
  - Gateway
  - Large Language Models
  - Router
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://openrouter.ai/
    name: OpenRouter
    type: Website
    description: 'null'
  - url: https://openrouter.ai/models
    name: Models
    type: Models
    description: 'null'
  - url: https://status.openrouter.ai/
    name: OpenRouter Status
    type: Status
    description: 'null'
  - url: https://openrouter.ai/docs/quickstart
    name: Getting Started
    type: GettingStarted
    description: 'null'
  - url: https://openrouter.ai/docs/faq
    name: OpenRouter FAQ
    type: FAQ
    description: 'null'
  - url: https://openrouter.ai/models?fmt=table
    name: Pricing
    type: Pricing
    description: 'null'
  - url: https://openrouter.ai/privacy
    name: Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://openrouter.ai/terms
    name: Terms Of Service
    type: TermsOfService
    description: 'null'
  - url: https://openrouter.ai/docs
    name: Documentation Portal
    type: Portal
    description: 'null'
  - url: https://openrouter.ai/docs/api/reference/overview
    name: API Reference
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/api/reference/authentication
    name: Authentication
    type: Authentication
    description: 'null'
  - url: https://openrouter.ai/docs/api/reference/limits
    name: Rate Limits
    type: RateLimits
    description: 'null'
  - url: https://openrouter.ai/docs/api/reference/errors-and-debugging
    name: Errors and Debugging
    type: Errors
    description: 'null'
  - url: https://openrouter.ai/docs/api/reference/streaming
    name: Streaming
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/openapi.json
    name: OpenAPI Specification (JSON)
    type: OpenAPI
    description: 'null'
  - url: https://openrouter.ai/openapi.yaml
    name: OpenAPI Specification (YAML)
    type: OpenAPI
    description: 'null'
  - url: https://openrouter.ai/pricing
    name: Platform Pricing
    type: Pricing
    description: 'null'
  - url: https://openrouter.ai/support
    name: Support
    type: Support
    description: 'null'
  - url: https://openrouter.ai/announcements
    name: Announcements and Blog
    type: Blog
    description: 'null'
  - url: https://discord.com/invite/openrouter
    name: Discord Community
    type: Discord
    description: 'null'
  - url: https://github.com/OpenRouterTeam
    name: GitHub Organization
    type: GitHubOrganization
    description: 'null'
  - url: https://github.com/OpenRouterTeam/typescript-sdk
    name: TypeScript SDK
    type: GitHubRepository
    description: 'null'
  - url: https://github.com/OpenRouterTeam/python-sdk
    name: Python SDK
    type: GitHubRepository
    description: 'null'
  - url: https://openrouter.ai/docs/sdks/typescript/overview
    name: TypeScript SDK Documentation
    type: SDKs
    description: 'null'
  - url: https://openrouter.ai/docs/sdks/python/overview
    name: Python SDK Documentation
    type: SDKs
    description: 'null'
  - url: https://openrouter.ai/docs/guides/community/frameworks-and-integrations-overview
    name: Frameworks and Integrations
    type: Integrations
    description: 'null'
  - url: https://openrouter.ai/docs/guides/community/openai-sdk
    name: OpenAI SDK Integration
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/routing/provider-selection
    name: Provider Routing
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/tool-calling
    name: Tool and Function Calling
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/structured-outputs
    name: Structured Outputs
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/model-routing
    name: Model Routing
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/guardrails
    name: Guardrails
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/zdr
    name: Zero Data Retention
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/features/plugins/web-search
    name: Web Search Plugin
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/overview/auth/byok
    name: Bring Your Own Key (BYOK)
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/docs/guides/guides/for-providers
    name: Provider Integration Guide
    type: Documentation
    description: 'null'
  - url: https://openrouter.ai/settings/keys
    name: API Keys
    type: APIKeys
    description: 'null'
  - url: https://openrouter.ai/docs/guides/overview/principles
    name: Principles
    type: Documentation
    description: 'null'
  - type: Features
    data:
      - 'Free: 25+ models, 50 req/day cap'
      - 'Pay-As-You-Go: 300+ models, 0% provider markup'
      - 5.5% platform fee on credit purchases
      - 'Enterprise: volume discounts, custom platform fee'
      - Failed/fallback attempts NOT billed
      - OpenAI-compatible Chat Completions API
      - 300+ models from OpenAI, Anthropic, Google, Mistral, Meta, etc.
      - Automatic fallback routing on errors
      - Bring Your Own Key (BYOK) for select providers
      - Streaming responses
      - Tool use / function calling (model-dependent)
      - Vision (model-dependent)
      - Per-model upstream rate limit passthrough
      - Bearer token auth
      - Provider transparency (see live latency/uptime/throughput)
      - Credits + Stripe payments + crypto
    sources:
      - https://openrouter.ai/pricing
    updated: '2026-05-04'
created: '2025-08-19T00:00:00.000Z'
modified: '2026-05-04'
position: Consuming
segments:
  - Gateways
description: OpenRouter is an API platform that provides unified access to multiple AI language models through a single interface. OpenRouter acts as a "router" or gateway that lets developers and applications access dozens of different AI models from various providers through one standardized API, rather than having to integrate with each provider separately.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
