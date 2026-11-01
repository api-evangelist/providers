---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/crunchyroll/well-known/crunchyroll-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crunchyroll-well-known.yml
- group: other
  href: https://artifacts.apis.io/crunchyroll/hosts/crunchyroll-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crunchyroll-hosts.yml
- group: other
  href: https://artifacts.apis.io/crunchyroll/vendors/crunchyroll-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crunchyroll-vendors.yml
- group: build
  href: https://artifacts.apis.io/crunchyroll/packages/crunchyroll-packages.yml
  title: ''
  type: SDKs
  url: packages/crunchyroll-packages.yml
- group: build
  href: https://artifacts.apis.io/crunchyroll/packages/crunchyroll-packages.yml
  title: ''
  type: Packages
  url: packages/crunchyroll-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crunchyroll.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.crunchyroll.com/sitemaps/news/de-DE/manga.xml?page=0
- group: docs
  title: ''
  type: Documentation
  url: https://help.crunchyroll.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crunchyroll
- group: auth
  href: https://artifacts.apis.io/crunchyroll/security/crunchyroll-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crunchyroll-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crunchyroll.com/
coverage:
  checked: '2026-10-26'
  detail: Crunchyroll provides no public developer portal or API documentation.
  evidence:
  - status: 200
    url: https://www.crunchyroll.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: 'Crunchyroll is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://static.crunchyroll.com/cxweb/assets/img/og-image.png
layout: provider
modified: '2026-10-26'
name: Crunchyroll
nav: Providers
network: true
overview: 'Crunchyroll is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Crunchyroll''s developer surface includes documentation and 10 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 32.1
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crunchyroll Domain Security
  slug: crunchyroll-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crunchyroll
tags:
- Company
website: https://crunchyroll.com/
---
