---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Bright Uro's Glean system.
  name: Bright Uro API
  slug: bright-uro-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bright-uro/hosts/bright-uro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bright-uro-hosts.yml
- group: other
  href: https://artifacts.apis.io/bright-uro/vendors/bright-uro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bright-uro-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bright-uro/security/bright-uro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bright-uro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brighturo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gleanuds.com/technology/
- group: company
  title: ''
  type: About
  url: https://www.gleanuds.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.gleanuds.com/category/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gleanuds.com/wp-content/uploads/2026/04/BrightUroTermsConditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gleanuds.com/wp-content/uploads/2026/06/BrightUroPrivacyPolicy-June-2026.pdf
coverage:
  checked: '2026-10-06'
  detail: Technology page renders via JavaScript, no machine‑readable API spec discovered.
  evidence:
  - status: 200
    url: https://www.gleanuds.com/technology/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Bright Uro offers innovative bladder function diagnostic technology through its Glean system, providing non‑invasive, real‑life data collection without catheters. The platform improves patient comfort and delivers high‑quality insights for clinicians, aiming to streamline diagnosis and treatment decisions in urology.
image: https://www.gleanuds.com/wp-content/uploads/2026/04/favicon-192x192-1.png
layout: provider
modified: '2026-10-06'
name: Bright Uro
nav: Providers
network: true
overview: 'Bright Uro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Medical Devices, Diagnostics, and Urology.


  Bright Uro''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 12.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bright-uro/bright-uro-2026-11-03T122613.png
security:
- kind: domain-security
  name: Bright Uro Domain Security
  slug: bright-uro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bright-uro
tags:
- Company
- Health Tech
- Medical Devices
- Diagnostics
- Urology
website: https://brighturo.com/
---
