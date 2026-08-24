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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/willing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://willing.com
created: '2026-07-17'
description: Willing was an online estate-planning and will-making platform (a 500 Global portfolio company) that let consumers create wills, living wills, and related documents. The brand has since been absorbed into MetLife Legal Plans; as of this enrichment pass willing.com live-redirects (HTTP 302) to legalplans.com. Willing publishes no independent public API, developer portal, or GitHub organization of its own, so it carries no API artifacts beyond a domain-security probe of the surviving willing.com host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/willing.png
layout: provider
modified: '2026-07-21'
name: Willing
nav: Providers
network: true
overview: Willing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Estate Planning, Wills, Legal, and Legal Tech.
random_paper: 2
score:
  band: minimal
  composite: 2.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Willing Domain Security
  slug: willing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: willing
tags:
- Company
- Estate Planning
- Wills
- Legal
- Legal Tech
- Consumer
- Insurance
website: https://willing.com
---
