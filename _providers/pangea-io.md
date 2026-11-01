---
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Full Stack FX Management API providing endpoints for foreign exchange risk management.
  name: Pangea API
  slug: pangea-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/pangea-io/plans/pangea-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pangea-io-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/pangea-io/hosts/pangea-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pangea-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/pangea-io/vendors/pangea-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pangea-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pangea.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pangea.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pangea.io/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.pangea.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pangea.io/
- group: auth
  href: https://artifacts.apis.io/pangea-io/security/pangea-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pangea-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pangea.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://docs.pangea.io/mcp
  - status: 200
    url: https://www.pangea.io/
  reason: partner-login
  state: gated
created: '2026-10-26'
description: Pangea provides a powerful financial risk management platform built by treasury and trading veterans to reduce FX volatility, improve transparency, and lower total cost of ownership. Their AI‑powered foreign exchange hedging solutions help enterprises mitigate currency risk, automate hedging strategies, and gain real‑time insights across global markets.
image: https://cdn.prod.website-files.com/63ab4ce341b0cab2cbe22132/640b5e5c97b40f170e67bdc9_pangea-seo-image-2023-03-10.jpg
layout: provider
modified: '2026-10-26'
name: Pangea
nav: Providers
network: true
overview: 'Pangea is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Risk Management, FX Hedging, and AI.


  Pangea''s developer surface includes pricing, documentation, and 8 more developer resources.'
plans:
- name: Pangea Io Plans Pricing
  plan_count: 1
  slug: pangea-io-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pangea Io Domain Security
  slug: pangea-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pangea-io
tags:
- Company
- Finance
- Risk Management
- FX Hedging
- AI
website: https://www.pangea.io/
---
