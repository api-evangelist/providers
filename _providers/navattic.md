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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Navattic REST API allows developers to programmatically create and manage interactive product demos, retrieve analytics and engagement data, and integrate demo activity into downstream systems. Th
  name: Navattic API
  slug: navattic-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/navattic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navattic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.navattic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.navattic.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Navattic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navattic
- group: company
  title: ''
  type: Blog
  url: https://www.navattic.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.navattic.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.navattic.com
- group: other
  title: ''
  type: X
  url: https://x.com/navattic
- group: commercial
  title: ''
  type: Plans
  url: plans/navattic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/navattic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/navattic-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/navattic-context.jsonld
created: 2026-06-13
description: Navattic is an interactive product demo platform that enables marketing and sales teams to create, manage, and embed no-code product demos without engineering involvement. The platform provides a REST API and webhook integration for automating demo workflows and syncing engagement data with CRM, marketing automation, and analytics tools. Navattic supports integrations with HubSpot, Salesforce, Marketo, Segment, Gong, and dozens of other go-to-market platforms. Teams use Navattic to accelerate sales cycles, improve lead qualification, and deliver personalized demo experiences across their entire funnel.
finops:
- name: Navattic Finops
  service_category: ''
  slug: navattic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navattic.png
jsonld:
- class_count: 21
  name: Navattic Context
  property_count: 0
  slug: navattic-context
layout: provider
modified: 2026-06-13
name: Navattic
nav: Providers
network: true
overview: 'Navattic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Interactive Demos, Product Demo, Sales Enablement, Marketing, and No-Code.


  The Navattic catalog on APIs.io includes 1 JSON-LD context.


  Navattic''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Navattic Plans Pricing
  plan_count: 5
  slug: navattic-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Navattic Rate Limits
  slug: navattic-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: -2.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/navattic/refs/heads/main/screenshots/navattic-2026-06-20T190058.png
security:
- kind: domain-security
  name: Navattic Domain Security
  slug: navattic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Navattic Vulnerability Disclosure
  slug: navattic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: navattic
tags:
- Interactive Demos
- Product Demo
- Sales Enablement
- Marketing
- No-Code
- Webhooks
- CRM Integration
- Sales Automation
website: https://www.navattic.com/
---
