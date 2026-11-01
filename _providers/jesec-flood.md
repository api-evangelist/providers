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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/jesec-flood/hosts/jesec-flood-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jesec-flood-hosts.yml
- group: other
  href: https://artifacts.apis.io/jesec-flood/vendors/jesec-flood-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jesec-flood-vendors.yml
- group: build
  href: https://artifacts.apis.io/jesec-flood/packages/jesec-flood-packages.yml
  title: ''
  type: SDKs
  url: packages/jesec-flood-packages.yml
- group: build
  href: https://artifacts.apis.io/jesec-flood/packages/jesec-flood-packages.yml
  title: ''
  type: Packages
  url: packages/jesec-flood-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.js.org/
- group: auth
  href: https://artifacts.apis.io/jesec-flood/security/jesec-flood-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jesec-flood-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flood.js.org
- group: company
  title: ''
  type: Blog
  url: https://flood.js.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jesec/flood
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://flood.js.org
  - status: 200
    url: https://github.com/jesec/flood
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Flood is an open-source web UI for torrent clients such as rTorrent, Transmission, and qBittorrent. It provides a modern, responsive interface with light and dark themes, multi-language support, and touch-friendly design. Users can monitor and control their torrent downloads, view statistics, and manage settings through a browser. The project is maintained by the community and hosted on GitHub, offering downloads via npm and detailed documentation on its website.
layout: provider
modified: '2026-10-28'
name: Flood
nav: Providers
network: true
overview: 'Flood is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, Torrent, WebUI, and JavaScript.


  Flood''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Jesec Flood Domain Security
  slug: jesec-flood-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jesec-flood
tags:
- Company
- OpenSource
- Torrent
- WebUI
- JavaScript
website: https://flood.js.org
---
