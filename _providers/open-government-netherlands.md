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
- description: Netherlands Government Open Data
  name: Open Government, Netherlands
  slug: open-government-netherlands
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-government-netherlands-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-government-netherlands-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.overheid.nl/en/ondersteuning/data-publiceren/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Netherlands Government Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-government-netherlands.png
layout: provider
modified: '2026-05-28'
name: Open Government, Netherlands
nav: Providers
network: true
overview: Open Government, Netherlands publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 39
score:
  band: minimal
  composite: 8.2
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-government-netherlands/refs/heads/main/screenshots/open-government-netherlands-2026-06-20T190808.png
security:
- kind: domain-security
  name: Open Government Netherlands Domain Security
  slug: open-government-netherlands-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Open Government Netherlands Vulnerability Disclosure
  slug: open-government-netherlands-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-government-netherlands
tags:
- Government
- Public APIs
website: https://data.overheid.nl/en/ondersteuning/data-publiceren/api
---
