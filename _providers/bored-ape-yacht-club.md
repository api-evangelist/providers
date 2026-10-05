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
  href: https://raw.githubusercontent.com/api-evangelist/bored-ape-yacht-club/refs/heads/main/hosts/bored-ape-yacht-club-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bored-ape-yacht-club-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bored-ape-yacht-club/refs/heads/main/vendors/bored-ape-yacht-club-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bored-ape-yacht-club-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bored-ape-yacht-club/refs/heads/main/security/bored-ape-yacht-club-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bored-ape-yacht-club-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yuga.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.yuga.com/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yuga.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yuga.com/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.yuga.com
  - status: null
    url: https://forgeglobal.com/bored-ape-yacht-club_stock/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Yuga Labs is a leading Web3 creator and brand studio behind iconic NFT collections such as Bored Ape Yacht Club, Mutant Ape Yacht Club, and Otherside. Founded by a group of friends, the company builds cultural experiences, community-driven products, and the ApeCoin ecosystem. It operates at the intersection of blockchain, gaming, and digital art, fostering a vibrant community and expanding the possibilities of on‑chain ownership and storytelling.
image: https://yuga.com/share.jpg
layout: provider
modified: '2026-10-02'
name: Yuga Labs
nav: Providers
network: true
overview: 'Yuga Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Web3, NFT, Gaming, and Community.


  Yuga Labs'' developer surface includes documentation and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
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
  name: Bored Ape Yacht Club Domain Security
  slug: bored-ape-yacht-club-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bored-ape-yacht-club
tags:
- Company
- Web3
- NFT
- Gaming
- Community
website: https://www.yuga.com
---
