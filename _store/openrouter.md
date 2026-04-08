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
  humanURL: ' https://openrouter.ai/'
  baseURL: https://openrouter.ai/api/v1
  properties:
  - url: ' https://openrouter.ai/'
    type: Documentation
  - url: https://openrouter.ai/docs/api/reference/overview
    type: Documentation
  - url: https://openrouter.ai/openapi.json
    type: OpenAPI
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
created: '2025-08-19T00:00:00.000Z'
modified: '2026-04-07'
position: Consuming
description: OpenRouter is an API platform that provides unified access to multiple AI language models through a single interface. OpenRouter acts as a "router" or gateway that lets developers and applications access dozens of different AI models from various providers through one standardized API, rather than having to integrate with each provider separately.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

