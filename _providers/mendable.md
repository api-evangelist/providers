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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mendable Agentic Access
  operation_count: 6
  slug: mendable-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mendable Chat API
  slug: open-mendable-chat-api
- collection_type: open
  name: Mendable Chat Conversations API
  slug: open-mendable-conversations-api
- collection_type: open
  name: Mendable Chat Ingestion API
  slug: open-mendable-ingestion-api
- collection_type: open
  name: Mendable Chat Ratings API
  slug: open-mendable-ratings-api
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
overview: 'Mendable publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Conversations API, Ingestion API, and 1 more. Tagged areas include Artificial Intelligence, Answers, Enterprise Search, RAG, and Support.


  Mendable''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mendable Plans Pricing
  plan_count: 2
  slug: mendable-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Mendable Rate Limits
  slug: mendable-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 54.9
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Artificial Intelligence
- Answers
- Enterprise Search
- RAG
- Support
website: https://www.mendable.ai
---
