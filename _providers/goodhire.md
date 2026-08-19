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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-08-19'
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
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoodHire Packages API
  slug: open-goodhire-packages-api
- collection_type: open
  name: GoodHire Packages Partner API
  slug: open-goodhire-partner-api
- collection_type: open
  name: GoodHire Packages Reports API
  slug: open-goodhire-reports-api
- collection_type: open
  name: GoodHire Packages Requestors API
  slug: open-goodhire-requestors-api
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
random_paper: 104
rate_limits:
- limit_count: 3
  name: Goodhire Rate Limits
  slug: goodhire-rate-limits
score:
  band: developing
  composite: 39.9
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 56.6
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
