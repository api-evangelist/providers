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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Water quality and level info for rivers and lakes
  name: USGS Water Services
  slug: usgs-water-services
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usgs-water-services-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waterservices.usgs.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Water quality and level info for rivers and lakes
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usgs-water-services.png
layout: provider
modified: '2026-05-28'
name: USGS Water Services
nav: Providers
network: true
overview: USGS Water Services publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Science And Math and Public APIs.
random_paper: 55
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/usgs-water-services/refs/heads/main/screenshots/usgs-water-services-2026-06-20T200726.png
security:
- kind: domain-security
  name: Usgs Water Services Domain Security
  slug: usgs-water-services-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: usgs-water-services
tags:
- Science And Math
- Public APIs
website: https://waterservices.usgs.gov/
---
