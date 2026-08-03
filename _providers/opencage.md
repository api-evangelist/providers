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
- description: Forward and reverse geocoding using open data
  name: OpenCage
  slug: opencage
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opencage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opencage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opencagedata.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://blog.opencagedata.com/feed.xml
created: '2026-05-28'
description: Forward and reverse geocoding using open data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opencage.png
layout: provider
modified: '2026-05-28'
name: OpenCage
nav: Providers
network: true
overview: 'OpenCage publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.


  OpenCage''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 74
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opencage/refs/heads/main/screenshots/opencage-2026-06-20T190916.png
security:
- kind: domain-security
  name: Opencage Domain Security
  slug: opencage-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Opencage Vulnerability Disclosure
  slug: opencage-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: opencage
tags:
- Geocoding
- Public APIs
website: https://opencagedata.com
---
