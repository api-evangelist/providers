---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bejewel/refs/heads/main/llms/bejewel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bejewel-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bejewel/refs/heads/main/well-known/bejewel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bejewel-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bejewel/refs/heads/main/hosts/bejewel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bejewel-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bejewel/refs/heads/main/vendors/bejewel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bejewel-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bejewel.design/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.bejewel.design/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bejewel/refs/heads/main/security/bejewel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bejewel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bejewel.design
created: '2026-09-27'
description: Bejewel is a sustainable jewelry brand that creates eco‑friendly jewelry pieces with a focus on preserving the environment. The company sources ethically sourced materials and offers a range of necklaces, bracelets, earrings and rings through its online store.
image: http://www.bejewel.design/cdn/shop/files/logo_transparent_background_215_1cf27a7b-163a-45b4-98b2-8f30381c45b2.png?height=628&pad_color=fff&v=1689966085&width=1200
layout: provider
modified: '2026-09-27'
name: Bejewel
nav: Providers
network: true
overview: Bejewel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Jewelry, Sustainable, E-Commerce, Fashion, and Eco-friendly.
random_paper: 8
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
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
  name: Bejewel Domain Security
  slug: bejewel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: bejewel
tags:
- Jewelry
- Sustainable
- E-Commerce
- Fashion
- Eco-friendly
- Company
website: https://www.bejewel.design
---
