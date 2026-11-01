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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.esri.ca/en-ca/about/trust
- group: other
  href: https://artifacts.apis.io/esri-canada/hosts/esri-canada-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esri-canada-hosts.yml
- group: other
  href: https://artifacts.apis.io/esri-canada/vendors/esri-canada-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esri-canada-vendors.yml
- group: auth
  href: https://artifacts.apis.io/esri-canada/security/esri-canada-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esri-canada-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/esri-canada/security/esri-canada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esri-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.esri.ca
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.esri.ca
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Esri Canada develops and sells ArcGIS, a geographic information system (GIS) platform that provides mapping, spatial analytics, and location intelligence solutions. It serves organizations across sectors such as government, utilities, law enforcement, and infrastructure planning, enabling them to integrate field and office data for operational and strategic decision‑making.
image: https://www.esri.ca/content/dam/distributor-restricted/esri-ca/gnav-tsow-frame.svg
layout: provider
modified: '2026-10-23'
name: Esri Canada
nav: Providers
network: true
overview: Esri Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include GIS, Mapping, Location Intelligence, Spatial Analytics, and Cloud Services.
random_paper: 0
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Esri Canada Domain Security
  slug: esri-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Esri Canada Trust Center
  slug: esri-canada-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018
slug: esri-canada
tags:
- GIS
- Mapping
- Location Intelligence
- Spatial Analytics
- Cloud Services
- Government
- Utilities
- Law Enforcement
website: http://www.esri.ca
---
