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
- description: UK official public record API
  name: Gazette Data, UK
  slug: gazette-data-uk
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gazette-data-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thegazette.co.uk/data
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.thegazette.co.uk/rss.xml
created: '2026-05-28'
description: UK official public record API
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gazette-data-uk.png
layout: provider
modified: '2026-05-28'
name: Gazette Data, UK
nav: Providers
network: true
overview: 'Gazette Data, UK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.


  Gazette Data, UK''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 6.9
  delta: -1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gazette-data-uk/refs/heads/main/screenshots/gazette-data-uk-2026-06-20T181654.png
security:
- kind: domain-security
  name: Gazette Data Uk Domain Security
  slug: gazette-data-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gazette-data-uk
tags:
- Government
- Public APIs
website: https://www.thegazette.co.uk/data
---
