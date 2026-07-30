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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RMV API (Public Transport in Hessen)
  name: Transport for Hessen, Germany
  slug: transport-for-hessen-germany
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transport-for-hessen-germany-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-hessen-germany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata.rmv.de/site/start.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: RMV API (Public Transport in Hessen)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-hessen-germany.png
layout: provider
modified: '2026-05-28'
name: Transport for Hessen, Germany
nav: Providers
network: true
overview: Transport for Hessen, Germany publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 80
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-hessen-germany/refs/heads/main/screenshots/transport-for-hessen-germany-2026-06-20T195604.png
security:
- kind: domain-security
  name: Transport For Hessen Germany Domain Security
  slug: transport-for-hessen-germany-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transport For Hessen Germany Vulnerability Disclosure
  slug: transport-for-hessen-germany-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transport-for-hessen-germany
tags:
- Transportation
- Public APIs
website: https://opendata.rmv.de/site/start.html
---
