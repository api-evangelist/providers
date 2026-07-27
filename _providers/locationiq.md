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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Provides forward/reverse geocoding and batch geocoding
  name: LocationIQ
  slug: locationiq
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/locationiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://locationiq.org/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://blog.locationiq.com/feed/
created: '2026-05-28'
description: Provides forward/reverse geocoding and batch geocoding
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/locationiq.png
layout: provider
modified: '2026-05-28'
name: LocationIQ
nav: Providers
network: true
overview: 'LocationIQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.


  LocationIQ''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 55
score:
  band: minimal
  composite: 7.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Locationiq Domain Security
  slug: locationiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: locationiq
tags:
- Geocoding
- Public APIs
website: https://locationiq.org/docs/
---
