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
  href: https://raw.githubusercontent.com/api-evangelist/bemyfriends/refs/heads/main/hosts/bemyfriends-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bemyfriends-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bemyfriends.com/privacy-policy?hl=null
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bemyfriends/refs/heads/main/security/bemyfriends-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bemyfriends-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bemyfriends.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bemyfriends
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Bemyfriends is a global fandom business company that transforms the value of fandoms into successful enterprises. It offers comprehensive solutions including IT platforms, e‑commerce fulfillment, fan‑based platforms, and strategic consulting to help brands leverage fan communities worldwide. The company connects fans, brands, and creators, delivering total solutions for the growing global fandom market.
image: https://bemyfriends.com/images/bemyfriends.jpg
layout: provider
modified: '2026-09-27'
name: Bemyfriends
nav: Providers
network: true
overview: Bemyfriends is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fandom, Business, Solutions, and Global.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
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
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bemyfriends Domain Security
  slug: bemyfriends-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bemyfriends
tags:
- Company
- Fandom
- Business
- Solutions
- Global
website: https://bemyfriends.com
---
