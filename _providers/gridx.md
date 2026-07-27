---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gridx Agentic Access
  operation_count: 8
  slug: gridx-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 4
apis:
- description: The Authentication API from GridX — 1 operation(s) for authentication.
  name: GridX Authentication API
  slug: gridx-authentication-api
- description: The Customer API from GridX — 2 operation(s) for customer.
  name: GridX Customer API
  slug: gridx-customer-api
- description: The OpenADR API from GridX — 2 operation(s) for openadr.
  name: GridX OpenADR API
  slug: gridx-openadr-api
- description: The Pricing API from GridX — 1 operation(s) for pricing.
  name: GridX Pricing API
  slug: gridx-pricing-api
artifact_total: 11
collections:
- collection_type: open
  name: GridX Enterprise Rate Platform API
  slug: open-gridx
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gridx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridx-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gridx-inc
- group: company
  title: ''
  type: Website
  url: https://www.gridx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-calculate-docs.gridx.com/calculate-apis-gridx-docs/get-pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/gridx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gridx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gridx-finops.yml
created: '2026-06-20'
description: GridX Inc. (Walnut Creek, California) is the Enterprise Rate Platform for modern utilities. Its cloud-based Rate Engine replicates utility billing-system (CIS) bill calculations to design, measure, implement, and bill advanced rates and programs. GridX exposes a partner/enterprise developer API (the Calculate / Empower APIs) for rate calculation, pricing retrieval, customer info/usage, bill and cost analysis, and OpenADR demand-response program subscriptions, currently documented for specific utility deployments (e.g., PG&E, SCE).
finops:
- name: Gridx Finops
  service_category: Energy and Utilities Software
  slug: gridx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gridx.png
layout: provider
modified: '2026-06-20'
name: GridX
nav: Providers
network: true
overview: 'GridX publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customer API, OpenADR API, and 1 more. Tagged areas include Energy, Utilities, Rate Engine, Billing, and Rate Analytics.


  GridX''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Gridx Plans Pricing
  plan_count: 1
  slug: gridx-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 3
  name: Gridx Rate Limits
  slug: gridx-rate-limits
score:
  band: thin
  composite: 37.5
  delta: 3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gridx/refs/heads/main/screenshots/gridx-2026-06-20T182406.png
security:
- kind: authentication
  name: Gridx Authentication
  slug: gridx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gridx Domain Security
  slug: gridx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gridx
tags:
- Energy
- Utilities
- Rate Engine
- Billing
- Rate Analytics
website: https://www.gridx.com/
---
