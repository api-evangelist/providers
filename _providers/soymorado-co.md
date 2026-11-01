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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/soymorado-co/hosts/soymorado-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soymorado-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/soymorado-co/vendors/soymorado-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soymorado-co-vendors.yml
- group: auth
  href: https://artifacts.apis.io/soymorado-co/security/soymorado-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soymorado-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soymorado.co/
coverage:
  checked: '2026-10-29'
  detail: Morado provides an online gaming platform with no public API surface.
  evidence:
  - status: 200
    url: https://soymorado.co/
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Morado is an online gaming and gambling platform offering slot and mahjong games. The company operates the website https://soymorado.co/, which promotes a variety of casino-style slot games with features such as scatter hits and maxwin payouts. Morado targets players seeking digital slot experiences and provides a storefront for game selection, betting, and account management. The platform appears to be part of the broader online entertainment market and is backed by venture investors as noted in its harvest record.
image: https://soymorado.co/img/favicon.png
layout: provider
modified: '2026-10-28'
name: Morado
nav: Providers
network: true
overview: Morado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Gambling, Slots, Entertainment, and Online.
plans:
- name: Soymorado Co Plans Pricing
  plan_count: 0
  slug: soymorado-co-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Soymorado Co Rate Limits
  slug: soymorado-co-rate-limits
scopes:
- name: Soymorado Co Scopes
  scope_count: 0
  slug: soymorado-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
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
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Soymorado Co Authentication
  slug: soymorado-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Soymorado Co Domain Security
  slug: soymorado-co-domain-security
  summary_line: TLSv1.3
slug: soymorado-co
tags:
- Gaming
- Gambling
- Slots
- Entertainment
- Online
website: https://soymorado.co/
---
