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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Bespoke MITA-built open-data portal (JS SPA) at portal.data.gov.mt / open.data.gov.mt. The catalog is DCAT-AP-compliant and harvested into data.europa.eu (~230+ datasets across sectors such as plannin
  name: Open Data Malta Portal
  slug: portal
- description: Malta's INSPIRE / geospatial stack exposing standard OGC services (GeoNetwork CSW, GeoServer WMS/WFS, ArcGIS). Distinct from the national open-data catalog.
  name: Malta Spatial Data Infrastructure (MSDI) geoportal
  slug: msdi
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/data-gov-mt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/data-gov-mt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portal.data.gov.mt/
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-23'
description: data.gov.mt is the national government open-data portal for Malta, operated by MITA (Malta Information Technology Agency) as a bespoke "Shared Data Governance and Data Management Platform" with a JavaScript single-page-app front end (served at portal.data.gov.mt / open.data.gov.mt). It is DCAT-AP-compliant for EU harvesting (~230+ datasets) but exposes no publicly documented JSON catalog API. Malta's geospatial APIs are available separately via the MSDI geoportal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/data-gov-mt.png
layout: provider
modified: '2026-06-23'
name: data.gov.mt (Open Data Malta)
nav: Providers
network: true
overview: data.gov.mt (Open Data Malta) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data, Custom Platform, DCAT-AP, Government Data, and National Government.
random_paper: 37
score:
  band: minimal
  composite: 11.8
  delta: 2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Data Gov Mt Domain Security
  slug: data-gov-mt-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Data Gov Mt Vulnerability Disclosure
  slug: data-gov-mt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: data-gov-mt
tags:
- Open Data
- Custom Platform
- DCAT-AP
- Government Data
- National Government
- Malta
- Europe
website: https://portal.data.gov.mt/
---
