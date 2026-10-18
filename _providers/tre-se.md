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
- description: Tre provides mobile and broadband services; no public developer API is documented.
  name: Tre API
  slug: tre-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tre-se/refs/heads/main/hosts/tre-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tre-se-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tre-se/refs/heads/main/vendors/tre-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tre-se-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.tre.se/site/terms
- group: operate
  title: ''
  type: Support
  url: https://www.tre.se/support
- group: company
  title: ''
  type: Newsroom
  url: https://www.tre.se/om-tre/kontakt/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tre-se/refs/heads/main/security/tre-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tre-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tre.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://community.tre.se/mcp
  - status: 200
    url: https://tre.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Tre (Hi3G) is one of Sweden’s largest mobile network operators, offering mobile phone plans, broadband internet, and a range of connected devices. With over 3 million customers, Tre focuses on delivering fast 5G connectivity, flexible contracts, and innovative services for both private and business users. The company emphasizes sustainability, customer support, and digital self‑service through its website and mobile apps, positioning itself as a modern telecom provider in the Nordic market.
image: https://images.ctfassets.net/vsfvlfn4iu1r/6CrBntjqHR0844goIlAgnQ/52a48dffea128125e0395077dc165fe6/tre_hero_desktop_3840x1280_1.jpg
layout: provider
modified: '2026-10-15'
name: Tre (Hi3G)
nav: Providers
network: true
overview: 'Tre (Hi3G) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Tre (Hi3G)''s developer surface includes support and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tre Se Domain Security
  slug: tre-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tre-se
tags:
- Company
website: https://tre.se/
---
