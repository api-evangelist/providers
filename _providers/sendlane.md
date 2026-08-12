---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for managing contacts, lists, campaigns, automations, custom fields, sender profiles, tags, and custom integration events for e-commerce email and SMS marketing.
  name: Sendlane API
  slug: sendlane-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendlane-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendlane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sendlane.stoplight.io/docs/api-documentation/c53add3c8b16f-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sendlane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendlane/
- group: company
  title: ''
  type: Blog
  url: https://www.sendlane.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendlane.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendlane.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/sendlane
- group: commercial
  title: ''
  type: Plans
  url: plans/sendlane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendlane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendlane-finops.yml
created: '2026-06-13'
description: Email and SMS marketing platform for e-commerce with a REST API for managing contacts, lists, campaigns, automations, forms, and revenue-driven email analytics.
finops:
- name: Sendlane Finops
  service_category: ''
  slug: sendlane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendlane.png
jsonld:
- class_count: 4
  name: Sendlane Context
  property_count: 14
  slug: sendlane-context
layout: provider
modified: '2026-06-13'
name: Sendlane
nav: Providers
network: true
overview: 'Sendlane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, SMS Marketing, E-Commerce, Marketing Automation, and Contacts.


  The Sendlane catalog on APIs.io includes 1 JSON-LD context.


  Sendlane''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Sendlane Plans Pricing
  plan_count: 4
  slug: sendlane-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 0
  name: Sendlane Rate Limits
  slug: sendlane-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendlane/refs/heads/main/screenshots/sendlane-2026-06-20T193659.png
security:
- kind: domain-security
  name: Sendlane Domain Security
  slug: sendlane-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendlane
tags:
- Email Marketing
- SMS Marketing
- E-Commerce
- Marketing Automation
- Contacts
- Campaigns
website: https://www.sendlane.com/
---
