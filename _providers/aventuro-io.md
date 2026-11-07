---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/aventuro-io/hosts/aventuro-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aventuro-io-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aventuro-io/security/aventuro-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aventuro-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aventuro.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aventuro.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aventuro.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://aventuro.io/support
coverage:
  checked: '2026-11-02'
  detail: Public website provides human‑readable information but no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://aventuro.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Aventuro provides an interactive map of curated places to help travelers plan trips city by city. Users can filter locations by kid‑friendliness, wheelchair accessibility, dog‑friendliness, free entry, parking, and more. They can save favorite spots, organize them by day, and create personalized itineraries. Founded to simplify travel discovery, Aventuro aggregates thousands of points of interest, offering powerful filters for families, accessibility, and pet owners, and enables sharing of itineraries.
image: https://aventuro.io/favicon.ico
layout: provider
modified: '2026-11-02'
name: Aventuro
nav: Providers
network: true
overview: 'Aventuro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Mapping, Trip Planning, Accessibility, and FamilyFriendly.


  Aventuro''s developer surface includes support and 5 more developer resources.'
plans:
- name: Aventuro Io Plans Pricing
  plan_count: 0
  slug: aventuro-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aventuro Io Rate Limits
  slug: aventuro-io-rate-limits
scopes:
- name: Aventuro Io Scopes
  scope_count: 0
  slug: aventuro-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 11.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aventuro Io Authentication
  slug: aventuro-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aventuro Io Domain Security
  slug: aventuro-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aventuro-io
tags:
- Travel
- Mapping
- Trip Planning
- Accessibility
- FamilyFriendly
website: https://aventuro.io/
---
