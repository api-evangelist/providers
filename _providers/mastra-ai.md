---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.6
  scored_at: '2026-08-06'
api_count: 12
apis:
- description: The Mastra framework is a TypeScript-first agentic stack distributed as the @mastra/* family of npm packages. The core package wires agents, workflows, memory, RAG, tools, MCP, evals, voice, and obser
  name: Mastra Framework
  slug: mastra-framework
- description: 'Mastra agents define behavior with a model, instructions, tools, memory, and processors, then expose .generate() and .stream() for typed text, object, and structured output generation. Agents support '
  name: Mastra Agents
  slug: mastra-agents
- description: Workflows are durable, graph-based pipelines composed from typed steps with branching, parallelism, loops, suspension, human-in-the-loop, and event triggers. Step inputs and outputs are validated agai
  name: Mastra Workflows
  slug: mastra-workflows
- description: The memory package provides conversation history, working memory, and semantic recall for agents, pluggable across PostgreSQL, LibSQL, Redis, Upstash, MongoDB, MS SQL, DynamoDB, Cloudflare D1, ClickHo
  name: Mastra Memory
  slug: mastra-memory
- description: The RAG package provides document loaders, chunkers, embedders (including FastEmbed local embeddings), rerankers, and retrieval helpers that compose with any Mastra vector store. Supports semantic, ke
  name: Mastra RAG
  slug: mastra-rag
- description: First-class Model Context Protocol support — Mastra ships an MCP client for connecting to any MCP server and exposing its tools to agents, plus an MCP server implementation for publishing your own age
  name: Mastra MCP
  slug: mastra-mcp
- description: Built-in evaluation library with model-graded (LLM-as-judge), rule-based, and statistical metrics for measuring agent output quality, hallucination, faithfulness, relevance, bias, toxicity, and answer
  name: Mastra Evals
  slug: mastra-evals
- description: Voice abstractions for speech-to-text, text-to-speech, and realtime voice agents with provider adapters for OpenAI (including Realtime API), ElevenLabs, Deepgram, Google, Google Gemini Live, Azure, AW
  name: Mastra Voice
  slug: mastra-voice
- description: OpenTelemetry-native tracing for agents, workflows, tools, and LLM calls with first-party exporters for Mastra Cloud, Langfuse, LangSmith, Braintrust, Arize, Arthur, Laminar, Datadog, Sentry, ClickHou
  name: Mastra Observability
  slug: mastra-observability
- description: The mastra CLI scaffolds projects (`npm create mastra`), runs the local dev server with hot reload, opens the Studio playground, generates types, runs migrations on memory stores, deploys to Mastra Cl
  name: Mastra CLI
  slug: mastra-cli
- description: 'Client-side SDKs that talk to a Mastra server from the browser, React applications, or any JavaScript runtime. Includes @mastra/client-js (universal JS client), @mastra/react (React hooks for agents, '
  name: Mastra Client SDKs
  slug: mastra-client-sdks
- description: Deployer packages that bundle a Mastra app for a target runtime. Built-in deployers cover Mastra Cloud, Cloudflare Workers, Vercel, and Netlify. Custom deployers can be written for any Node-compatible
  name: Mastra Deployers
  slug: mastra-deployers
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mastra-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mastra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://mastra.ai/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mastra-ai/mastra
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mastra-ai
- group: company
  title: ''
  type: Blog
  url: https://mastra.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/mastra-ai/mastra/releases
- group: commercial
  title: ''
  type: Pricing
  url: https://mastra.ai/pricing
- group: build
  title: ''
  type: PackageManager
  url: https://www.npmjs.com/org/mastra
- group: build
  title: ''
  type: Examples
  url: https://github.com/mastra-ai/mastra/tree/main/examples
- group: other
  title: ''
  type: Templates
  url: https://mastra.ai/templates
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/BTYqqHKUrf
- group: company
  title: ''
  type: XTwitter
  url: https://x.com/mastra_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mastra-ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@mastra-ai
- group: learn
  title: ''
  type: Course
  url: https://mastra.ai/course
- group: other
  title: ''
  type: Book
  url: https://mastra.ai/book
- group: other
  title: ''
  type: Podcast
  url: https://mastra.ai/agent-hour
- group: commercial
  title: ''
  type: License
  url: https://github.com/mastra-ai/mastra/blob/main/LICENSE.md
- group: other
  title: ''
  type: YCombinator
  url: https://www.ycombinator.com/companies/mastra
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/mastra-44ba
created: '2026-05-25'
description: Mastra is a TypeScript framework for building AI-powered applications and agents, built by the team behind Gatsby (Sam Bhagwat, Abhi Aiyer, Shane Thomas). The framework provides production-grade primitives for agents, workflows, RAG, tools, memory, evals, voice, and observability, and integrates with 40+ model providers through the Vercel AI SDK. The framework is Apache 2.0 licensed open source, with a hosted commercial offering (Mastra Cloud) for deployment, tracing, and team collaboration, and an enterprise self-hosted edition for regulated environments.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mastra-ai.png
layout: provider
modified: '2026-05-25'
name: Mastra
nav: Providers
network: true
overview: 'Mastra publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Artificial Intelligence, Workflows, RAG, and MCP.


  Mastra''s developer surface includes documentation, GitHub presence, engineering blog, changelog, pricing, code examples, YouTube channel, and 14 more developer resources.'
random_paper: 104
score:
  band: emerging
  composite: 13.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mastra-ai/refs/heads/main/screenshots/mastra-ai-2026-06-20T185028.png
security:
- kind: domain-security
  name: Mastra Ai Domain Security
  slug: mastra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mastra-ai
tags:
- Agents
- Artificial Intelligence
- Workflows
- RAG
- MCP
- Memory
- Evaluation
- LLM Observability
- TypeScript
- Voice
- Open Source
website: https://mastra.ai
---
