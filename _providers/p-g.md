---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The central API hub for Developers, Consumers, Application Managers, and Architects to discover and use P&G APIs.
  name: P&G Developer API Marketplace
  slug: p-g
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/p-g-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/p-g-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/procter-gamble
- group: start
  title: ''
  type: Portal
  url: https://developer.pg.com/
- group: company
  title: ''
  type: Website
  url: https://www.pg.com/
created: '2025-02-08'
description: Procter & Gamble provides an API Marketplace - the central API hub for Developers, Consumers, Application Managers, and Architects to discover and use P&G APIs.
finops:
- name: P G Finops
  service_category: API
  slug: p-g-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/p-g.png
layout: provider
modified: '2026-04-28'
name: P&G
nav: Providers
network: true
overview: 'P&G publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Marketplace and Consumer Goods.


  P&G''s developer surface includes developer portal and 4 more developer resources.'
plans:
- name: P G Plans Pricing
  plan_count: 3
  slug: p-g-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: P G Rate Limits
  slug: p-g-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 19.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/p-g/refs/heads/main/screenshots/p-g-2026-06-20T191300.png
security:
- kind: domain-security
  name: P G Domain Security
  slug: p-g-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: P G Vulnerability Disclosure
  slug: p-g-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: p-g
tags:
- API Marketplace
- Consumer Goods
website: https://www.pg.com/
---
