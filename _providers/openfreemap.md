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
  href: https://artifacts.apis.io/openfreemap/hosts/openfreemap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openfreemap-hosts.yml
- group: other
  href: https://artifacts.apis.io/openfreemap/vendors/openfreemap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openfreemap-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/msbarry
- group: auth
  href: https://artifacts.apis.io/openfreemap/security/openfreemap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openfreemap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openfreemap.org/
- group: company
  title: ''
  type: Blog
  url: https://openfreemap.org/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openfreemap.org/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openfreemap.org/tos/
- group: start
  title: ''
  type: GettingStarted
  url: https://openfreemap.org/quick_start/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider's API host.
  evidence:
  - status: error
    url: https://api.openfreemap.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OpenFreeMap provides open-source vector map styles and hosting, enabling developers to display custom maps on websites and applications for free. The platform offers a collection of ready-to-use map tiles, styling tools, and documentation for integrating maps into web and mobile projects, supporting open-source GIS initiatives and community contributions.
image: https://openfreemap.org/og/_index.png
layout: provider
modified: '2026-10-28'
name: OpenFreeMap vector styles
nav: Providers
network: true
overview: 'OpenFreeMap vector styles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-source, Mapping, GIS, and Vector Tiles.


  OpenFreeMap vector styles'' developer surface includes engineering blog, getting-started guide, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openfreemap Domain Security
  slug: openfreemap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openfreemap
tags:
- Company
- Open-source
- Mapping
- GIS
- Vector Tiles
- Free Hosting
website: https://openfreemap.org/
---
