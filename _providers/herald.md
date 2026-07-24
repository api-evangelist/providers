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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Herald Agentic Access
  operation_count: 18
  slug: herald-agentic-access
  summary_line: 18 operations · 8 acting
api_count: 10
apis:
- description: The Applications API from Herald — 2 operation(s) for applications.
  name: Herald Applications API
  slug: herald-applications-api
- description: The Authentication API from Herald — 1 operation(s) for authentication.
  name: Herald Authentication API
  slug: herald-authentication-api
- description: The Classifications API from Herald — 1 operation(s) for classifications.
  name: Herald Classifications API
  slug: herald-classifications-api
- description: The Distributors API from Herald — 1 operation(s) for distributors.
  name: Herald Distributors API
  slug: herald-distributors-api
- description: The Files API from Herald — 1 operation(s) for files.
  name: Herald Files API
  slug: herald-files-api
- description: The Producers API from Herald — 1 operation(s) for producers.
  name: Herald Producers API
  slug: herald-producers-api
- description: The Products API from Herald — 2 operation(s) for products.
  name: Herald Products API
  slug: herald-products-api
- description: The Quotes API from Herald — 1 operation(s) for quotes.
  name: Herald Quotes API
  slug: herald-quotes-api
- description: The Submissions API from Herald — 2 operation(s) for submissions.
  name: Herald Submissions API
  slug: herald-submissions-api
- description: The Webhooks API from Herald — 2 operation(s) for webhooks.
  name: Herald Webhooks API
  slug: herald-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Herald API
  slug: open-herald
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/herald-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/herald-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/herald-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heraldapi
- group: company
  title: ''
  type: Website
  url: https://www.heraldapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heraldapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/herald-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/herald-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/herald-finops.yml
created: '2026-06-25'
description: Herald builds digital infrastructure for commercial insurance, providing a single unified REST API that lets software platforms quote and bind across many carriers and lines of business. Developers create applications, submit them to carriers, and receive normalized quotes, products, classifications, and files through one integration secured with OAuth2 client-credentials bearer tokens.
finops:
- name: Herald Finops
  service_category: Insurance
  slug: herald-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/herald.png
layout: provider
modified: '2026-06-25'
name: Herald
nav: Providers
network: true
overview: 'Herald publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Classifications API, and 7 more. Tagged areas include Insurance, Insurtech, Commercial Insurance, Quoting, and Carriers.


  Herald''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Herald Plans Pricing
  plan_count: 1
  slug: herald-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Herald Rate Limits
  slug: herald-rate-limits
score:
  band: thin
  composite: 34.1
  delta: -1.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.6
  regulatory:
    applies: true
    regime: Insurance
    regime_id: insurance
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Herald Authentication
  slug: herald-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Herald Domain Security
  slug: herald-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: herald
tags:
- Insurance
- Insurtech
- Commercial Insurance
- Quoting
- Carriers
website: https://www.heraldapi.com
---
