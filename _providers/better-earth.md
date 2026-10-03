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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-earth/refs/heads/main/hosts/better-earth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-earth-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-earth/refs/heads/main/vendors/better-earth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-earth-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://betterearth.org/news/greenwashing-is-over-on-ab-1305/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-earth/refs/heads/main/security/better-earth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-earth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterearth.org
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Better Earth is a philanthropic initiative cultivating cultural change for people and planet. It offers impact‑oriented event activations, transforms cultural and educational institutions, and promotes climate hope and holistic wellness. The organization aims to catalyze positive change through honest communications and creative solutions, engaging global climate leaders to foster a better world.
image: https://betterearth.org/wp-content/uploads/2024/02/TimeforBetter-SHARE.jpg
layout: provider
modified: '2026-09-28'
name: Better Earth
nav: Providers
network: true
overview: Better Earth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Philanthropy, Event, and Sustainability.
random_paper: 13
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 5
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Better Earth Domain Security
  slug: better-earth-domain-security
  summary_line: TLSv1.3
slug: better-earth
tags:
- Company
- Climate
- Philanthropy
- Event
- Sustainability
- Community
website: https://betterearth.org
---
