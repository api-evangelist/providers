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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Radar data collected from different websites across the Internet
  name: RainViewer
  slug: rainviewer
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rainviewer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rainviewer.com/api.html
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.rainviewer.com/blog/index.xml
created: '2026-05-28'
description: Radar data collected from different websites across the Internet
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rainviewer.png
layout: provider
modified: '2026-05-28'
name: RainViewer
nav: Providers
network: true
overview: 'RainViewer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.


  RainViewer''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rainviewer/refs/heads/main/screenshots/rainviewer-2026-06-20T192537.png
security:
- kind: domain-security
  name: Rainviewer Domain Security
  slug: rainviewer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rainviewer
tags:
- Weather
- Public APIs
website: https://www.rainviewer.com/api.html
---
