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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Orama Agentic Access
  operation_count: 8
  slug: orama-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 5
apis:
- description: The open-source @orama/orama library (Apache 2.0) - a complete in-memory search engine and RAG pipeline that runs in the browser, on the server, or at the edge in under 2kb. Exposes JavaScript functio
  name: Orama Open Source Engine
  slug: oss-engine
- description: Generate retrieval-augmented (RAG) answers over an index.
  name: Orama Answer API
  slug: orama-answer-api
- description: Insert, update, delete, and bulk-replace documents in an index.
  name: Orama Documents API
  slug: orama-documents-api
- description: Manage Orama Cloud index schema and deployments.
  name: Orama Indexes API
  slug: orama-indexes-api
- description: Run full-text, vector, and hybrid search queries.
  name: Orama Search API
  slug: orama-search-api
artifact_total: 12
collections:
- collection_type: open
  name: Orama Cloud API
  slug: open-orama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orama-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oramasearch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/askorama
- group: company
  title: ''
  type: Website
  url: https://orama.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orama.com
- group: commercial
  title: ''
  type: Plans
  url: plans/orama-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orama-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/orama-finops.yml
created: '2026-06-21'
description: Orama is an open-source, in-memory search engine and RAG pipeline (full-text, vector, and hybrid search in under 2kb) plus Orama Cloud, a hosted REST platform for managing indexes, ingesting documents, running search, and building answer (RAG) experiences. The OSS engine is a JavaScript library; Orama Cloud is the managed API and dashboard layered on top.
finops:
- name: Orama Finops
  service_category: Analytics
  slug: orama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orama.png
layout: provider
modified: '2026-06-21'
name: Orama
nav: Providers
network: true
overview: 'Orama publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Answer API, Documents API, Indexes API, and 1 more. Tagged areas include Search, Vector Search, RAG, Open Source, and Search as a Service.


  Orama''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Orama Plans Pricing
  plan_count: 5
  slug: orama-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 6
  name: Orama Rate Limits
  slug: orama-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Orama Authentication
  slug: orama-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orama Domain Security
  slug: orama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orama
tags:
- Search
- Vector Search
- RAG
- Open Source
- Search as a Service
website: https://orama.com
---
