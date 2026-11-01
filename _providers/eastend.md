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
  href: https://artifacts.apis.io/eastend/hosts/eastend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eastend-hosts.yml
- group: other
  href: https://artifacts.apis.io/eastend/vendors/eastend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eastend-vendors.yml
- group: auth
  href: https://artifacts.apis.io/eastend/security/eastend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eastend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/eastend
created: '2026-10-24'
description: 'Eastend is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling. No public API documentation or endpoints have been identified for this entity, and attempts to locate a legitimate corporate website have only returned unrelated businesses such as a Long Island shirt retailer. As a result, this profile remains a placeholder pending discovery of authentic API resources.'
layout: provider
modified: '2026-10-24'
name: Eastend
nav: Providers
network: true
overview: Eastend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Data, Technology, and Platform.
random_paper: 20
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Eastend Domain Security
  slug: eastend-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eastend
tags:
- Company
- API
- Data
- Technology
- Platform
website: https://equityzen.com/company/eastend
---
