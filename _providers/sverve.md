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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sverve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sverve.com
created: '2026-07-17'
description: Sverve was surfaced as a portfolio company of 500 Global and added to the API Evangelist network as a stub. During the enrichment pass the company's website (sverve.com) was offline — the origin returned HTTP 522 behind Cloudflare, and its DNS (NameBright registrar-parking MX/SPF and a "comingsoon.namebright.com" DMARC target) indicates the domain is parked and the company appears inactive. No developer portal, documentation, OpenAPI, or public API surface could be found, so there is nothing to enrich beyond a probed domain-security record. Left as an inactive lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sverve.png
layout: provider
modified: '2026-07-21'
name: Sverve
nav: Providers
network: true
overview: Sverve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Portfolio Lead, 500 Global, Inactive, and Influencer Marketing.
random_paper: 35
score:
  band: minimal
  composite: 5.0
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Sverve Domain Security
  slug: sverve-domain-security
  summary_line: TLSv1.3
slug: sverve
tags:
- Company
- Portfolio Lead
- 500 Global
- Inactive
- Influencer Marketing
website: https://sverve.com
---
