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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/embark-studios/refs/heads/main/llms/embark-studios-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/embark-studios-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/embark-studios/refs/heads/main/well-known/embark-studios-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/embark-studios-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/embark-studios/refs/heads/main/hosts/embark-studios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/embark-studios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/embark-studios/refs/heads/main/vendors/embark-studios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/embark-studios-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.embark-studios.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.embark-studios.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.embark-studios.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/embark-studios/refs/heads/main/security/embark-studios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/embark-studios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.embark-studios.com/
- group: company
  title: ''
  type: Blog
  url: https://www.embark-studios.com/blog
coverage:
  checked: '2026-10-15'
  detail: Embark Studios' website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://embark-studios.com/
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Embark Studios is a Swedish game development studio creating innovative multiplayer experiences. Their flagship titles include The Finals, a free‑to‑play dynamic shooter, and ARC Raiders, a multiplayer extraction adventure. The company focuses on cutting‑edge technology, community‑driven design, and immersive worlds, aiming to push the boundaries of interactive entertainment.
image: http://static1.squarespace.com/static/60dc7ac5f8d9650eee1d12c4/t/61b2260a16a89738079b4cf2/1788894380074/channel_banner_2560x1440_youtube.jpg?format=1500w
layout: provider
modified: '2026-10-14'
name: Embark Studios
nav: Providers
network: true
overview: 'Embark Studios is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Multiplayer, Sweden, and Innovation.


  Embark Studios'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Embark Studios Domain Security
  slug: embark-studios-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: embark-studios
tags:
- Company
- Gaming
- Multiplayer
- Sweden
- Innovation
website: https://www.embark-studios.com/
---
