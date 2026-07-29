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
- description: Detect proxy and VPN using IP address
  name: IP2Proxy
  slug: ip2proxy
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ip2proxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ip2location.com/web-service/ip2proxy
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Detect proxy and VPN using IP address
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ip2proxy.png
layout: provider
modified: '2026-05-28'
name: IP2Proxy
nav: Providers
network: true
overview: IP2Proxy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 75
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
screenshot: https://raw.githubusercontent.com/api-evangelist/ip2proxy/refs/heads/main/screenshots/ip2proxy-2026-06-20T183542.png
security:
- kind: domain-security
  name: Ip2Proxy Domain Security
  slug: ip2proxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ip2proxy
tags:
- Geocoding
- Public APIs
website: https://www.ip2location.com/web-service/ip2proxy
---
