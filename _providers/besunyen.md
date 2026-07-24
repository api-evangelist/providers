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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/besunyen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://besunyen.com
created: '2026-07-17'
description: Besunyen is a Chinese consumer-health company known for herbal weight-management, functional and detox teas plus related wellness and nutrition products, surfaced as a portfolio company of Qiming and added to the API Evangelist network as a stub. Enrichment on 2026-07-18 found no public developer, API, or documentation surface — besunyen.com serves only an nginx 404 and its TLS certificate is issued for besunyen.co (hostname mismatch); the only real artifact captured is a domain-security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/besunyen.png
layout: provider
modified: '2026-07-18'
name: besunyen
nav: Providers
network: true
overview: besunyen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Wellness, Consumer Goods, and Nutrition.
random_paper: 6
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Besunyen Domain Security
  slug: besunyen-domain-security
  summary_line: no transport/DNS hardening detected
slug: besunyen
tags:
- Company
- Health
- Wellness
- Consumer Goods
- Nutrition
- China
website: https://besunyen.com
---
