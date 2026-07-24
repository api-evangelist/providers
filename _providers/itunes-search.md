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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Software products
  name: iTunes Search
  slug: itunes-search
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/itunes-search-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itunes-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Software products
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/itunes-search.png
layout: provider
modified: '2026-05-28'
name: iTunes Search
nav: Providers
network: true
overview: iTunes Search publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music and Public APIs.
random_paper: 13
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Itunes Search Domain Security
  slug: itunes-search-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Itunes Search Vulnerability Disclosure
  slug: itunes-search-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: itunes-search
tags:
- Music
- Public APIs
website: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
---
