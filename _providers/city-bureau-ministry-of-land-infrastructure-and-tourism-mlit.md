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
  href: https://artifacts.apis.io/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit/hosts/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-hosts.yml
- group: other
  href: https://artifacts.apis.io/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit/vendors/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-vendors.yml
- group: auth
  href: https://artifacts.apis.io/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit/security/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mlit.go.jp/plateau/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mlit.go.jp/plateau/
- group: docs
  title: ''
  type: APIReference
  url: https://www.mlit.go.jp/plateau/open-data/
- group: operate
  title: ''
  type: Support
  url: https://www.mlit.go.jp/plateau/contact/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Project-PLATEAU
coverage:
  checked: '2026-10-26'
  detail: The open-data documentation page renders via JavaScript, providing no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.mlit.go.jp/plateau/open-data/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: The Ministry of Land, Infrastructure, Transport and Tourism (MLIT) of Japan operates the PLATEAU project, a nationwide initiative to develop and open 3D city models. It provides extensive geospatial data, APIs, and tools for urban planning, disaster prevention, and tourism, supporting developers, researchers, and public agencies with open data and services.
image: https://www.mlit.go.jp/plateau/assets/img/ogp.png
layout: provider
modified: '2026-10-26'
name: City Bureau, Ministry of Land, Infrastructure and Tourism (MLIT)
nav: Providers
network: true
overview: 'City Bureau, Ministry of Land, Infrastructure and Tourism (MLIT) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Geospatial, OpenData, UrbanPlanning, and Japan.


  City Bureau, Ministry of Land, Infrastructure and Tourism (MLIT)''s developer surface includes documentation, API reference, support, GitHub presence, and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: City Bureau Ministry Of Land Infrastructure And Tourism Mlit Domain Security
  slug: city-bureau-ministry-of-land-infrastructure-and-tourism-mlit-domain-security
  summary_line: TLSv1.3
slug: city-bureau-ministry-of-land-infrastructure-and-tourism-mlit
tags:
- Government
- Geospatial
- OpenData
- UrbanPlanning
- Japan
website: https://www.mlit.go.jp/plateau/
---
