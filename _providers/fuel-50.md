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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://fuel50.com/privacy-and-legal
- group: agent
  href: https://artifacts.apis.io/fuel-50/well-known/fuel-50-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fuel-50-well-known.yml
- group: other
  href: https://artifacts.apis.io/fuel-50/hosts/fuel-50-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fuel-50-hosts.yml
- group: other
  href: https://artifacts.apis.io/fuel-50/vendors/fuel-50-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fuel-50-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://fuel50.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://fuel50.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fuel50.com/
- group: auth
  href: https://artifacts.apis.io/fuel-50/security/fuel-50-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fuel-50-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fuel-50/security/fuel-50-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fuel-50-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fuel50.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fuel50.com/privacy-and-legal
- group: company
  title: ''
  type: Blog
  url: https://fuel50.com/blog
coverage:
  checked: '2026-10-25'
  detail: The Fuel50 developer documentation is only available via JavaScript‑rendered pages, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://fuel50.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Fuel 50 provides a modern workforce management platform that helps organizations optimize employee scheduling, time tracking, and labor compliance. The solution offers real‑time visibility into labor costs, automated shift planning, and integration with payroll and HR systems, enabling businesses to improve operational efficiency and employee satisfaction. Backed by Bonfire Ventures, Fuel 50 serves enterprises across various industries seeking to streamline workforce operations and enhance productivity.
layout: provider
modified: '2026-10-25'
name: Fuel 50
nav: Providers
network: true
overview: 'Fuel 50 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce, Scheduling, Time Tracking, and Labor Compliance.


  Fuel 50''s developer surface includes pricing, documentation, engineering blog, and 9 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 45.5
    operational_transparency: 0.0
  previous_composite: 15.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fuel-50/fuel-50-2026-11-03T132356.png
security:
- kind: domain-security
  name: Fuel 50 Domain Security
  slug: fuel-50-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fuel 50 Trust Center
  slug: fuel-50-trust-center
  summary_line: GDPR
slug: fuel-50
tags:
- Company
- Workforce
- Scheduling
- Time Tracking
- Labor Compliance
website: https://fuel50.com
---
