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
- description: Data on international sanctions, crime and politically exposed persons
  name: OpenSanctions
  slug: opensanctions
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opensanctions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opensanctions.org/docs/api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.opensanctions.org/articles/rss/
created: '2026-05-28'
description: Data on international sanctions, crime and politically exposed persons
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensanctions.png
layout: provider
modified: '2026-05-28'
name: OpenSanctions
nav: Providers
network: true
overview: 'OpenSanctions publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.


  OpenSanctions'' developer surface includes engineering blog and 3 more developer resources.'
random_paper: 35
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
screenshot: https://raw.githubusercontent.com/api-evangelist/opensanctions/refs/heads/main/screenshots/opensanctions-2026-06-20T191029.png
security:
- kind: domain-security
  name: Opensanctions Domain Security
  slug: opensanctions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: opensanctions
tags:
- Open Data
- Public APIs
website: https://www.opensanctions.org/docs/api/
---
