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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/royal-meteorological-institute-belgium/hosts/royal-meteorological-institute-belgium-hosts.yml
  title: ''
  type: Hosts
  url: hosts/royal-meteorological-institute-belgium-hosts.yml
- group: auth
  href: https://artifacts.apis.io/royal-meteorological-institute-belgium/security/royal-meteorological-institute-belgium-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/royal-meteorological-institute-belgium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meteo.be/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meteo.be/nl/diensten/algemene-voorwaarden
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meteo.be/nl/legal/modal/legal_privacy_policy
- group: operate
  title: ''
  type: Support
  url: https://www.meteo.be/nl/over-het-kmi/contact
coverage:
  checked: '2026-10-28'
  detail: API documentation is behind a login page at https://app.meteo.be/
  evidence:
  - status: 200
    url: https://app.meteo.be/
  reason: customer-only-docs
  state: gated
created: '2026-10-28'
description: The Royal Meteorological Institute of Belgium (KMI) provides weather forecasts, climate data, and meteorological services for Belgium. It operates as a public scientific institute, offering open data on observations, forecasts, climate change analyses, and specialized services for government, businesses, and the public. The institute also publishes data portals and documentation for developers to access weather APIs and datasets.
image: https://www.meteo.be/frontend/img/general/logo-kmi--nl.svg?v20250829-1211
layout: provider
modified: '2026-10-28'
name: RMI Belgium WOW-BE
nav: Providers
network: true
overview: 'RMI Belgium WOW-BE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Climate, Meteorology, Belgium, and PublicSector.


  RMI Belgium WOW-BE''s developer surface includes support and 5 more developer resources.'
plans:
- name: Royal Meteorological Institute Belgium Plans Pricing
  plan_count: 0
  slug: royal-meteorological-institute-belgium-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Royal Meteorological Institute Belgium Rate Limits
  slug: royal-meteorological-institute-belgium-rate-limits
scopes:
- name: Royal Meteorological Institute Belgium Scopes
  scope_count: 0
  slug: royal-meteorological-institute-belgium-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Royal Meteorological Institute Belgium Authentication
  slug: royal-meteorological-institute-belgium-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Royal Meteorological Institute Belgium Domain Security
  slug: royal-meteorological-institute-belgium-domain-security
  summary_line: TLSv1.3 · DMARC
slug: royal-meteorological-institute-belgium
tags:
- Weather
- Climate
- Meteorology
- Belgium
- PublicSector
website: https://meteo.be/
---
