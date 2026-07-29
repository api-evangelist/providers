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
- description: Address geocoding / reverse geocoding in bulk
  name: Geocod.io
  slug: geocodio
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/geocod-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/geocod-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geocod-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.geocod.io/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.geocod.io/updates/rss.xml
created: '2026-05-28'
description: Address geocoding / reverse geocoding in bulk
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geocod-io.png
layout: provider
modified: '2026-05-28'
name: Geocod.io
nav: Providers
network: true
overview: 'Geocod.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.


  Geocod.io''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.8
  delta: -1.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geocod-io/refs/heads/main/screenshots/geocod-io-2026-06-20T181809.png
security:
- kind: domain-security
  name: Geocod Io Domain Security
  slug: geocod-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Geocod Io Vulnerability Disclosure
  slug: geocod-io-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Geocod Io Trust Center
  slug: geocod-io-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: geocod-io
tags:
- Geocoding
- Public APIs
website: https://www.geocod.io/
---
