---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful OAuth API for managing leads, matters, contacts, intake forms, pipelines, and automated client follow-ups within the Lawmatics legal CRM platform.
  name: Lawmatics OAuth API
  slug: lawmatics-oauth-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lawmatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lawmatics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lawmatics.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lawmatics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lawmatics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lawmatics.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lawmatics
- group: other
  title: ''
  type: X
  url: https://x.com/lawmatics
- group: commercial
  title: ''
  type: Plans
  url: plans/lawmatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lawmatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lawmatics-finops.yml
created: '2026-06-13'
description: Lawmatics is a legal CRM and automation platform with a REST API for managing leads, matters, contacts, intake forms, pipelines, and automated client follow-ups for law firms of all sizes.
finops:
- name: Lawmatics Finops
  service_category: ''
  slug: lawmatics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lawmatics.png
jsonld:
- class_count: 5
  name: Lawmatics Context
  property_count: 26
  slug: lawmatics-context
layout: provider
modified: '2026-06-13'
name: Lawmatics
nav: Providers
network: true
overview: 'Lawmatics publishes 1 API on the [APIs.io](https://apis.io/) network: OAuth API. Tagged areas include Legal, CRM, Law Firms, Client Intake, and Marketing Automation.


  The Lawmatics catalog on APIs.io includes 1 JSON-LD context.


  Lawmatics'' developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Lawmatics Plans Pricing
  plan_count: 3
  slug: lawmatics-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Lawmatics Rate Limits
  slug: lawmatics-rate-limits
score:
  band: thin
  composite: 32.7
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 36.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lawmatics/refs/heads/main/screenshots/lawmatics-2026-06-20T184337.png
security:
- kind: domain-security
  name: Lawmatics Domain Security
  slug: lawmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lawmatics
tags:
- Legal
- CRM
- Law Firms
- Client Intake
- Marketing Automation
- Matter Management
- E-Signature
- Workflow Automation
website: https://www.lawmatics.com/
---
