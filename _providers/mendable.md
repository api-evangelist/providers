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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mendable Agentic Access
  operation_count: 6
  slug: mendable-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 4
apis:
- description: Ask grounded questions over ingested content.
  name: Mendable Chat API
  slug: mendable-chat-api
- description: Create conversation sessions.
  name: Mendable Conversations API
  slug: mendable-conversations-api
- description: Ingest and track data sources.
  name: Mendable Ingestion API
  slug: mendable-ingestion-api
- description: Rate answer messages.
  name: Mendable Ratings API
  slug: mendable-ratings-api
artifact_total: 12
collections:
- collection_type: open
  name: Mendable API
  slug: open-mendable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mendable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mendable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mendable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mendable-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mendableai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mendable
- group: company
  title: ''
  type: Website
  url: https://www.mendable.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mendable.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/mendable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mendable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mendable-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mendable.ai/blog
created: '2026-06-20'
description: Mendable is an AI answers and enterprise search platform that lets teams ingest their documentation, websites, and knowledge sources and serve grounded, cited AI chat answers over them. Built by the Firecrawl / Mendable team, it exposes a REST API at https://api.mendable.ai/v1 for creating conversations, asking questions over ingested content with streaming, ingesting and managing data sources, and rating answers.
finops:
- name: Mendable Finops
  service_category: AI and Machine Learning
  slug: mendable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mendable.png
layout: provider
modified: '2026-06-20'
name: Mendable
nav: Providers
network: true
overview: 'Mendable publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Conversations API, Ingestion API, and 1 more. Tagged areas include AI, Answers, Enterprise Search, RAG, and Support.


  Mendable''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mendable Plans Pricing
  plan_count: 2
  slug: mendable-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Mendable Rate Limits
  slug: mendable-rate-limits
score:
  band: thin
  composite: 39.1
  delta: -2.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 61.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mendable/refs/heads/main/screenshots/mendable-2026-06-20T185156.png
security:
- kind: authentication
  name: Mendable Authentication
  slug: mendable-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mendable Domain Security
  slug: mendable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mendable Trust Center
  slug: mendable-trust-center
  summary_line: SOC 2, GDPR
slug: mendable
tags:
- AI
- Answers
- Enterprise Search
- RAG
- Support
website: https://www.mendable.ai
---
