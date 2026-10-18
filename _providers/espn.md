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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Developer APIs for ESPN sports data and media content.
  name: ESPN API
  slug: espn-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/espn/refs/heads/main/hosts/espn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/espn-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/espn/refs/heads/main/vendors/espn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/espn-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.espn.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://developer.espn.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/espn
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/espn/refs/heads/main/security/espn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/espn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.espn.com
coverage:
  checked: '2026-10-14'
  detail: ESPN developer site returns a JavaScript shell with no machine‑readable OpenAPI spec.
  evidence:
  - status: 202
    url: https://www.espn.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: ESPN, the worldwide leader in sports broadcasting, provides comprehensive coverage of live events, news, scores, and analysis across a multitude of sports. Through its digital platforms, ESPN delivers real-time updates, video highlights, and in-depth articles to fans globally. The company also offers a suite of APIs that enable developers to integrate sports data, media content, and interactive features into applications, enhancing user engagement with timely and accurate sports information.
image: https://a1.espncdn.com/combiner/i?img=%2Fi%2Fespn%2Fespn_logos%2Fespn_red.png
layout: provider
modified: '2026-10-13'
name: ESPN
nav: Providers
network: true
overview: 'ESPN is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Media, and Broadcasting.


  ESPN''s developer surface includes support, documentation, and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Espn Domain Security
  slug: espn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: espn
tags:
- Company
- Sports
- Media
- Broadcasting
website: https://www.espn.com
---
