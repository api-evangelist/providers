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
- description: The Moosend REST API (v3) enables programmatic access to email marketing and automation capabilities including managing email lists, subscribers, campaigns, segments, and transactional emails. Authent
  name: Moosend API
  slug: moosend-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/moosend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moosend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moosend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moosend.com/developers/api-documentation/en/index-en.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/moosend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moosend
- group: company
  title: ''
  type: Blog
  url: https://moosend.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://moosend.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moosend.com/
- group: other
  title: ''
  type: X
  url: https://x.com/moosend
- group: commercial
  title: ''
  type: Plans
  url: plans/moosend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moosend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moosend-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/moosend-context.jsonld
created: '2026-06-13'
description: Moosend is an email marketing and automation platform with a REST API for managing mailing lists, campaigns, subscribers, automations, and tracking email performance metrics. The API uses HTTPS with API key authentication and provides programmatic access to email lists, subscriber management, campaign creation and scheduling, audience segmentation, transactional emails, and real-time reporting.
finops:
- name: Moosend Finops
  service_category: ''
  slug: moosend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moosend.png
jsonld:
- class_count: 20
  name: Moosend Context
  property_count: 0
  slug: moosend-context
layout: provider
modified: '2026-06-13'
name: Moosend
nav: Providers
network: true
overview: 'Moosend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Marketing Automation, Campaigns, Mailing Lists, and Subscribers.


  The Moosend catalog on APIs.io includes 1 JSON-LD context.


  Moosend''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Moosend Plans Pricing
  plan_count: 5
  slug: moosend-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 10
  name: Moosend Rate Limits
  slug: moosend-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 38.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moosend/refs/heads/main/screenshots/moosend-2026-06-20T185801.png
security:
- kind: domain-security
  name: Moosend Domain Security
  slug: moosend-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Moosend Trust Center
  slug: moosend-trust-center
  summary_line: GDPR
slug: moosend
tags:
- Email Marketing
- Marketing Automation
- Campaigns
- Mailing Lists
- Subscribers
- Transactional Email
- SMTP
- Segmentation
- Analytics
website: https://moosend.com/
---
