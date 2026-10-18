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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bp-pulse/refs/heads/main/hosts/bp-pulse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bp-pulse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bp-pulse/refs/heads/main/vendors/bp-pulse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bp-pulse-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bppulse.com/en-us/legal-notice
- group: operate
  title: ''
  type: Support
  url: https://www.bppulse.com/en-au/help-and-support/charging-on-the-go/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bppulse.com/en-us/privacy-notice
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bppulse.com/en-us/public-ev-charging/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.bppulse.com/en-us/going-electric/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bp-pulse/refs/heads/main/security/bp-pulse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bp-pulse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bppulse.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.bppulse.com/mcp
  - status: 200
    url: https://www.bppulse.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: bp pulse provides public EV charging stations and fleet management solutions across multiple countries. It offers businesses and consumers fast, reliable charging infrastructure, mobile app integration, and tools to monitor and optimize electric vehicle usage. The company leverages over a century of energy expertise to deliver scalable charging networks, supporting sustainability and the transition to electric mobility.
image: http://localhost:3000/en-us/bp-pulse-eom.png
layout: provider
modified: '2026-10-13'
name: bp pulse
nav: Providers
network: true
overview: 'bp pulse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EVCharging, Fleet Management, Sustainability, and Energy.


  bp pulse''s developer surface includes support, pricing, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bp Pulse Domain Security
  slug: bp-pulse-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bp-pulse
tags:
- Company
- EVCharging
- Fleet Management
- Sustainability
- Energy
website: https://www.bppulse.com/
---
