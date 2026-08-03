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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextravel.com
created: '2026-07-17'
description: Jetway was surfaced as a 500 Global portfolio lead pointing at nextravel.com. Enrichment found that nextravel.com now 301-redirects to TravelPerk (www.travelperk.com), which itself redirects to www.perk.com, an all-in-one business travel and expense-management platform. NexTravel was a US corporate-travel startup acquired by TravelPerk; it no longer operates as an independent brand and publishes no public developer API, API documentation, developer portal, or /.well-known discovery documents at nextravel.com (every probed path soft-404s to the Perk marketing site). This profile is retained as an acquired/redirected lead with no independent developer surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetway.png
layout: provider
modified: '2026-07-19'
name: Jetway
nav: Providers
network: true
overview: Jetway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Corporate Travel, Business Travel, and Expense Management.
random_paper: 90
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jetway/refs/heads/main/screenshots/jetway-2026-07-25T223138.png
security:
- kind: domain-security
  name: Jetway Domain Security
  slug: jetway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jetway
tags:
- Company
- Travel
- Corporate Travel
- Business Travel
- Expense Management
- Acquired
website: https://nextravel.com
---
