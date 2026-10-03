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
  href: https://raw.githubusercontent.com/api-evangelist/berlin-brands-group/refs/heads/main/hosts/berlin-brands-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/berlin-brands-group-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/berlin-brands-group/refs/heads/main/security/berlin-brands-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/berlin-brands-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.berlinbrands.de/en/
- group: company
  title: ''
  type: AboutUs
  url: https://www.berlinbrands.de/en/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.berlinbrands.de/en/about-us/contact
- group: other
  title: ''
  type: Imprint
  url: https://www.berlinbrands.de/en/about-us/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.berlinbrands.de/en/about-us/datenschutz
coverage:
  checked: '2026-09-27'
  detail: The website https://www.berlinbrands.de/en/ returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.berlinbrands.de/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Berlin Brands Group (BBG) is a Berlin‑based holding company that creates, builds, buys and scales consumer brands globally. Founded in 2005, it operates multiple e‑commerce brands across home appliances, audio, lighting and lifestyle, employing thousands and serving European markets.
layout: provider
modified: '2026-09-27'
name: Berlin Brands Group
nav: Providers
network: true
overview: Berlin Brands Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Consumer Goods, Berlin, and Holding.
random_paper: 3
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Berlin Brands Group Domain Security
  slug: berlin-brands-group-domain-security
  summary_line: TLSv1.3 · HSTS
slug: berlin-brands-group
tags:
- Company
- E-Commerce
- Consumer Goods
- Berlin
- Holding
website: https://www.berlinbrands.de/en/
---
