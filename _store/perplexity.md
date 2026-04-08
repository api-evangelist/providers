---
aid: perplexity
url: https://raw.githubusercontent.com/api-evangelist/perplexity/refs/heads/main/apis.yml
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
name: Perplexity
tags:
- API
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-21'
modified: '2026-04-07'
position: Consumer
description: Perplexity AI is an answer engine that delivers accurate answers to complex questions using large language models with real-time web search capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

