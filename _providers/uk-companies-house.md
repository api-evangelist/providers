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
- description: UK Companies House Data from the UK government
  name: UK Companies House
  slug: uk-companies-house
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uk-companies-house-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developer.company-information.service.gov.uk/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://companieshouse.blog.gov.uk/feed/
created: '2026-05-28'
description: UK Companies House Data from the UK government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uk-companies-house.png
layout: provider
modified: '2026-05-28'
name: UK Companies House
nav: Providers
network: true
overview: 'UK Companies House publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.


  UK Companies House''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 4.6
  delta: -2.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uk-companies-house/refs/heads/main/screenshots/uk-companies-house-2026-06-20T200000.png
security:
- kind: domain-security
  name: Uk Companies House Domain Security
  slug: uk-companies-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uk-companies-house
tags:
- Government
- Public APIs
website: https://developer.company-information.service.gov.uk/
---
