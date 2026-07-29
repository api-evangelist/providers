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
- description: Deutsche Bahn (DB) API
  name: Transport for Germany
  slug: transport-for-germany
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transport-for-germany-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transport-for-germany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://data.deutschebahn.com/dataset/api-fahrplan
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Deutsche Bahn (DB) API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transport-for-germany.png
layout: provider
modified: '2026-05-28'
name: Transport for Germany
nav: Providers
network: true
overview: Transport for Germany publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.
random_paper: 44
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
screenshot: https://raw.githubusercontent.com/api-evangelist/transport-for-germany/refs/heads/main/screenshots/transport-for-germany-2026-06-20T195702.png
security:
- kind: domain-security
  name: Transport For Germany Domain Security
  slug: transport-for-germany-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transport For Germany Vulnerability Disclosure
  slug: transport-for-germany-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: transport-for-germany
tags:
- Transportation
- Public APIs
website: http://data.deutschebahn.com/dataset/api-fahrplan
---
