---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Gemini Agentic Access
  operation_count: 11
  slug: gemini-agentic-access
  summary_line: 11 operations · 7 acting
api_count: 1
apis:
- description: Python client library for the Gemini API.
  name: Gemini Python SDK
  slug: gemini-python-sdk
- description: Node.js client library for the Gemini API.
  name: Gemini Node.js SDK
  slug: gemini-nodejs-sdk
- description: Go client library for the Gemini API, providing an interface for developers to integrate Google generative models into Go applications.
  name: Gemini Go SDK
  slug: gemini-go-sdk
- description: Java client library for the Gemini API, providing an interface for developers to integrate Google generative models into Java applications.
  name: Gemini Java SDK
  slug: gemini-java-sdk
- description: C# client library for the Gemini API, providing an interface for developers to integrate Google generative models into .NET applications.
  name: Gemini C# SDK
  slug: gemini-c-sdk
- description: Low-latency bidirectional streaming API enabling real-time voice and video interactions with Gemini models over WebSocket connections.
  name: Gemini Live API
  slug: gemini-live-api
- description: A single unified endpoint for Gemini models and agents with server-side state, background execution, tool combination, and multimodal generation. Now generally available, it is Google's recommended in
  name: Gemini Interactions API
  slug: gemini-interactions-api
- description: Image generation capabilities through the Gemini API, supporting text-to-image generation, image editing, and multi-turn conversational editing.
  name: Gemini Image Generation API
  slug: gemini-image-generation-api
- description: Video generation capabilities through the Gemini API powered by Veo, supporting text-to-video and image-to-video generation in resolutions up to 4K.
  name: Gemini Video Generation API
  slug: gemini-video-generation-api
- description: Native audio generation text-to-speech capabilities through the Gemini API, supporting single and multi-speaker speech synthesis with natural language control over style, accent, pace, and tone.
  name: Gemini Text-to-Speech API
  slug: gemini-text-to-speech-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: API for uploading and managing media files for use with Gemini models, supporting images, audio, video, and documents up to 2 GB per file with 20 GB per project storage.
  name: Gemini Files API
  slug: gemini-files-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: Text embedding capabilities through the Gemini API, generating vector representations for semantic search, classification, clustering, and retrieval augmented generation (RAG) applications.
  name: Gemini Embeddings API
  slug: gemini-embeddings-api
- description: Asynchronous batch processing API for submitting large volumes of Gemini API requests at 50 percent of the standard cost, with support for content generation, embeddings, and OpenAI compatibility.
  name: Gemini Batch API
  slug: gemini-batch-api
- description: Agentic research capability powered by the Interactions API that autonomously plans, executes, and synthesizes multi-step research tasks using web search and URL context to produce detailed cited repo
  name: Gemini Deep Research API
  slug: gemini-deep-research-api
- description: REST and WebSocket APIs for the Gemini cryptocurrency exchange, providing market data, order management, account balances, clearing, earn/staking, and institutional capital account operations.
  name: Gemini Exchange API
  slug: gemini-exchange-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: Create embeddings for text
  name: Gemini Embeddings API
  slug: gemini-embeddings-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: Upload and manage files used as model input
  name: Gemini Files API
  slug: gemini-files-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: Generate content from prompts
  name: Gemini Generation API
  slug: gemini-generation-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: List and inspect available Gemini models
  name: Gemini Models API
  slug: gemini-models-api
- baseURL: https://generativelanguage.googleapis.com
  baseurl_source: declared
  description: Token counting and other helpers
  name: Gemini Utility API
  slug: gemini-utility-api
artifact_total: 56
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Gemini Embeddings API
  slug: open-gemini-embeddings-api
- collection_type: open
  name: Google Gemini Embeddings Files API
  slug: open-gemini-files-api
- collection_type: open
  name: Google Gemini Embeddings Generation API
  slug: open-gemini-generation-api
- collection_type: open
  name: Google Gemini Embeddings Models API
  slug: open-gemini-models-api
- collection_type: open
  name: Google Gemini Embeddings Utility API
  slug: open-gemini-utility-api
- collection_type: open
  name: Google Gemini API
  slug: open-gemini
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/gemini-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gemini-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gemini-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gemini-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.googleblog.com/closing-the-knowledge-gap-with-agent-skills/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geminitrust
- group: start
  title: ''
  type: GettingStarted
  url: https://ai.google.dev/gemini-api/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://aistudio.google.com/app/apikey
- group: commercial
  title: ''
  type: Pricing
  url: https://ai.google.dev/pricing
- group: other
  title: ''
  type: Models
  url: https://ai.google.dev/gemini-api/docs/models
- group: operate
  title: ''
  type: RateLimits
  url: https://ai.google.dev/gemini-api/docs/quota
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ai.google.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://developers.googleblog.com/
- group: operate
  title: ''
  type: Support
  url: https://discuss.ai.google.dev/
- group: build
  title: ''
  type: SDKs
  url: https://ai.google.dev/gemini-api/docs/libraries
- group: operate
  title: ''
  type: ChangeLog
  url: https://ai.google.dev/gemini-api/docs/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://aistudio.google.com/status
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/google-gemini/cookbook
- group: start
  title: ''
  type: Console
  url: https://aistudio.google.com/
created: '2024'
description: Google's Gemini API provides access to state-of-the-art generative AI models for text generation, multimodal understanding, code generation, and more.
features:
- description: Process and understand text, images, audio, video, and documents in a single model.
  name: Multimodal Understanding
- description: Define custom functions that Gemini can invoke to interact with external systems and APIs.
  name: Function Calling
- description: Generate JSON responses conforming to specified schemas for reliable data extraction.
  name: Structured Output
- description: Cache large context windows to reduce latency and cost for repeated queries.
  name: Context Caching
- description: Execute Python code in a sandboxed environment for computational tasks.
  name: Code Execution
- description: Ground model responses with real-time Google Search results for factual accuracy.
  name: Grounding with Google Search
- description: Real-time bidirectional voice and video interactions over WebSocket connections.
  name: Live Streaming API
- description: Generate images and videos from text prompts using Gemini and Veo models.
  name: Image and Video Generation
- description: Native audio generation with multi-speaker support and natural language style control.
  name: Text-to-Speech
- description: Autonomous multi-step research agent that synthesizes cited reports from web sources.
  name: Deep Research
- description: Extended reasoning capability for complex problem-solving and analysis tasks.
  name: Thinking Mode
finops:
- name: Gemini Finops
  service_category: API
  slug: gemini-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the [Gemini Exchange](https://gemini.com) cryptocurrency exchange API. Gemini is a regulated cryptocurrency exchange offering REST and WebSocket
  name: Gemini Exchange GraphQL Schema
  slug: gemini-graphql
image: https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg
integrations:
- description: Access Gemini models through Vertex AI for enterprise-grade deployment and management.
  name: Google Cloud Vertex AI
- description: Prototype and test Gemini API calls with the web-based development environment.
  name: Google AI Studio
- description: Use Gemini as a provider in LangChain for building AI application pipelines.
  name: LangChain
- description: Integrate Gemini with Firebase for mobile and web app AI features.
  name: Firebase
- description: Use Gemini through OpenAI-compatible API endpoints for easy migration.
  name: OpenAI Compatibility
layout: provider
modified: '2026-06-22'
name: Gemini
nav: Providers
network: true
overview: 'Gemini publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Files API, Embeddings API, and 5 more. Tagged areas include Agents, Artificial Intelligence, Audio Understanding, Batch Processing, and Deep Research.


  Gemini''s developer surface includes authentication, getting-started guide, pricing, engineering blog, support, changelog, developer console, and 13 more developer resources.'
plans:
- name: Gemini Plans Pricing
  plan_count: 3
  slug: gemini-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Gemini Rate Limits
  slug: gemini-rate-limits
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 69.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gemini/refs/heads/main/screenshots/gemini-2026-06-20T181714.png
security:
- kind: authentication
  name: Gemini Authentication
  slug: gemini-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Gemini Domain Security
  slug: gemini-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gemini
tags:
- Agents
- Artificial Intelligence
- Audio Understanding
- Batch Processing
- Deep Research
- Document Understanding
- Embeddings
- Function Calling
- Generative AI
- Image-Generation
- Large Language Models
- Machine-Learning
- Multi-Modal
- Structured Output
- Text-to-Speech
- Video Generation
- Video Understanding
use_cases:
- description: Build conversational AI assistants with multimodal understanding and function calling.
  name: AI-Powered Chatbots
- description: Extract structured data from documents, PDFs, and images using vision capabilities.
  name: Document Processing
- description: Generate text, images, and video content with AI for marketing and creative workflows.
  name: Content Generation
- description: Generate, explain, and debug code across multiple programming languages.
  name: Code Generation
- description: Build search systems using Gemini embeddings for semantic similarity matching.
  name: Semantic Search
- description: Translate text and audio in real-time using multimodal capabilities.
  name: Real-Time Translation
---
