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
  url: security/getdinghy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getdinghy.com/
created: '2026-07-17'
description: Dinghy (getdinghy.com) was a UK insurtech offering on-demand professional indemnity and business insurance for freelancers and contractors, and a Balderton Capital portfolio company. As of this enrichment pass the domain no longer serves an independent site - its TLS certificate and HTTP responses resolve to Kingsbridge Group infrastructure (kingsbridge.co.uk / kingsbridgegroup.com / kng.io) and every path returns HTTP 502, indicating the brand has been absorbed by Kingsbridge. No public API, developer portal, documentation, SDK, or well-known discovery surface is exposed, so no spec-grounded artifacts could be searched or derived. Retained as a network lead with evidence of the successor.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getdinghy.png
layout: provider
modified: '2026-07-19'
name: getdinghy
nav: Providers
network: true
overview: getdinghy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, InsurTech, Freelancers, and Contractors.
random_paper: 35
score:
  band: minimal
  composite: 5.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Getdinghy Domain Security
  slug: getdinghy-domain-security
  summary_line: no transport/DNS hardening detected
slug: getdinghy
tags:
- Company
- Insurance
- InsurTech
- Freelancers
- Contractors
- United Kingdom
- Financial Services
website: https://getdinghy.com/
---
