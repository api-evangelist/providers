---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Trieve Agentic Access
  operation_count: 5
  slug: trieve-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 21
apis:
- description: Production REST API for Trieve Cloud. Organizes resources around organizations, datasets, chunks, chunk groups, files, search, topics, messages, crawls, analytics, events, experiments, and billing. Do
  name: Trieve REST API
  slug: rest-api
- description: Manage chunks - the individual searchable units of content stored in a dataset - including create, update, delete, get, and bulk operations.
  name: Trieve Chunk API
  slug: chunk
- description: Group chunks into bookmark-style folders for organization, recommendations, and group-scoped search within a dataset.
  name: Trieve Chunk Group API
  slug: chunk-group
- description: Create and configure datasets that hold chunks, chunk groups, and search / RAG configuration for a workload.
  name: Trieve Dataset API
  slug: dataset
- description: Run vector, full-text, and hybrid search across a dataset, with filters, boosts, re-ranking, and highlights.
  name: Trieve Search API
  slug: search
- description: Upload files (up to 1 GB), extract text, and chunk them into a dataset. Asynchronous - completion is signaled via the Events API.
  name: Trieve File API
  slug: file
- description: Topics persist conversational state for generative-AI chat sessions backed by a Trieve dataset.
  name: Trieve Topic API
  slug: topic
- description: Messages are turns within a topic; the Message API drives RAG completions, streaming responses, and citation-aware chat against a dataset.
  name: Trieve Message API
  slug: message
- description: Create and manage web crawls that ingest pages into a dataset for search and RAG.
  name: Trieve Crawl API
  slug: crawl
- description: Query search and RAG analytics - top queries, no-result queries, latency, click-through, and experiment outcomes.
  name: Trieve Analytics API
  slug: analytics
- description: Server-sent notifications about asynchronous work such as file processing, crawl completion, and chunk ingestion.
  name: Trieve Events API
  slug: events
- description: Manage organizations, roles, and members.
  name: Trieve Organization API
  slug: organization
- description: Registration, login, and session handling for Trieve users.
  name: Trieve Auth API
  slug: auth
- description: Official TypeScript / JavaScript client library for the Trieve REST API.
  name: Trieve TypeScript SDK
  slug: typescript-sdk
- description: Official Python client library (trieve-py-client) for the Trieve REST API.
  name: Trieve Python SDK
  slug: python-sdk
- description: Self-hostable Trieve server (Rust / Actix-web), dashboard, search and chat UIs, ingestion / file / delete workers, batch-ETL utilities, pdf2md converter, and Helm charts for Kubernetes deployment.
  name: Trieve Open Source Server
  slug: open-source
- description: The Chunk API from Trieve — 1 operation(s) for chunk.
  name: Trieve Chunk API
  slug: trieve-chunk-api
- description: The Dataset API from Trieve — 1 operation(s) for dataset.
  name: Trieve Dataset API
  slug: trieve-dataset-api
- description: The File API from Trieve — 1 operation(s) for file.
  name: Trieve File API
  slug: trieve-file-api
- description: The Message API from Trieve — 1 operation(s) for message.
  name: Trieve Message API
  slug: trieve-message-api
- description: The Topic API from Trieve — 1 operation(s) for topic.
  name: Trieve Topic API
  slug: trieve-topic-api
artifact_total: 28
collections:
- collection_type: open
  name: Trieve REST API
  slug: open-trieve
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/devflowinc/trieve/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trieve-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trieve-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trieve-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trieve.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trieve.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/devflowinc
- group: commercial
  title: ''
  type: Pricing
  url: https://trieve.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://trieve.ai/blog
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.trieve.ai/llms.txt
created: '2026-05-23'
description: Trieve (Devflow, Inc.) is an open-source, all-in-one search, recommendations, RAG, and analytics platform delivered as a REST API. The backend is written in Rust (Actix-web) and exposes endpoints for managing organizations, datasets, chunks, chunk groups, files, search, topics / messages (LLM chat), web crawls, events, analytics, and experiments. Trieve Cloud is hosted at api.trieve.ai; the same server can be self-hosted from the devflowinc/trieve repository. Official SDKs are published for TypeScript and Python.
finops:
- name: Trieve Finops
  service_category: API
  slug: trieve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trieve.png
layout: provider
modified: '2026-05-23'
name: Trieve
nav: Providers
network: true
overview: 'Trieve publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chunk API, Dataset API, File API, and 2 more. Tagged areas include Search, RAG, Vector Search, Hybrid Search, and Recommendations.


  Trieve''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 5 more developer resources.'
plans:
- name: Trieve Plans Pricing
  plan_count: 1
  slug: trieve-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 2
  name: Trieve Rate Limits
  slug: trieve-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.1
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trieve/refs/heads/main/screenshots/trieve-2026-06-20T195811.png
security:
- kind: authentication
  name: Trieve Authentication
  slug: trieve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trieve Domain Security
  slug: trieve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trieve
tags:
- Search
- RAG
- Vector Search
- Hybrid Search
- Recommendations
- Analytics
- Open Source
website: https://trieve.ai/
---
