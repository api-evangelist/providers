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
api_count: 1
apis:
- description: Development Seed provides geospatial data science APIs, but no machine‑readable contract was found.
  name: Development Seed API
  slug: development-seed-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/development-seed/hosts/development-seed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/development-seed-hosts.yml
- group: other
  href: https://artifacts.apis.io/development-seed/vendors/development-seed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/development-seed-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://developmentseed.org/team/
- group: auth
  href: https://artifacts.apis.io/development-seed/security/development-seed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/development-seed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developmentseed.org
- group: company
  title: ''
  type: Blog
  url: https://developmentseed.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/developmentseed
- group: operate
  title: ''
  type: Support
  url: https://developmentseed.org/contact
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was discovered on any host.
  evidence:
  - status: 0
    url: https://api.developmentseed.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Development Seed is a geospatial data science and engineering firm that builds open-source tools and platforms to help organizations make better decisions about the planet. They provide cloud‑first infrastructure, AI for Earth solutions, and consulting services, working with partners across environmental, humanitarian, and commercial sectors to deliver streaming insights and analytics.
image: https://developmentseed.org/meta/default-meta-image.png
layout: provider
modified: '2026-10-26'
name: Development Seed
nav: Providers
network: true
overview: 'Development Seed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, DataScience, OpenSource, CloudInfrastructure, and AIforEarth.


  Development Seed''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.6
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
    developer_ergonomics: 7.1
    discoverability: 58.9
    operational_transparency: 5.3
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
  name: Development Seed Domain Security
  slug: development-seed-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: development-seed
tags:
- Geospatial
- DataScience
- OpenSource
- CloudInfrastructure
- AIforEarth
- Company
website: https://developmentseed.org
---
