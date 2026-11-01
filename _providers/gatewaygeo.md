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
- group: operate
  href: https://artifacts.apis.io/gatewaygeo/changelog/gatewaygeo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gatewaygeo-changelog.yml
- group: other
  href: https://artifacts.apis.io/gatewaygeo/hosts/gatewaygeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatewaygeo-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qgis.org/
- group: auth
  href: https://artifacts.apis.io/gatewaygeo/security/gatewaygeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatewaygeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gatewaygeomatics.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://gatewaygeomatics.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: GatewayGeo specializes in publishing geospatial information to the Internet using Free and Open Source Software for Geomatics (FOSS4G). It offers consulting, training, and development services around tools such as MapServer, QGIS, GRASS GIS, GDAL, and PostGIS. The company also provides custom solutions for web mapping, spatial data processing, and open-source GIS integration, helping clients leverage open standards and community-driven software for their geospatial needs.
layout: provider
modified: '2026-10-26'
name: GatewayGeo
nav: Providers
network: true
overview: 'GatewayGeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Consulting, OpenSource, and FOSS4G.


  GatewayGeo''s developer surface includes changelog, documentation, and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: unknown
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
  name: Gatewaygeo Domain Security
  slug: gatewaygeo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: gatewaygeo
tags:
- Company
- Geospatial
- Consulting
- OpenSource
- FOSS4G
website: https://gatewaygeomatics.com/
---
