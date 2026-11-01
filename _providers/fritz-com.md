---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/fritz-com/llms/fritz-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fritz-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/fritz-com/well-known/fritz-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fritz-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fritz-com/hosts/fritz-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fritz-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fritz-com/vendors/fritz-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fritz-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fritz.com/policies/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fritz.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://fritz.com/pages/login
- group: auth
  href: https://artifacts.apis.io/fritz-com/security/fritz-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fritz-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fritz.com/
created: '2026-10-28'
description: FRITZ! (formerly AVM, FRITZ!Box) provides networking hardware and smart home solutions, including routers, repeaters, and home automation devices. The company offers APIs for device management, firmware updates, and integration with smart home platforms, serving both consumers and developers.
image: http://fritz.com/cdn/shop/files/kampagne_2025_willkommen_header_1200x628_b3221394-5c8a-4011-88a1-1d2c697c8210.webp?v=1758531012
layout: provider
modified: '2026-10-28'
name: FRITZ! (formerly AVM, FRITZ!Box)
nav: Providers
network: true
overview: FRITZ! (formerly AVM, FRITZ!Box) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Routers, Mesh Wi‑Fi, Smart Home, and Telephony.
random_paper: 11
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fritz Com Domain Security
  slug: fritz-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fritz-com
tags:
- Routers
- Mesh Wi‑Fi
- Smart Home
- Telephony
website: https://fritz.com/
---
