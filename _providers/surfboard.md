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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/surfboard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://teamsurfboard.com
created: '2026-07-17'
description: Surfboard (teamsurfboard.com) was a workforce management (WFM) SaaS for customer support teams — scheduling, forecasting, and real-time staffing for contact centers — backed by Seedcamp and Speedinvest. As of this enrichment pass the standalone product no longer operates independently; teamsurfboard.com returns an HTTP 301 permanent redirect to Dialpad's workforce management software page (dialpad.com/features/workforce-management-software), indicating Surfboard was acquired by / folded into Dialpad. No standalone Surfboard developer portal, API reference, or OpenAPI surface is publicly reachable; all probed /.well-known/ discovery endpoints return 404.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/surfboard.png
layout: provider
modified: '2026-07-21'
name: Surfboard
nav: Providers
network: true
overview: Surfboard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Customer Support, Contact Center, and Scheduling.
random_paper: 8
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
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Surfboard Domain Security
  slug: surfboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: surfboard
tags:
- Company
- Workforce Management
- Customer Support
- Contact Center
- Scheduling
- WFM
- Acquired
website: http://teamsurfboard.com
---
