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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Weather and climate data
  name: Meteorologisk Institutt
  slug: meteorologisk-institutt
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meteorologisk-institutt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meteorologisk-institutt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.met.no/weatherapi/documentation
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Weather and climate data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meteorologisk-institutt.png
layout: provider
modified: '2026-05-28'
name: Meteorologisk Institutt
nav: Providers
network: true
overview: Meteorologisk Institutt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 16
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meteorologisk-institutt/refs/heads/main/screenshots/meteorologisk-institutt-2026-06-20T185255.png
security:
- kind: domain-security
  name: Meteorologisk Institutt Domain Security
  slug: meteorologisk-institutt-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Meteorologisk Institutt Vulnerability Disclosure
  slug: meteorologisk-institutt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meteorologisk-institutt
tags:
- Weather
- Public APIs
website: https://api.met.no/weatherapi/documentation
---
