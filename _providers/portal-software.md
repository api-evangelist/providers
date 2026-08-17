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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portal-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.portal.com
created: '2026-07-17'
description: Portal Software was an Accel-backed billing and revenue-management software company whose portal.com domain now permanently redirects (HTTP 301) to Oracle WebCenter Portal, indicating the business and its assets have been absorbed into Oracle. It was surfaced as an Accel portfolio company and added to the API Evangelist network as a stub, but the enrichment pass finds no independent developer portal, OpenAPI specification, SDKs, MCP server, or published security program under portal.com — the domain serves only an Oracle marketing redirect, so there is no standalone API surface to enrich beyond the domain-level TLS/DNS security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portal-software.png
layout: provider
modified: '2026-07-20'
name: Portal Software
nav: Providers
network: true
overview: Portal Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Billing, Revenue Management, Defunct, and Acquired.
random_paper: 88
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
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Portal Software Domain Security
  slug: portal-software-domain-security
  summary_line: TLSv1.3 · HSTS
slug: portal-software
tags:
- Company
- Billing
- Revenue Management
- Defunct
- Acquired
- Oracle
website: http://www.portal.com
---
