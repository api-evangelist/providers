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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theportal.to/
created: '2026-07-17'
description: 'Portals (theportal.to) is a consumer platform organized around three activities — play, collect, and create — surfaced through the API Evangelist network as a Greylock portfolio company. As of this enrichment pass the public site is a single-page consumer application: no published developer API, OpenAPI definition, developer portal, documentation, or /.well-known discovery documents were found. The only machine-verifiable surface is the web domain itself (HTTPS with TLS 1.3, HSTS, SPF, and DMARC present). This profile will be upgraded if and when a public API surface appears.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portals.png
layout: provider
modified: '2026-07-20'
name: Portals
nav: Providers
network: true
overview: Portals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Play, Collect, and Create.
random_paper: 77
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Portals Domain Security
  slug: portals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portals
tags:
- Company
- Consumer
- Play
- Collect
- Create
- Creator
website: https://theportal.to/
---
