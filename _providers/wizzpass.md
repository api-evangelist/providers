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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wizzpass-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wizzpass.com/
created: '2026-07-17'
description: WizzPass is a visitor and workplace access management platform, surfaced as a Techstars portfolio company and added to the API Evangelist network as a lead for enrichment. At the time of this enrichment pass the company's public web presence at wizzpass.com is dormant behind Cloudflare (HTTP 409 / error 1001) and refuses TLS handshakes, so no live developer portal, documentation, OpenAPI, or API surface could be reached. Email infrastructure is active (AWS SES inbound in eu-west-1, SPF authorizing Amazon SES and TeamSupport), indicating an operating SaaS organization even though the site itself is not currently serving. This profile records the honest probed state and awaits a future pass once the web/API surface is reachable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wizzpass.png
layout: provider
modified: '2026-07-21'
name: WizzPass
nav: Providers
network: true
overview: WizzPass is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Visitor Management, Access Control, Workplace, and Security.
random_paper: 95
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Wizzpass Domain Security
  slug: wizzpass-domain-security
  summary_line: DMARC
slug: wizzpass
tags:
- Company
- Visitor Management
- Access Control
- Workplace
- Security
- Techstars
website: https://wizzpass.com/
---
