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
  url: security/treatco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://treat.co
created: '2026-07-17'
description: 'Treat.co was a consumer gifting e-commerce startup surfaced as a portfolio company of 500 Global and added to the API Evangelist network as an enrichment lead. As of this enrichment pass the treat.co domain is controlled by Mars, Incorporated: it resolves to an AWS Application Load Balancer presenting a certificate for alb-redirect.mars.com and returns HTTP 403 on every probed path (homepage, /.well-known/security.txt, /api, /developers), with no MX record for email. The company therefore exposes no public website, developer portal, documentation, or API surface today; it appears dormant or absorbed following acquisition. This profile records the domain-security probe and is retained as a network lead pending any revived or successor developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treatco.png
layout: provider
modified: '2026-07-21'
name: Treat.co
nav: Providers
network: true
overview: Treat.co is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gifting, E-Commerce, Consumer, and Retail.
random_paper: 34
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
  name: Treatco Domain Security
  slug: treatco-domain-security
  summary_line: DMARC
slug: treatco
tags:
- Company
- Gifting
- E-Commerce
- Consumer
- Retail
- Confectionery
website: https://treat.co
---
