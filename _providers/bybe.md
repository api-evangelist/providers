---
access_model:
  confidence: high
  label: Public docs, gated credentials
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.bybe.io/v1/swagger.yaml
  - https://bybe.com/pricing
  - https://developer.bybe.io/
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bybe Agentic Access
  operation_count: 16
  slug: bybe-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- description: 'The BYBE Retail API, version 1. A REST/JSON API over BYBE''s records of manufacturers, rebate offers and products, plus the write surface that clips offers for consumers, validates redemptions against '
  name: BYBE API
  slug: bybe-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://bybe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bybe.io/
- group: docs
  title: ''
  type: Documentation
  url: https://bybe.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bybe.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://bybe.com/developers
- group: start
  title: ''
  type: Login
  url: https://dashboard.bybe.io/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://bybe.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bybe.com/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bybe.com/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: mailto:support@bybe.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BYBE-INC
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bybe.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bybe-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bybe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bybe-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bybe-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bybe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bybe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bybe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bybe-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bybe-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bybe-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bybe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bybe-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bybe-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bybe-llms.txt
created: '2026-07-17'
description: BYBE, Inc. is a promotion platform for the beer, wine, and spirits industry, connecting alcohol beverage brands, retailers, and consumers through digital cash-back rebates. Brands fund offers in the BYBE dashboard; retailers embed those offers in their own apps, sites and loyalty programs, and BYBE handles US state-by-state alcohol promotion compliance, redemption validation, clearing and consumer payout. BYBE publishes a real OpenAPI 3.0.1 contract for its Retail API at api.bybe.io covering manufacturers, products, offers, clips, consumers, stores and redemption disbursements, with HTTP Basic authentication and a documented SFTP CSV batch alternative for retailers that cannot call the API in real time. Backed by Techstars and Rev1 Ventures, BYBE was acquired by Swiftly in March 2024 and continues to operate under its own brand and domains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bybe.png
layout: provider
modified: '2026-08-13'
name: BYBE
nav: Providers
network: true
overview: 'BYBE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alcohol, Beverages, Promotions, and Rebates.


  BYBE''s developer surface includes documentation, API reference, getting-started guide, pricing, support, authentication, sandbox, and 20 more developer resources.'
plans:
- name: Bybe Plans Pricing
  plan_count: 2
  slug: bybe-plans-pricing
random_paper: 120
rate_limits:
- limit_count: 0
  name: Bybe Rate Limits
  slug: bybe-rate-limits
score:
  band: developing
  composite: 49.1
  delta: 44.1
  facets:
    commercial_clarity: 65.8
    contract_quality: 44.8
    developer_ergonomics: 63.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bybe/refs/heads/main/screenshots/bybe-2026-07-25T204132.png
security:
- kind: authentication
  name: Bybe Authentication
  slug: bybe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bybe Domain Security
  slug: bybe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bybe
tags:
- Company
- Alcohol
- Beverages
- Promotions
- Rebates
- Marketing
- Retail
- CPG
- Loyalty
- Payments
- Disbursements
- Compliance
website: https://bybe.com/
---
