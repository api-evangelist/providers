---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cherre Agentic Access
  operation_count: 2
  slug: cherre-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: The Auth API from Cherre — 1 operation(s) for auth.
  name: Cherre Auth API
  slug: cherre-auth-api
- description: The GraphQL API from Cherre — 1 operation(s) for graphql.
  name: Cherre GraphQL API
  slug: cherre-graphql-api
artifact_total: 11
collections:
- collection_type: open
  name: Cherre GraphQL API
  slug: open-cherre
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cherre-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cherre-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cherre-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cherre-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cherreco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cherre
- group: company
  title: ''
  type: Website
  url: https://www.cherre.com
- group: docs
  title: ''
  type: Documentation
  url: https://cherre.com/products/platform/
- group: commercial
  title: ''
  type: Plans
  url: plans/cherre-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cherre-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cherre-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.cherre.com/feed/
created: '2026-06-21'
description: Cherre is a real-estate data-integration and property-intelligence platform that connects, cleans, and resolves public, third-party, and proprietary real-estate datasets - property characteristics, tax and assessments, recorder and deeds, owners, parcel boundaries, and connected portfolio data - and serves them back through a single GraphQL API built on Hasura.
finops:
- name: Cherre Finops
  service_category: Analytics and Data
  slug: cherre-finops
graphqls:
- description: Cherre is a real-estate data-integration and property-intelligence platform. It ingests
  name: Cherre GraphQL API
  slug: cherre-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cherre.png
layout: provider
modified: '2026-06-21'
name: Cherre
nav: Providers
network: true
overview: 'Cherre publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and GraphQL API. Tagged areas include Real Estate, Property Intelligence, Data Integration, Knowledge Graph, and GraphQL.


  Cherre''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Cherre Plans Pricing
  plan_count: 3
  slug: cherre-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Cherre Rate Limits
  slug: cherre-rate-limits
score:
  band: thin
  composite: 41.6
  delta: -0.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 64.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cherre/refs/heads/main/screenshots/cherre-2026-07-25T205151.png
security:
- kind: authentication
  name: Cherre Authentication
  slug: cherre-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cherre Domain Security
  slug: cherre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cherre Trust Center
  slug: cherre-trust-center
  summary_line: SOC 2, ISO 27001
slug: cherre
tags:
- Real Estate
- Property Intelligence
- Data Integration
- Knowledge Graph
- GraphQL
website: https://www.cherre.com
---
