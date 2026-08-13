---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Nuclia Agentic Access
  operation_count: 23
  slug: nuclia-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 5
apis:
- description: Generative RAG answers, chat and summarization grounded in a Knowledge Box.
  name: Nuclia Ask API
  slug: nuclia-ask-api
- description: Create, configure and inspect Knowledge Boxes and their label sets.
  name: Nuclia Knowledge Boxes API
  slug: nuclia-knowledge-boxes-api
- description: Nuclia Understanding API (NUA) - generation, summarize, rephrase, rerank, embeddings and tokenization.
  name: Nuclia Predict API
  slug: nuclia-predict-api
- description: Ingest and manage resources - files, text, links and conversations.
  name: Nuclia Resources API
  slug: nuclia-resources-api
- description: Hybrid search, find (RAG retrieval) and suggest over a Knowledge Box.
  name: Nuclia Search API
  slug: nuclia-search-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of Nuclia's **ask / chat generative answer streaming** surface. Nuclia does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://do
  name: Nuclia Ask / Chat Generative Answer Stream (HTTP + ndjson/SSE)
  slug: nuclia-asyncapi
collections:
- collection_type: open
  name: Nuclia RAG-as-a-Service API
  slug: open-nuclia
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nuclia-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/nuclia-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuclia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nuclia-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nuclia
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuclia
- group: company
  title: ''
  type: Website
  url: https://nuclia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nuclia.dev/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/nuclia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nuclia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nuclia-finops.yml
created: '2026-06-20'
description: Nuclia is a RAG-as-a-Service / AI search platform (now part of Progress as Progress Agentic RAG). It ingests unstructured data - documents, files, audio, video, web pages and conversations - into Knowledge Boxes, automatically extracting, embedding and indexing it so applications can run hybrid (semantic, keyword, graph) search and get grounded generative answers through a regional REST API.
finops:
- name: Nuclia Finops
  service_category: AI and Machine Learning
  slug: nuclia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuclia.png
layout: provider
modified: '2026-06-20'
name: Nuclia
nav: Providers
network: true
overview: 'Nuclia publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ask API, Knowledge Boxes API, Predict API, and 2 more. Tagged areas include AI, RAG, Search, Knowledge Base, and Unstructured Data.


  The Nuclia catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nuclia''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Nuclia Plans Pricing
  plan_count: 3
  slug: nuclia-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Nuclia Rate Limits
  slug: nuclia-rate-limits
rules:
- name: Nuclia API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: nuclia-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 68.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuclia/refs/heads/main/screenshots/nuclia-2026-06-20T190517.png
security:
- kind: authentication
  name: Nuclia Authentication
  slug: nuclia-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Nuclia Domain Security
  slug: nuclia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Nuclia Trust Center
  slug: nuclia-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: nuclia
tags:
- AI
- RAG
- Search
- Knowledge Base
- Unstructured Data
website: https://nuclia.com/
---
