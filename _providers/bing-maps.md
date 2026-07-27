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
- description: Create/customize digital maps based on Bing Maps data
  name: Bing Maps
  slug: bing-maps
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bing-maps-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bing-maps-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bing-maps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/maps/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Create/customize digital maps based on Bing Maps data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bing-maps.png
layout: provider
modified: '2026-05-28'
name: Bing Maps
nav: Providers
network: true
overview: Bing Maps publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 10
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bing-maps/refs/heads/main/screenshots/bing-maps-2026-06-20T173249.png
security:
- kind: domain-security
  name: Bing Maps Domain Security
  slug: bing-maps-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bing Maps Vulnerability Disclosure
  slug: bing-maps-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Bing Maps Trust Center
  slug: bing-maps-trust-center
  summary_line: GDPR
slug: bing-maps
tags:
- Geocoding
- Public APIs
website: https://www.microsoft.com/maps/
---
