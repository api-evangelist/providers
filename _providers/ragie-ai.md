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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Ragie Ai Agentic Access
  operation_count: 38
  slug: ragie-ai-agentic-access
  summary_line: 38 operations · 22 acting
api_count: 5
apis:
- description: The Connections API from Ragie — 8 operation(s) for connections.
  name: Ragie Connections API
  slug: ragie-ai-connections-api
- description: The Documents API from Ragie — 10 operation(s) for documents.
  name: Ragie Documents API
  slug: ragie-ai-documents-api
- description: The Entities API from Ragie — 4 operation(s) for entities.
  name: Ragie Entities API
  slug: ragie-ai-entities-api
- description: The Partitions API from Ragie — 3 operation(s) for partitions.
  name: Ragie Partitions API
  slug: ragie-ai-partitions-api
- description: The Retrievals API from Ragie — 2 operation(s) for retrievals.
  name: Ragie Retrievals API
  slug: ragie-ai-retrievals-api
artifact_total: 13
collections:
- collection_type: open
  name: Ragie API
  slug: open-ragie-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ragie-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ragie-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ragie-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ragie-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ragieai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ragie
- group: company
  title: ''
  type: Website
  url: https://www.ragie.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ragie.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/ragie-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ragie-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ragie-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ragie.ai/blog
created: '2026-06-20'
description: Ragie is a fully-managed Retrieval-Augmented Generation (RAG) as-a-service platform. Its REST API ingests documents (file upload, raw, or from URL), processes them into searchable chunks, and serves low-latency semantic retrieval, agentic responses, entity extraction, and managed data connectors to sources like Google Drive, Notion, and Confluence.
finops:
- name: Ragie Ai Finops
  service_category: AI and Machine Learning
  slug: ragie-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ragie-ai.png
layout: provider
modified: '2026-06-20'
name: Ragie
nav: Providers
network: true
overview: 'Ragie publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Documents API, Entities API, and 2 more. Tagged areas include AI, RAG, Retrieval, Vector Search, and Document Ingestion.


  Ragie''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ragie Ai Plans Pricing
  plan_count: 4
  slug: ragie-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Ragie Ai Rate Limits
  slug: ragie-ai-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ragie-ai/refs/heads/main/screenshots/ragie-ai-2026-06-20T192529.png
security:
- kind: authentication
  name: Ragie Ai Authentication
  slug: ragie-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ragie Ai Domain Security
  slug: ragie-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ragie Ai Vulnerability Disclosure
  slug: ragie-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ragie-ai
tags:
- AI
- RAG
- Retrieval
- Vector Search
- Document Ingestion
website: https://www.ragie.ai
---
