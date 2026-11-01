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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/nflverse/plans/nflverse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nflverse-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/nflverse/hosts/nflverse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nflverse-hosts.yml
- group: other
  href: https://artifacts.apis.io/nflverse/vendors/nflverse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nflverse-vendors.yml
- group: build
  href: https://artifacts.apis.io/nflverse/packages/nflverse-packages.yml
  title: ''
  type: SDKs
  url: packages/nflverse-packages.yml
- group: build
  href: https://artifacts.apis.io/nflverse/packages/nflverse-packages.yml
  title: ''
  type: Packages
  url: packages/nflverse-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Corg-login%3E&source=header
- group: auth
  title: ''
  type: Security
  url: https://github.com/security/advanced-security/code-security
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.github.com/
- group: auth
  href: https://artifacts.apis.io/nflverse/security/nflverse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nflverse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/nflverse
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on discovered hosts.
  evidence:
  - status: DNS resolution failed
    url: https://api.nflverse.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: nflverse provides a suite of open-source data packages and APIs for comprehensive NFL analytics. Through R, Python, and other language bindings, it offers access to play-by-play data, player statistics, and advanced metrics, all licensed under permissive CC-BY terms. The platform supports researchers, developers, and fans in building models, visualizations, and applications around NFL data.
image: https://avatars.githubusercontent.com/u/79467114?s=280&v=4
layout: provider
modified: '2026-10-28'
name: nflverse data via nflreadr
nav: Providers
network: true
overview: 'nflverse data via nflreadr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, Data, Analytics, Open-Source, and NFL.


  nflverse data via nflreadr''s developer surface includes signup flow, pricing, documentation, and 9 more developer resources.'
plans:
- name: Nflverse Plans Pricing
  plan_count: 3
  slug: nflverse-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Nflverse Domain Security
  slug: nflverse-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nflverse
tags:
- Sports
- Data
- Analytics
- Open-Source
- NFL
---
