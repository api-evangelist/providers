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
- description: Contains D.C. government public datasets, including crime, GIS, financial data, and so on
  name: District of Columbia Open Data
  slug: district-of-columbia-open-data
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/district-of-columbia-open-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/district-of-columbia-open-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://opendata.dc.gov/pages/using-apis
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Contains D.C. government public datasets, including crime, GIS, financial data, and so on
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/district-of-columbia-open-data.png
layout: provider
modified: '2026-05-28'
name: District of Columbia Open Data
nav: Providers
network: true
overview: District of Columbia Open Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 28
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
screenshot: https://raw.githubusercontent.com/api-evangelist/district-of-columbia-open-data/refs/heads/main/screenshots/district-of-columbia-open-data-2026-06-20T180053.png
security:
- kind: domain-security
  name: District Of Columbia Open Data Domain Security
  slug: district-of-columbia-open-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: District Of Columbia Open Data Vulnerability Disclosure
  slug: district-of-columbia-open-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: district-of-columbia-open-data
tags:
- Government
- Public APIs
website: http://opendata.dc.gov/pages/using-apis
---
