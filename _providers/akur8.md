---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Akur8 Deploy auto-generates a real-time REST rating endpoint from a finalized pricing model built in Akur8 Rate. A customer's policy admin system or quoting engine calls the generated endpoint to scor
  name: Akur8 Deploy Rating API
  slug: akur8-deploy-rating-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/akur8-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akur8-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akur8
- group: company
  title: ''
  type: Website
  url: https://www.akur8.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/akur8-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akur8-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.akur8.com/blog
created: '2026-07-03'
description: Akur8 is a cloud-based actuarial AI platform for P&C and life insurers, covering pricing (Data, Risk, Demand, Rate, Rate Repo, Optim, Discover), reserving, and production deployment of rating models. There is no self-serve public developer API or public API reference published on akur8.com; the platform is sold and onboarded as enterprise SaaS through a sales-led, typically two-week free pilot. The one confirmed API capability is Akur8 Deploy - once a pricing model built in Akur8 Rate is finalized, Deploy auto-generates a private, tenant-specific real-time REST rating/scoring endpoint that a customer's own policy admin or quoting system calls at quote time to return a price in milliseconds. Access to that generated endpoint is provisioned per customer within a paid contract, not published for anonymous developer signup; rating tables can also be exported in CSV, JSON, PMML, and POJO formats for offline integration.
finops:
- name: Akur8 Finops
  service_category: Insurtech / Actuarial Software
  slug: akur8-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akur8.png
layout: provider
modified: '2026-07-03'
name: Akur8
nav: Providers
network: true
overview: 'Akur8 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Insurtech, Actuarial, Pricing, and GLM.


  Akur8''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Akur8 Plans Pricing
  plan_count: 2
  slug: akur8-plans-pricing
random_paper: 29
score:
  band: emerging
  composite: 14.2
  delta: -2.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akur8/refs/heads/main/screenshots/akur8-2026-07-25T195528.png
security:
- kind: domain-security
  name: Akur8 Domain Security
  slug: akur8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Akur8 Trust Center
  slug: akur8-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, GDPR
slug: akur8
tags:
- Insurance
- Insurtech
- Actuarial
- Pricing
- GLM
- Rating Engine
website: https://www.akur8.com/
---
