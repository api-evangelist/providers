---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The first-party JSON API behind portal.pragmaticsemi.com, the Pragmatic Customer Portal. Discovered by reading the portal's own published JavaScript bundle, which sets REACT_APP_BASE_URL to https://ap
  name: Pragmatic Customer Portal API
  slug: customer-portal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pragmatic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pragmaticsemi.com/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/pragmatic-stock
- group: company
  title: ''
  type: Blog
  url: https://www.pragmaticsemi.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.pragmaticsemi.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pragmaticsemi.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pragmaticsemi.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://portal.pragmaticsemi.com/
- group: company
  title: ''
  type: Investors
  url: https://www.pragmaticsemi.com/investors
- group: company
  title: ''
  type: Careers
  url: https://talent.pragmaticsemi.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pragmatic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/pragmatic-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pragmatic-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pragmatic-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pragmatic-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pragmatic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pragmatic-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/pragmatic-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Pragmatic ships a real, live first-party JSON API - api-portal.pragmaticsemi.com/v1/, the backend of its Customer Portal, found by reading the portal's own JavaScript bundle - but publishes no reference, no OpenAPI and no developer portal for it; GET /v1/auth/login/ answers 405 Method Not Allowed, proving the route exists while every route beyond it needs an authenticated foundry-customer session.
  evidence:
  - status: 405
    url: https://api-portal.pragmaticsemi.com/v1/auth/login/
  - status: 404
    url: https://api-portal.pragmaticsemi.com/openapi.json
  - status: 200
    url: https://portal.pragmaticsemi.com/
  - status: 202
    url: https://www.pragmaticsemi.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Pragmatic Semiconductor Limited is a UK semiconductor manufacturer that designs and produces FlexICs - ultra-thin, physically flexible integrated circuits built on thin-film transistor (TFT) technology rather than conventional crystalline silicon. Founded in 2010 by Richard Price and Scott White and headquartered at Cambridge Science Park with manufacturing at Pragmatic Park in Sedgefield, County Durham, the company operates the Pragmatic FlexIC Foundry, a service that takes third-party custom flexible IC designs from tape-out to delivery in roughly six weeks. Product lines include the FlexIC Platform Gen 3 mixed-signal flexible ASIC design flow, Pragmatic NFC Connect and Pragmatic NFC Protect. The company raised a $231M Series D in 2023. Its only network-reachable API surface is the undocumented, authentication-gated backend of its customer portal; it publishes no developer program, no machine-readable contract and no public API reference.
layout: provider
modified: '2026-08-26'
name: Pragmatic
nav: Providers
network: true
overview: 'Pragmatic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Manufacturing, and Flexible Electronics.


  Pragmatic''s developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Pragmatic Plans Pricing
  plan_count: 0
  slug: pragmatic-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Pragmatic Rate Limits
  slug: pragmatic-rate-limits
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Pragmatic Authentication
  slug: pragmatic-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pragmatic Domain Security
  slug: pragmatic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pragmatic
tags:
- Company
- Semiconductors
- Hardware
- Manufacturing
- Flexible Electronics
- Integrated Circuits
- Foundry
- NFC
- RFID
- Internet of Things
- United Kingdom
website: https://www.pragmaticsemi.com/
---
