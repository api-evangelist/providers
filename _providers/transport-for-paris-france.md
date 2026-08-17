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
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: RATP Open Data API
  name: Transport for Paris, France
  slug: transport-for-paris-france
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transport-for-paris-france-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-paris-france-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://data.ratp.fr/api/v1/console/datasets/1.0/search/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: RATP Open Data API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-paris-france.png
layout: provider
modified: '2026-05-28'
name: Transport for Paris, France
nav: Providers
network: true
overview: Transport for Paris, France publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 100
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-paris-france/refs/heads/main/screenshots/transport-for-paris-france-2026-06-20T195615.png
security:
- kind: domain-security
  name: Transport For Paris France Domain Security
  slug: transport-for-paris-france-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transport For Paris France Vulnerability Disclosure
  slug: transport-for-paris-france-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transport-for-paris-france
tags:
- Transportation
- Public APIs
website: http://data.ratp.fr/api/v1/console/datasets/1.0/search/
---
