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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluespine/refs/heads/main/hosts/bluespine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluespine-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bluespine/refs/heads/main/vendors/bluespine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluespine-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bluespine/refs/heads/main/security/bluespine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluespine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluespine.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluespine.io/privacy-policy
coverage:
  checked: '2026-09-29'
  detail: The site provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.bluespine.io/
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Bluespine is an AI‑driven platform that helps self‑insured employers and health‑plan sponsors reduce medical claims overbilling, monitor plan performance, and meet fiduciary duties under ERISA. Founded in 2023 and based in New York, the company leverages machine‑readable price transparency files, carrier billing guidelines, and proprietary data sources to detect policy violations and recover savings for plan participants.
image: https://cdn.prod.website-files.com/65f956e060d658e1a054f39d/6624e107774554a954841817_Open%20Graph.webp
layout: provider
modified: '2026-09-29'
name: Bluespine
nav: Providers
network: true
overview: Bluespine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Claims, and Fiduciary.
random_paper: 21
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluespine Domain Security
  slug: bluespine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluespine
tags:
- Company
- Healthcare
- Artificial Intelligence
- Claims
- Fiduciary
website: https://www.bluespine.io/
---
