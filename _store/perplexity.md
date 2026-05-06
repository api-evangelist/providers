---
aid: perplexity
name: Perplexity
description: Perplexity AI is an answer engine that delivers accurate answers to complex questions using large language models with real-time web search capabilities.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags: []
created: '2025-02-21'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/perplexity/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: perplexity:perplexity
    name: Perplexity
    description: What do you want to know?
    humanURL: ' https://www.perplexity.ai/'
    tags: []
    properties:
      - type: Documentation
        url: ' https://www.perplexity.ai/'
  - aid: perplexity:sonar-api
    name: Perplexity Sonar API
    description: The Sonar API provides access to Perplexity's Sonar family of models including sonar, sonar-pro, sonar-reasoning-pro, and sonar-deep-research via an OpenAI-compatible chat completions endpoint with built-in web search grounding.
    humanURL: https://docs.perplexity.ai/docs/sonar/quickstart
    baseURL: https://api.perplexity.ai
    tags:
      - Artificial Intelligence
      - Chat Completions
      - Grounding
      - Large Language Models
      - Search
    properties:
      - type: Documentation
        url: https://docs.perplexity.ai/docs/sonar/quickstart
      - type: API Reference
        url: https://docs.perplexity.ai/api-reference/chat-completions-post
      - type: Authentication
        url: https://docs.perplexity.ai/guides/api-key-management
      - type: Pricing
        url: https://docs.perplexity.ai/docs/getting-started/pricing
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/perplexity/refs/heads/main/openapi/perplexity-openapi.json
  - aid: perplexity:async-chat-completions-api
    name: Perplexity Async Chat Completions API
    description: The Async Chat Completions API enables developers to submit long-running chat completion requests for background processing. Requests are queued and processed asynchronously, returning a unique identifier for tracking status through creation, processing, completion, or failure stages, making it ideal for deep research and computationally intensive queries.
    humanURL: https://docs.perplexity.ai/api-reference/async-chat-completions-post
    baseURL: https://api.perplexity.ai
    tags:
      - Artificial Intelligence
      - Asynchronous
      - Chat Completions
      - Large Language Models
    properties:
      - type: Documentation
        url: https://docs.perplexity.ai/api-reference/async-chat-completions-post
      - type: API Reference
        url: https://docs.perplexity.ai/api-reference/async-chat-completions-get
      - type: Authentication
        url: https://docs.perplexity.ai/guides/api-key-management
  - aid: perplexity:search-api
    name: Perplexity Search API
    description: The Search API enables developers to perform ranked web searches with advanced filtering including domain, language, country, and date recency controls, returning structured results with titles, URLs, snippets, and publication dates.
    humanURL: https://docs.perplexity.ai/guides/search-quickstart
    baseURL: https://api.perplexity.ai
    tags:
      - Filtering
      - Ranking
      - Search
      - Web Search
    properties:
      - type: Documentation
        url: https://docs.perplexity.ai/guides/search-quickstart
      - type: API Reference
        url: https://docs.perplexity.ai/api-reference/search-post
      - type: Authentication
        url: https://docs.perplexity.ai/guides/api-key-management
      - type: Best Practices
        url: https://docs.perplexity.ai/guides/search-best-practices
  - aid: perplexity:responses-api
    name: Perplexity Responses API
    description: The Responses API (Agentic Research API) provides access to third-party frontier models from providers like OpenAI, Anthropic, Google, and xAI with integrated web search tools, URL fetching, function calling, and multi-step reasoning presets such as pro-search and deep-research.
    humanURL: https://docs.perplexity.ai/docs/grounded-llm/responses/quickstart
    baseURL: https://api.perplexity.ai
    tags:
      - Agents
      - Artificial Intelligence
      - Large Language Models
      - Research
      - Web Search
    properties:
      - type: Documentation
        url: https://docs.perplexity.ai/docs/grounded-llm/responses/quickstart
      - type: API Reference
        url: https://docs.perplexity.ai/api-reference/responses-post
      - type: Authentication
        url: https://docs.perplexity.ai/guides/api-key-management
  - aid: perplexity:embeddings-api
    name: Perplexity Embeddings API
    description: The Embeddings API generates high-quality text embeddings for semantic search and retrieval, offering both standard embeddings for independent texts and contextualized embeddings for document chunks that share context, with support for Matryoshka representation learning for flexible dimensionality.
    humanURL: https://docs.perplexity.ai/docs/embeddings/quickstart
    baseURL: https://api.perplexity.ai
    tags:
      - Embeddings
      - Retrieval
      - Semantic Search
      - Vectors
    properties:
      - type: Documentation
        url: https://docs.perplexity.ai/docs/embeddings/quickstart
      - type: API Reference
        url: https://docs.perplexity.ai/api-reference/embeddings-post
      - type: Authentication
        url: https://docs.perplexity.ai/guides/api-key-management
      - type: Best Practices
        url: https://docs.perplexity.ai/docs/embeddings/best-practices
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - FN: Perplexity AI
    email: support@perplexity.ai
    url: https://www.perplexity.ai
common:
  - url: https://docs.perplexity.ai/docs/getting-started
    type: Getting Started
  - url: https://docs.perplexity.ai/reference/post_chat_completions
    type: API Reference
  - url: https://docs.perplexity.ai/docs/model-cards
    type: Models
  - url: https://docs.perplexity.ai/docs/pricing
    type: Pricing
  - url: https://www.perplexity.ai/hub/terms
    type: Terms of Service
  - url: https://www.perplexity.ai/hub/privacy
    type: Privacy Policy
  - url: https://www.perplexity.ai/hub/blog
    type: Blog
  - url: https://docs.perplexity.ai/docs/getting-started/quickstart
    type: Quickstart
  - url: https://docs.perplexity.ai/docs/getting-started/pricing
    type: Pricing Page
  - url: https://docs.perplexity.ai/docs/getting-started/models
    type: Model Directory
  - url: https://docs.perplexity.ai/docs/resources/changelog
    type: Change Log
  - url: https://www.perplexity.ai/changelog
    type: Product Change Log
  - url: https://docs.perplexity.ai/guides/usage-tiers
    type: Rate Limits
  - url: https://perplexity.ai/account/api
    type: Sign Up
  - url: https://www.perplexity.ai/account/api/group
    type: Dashboard
  - url: https://perplexity.ai/account/api/playground/search
    type: API Playground
  - url: https://docs.perplexity.ai/guides/perplexity-sdk
    type: SDKs
  - url: https://github.com/perplexityai
    type: GitHub Org
  - url: https://github.com/perplexityai/perplexity-py
    type: Python SDK
  - url: https://docs.perplexity.ai/guides/search-best-practices
    type: Best Practices
  - url: https://docs.perplexity.ai/guides/mcp-server
    type: MCP Server
  - url: https://www.perplexity.ai/help-center/en
    type: Support
  - url: https://community.perplexity.ai
    type: Forum
  - url: https://www.perplexity.ai/api-platform
    type: Portal
  - url: https://docs.perplexity.ai/llms.txt
    type: LLMs TXT
  - url: https://www.perplexity.ai
    type: Website
  - url: https://docs.perplexity.ai
    type: Documentation
  - url: https://docs.perplexity.ai/guides/api-key-management
    type: Authentication
  - url: https://status.perplexity.com
    type: Status
  - url: https://docs.perplexity.ai/feature-roadmap
    type: Roadmap
  - url: https://docs.perplexity.ai/docs/cookbook
    type: Cookbook
  - url: https://docs.perplexity.ai/guides/prompt-guide
    type: Prompt Guide
  - url: https://docs.perplexity.ai/guides/structured-outputs
    type: Structured Outputs Guide
  - url: https://docs.perplexity.ai/guides/perplexity-sdk-performance
    type: Performance Guide
  - url: https://docs.perplexity.ai/guides/date-range-filter-guide
    type: Date Range Filter Guide
  - url: https://docs.perplexity.ai/guides/academic-filter-guide
    type: Academic Filter Guide
  - url: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
    type: Crawlers
  - url: https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service
    type: API Terms of Service
  - url: https://docs.perplexity.ai/discussions/discussions
    type: Discussions
  - url: https://discord.com/invite/perplexity-ai
    type: Discord
  - url: https://x.com/perplexity_ai
    type: X
  - type: Features
    data:
      - Sonar at $1/$1 MTok + $5-$12/1K searches
      - Sonar Pro at $3/$15 MTok + $6-$14/1K searches
      - Sonar Reasoning Pro at $2/$8 MTok
      - Sonar Deep Research at $2/$8 MTok + $5/1K queries + $2/MTok citations
      - Web-grounded answers with inline citations
      - OpenAI-compatible Chat Completions
      - Search context size affects pricing
      - Default 50 req/min Sonar, 5 req/min Deep Research
      - Tiered spend limits starting at $5/mo
      - Citation tokens and reasoning tokens billed separately on Deep Research
      - Multi-step research synthesis
      - Filter by date, domain, recency
      - Structured output (JSON schema)
      - Image input on Sonar Pro
      - Streaming responses
      - Asynchronous batch endpoint (beta)
    sources:
      - https://docs.perplexity.ai/guides/pricing
    updated: '2026-05-04'
---
