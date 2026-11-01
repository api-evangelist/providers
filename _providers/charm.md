---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for Charm platform, documented at https://charm.land/docs
  name: Charm API
  slug: charm-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/charm/hosts/charm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charm-hosts.yml
- group: other
  href: https://artifacts.apis.io/charm/vendors/charm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charm-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.charm.sh/
- group: auth
  href: https://artifacts.apis.io/charm/security/charm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charm.sh/
- group: auth
  href: https://artifacts.apis.io/charm/security/charm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charm.sh/
created: '2026-10-29'
description: Charm is an open‑source developer‑focused platform that builds glamorous terminal‑based tools and libraries. It offers the Hyper routing model, a suite of Go libraries such as Bubble Tea, Lip Gloss, and provides a community hub at charm.land with blog, Discord, Slack, and social links. The company creates high‑availability, cost‑efficient AI‑enhanced tooling for macOS, Linux, Windows and BSD, empowering developers to build fast, beautiful CLI applications.
image: https://charm.land/charm-share.6f7acd00931169c9.jpg
layout: provider
modified: '2026-10-29'
name: Charm
nav: Providers
network: true
overview: Charm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, DeveloperTools, CLI, and Go.
random_paper: 19
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
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
  name: Charm Domain Security
  slug: charm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: charm
tags:
- Company
- OpenSource
- DeveloperTools
- CLI
- Go
website: https://charm.sh/
---
