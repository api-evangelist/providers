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
- description: Recreational areas, federal lands, historic sites, museums, and other attractions/resources(US)
  name: Recreation Information Database
  slug: recreation-information-database
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recreation-information-database-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recreation-information-database-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridb.recreation.gov/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Recreational areas, federal lands, historic sites, museums, and other attractions/resources(US)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recreation-information-database.png
layout: provider
modified: '2026-05-28'
name: Recreation Information Database
nav: Providers
network: true
overview: Recreation Information Database publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 9
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
screenshot: https://raw.githubusercontent.com/api-evangelist/recreation-information-database/refs/heads/main/screenshots/recreation-information-database-2026-06-20T192708.png
security:
- kind: domain-security
  name: Recreation Information Database Domain Security
  slug: recreation-information-database-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recreation Information Database Vulnerability Disclosure
  slug: recreation-information-database-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: recreation-information-database
tags:
- Open Data
- Public APIs
website: https://ridb.recreation.gov/
---
