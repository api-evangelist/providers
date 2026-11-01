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
- group: other
  href: https://artifacts.apis.io/cfl/hosts/cfl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cfl-hosts.yml
- group: other
  href: https://artifacts.apis.io/cfl/vendors/cfl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cfl-vendors.yml
- group: build
  href: https://artifacts.apis.io/cfl/packages/cfl-packages.yml
  title: ''
  type: SDKs
  url: packages/cfl-packages.yml
- group: build
  href: https://artifacts.apis.io/cfl/packages/cfl-packages.yml
  title: ''
  type: Packages
  url: packages/cfl-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cfl.ca/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cfl.ca/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cfl.ca/categories/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cfl
- group: auth
  href: https://artifacts.apis.io/cfl/security/cfl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cfl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cfl.ca/
coverage:
  checked: '2026-10-28'
  detail: The CFL website provides no public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable API specifications.
  evidence:
  - status: 404
    url: https://cfl.ca/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The Canadian Football League (CFL) provides professional football in Canada, offering a comprehensive online presence that includes game schedules, live scores, team statistics, news articles, ticket sales, and a fan shop. The official website cfl.ca serves as the central hub for fans to access standings, watch highlights, and engage with league content across English and French languages.
image: https://images.ctfassets.net/yfsr4emgn242/6irHSoTcN8dtCf4kNcZxWp/4cb3324da1b65baee6f103b5e74c69ad/6ed59a5de5a1bb9146f0611ff460986221ae2534.jpg?w=1200&h=630&fit=fill
layout: provider
modified: '2026-10-28'
name: CFL scoreboard JSON
nav: Providers
network: true
overview: CFL scoreboard JSON is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Football, Canada, ProfessionalLeague, and Entertainment.
random_paper: 21
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
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
  name: Cfl Domain Security
  slug: cfl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cfl
tags:
- Sports
- Football
- Canada
- ProfessionalLeague
- Entertainment
website: https://cfl.ca/
---
