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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novocall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://novocall.co
created: '2026-07-17'
description: Novocall was a Singapore-based callback and lead-conversion SaaS (a click-to-call and callback-scheduling widget that turned website visitors into inbound phone calls and booked meetings), surfaced as a 500 Global portfolio company and added to the API Evangelist network as a stub for enrichment. As of the July 2026 enrichment pass the company's public web presence is unreachable. The apex novocall.co has live email DNS (SPF, DMARC quarantine, CAA) but no web host, www.novocall.co returns a Cloudflare 530 (origin down), novocall.com is a parked/for-sale domain, and getnovocall.com refuses connections. No public API, developer portal, or documentation surface could be reached, so no API artifacts were harvested; only a live domain-security probe of the remaining DNS/TLS footprint was captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novocall.png
layout: provider
modified: '2026-07-20'
name: Novocall
nav: Providers
network: true
overview: Novocall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Callback, Lead Conversion, Click To Call, and Sales.
random_paper: 71
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
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Novocall Domain Security
  slug: novocall-domain-security
  summary_line: DMARC
slug: novocall
tags:
- Company
- Callback
- Lead Conversion
- Click To Call
- Sales
- Marketing
- SaaS
website: https://novocall.co
---
