---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.toogoodtogo.com/en-us
- group: start
  title: ''
  type: Login
  url: https://store.toogoodtogo.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.toogoodtogo.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/too-good-to-go-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/too-good-to-go-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/too-good-to-go-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/too-good-to-go-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/too-good-to-go-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toogoodtogo.com/en-gb/terms-and-conditions-using-the-app
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toogoodtogo.com/en-us/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/too-good-to-go-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/too-good-to-go-security.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/too-good-to-go-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/too-good-to-go-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/too-good-to-go-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/too-good-to-go-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/too-good-to-go-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/too-good-to-go-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/too-good-to-go-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/too-good-to-go-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Too Good To Go runs a developer subdomain at developers.toogoodtogo.com, but it answers 401 with a "Login with JumpCloud" SSO interstitial, and its two live backends (api.toogoodtogo.com and apptoogoodtogo.com) return RFC 9457 404s on all 13 OpenAPI, Swagger and GraphQL discovery paths — the only machine surface is the private mobile-app and MyStore partner backend, fronted by DataDome.
  evidence:
  - status: 401
    url: https://developers.toogoodtogo.com/
  - status: 404
    url: https://api.toogoodtogo.com/openapi.json
  - status: 403
    url: https://apptoogoodtogo.com/api/auth/v5/authByEmail
  - status: 429
    url: https://www.toogoodtogo.com/en-us
  - status: 200
    url: https://www.toogoodtogo.com/.well-known/security.txt
  reason: partner-login
  state: gated
created: '2026-08-30'
description: 'Too Good To Go is a Danish certified B Corporation, founded in Copenhagen in 2015, that operates the world''s largest marketplace for surplus food. Consumers use its mobile app to buy discounted "Surprise Bags" of unsold food from bakeries, restaurants, supermarkets and hotels near closing time, and partner businesses list that surplus through the MyStore partner portal at store.toogoodtogo.com. Alongside the consumer marketplace the company sells Too Good To Go Platform, a modular AI-assisted surplus-management product for grocery retailers that tracks near-expiry inventory, sets automated markdowns, routes unsold stock to charity and pushes the remainder onto the marketplace. It also runs the Look-Smell-Taste date-label campaign and Too Good To Go Parcels. Too Good To Go publishes no public API, developer portal, or machine-readable contract: its developer subdomain answers 401 behind a JumpCloud SSO login, and the live backends at api.toogoodtogo.com and apptoogoodtogo.com
  serve only the mobile app and the partner portal.'
image: https://store.toogoodtogo.com/apple-touch-icon.png
layout: provider
modified: '2026-08-30'
name: Too Good To Go
nav: Providers
network: true
overview: Too Good To Go is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Waste, Surplus Food, Marketplace, and Sustainability.
plans:
- name: Too Good To Go Plans Pricing
  plan_count: 0
  slug: too-good-to-go-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Too Good To Go Rate Limits
  slug: too-good-to-go-rate-limits
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 17.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Too Good To Go Domain Security
  slug: too-good-to-go-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Too Good To Go Vulnerability Disclosure
  slug: too-good-to-go-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Too Good To Go Trust Center
  slug: too-good-to-go-trust-center
  summary_line: SOC 2 Type 2, PCI DSS v4.0.1
slug: too-good-to-go
tags:
- Company
- Food Waste
- Surplus Food
- Marketplace
- Sustainability
- Grocery Retail
- Consumer App
- Climate Tech
- B Corporation
- Denmark
website: https://www.toogoodtogo.com/en-us
---
