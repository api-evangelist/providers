---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
- acting_count: 3
  human_in_the_loop: 0
  name: Goodhire Agentic Access
  operation_count: 8
  slug: goodhire-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 4
apis:
- description: List available screening packages (product bundles) and prices.
  name: GoodHire Packages API
  slug: goodhire-packages-api
- description: Partner API app-access flow for embedded HR platforms.
  name: GoodHire Partner API
  slug: goodhire-partner-api
- description: Order and track background check reports.
  name: GoodHire Reports API
  slug: goodhire-reports-api
- description: Manage the users who order and are associated with reports.
  name: GoodHire Requestors API
  slug: goodhire-requestors-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goodhire-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodhire-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodhire-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goodhire
- group: company
  title: ''
  type: Website
  url: https://www.goodhire.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.goodhire.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goodhire.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/goodhire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goodhire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/goodhire-finops.yml
created: '2026-07-03'
description: GoodHire is an FCRA-compliant employment background check platform aimed at small and midsize businesses, offering criminal, identity, employment, education, and reference screening with candidate self-consent workflows. GoodHire was acquired by Checkr (the developer-first background check company) in 2021 - the deal was reported at roughly $400M - and now operates as "GoodHire, A Checkr Company." The GoodHire API is a RESTful, FCRA-compliant background screening API split into a Customer API (a single company ordering its own reports) and a Partner API (HR platforms that let their employer customers order GoodHire reports). Background checks are ordered by creating a report object tied to a candidate and a package; status changes are delivered via webhooks. API keys are gated - developers request access from api@goodhire.com and build against a sandbox before production.
finops:
- name: Goodhire Finops
  service_category: Background Screening and Compliance
  slug: goodhire-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goodhire.png
layout: provider
modified: '2026-07-03'
name: GoodHire
nav: Providers
network: true
overview: 'GoodHire publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Packages API, Partner API, Reports API, and 1 more. Tagged areas include Background Checks, Employment Screening, Identity Verification, HR, and Compliance.


  GoodHire''s developer surface includes authentication, documentation, pricing, and 7 more developer resources.'
plans:
- name: Goodhire Plans Pricing
  plan_count: 4
  slug: goodhire-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 3
  name: Goodhire Rate Limits
  slug: goodhire-rate-limits
score:
  band: thin
  composite: 42.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.5
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goodhire/refs/heads/main/screenshots/goodhire-2026-07-25T220045.png
security:
- kind: authentication
  name: Goodhire Authentication
  slug: goodhire-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goodhire Domain Security
  slug: goodhire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodhire
tags:
- Background Checks
- Employment Screening
- Identity Verification
- HR
- Compliance
- FCRA
- Checkr
website: https://www.goodhire.com/
---
