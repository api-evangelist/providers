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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Ragie Ai Agentic Access
  operation_count: 38
  slug: ragie-ai-agentic-access
  summary_line: 38 operations · 22 acting
api_count: 1
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ragie Connections API
  slug: open-ragie-ai-connections-api
- collection_type: open
  name: Ragie Connections Documents API
  slug: open-ragie-ai-documents-api
- collection_type: open
  name: Ragie Connections Entities API
  slug: open-ragie-ai-entities-api
- collection_type: open
  name: Ragie Connections Partitions API
  slug: open-ragie-ai-partitions-api
- collection_type: open
  name: Ragie Connections Retrievals API
  slug: open-ragie-ai-retrievals-api
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
overview: 'Ragie publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Connections API, Documents API, Entities API, and 2 more. Tagged areas include Artificial Intelligence, RAG, Retrieval, Vector Search, and Document Ingestion.


  Ragie''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ragie Ai Plans Pricing
  plan_count: 4
  slug: ragie-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Ragie Ai Rate Limits
  slug: ragie-ai-rate-limits
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Artificial Intelligence
- RAG
- Retrieval
- Vector Search
- Document Ingestion
website: https://www.ragie.ai
---
