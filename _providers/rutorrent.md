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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/rutorrent/security/rutorrent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rutorrent-domain-security.yml
- group: other
  href: https://artifacts.apis.io/rutorrent/hosts/rutorrent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rutorrent-hosts.yml
- group: other
  href: https://artifacts.apis.io/rutorrent/vendors/rutorrent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rutorrent-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://publicsuffix.org/list/public_suffix_list.dat
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Novik/ruTorrent/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Novik/ruTorrent/wiki/WebSERVER
created: '2026-10-28'
description: ruTorrent is a web-based front‑end for the popular BitTorrent client rtorrent. It provides a lightweight, extensible interface that can be installed on low‑end servers or routers, offering features such as plugin support, customizable UI, and easy torrent management via a browser. The project is open‑source under GPL‑v3 and is maintained on GitHub, with documentation, releases, and community contributions available through its repository and wiki.
layout: provider
modified: '2026-10-28'
name: ruTorrent
nav: Providers
network: true
overview: 'ruTorrent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, BitTorrent, OpenSource, WebUI, and GPLv3.


  ruTorrent''s developer surface includes documentation, getting-started guide, and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rutorrent Domain Security
  slug: rutorrent-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rutorrent
tags:
- Company
- BitTorrent
- OpenSource
- WebUI
- GPLv3
website: https://publicsuffix.org/list/public_suffix_list.dat
---
