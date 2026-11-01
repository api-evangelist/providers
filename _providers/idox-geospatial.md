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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Integrate geospatial data directly into systems via Idox Geospatial's API access as described in their developer documentation.
  name: Idox Geospatial API
  slug: idox-geospatial-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/idox-geospatial/llms/idox-geospatial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idox-geospatial-llms.txt
- group: other
  href: https://artifacts.apis.io/idox-geospatial/hosts/idox-geospatial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idox-geospatial-hosts.yml
- group: other
  href: https://artifacts.apis.io/idox-geospatial/vendors/idox-geospatial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idox-geospatial-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://idoxgeospatial.co.uk/2025/06/28/registers-of-scotland-inspire-themapcloud/
- group: commercial
  title: ''
  type: Pricing
  url: https://idoxgeospatial.co.uk/plans/
- group: auth
  href: https://artifacts.apis.io/idox-geospatial/security/idox-geospatial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idox-geospatial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://idoxgeospatial.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://idoxgeospatial.co.uk/2026/10/07/data-integration-and-api-access/
- group: company
  title: ''
  type: Blog
  url: https://idoxgeospatial.co.uk/idox-geospatial-blog/
coverage:
  checked: '2026-10-26'
  detail: Documentation page renders via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://idoxgeospatial.co.uk/2026/10/07/data-integration-and-api-access/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Idox Geospatial, part of Idox Ltd, provides location data, geospatial software and services. Their platform enables organizations to achieve more with location insight, offering mapping, analytics, and data integration solutions for various industries.
layout: provider
modified: '2026-10-26'
name: Idox Geospatial
nav: Providers
network: true
overview: 'Idox Geospatial is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Mapping, DataAnalytics, and LocationInsight.


  Idox Geospatial''s developer surface includes signup flow, pricing, documentation, engineering blog, and 5 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 0.0
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
  name: Idox Geospatial Domain Security
  slug: idox-geospatial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: idox-geospatial
tags:
- Company
- Geospatial
- Mapping
- DataAnalytics
- LocationInsight
website: https://idoxgeospatial.co.uk/
---
