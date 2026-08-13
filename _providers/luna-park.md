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
  url: security/luna-park-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lunapark.com
created: '2026-07-17'
description: 'Luna Park is a consumer-sector company surfaced as a portfolio company of GV (Google Ventures) and added to the API Evangelist network. Its registered domain lunapark.com now redirects (HTTP 301) to meetquinn.ai — Quinn, described on-site as an AI training platform focused on "operational readiness for the trades." As of this enrichment pass the company publishes a minimal marketing landing page with no public developer portal, API documentation, OpenAPI specification, or other machine-readable API surface. Domain-security posture was probed live: TLS 1.3 with SPF and DMARC (quarantine) present; no HSTS, DNSSEC, or CAA records.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/luna-park.png
layout: provider
modified: '2026-07-20'
name: Luna Park
nav: Providers
network: true
overview: Luna Park is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, GV, Portfolio, and AI.
random_paper: 67
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
screenshot: https://raw.githubusercontent.com/api-evangelist/luna-park/refs/heads/main/screenshots/luna-park-2026-07-25T225723.png
security:
- kind: domain-security
  name: Luna Park Domain Security
  slug: luna-park-domain-security
  summary_line: TLSv1.3 · DMARC
slug: luna-park
tags:
- Company
- Consumer
- GV
- Portfolio
- AI
- Trades
- Training
website: https://lunapark.com
---
