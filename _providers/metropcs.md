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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metropcs-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metropcs-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/metropcs-security.txt
- group: company
  title: ''
  type: Website
  url: https://www.metropcs.com
created: '2026-07-17'
description: 'MetroPCS is a company surfaced as a portfolio company of accel, battery-ventures and added to the API Evangelist network as a stub for enrichment. Sector: consumer. This profile is a lead awaiting the enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metropcs.png
layout: provider
modified: '2026-07-20'
name: MetroPCS
nav: Providers
network: true
overview: MetroPCS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Telecommunications, Wireless, and Mobile.
random_paper: 16
score:
  band: minimal
  composite: 2.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Metropcs Domain Security
  slug: metropcs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metropcs
tags:
- Company
- Consumer
- Telecommunications
- Wireless
- Mobile
- Prepaid
- Carrier
website: https://www.metropcs.com
---
