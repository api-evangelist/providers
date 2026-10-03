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
api_count: 1
apis:
- description: GraphQL API for Anique services
  name: Anique GraphQL API
  slug: anique-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anique/refs/heads/main/llms/anique-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anique-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anique/refs/heads/main/well-known/anique-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anique-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anique/refs/heads/main/hosts/anique-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anique-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anique/refs/heads/main/vendors/anique-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anique-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://anique.jp/releases
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anique/refs/heads/main/security/anique-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anique-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anique.jp
- group: docs
  title: ''
  type: Documentation
  url: https://anique.jp/en/about/
- group: other
  title: ''
  type: Services
  url: https://anique.jp/en/services/
- group: other
  title: ''
  type: Shop
  url: https://shop.anique.jp
created: '2026-09-24'
description: Anique Inc. is a Japan‑based company that maximizes the value of intellectual property and brands through both real‑world and digital experiences. It operates Anique Shop, Anique Museum, AR and digital collection services, creating limited‑edition merchandise and virtual exhibitions that connect creators with global fans. The company emphasizes creative content, IP‑driven experiences, and supports creators in both physical and digital realms.
image: https://anique.jp/wp-content/uploads/2024/08/IMG_20240809_1922477112.jpg
layout: provider
modified: '2026-09-24'
name: Anique
nav: Providers
network: true
overview: 'Anique publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IP, Digital, Merchandise, and Japan.


  Anique''s developer surface includes changelog, documentation, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 15.8
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
  name: Anique Domain Security
  slug: anique-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: anique
tags:
- Company
- IP
- Digital
- Merchandise
- Japan
website: https://anique.jp
---
