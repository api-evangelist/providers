---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for Logility's AI-powered supply chain planning platform, enabling integration with demand sensing, inventory optimization, supply planning, S&OP process management, and supply chain analytic
  name: Logility Supply Chain API
  slug: logility-supply-chain-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.logility.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.logility.com/solutions/platform/
- group: company
  title: ''
  type: Blog
  url: https://www.logility.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logility.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/logility
- group: other
  title: ''
  type: X
  url: https://twitter.com/logilityinc
- group: operate
  title: ''
  type: Contact
  url: https://www.logility.com/contact-us/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/logility/refs/heads/main/plans/logility-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/logility/refs/heads/main/rate-limits/logility-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/logility/refs/heads/main/finops/logility-finops.yml
created: 2026-06-13
description: Logility is an AI-powered supply chain planning platform providing solutions for demand sensing, inventory optimization, supply planning, S&OP process management, and supply chain analytics. Part of Aptean, Logility serves 600+ clients across 80 countries with capabilities for demand planning, inventory optimization, scenario planning, manufacturing execution, and supplier management across 12+ industry verticals.
finops:
- name: Logility Finops
  service_category: ''
  slug: logility-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logility.png
layout: provider
modified: 2026-06-13
name: Logility
nav: Providers
network: true
overview: 'Logility publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Demand Planning, Inventory Optimization, Supply Planning, and S&OP.


  Logility''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Logility Plans Pricing
  plan_count: 1
  slug: logility-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 0
  name: Logility Rate Limits
  slug: logility-rate-limits
score:
  band: emerging
  composite: 16.9
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logility/refs/heads/main/screenshots/logility-2026-06-20T184655.png
security:
- kind: domain-security
  name: Logility Domain Security
  slug: logility-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: logility
tags:
- Supply Chain
- Demand Planning
- Inventory Optimization
- Supply Planning
- S&OP
- Supply Chain Analytics
- AI
- Machine Learning
website: https://www.logility.com/
---
