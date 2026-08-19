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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Convert British OSGB36 easting and northing (British National Grid) to WGS84 latitude and longitude
  name: bng2latlong
  slug: bng2latlong
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bng2latlong-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getthedata.com/bng2latlong
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Convert British OSGB36 easting and northing (British National Grid) to WGS84 latitude and longitude
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bng2latlong.png
layout: provider
modified: '2026-05-28'
name: bng2latlong
nav: Providers
network: true
overview: bng2latlong publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 71
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bng2latlong/refs/heads/main/screenshots/bng2latlong-2026-07-25T203515.png
security:
- kind: domain-security
  name: Bng2Latlong Domain Security
  slug: bng2latlong-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bng2latlong
tags:
- Geocoding
- Public APIs
website: https://www.getthedata.com/bng2latlong
---
