---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Historical CKAN Action API for Kosovo's national open-data portal. Platform confirmed as CKAN ~2.7 from archived snapshots. The canonical CKAN endpoint path would be /api/3/action/, but the host is cu
  name: RKS Open Data CKAN Action API (historical)
  slug: catalog
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opendata-rks-gov-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.rks-gov.net/en/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: opendata.rks-gov.net (RKS Open Data) was the national government open-data portal for the Republic of Kosovo, historically running CKAN (~v2.7). As of mid-2025 the hostname no longer resolves (NXDOMAIN) and the portal is offline; the last Internet Archive snapshots are from June 2025. It is cataloged here as historical pending restoration. Sectoral government open-data services remain available (e.g. Kosovo Customs at dogana.rks-gov.net/OpenData and the national geoportal at geoportal.rks-gov.net).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opendata-rks-gov-net.png
layout: provider
modified: '2026-06-23'
name: opendata.rks-gov.net (Kosovo Open Data) [offline]
nav: Providers
network: true
overview: opendata.rks-gov.net (Kosovo Open Data) [offline] publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, CKAN, Data Catalog, Government Data, and National Government.
random_paper: 0
score:
  band: minimal
  composite: 5.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opendata-rks-gov-net/refs/heads/main/screenshots/opendata-rks-gov-net-2026-08-07T190549.png
security:
- kind: domain-security
  name: Opendata Rks Gov Net Domain Security
  slug: opendata-rks-gov-net-domain-security
  summary_line: DMARC
slug: opendata-rks-gov-net
tags:
- Open Data
- CKAN
- Data Catalog
- Government Data
- National Government
- Kosovo
- Europe
- Offline
website: https://opendata.rks-gov.net/en/
---
