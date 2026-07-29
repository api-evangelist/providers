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
api_count: 3
apis:
- description: The legacy v2 REST API providing access to contacts, campaigns, SMS, programs, pages, forms, data fields, and engagement reporting.
  name: Dotdigital v2 API
  slug: dotdigital-v2-api
- description: The newer v3 REST API framework with unified contacts, improved REST practices, omnichannel communications, and advanced marketing automation features.
  name: Dotdigital v3 API
  slug: dotdigital-v3-api
- description: Communications Platform as a Service API for omnichannel messaging including SMS, MMS, WhatsApp, and push notifications via the Dotdigital Global platform.
  name: Dotdigital CPaaS API
  slug: dotdigital-cpaas-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dotdigital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dotdigital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dotdigital.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dotdigital.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/dotmailer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotdigital
- group: company
  title: ''
  type: Blog
  url: https://dotdigital.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://dotdigital.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://dotdigitalstatus.com
- group: other
  title: ''
  type: X
  url: https://x.com/dotdigital
- group: commercial
  title: ''
  type: Plans
  url: plans/dotdigital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dotdigital-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dotdigital-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/dotdigital-context.jsonld
created: '2026-06-13'
description: Marketing automation platform with a REST API for managing contacts, email campaigns, SMS, automation programs, pages, and accessing engagement data.
finops:
- name: Dotdigital Finops
  service_category: ''
  slug: dotdigital-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotdigital.png
jsonld:
- class_count: 0
  name: Dotdigital Context
  property_count: 10
  slug: dotdigital-context
layout: provider
modified: '2026-06-13'
name: Dotdigital
nav: Providers
network: true
overview: 'Dotdigital publishes 2 APIs on the [APIs.io](https://apis.io/) network: v2 API and v3 API. Tagged areas include Marketing Automation, Email Marketing, SMS, WhatsApp, and Contacts.


  The Dotdigital catalog on APIs.io includes 1 JSON-LD context.


  Dotdigital''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Dotdigital Plans Pricing
  plan_count: 1
  slug: dotdigital-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 0
  name: Dotdigital Rate Limits
  slug: dotdigital-rate-limits
score:
  band: thin
  composite: 29.6
  delta: -5.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/dotdigital/refs/heads/main/screenshots/dotdigital-2026-06-20T180203.png
security:
- kind: domain-security
  name: Dotdigital Domain Security
  slug: dotdigital-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dotdigital Vulnerability Disclosure
  slug: dotdigital-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dotdigital
tags:
- Marketing Automation
- Email Marketing
- SMS
- WhatsApp
- Contacts
- Campaigns
- Push Notifications
- Transactional Email
- Engagement
- Automation
website: https://dotdigital.com
---
