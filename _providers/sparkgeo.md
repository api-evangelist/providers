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
api_count: 1
apis:
- description: Sparkgeo provides geospatial analytics and mapping services.
  name: Sparkgeo API
  slug: sparkgeo-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/sparkgeo/hosts/sparkgeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sparkgeo-hosts.yml
- group: other
  href: https://artifacts.apis.io/sparkgeo/vendors/sparkgeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sparkgeo-vendors.yml
- group: build
  href: https://artifacts.apis.io/sparkgeo/packages/sparkgeo-packages.yml
  title: ''
  type: SDKs
  url: packages/sparkgeo-packages.yml
- group: build
  href: https://artifacts.apis.io/sparkgeo/packages/sparkgeo-packages.yml
  title: ''
  type: Packages
  url: packages/sparkgeo-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://sparkgeo.com/press/
- group: company
  title: ''
  type: Blog
  url: https://sparkgeo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sparkgeo
- group: auth
  href: https://artifacts.apis.io/sparkgeo/security/sparkgeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sparkgeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparkgeo.com
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI or other machine-readable contract found on Sparkgeo website or docs.
  evidence:
  - status: error
    url: https://sparkgeo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Sparkgeo provides geospatial software development, consulting, and data science services to organizations across sectors. It builds custom location‑based technologies, including data pipelines, analytics, and operational intelligence platforms, and offers managed geospatial operations and cloud‑native infrastructure.
image: https://sparkgeo.com/wp-content/uploads/2018/10/sparkgeo-facebook-og-image.webp
layout: provider
modified: '2026-10-23'
name: Sparkgeo
nav: Providers
network: true
overview: 'Sparkgeo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial Software Development, Location-based Analytics, Data Engineering, Operational Intelligence, and Managed Geospatial Services.


  Sparkgeo''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.9
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
  name: Sparkgeo Domain Security
  slug: sparkgeo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sparkgeo
tags:
- Geospatial Software Development
- Location-based Analytics
- Data Engineering
- Operational Intelligence
- Managed Geospatial Services
- Cloud-native Platforms
website: https://sparkgeo.com
---
