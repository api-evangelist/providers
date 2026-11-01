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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Audnexus provides endpoints for audiobook metadata aggregation.
  name: Audnexus API
  slug: audnexus-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/audnexus/hosts/audnexus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audnexus-hosts.yml
- group: other
  href: https://artifacts.apis.io/audnexus/vendors/audnexus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audnexus-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.audnex.us/status/audnexus
- group: auth
  href: https://artifacts.apis.io/audnexus/security/audnexus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audnexus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audnex.us/
- group: start
  title: ''
  type: GettingStarted
  url: https://audnex.us/#/
created: '2026-10-28'
description: Audnexus provides an API that aggregates audiobook metadata and availability information from multiple sources, offering developers a unified endpoint to search, retrieve details, and integrate audiobook data into applications. The service includes endpoints for authors, books, chapters, and search capabilities, and is documented via an interactive Redoc UI. It is open-source, hosted on GitHub, and licensed under GPL v3.
layout: provider
modified: '2026-10-28'
name: Audnexus
nav: Providers
network: true
overview: 'Audnexus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Audiobooks, Metadata, Search, and OpenSource.


  Audnexus'' developer surface includes getting-started guide and 5 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 32.9
    developer_ergonomics: 11.9
    discoverability: 62.5
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Audnexus Domain Security
  slug: audnexus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: audnexus
tags:
- Company
- Audiobooks
- Metadata
- Search
- OpenSource
website: https://audnex.us/
---
