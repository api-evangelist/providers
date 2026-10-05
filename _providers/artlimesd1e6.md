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
  href: https://raw.githubusercontent.com/api-evangelist/artlimesd1e6/refs/heads/main/hosts/artlimesd1e6-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artlimesd1e6-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artlimesd1e6/refs/heads/main/vendors/artlimesd1e6-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artlimesd1e6-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://artlimes.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artlimes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artlimesd1e6/refs/heads/main/security/artlimesd1e6-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artlimesd1e6-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artlimes.com
- group: docs
  title: ''
  type: Documentation
  url: https://artlimes.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artlimes.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artlimes.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://artlimes.com/help
- group: company
  title: ''
  type: Blog
  url: https://blog.musicartmagazine.com/artlimes-launches-innovative-global-marketplace-art-online/
coverage:
  checked: 2026-09-26
  detail: Documentation pages require JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://artlimes.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Artlimesd1e6 operates Artlimes, a global online marketplace connecting artists, galleries, and collectors to buy and sell original art, prints, design, jewellery, and NFTs. The platform offers a curated catalog across 75 countries, supports multiple payment methods, and provides tools for creators to showcase and monetize their work, aiming to democratize access to art and design worldwide.
layout: provider
modified: '2026-09-26'
name: Artlimesd1e6
nav: Providers
network: true
overview: 'Artlimesd1e6 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Art, Design, and NFT.


  Artlimesd1e6''s developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 5.3
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
  name: Artlimesd1E6 Domain Security
  slug: artlimesd1e6-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: artlimesd1e6
tags:
- Company
- Marketplace
- Art
- Design
- NFT
- E-Commerce
website: https://artlimes.com
---
