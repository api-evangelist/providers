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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Dremio Intelligent Lakehouse Platform Agentic Access
  operation_count: 20
  slug: dremio-intelligent-lakehouse-platform-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 9
apis:
- description: Dremio is an agentic lakehouse platform built natively on Apache Iceberg, Polaris, and Arrow. It provides AI-powered analytics, an intelligent SQL query engine, an AI semantic layer, and an open catal
  name: Dremio | Intelligent Lakehouse Platform
  slug: dremio-intelligent-lakehouse-platform
- description: The Authentication API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for authentication.
  name: Dremio | Intelligent Lakehouse Platform Authentication API
  slug: dremio-intelligent-lakehouse-platform-authentication-api
- description: The Catalog API from Dremio | Intelligent Lakehouse Platform — 3 operation(s) for catalog.
  name: Dremio | Intelligent Lakehouse Platform Catalog API
  slug: dremio-intelligent-lakehouse-platform-catalog-api
- description: The Jobs API from Dremio | Intelligent Lakehouse Platform — 4 operation(s) for jobs.
  name: Dremio | Intelligent Lakehouse Platform Jobs API
  slug: dremio-intelligent-lakehouse-platform-jobs-api
- description: The PAT API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for pat.
  name: Dremio | Intelligent Lakehouse Platform PAT API
  slug: dremio-intelligent-lakehouse-platform-pat-api
- description: The Reflections API from Dremio | Intelligent Lakehouse Platform — 2 operation(s) for reflections.
  name: Dremio | Intelligent Lakehouse Platform Reflections API
  slug: dremio-intelligent-lakehouse-platform-reflections-api
- description: The Roles API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for roles.
  name: Dremio | Intelligent Lakehouse Platform Roles API
  slug: dremio-intelligent-lakehouse-platform-roles-api
- description: The Scripts API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for scripts.
  name: Dremio | Intelligent Lakehouse Platform Scripts API
  slug: dremio-intelligent-lakehouse-platform-scripts-api
- description: The Sources API from Dremio | Intelligent Lakehouse Platform — 1 operation(s) for sources.
  name: Dremio | Intelligent Lakehouse Platform Sources API
  slug: dremio-intelligent-lakehouse-platform-sources-api
artifact_total: 17
collections:
- collection_type: open
  name: Dremio Intelligent Lakehouse REST API
  slug: open-dremio-intelligent-lakehouse-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dremio-intelligent-lakehouse-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dremio-intelligent-lakehouse-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dremio-intelligent-lakehouse-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dremio-intelligent-lakehouse-platform-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dremio
- group: company
  title: ''
  type: Website
  url: https://www.dremio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dremio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dremio.com/
- group: operate
  title: ''
  type: Community
  url: https://community.dremio.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dremio.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.dremio.com/blog/feed/
created: '2025-07-15'
description: Dremio is an agentic lakehouse platform built natively on Apache Iceberg, Polaris, and Arrow, combining AI-powered analytics with unified data access and governance across multiple data sources without requiring ETL pipelines.
finops:
- name: Dremio Intelligent Lakehouse Platform Finops
  service_category: API
  slug: dremio-intelligent-lakehouse-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dremio-intelligent-lakehouse-platform.png
layout: provider
modified: '2026-04-28'
name: Dremio | Intelligent Lakehouse Platform
nav: Providers
network: true
overview: 'Dremio | Intelligent Lakehouse Platform publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Catalog API, Jobs API, and 5 more. Tagged areas include Data, Analytics, Lakehouse, Apache Iceberg, and SQL.


  Dremio | Intelligent Lakehouse Platform''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Dremio Intelligent Lakehouse Platform Plans Pricing
  plan_count: 3
  slug: dremio-intelligent-lakehouse-platform-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: Dremio Intelligent Lakehouse Platform Rate Limits
  slug: dremio-intelligent-lakehouse-platform-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.2
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dremio-intelligent-lakehouse-platform/refs/heads/main/screenshots/dremio-intelligent-lakehouse-platform-2026-06-20T180225.png
security:
- kind: authentication
  name: Dremio Intelligent Lakehouse Platform Authentication
  slug: dremio-intelligent-lakehouse-platform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dremio Intelligent Lakehouse Platform Domain Security
  slug: dremio-intelligent-lakehouse-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dremio Intelligent Lakehouse Platform Vulnerability Disclosure
  slug: dremio-intelligent-lakehouse-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dremio-intelligent-lakehouse-platform
tags:
- Data
- Analytics
- Lakehouse
- Apache Iceberg
- SQL
- AI
website: https://www.dremio.com/
---
