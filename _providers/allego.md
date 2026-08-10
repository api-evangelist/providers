---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'REST API for the Allego sales enablement platform enabling programmatic access to video coaching sessions, content libraries, learning modules, certifications, rep readiness assessments, conversation '
  name: Allego API
  slug: allego-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/allego-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.allego.com/platform/integrations/
- group: company
  title: ''
  type: Blog
  url: https://www.allego.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.allego.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.allego.com/support/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allego/
- group: other
  title: ''
  type: X
  url: https://twitter.com/allegosoftware
- group: commercial
  title: ''
  type: Plans
  url: plans/allego-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/allego-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/allego-finops.yml
created: '2026-06-13'
description: Allego is an AI-powered sales enablement and revenue training platform providing a REST API for managing video coaching, content libraries, certifications, rep readiness assessments, conversation intelligence, and deal intelligence to help revenue teams improve performance.
finops:
- name: Allego Finops
  service_category: ''
  slug: allego-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allego.png
layout: provider
modified: '2026-06-13'
name: Allego
nav: Providers
network: true
overview: 'Allego publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Sales Training, Video Coaching, Content Management, and Conversation Intelligence.


  Allego''s developer surface includes documentation, engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Allego Plans Pricing
  plan_count: 4
  slug: allego-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Allego Rate Limits
  slug: allego-rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 32.3
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allego/refs/heads/main/screenshots/allego-2026-06-20T171529.png
security:
- kind: domain-security
  name: Allego Domain Security
  slug: allego-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Allego Trust Center
  slug: allego-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: allego
tags:
- Sales Enablement
- Sales Training
- Video Coaching
- Content Management
- Conversation Intelligence
- Deal Intelligence
- Revenue Enablement
- Certifications
- AI
website: https://www.allego.com/
---
