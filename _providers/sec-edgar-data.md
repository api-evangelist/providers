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
- description: API to access annual reports of public US companies
  name: SEC EDGAR Data
  slug: sec-edgar-data
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sec-edgar-data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sec.gov/edgar/sec-api-documentation
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.sec.gov/news/pressreleases.rss
created: '2026-05-28'
description: API to access annual reports of public US companies
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sec-edgar-data.png
layout: provider
modified: '2026-05-28'
name: SEC EDGAR Data
nav: Providers
network: true
overview: 'SEC EDGAR Data publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance and Public APIs.


  SEC EDGAR Data''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 38
score:
  band: minimal
  composite: 7.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sec-edgar-data/refs/heads/main/screenshots/sec-edgar-data-2026-06-20T193621.png
security:
- kind: domain-security
  name: Sec Edgar Data Domain Security
  slug: sec-edgar-data-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: sec-edgar-data
tags:
- Finance
- Public APIs
website: https://www.sec.gov/edgar/sec-api-documentation
---
