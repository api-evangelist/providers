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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diageo/refs/heads/main/hosts/diageo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diageo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/diageo/refs/heads/main/vendors/diageo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diageo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/diageo/refs/heads/main/security/diageo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diageo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diageo.com
- group: company
  title: ''
  type: Investors
  url: https://www.diageo.com/en/investors
- group: company
  title: ''
  type: Careers
  url: https://www.diageo.com/en/careers
- group: operate
  title: ''
  type: ContactUs
  url: https://www.diageo.com/en/contact-us
- group: company
  title: ''
  type: NewsAndMedia
  url: https://www.diageo.com/en/news-and-media
coverage:
  checked: '2026-10-13'
  detail: Diageo does not provide a public developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.diageo.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Diageo is a global leader in premium drinks, producing a diverse portfolio of spirits, beer, wine and other alcoholic beverages. The company operates in over 180 markets, with iconic brands such as Johnnie Walker, Guinness, Smirnoff and Baileys. It focuses on sustainable growth, innovation and responsible drinking, offering extensive consumer experiences worldwide.
image: https://www.diageo.com/~/media/Images/D/Diageo-V2/Universal/logo/diageo-og-logo.jpg
layout: provider
modified: '2026-10-13'
name: Diageo
nav: Providers
network: true
overview: Diageo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alcohol, Spirits, Beverages, and Global.
random_paper: 1
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
    mcp: derived
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
  name: Diageo Domain Security
  slug: diageo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: diageo
tags:
- Company
- Alcohol
- Spirits
- Beverages
- Global
website: https://www.diageo.com
---
