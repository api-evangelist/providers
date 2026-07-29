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
- acting_count: 4
  human_in_the_loop: 0
  name: Boost Insurance Agentic Access
  operation_count: 4
  slug: boost-insurance-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
apis:
- description: The Authentication API from Boost Insurance — 1 operation(s) for authentication.
  name: Boost Insurance Authentication API
  slug: boost-insurance-authentication-api
- description: The Claims API from Boost Insurance — 1 operation(s) for claims.
  name: Boost Insurance Claims API
  slug: boost-insurance-claims-api
- description: The Policies API from Boost Insurance — 1 operation(s) for policies.
  name: Boost Insurance Policies API
  slug: boost-insurance-policies-api
- description: The Quotes API from Boost Insurance — 1 operation(s) for quotes.
  name: Boost Insurance Quotes API
  slug: boost-insurance-quotes-api
artifact_total: 12
collections:
- collection_type: open
  name: Boost Insurance API
  slug: open-boost-insurance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boost-insurance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boost-insurance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boost-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/boost-insurance-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boostinsurance
- group: company
  title: ''
  type: Website
  url: https://www.boostinsurance.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.boostinsurance.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/boost-insurance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boost-insurance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/boost-insurance-finops.yml
created: '2026-06-25'
description: Boost Insurance is an insurance-as-a-service / embedded-insurance infrastructure platform that packages compliance, capital, and technology into a turnkey, white-labeled program accessible through a modern RESTful API. The Boost Policy Admin System (PAS) lets partners quote, bind, issue, endorse, cancel, and manage claims for admitted and surplus-lines products using JSON over OAuth 2.0.
finops:
- name: Boost Insurance Finops
  service_category: Insurance
  slug: boost-insurance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boost-insurance.png
layout: provider
modified: '2026-06-25'
name: Boost Insurance
nav: Providers
network: true
overview: 'Boost Insurance publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Claims API, Policies API, and 1 more. Tagged areas include Insurance, Embedded Insurance, Insurance-as-a-Service, Policy Administration, and Claims.


  Boost Insurance''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Boost Insurance Plans Pricing
  plan_count: 1
  slug: boost-insurance-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 1
  name: Boost Insurance Rate Limits
  slug: boost-insurance-rate-limits
scopes:
- name: Boost Insurance Scopes
  scope_count: 0
  slug: boost-insurance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.5
  delta: -2.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 43.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boost-insurance/refs/heads/main/screenshots/boost-insurance-2026-07-25T203625.png
security:
- kind: authentication
  name: Boost Insurance Authentication
  slug: boost-insurance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Boost Insurance Domain Security
  slug: boost-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boost-insurance
tags:
- Insurance
- Embedded Insurance
- Insurance-as-a-Service
- Policy Administration
- Claims
website: https://www.boostinsurance.com
---
