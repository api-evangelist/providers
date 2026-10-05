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
api_count: 1
apis:
- description: Bongo provides streaming media services in Bangladesh.
  name: BongoBD
  slug: bongobd
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bongobd/refs/heads/main/hosts/bongobd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bongobd-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bongobd/refs/heads/main/vendors/bongobd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bongobd-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bongobd.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BongoBD
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bongobd/refs/heads/main/security/bongobd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bongobd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bongobd.com
- group: docs
  title: ''
  type: Documentation
  url: https://bongobd.com/about
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://bongobd.com/mcp
  - status: 403
    url: https://equityzen.com/company/bongobd
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bongobd, operating as Bongo, is Bangladesh’s leading OTT and VOD platform since 2013, offering a vast catalog of Bangla movies, natok, web series, live TV channels, and originals. It streams content in HD, provides subtitles and dubbing in multiple languages, and supports offline downloads via its app. With over 500 YouTube channels, 83+ million subscribers, and a reach of 210 million unique viewers monthly, Bongo serves a South Asian audience across multiple countries, delivering entertainment through state‑of‑the‑art video delivery technology.
layout: provider
modified: '2026-10-02'
name: Bongobd
nav: Providers
network: true
overview: 'Bongobd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OTT, VOD, Streaming, and Bangladesh.


  Bongobd''s developer surface includes documentation and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bongobd Domain Security
  slug: bongobd-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bongobd
tags:
- Company
- OTT
- VOD
- Streaming
- Bangladesh
website: https://bongobd.com
---
