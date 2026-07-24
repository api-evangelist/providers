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
- description: National Plan & Provider Enumeration System, info on healthcare providers registered in US
  name: NPPES
  slug: nppes
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nppes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://npiregistry.cms.hhs.gov/registry/help-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: National Plan & Provider Enumeration System, info on healthcare providers registered in US
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nppes.png
layout: provider
modified: '2026-05-28'
name: NPPES
nav: Providers
network: true
overview: NPPES publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 40
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nppes/refs/heads/main/screenshots/nppes-2026-06-20T190448.png
security:
- kind: domain-security
  name: Nppes Domain Security
  slug: nppes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nppes
tags:
- Health
- Public APIs
website: https://npiregistry.cms.hhs.gov/registry/help-api
---
