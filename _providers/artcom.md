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
  href: https://raw.githubusercontent.com/api-evangelist/artcom/refs/heads/main/hosts/artcom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artcom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artcom/refs/heads/main/vendors/artcom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artcom-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artcom/refs/heads/main/security/artcom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artcom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.art.com
- group: company
  title: ''
  type: Blog
  url: https://www.art.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.art.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.art.com/terms
coverage:
  checked: 2026-09-26
  detail: Main website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.art.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Art.com is a leading online retailer of wall art, canvas prints, framed artwork, photography, and home decor. The platform offers millions of artworks from a wide range of artists and styles, allowing customers to search, customize, and purchase prints for personal or commercial use. It provides tools for framing, matting, and shipping worldwide, and includes features such as AI‑powered search, curated collections, and a marketplace for artists. Art.com serves both individual consumers and businesses looking to decorate spaces with high‑quality art and prints.
layout: provider
modified: '2026-09-26'
name: Art.com
nav: Providers
network: true
overview: 'Art.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Art, Retail, and Marketplace.


  Art.com''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artcom Domain Security
  slug: artcom-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: artcom
tags:
- Company
- E-Commerce
- Art
- Retail
- Marketplace
- Online
website: https://www.art.com
---
