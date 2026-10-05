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
  href: https://raw.githubusercontent.com/api-evangelist/anipen/refs/heads/main/hosts/anipen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anipen-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anipen.com/termsofservice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anipen.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.anipen.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.anipen.com/news/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anipen/refs/heads/main/security/anipen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anipen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anipen.com
created: '2026-09-24'
description: Anipen (애니펜) is a South Korean technology company focused on immersive XR, AR, and AI-driven content platforms. It develops metaverse infrastructure, AR kiosks, AI-powered avatar engines, and digital twin solutions for various industries. Since 2013, Anipen has delivered over 19 million global app downloads, 7.5 million AR video views, and operates services such as AR live streaming, XR commerce, and AI character platforms, positioning itself as a key player in the Korean and global metaverse ecosystem.
image: https://www.anipen.com/wp-content/themes/anipen/assets/images/anipen_preview.jpg
layout: provider
modified: '2026-09-24'
name: Anipen
nav: Providers
network: true
overview: 'Anipen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, XR, AR, Artificial Intelligence, and Metaverse.


  Anipen''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anipen Domain Security
  slug: anipen-domain-security
  summary_line: no transport/DNS hardening detected
slug: anipen
tags:
- Company
- XR
- AR
- Artificial Intelligence
- Metaverse
website: https://www.anipen.com
---
