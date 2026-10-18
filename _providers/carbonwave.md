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
api_count: 1
apis:
- description: Carbonwave provides a developer API (not publicly documented).
  name: Carbonwave API
  slug: carbonwave-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonwave/refs/heads/main/hosts/carbonwave-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonwave-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbonwave/refs/heads/main/vendors/carbonwave-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbonwave-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://carbonwave.com/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbonwave/refs/heads/main/security/carbonwave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonwave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonwave.com/
- group: company
  title: ''
  type: Blog
  url: https://carbonwave.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://carbonwave.com/contact/
coverage:
  checked: '2026-10-07'
  detail: Carbonwave's website provides no public developer documentation or API specification.
  evidence:
  - status: 200
    url: https://carbonwave.com/
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Carbonwave develops ultra‑regenerative, plant‑based biomaterials derived from Sargassum seaweed. By upcycling this abundant ocean bloom, they create sustainable materials that restore soils, reduce micro‑plastic waste, and help achieve carbon neutrality, addressing climate change and ocean health.
layout: provider
modified: '2026-10-07'
name: Carbonwave
nav: Providers
network: true
overview: 'Carbonwave is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biomaterials, Sustainability, Seaweed, and Climate Tech.


  Carbonwave''s developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbonwave Domain Security
  slug: carbonwave-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carbonwave
tags:
- Company
- Biomaterials
- Sustainability
- Seaweed
- Climate Tech
website: https://carbonwave.com/
---
