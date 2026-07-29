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
- description: European patent search system api
  name: EPO
  slug: epo
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/epo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.epo.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.epo.org/rss.xml
created: '2026-05-28'
description: European patent search system api
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/epo.png
layout: provider
modified: '2026-05-28'
name: EPO
nav: Providers
network: true
overview: 'EPO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Patent and Public APIs.


  EPO''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.2
  delta: -1.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/epo/refs/heads/main/screenshots/epo-2026-06-20T180757.png
security:
- kind: domain-security
  name: Epo Domain Security
  slug: epo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: epo
tags:
- Patent
- Public APIs
website: https://developers.epo.org/
---
