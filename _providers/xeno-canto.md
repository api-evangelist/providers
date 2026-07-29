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
- description: Bird recordings
  name: xeno-canto
  slug: xeno-canto
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xeno-canto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xeno-canto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xeno-canto.org/explore/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Bird recordings
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xeno-canto.png
layout: provider
modified: '2026-05-28'
name: xeno-canto
nav: Providers
network: true
overview: xeno-canto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animals and Public APIs.
random_paper: 48
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
screenshot: https://raw.githubusercontent.com/api-evangelist/xeno-canto/refs/heads/main/screenshots/xeno-canto-2026-06-20T201656.png
security:
- kind: domain-security
  name: Xeno Canto Domain Security
  slug: xeno-canto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Xeno Canto Vulnerability Disclosure
  slug: xeno-canto-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: xeno-canto
tags:
- Animals
- Public APIs
website: https://xeno-canto.org/explore/api
---
