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
- description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
  name: Voidly
  slug: voidly
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/voidly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voidly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voidly.ai/api-docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Internet censorship measurements, incidents, and ISP-level blocking data across 126 countries
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/voidly.png
layout: provider
modified: '2026-05-28'
name: Voidly
nav: Providers
network: true
overview: Voidly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 51
score:
  band: minimal
  composite: 9.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/voidly/refs/heads/main/screenshots/voidly-2026-06-20T201129.png
security:
- kind: domain-security
  name: Voidly Domain Security
  slug: voidly-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Voidly Vulnerability Disclosure
  slug: voidly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: voidly
tags:
- Open Data
- Public APIs
website: https://voidly.ai/api-docs
---
