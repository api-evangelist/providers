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
- description: REST API for managing email campaigns, mailing lists, subscribers, templates, and analytics in Zoho Campaigns. Supports campaign creation, scheduling, sending, cloning, and reporting as well as contac
  name: Zoho Campaigns API
  slug: zoho-campaigns-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-campaigns-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-campaigns-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/campaigns/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/campaigns/help/developers/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zoho-campaigns/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/campaigns/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/campaigns/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: other
  title: ''
  type: X
  url: https://x.com/zohocampaigns
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-campaigns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-campaigns-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-campaigns-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/campaigns/
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zoho-campaigns.json
created: '2026-06-13'
description: Zoho Campaigns is an email marketing platform with a REST API for managing mailing lists, campaigns, subscribers, email templates, A/B tests, and campaign analytics. The API (v1.1) uses OAuth 2.0 authentication and supports JSON and XML response formats, enabling developers to create, schedule, send, and report on email campaigns programmatically.
finops:
- name: Zoho Campaigns Finops
  service_category: ''
  slug: zoho-campaigns-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-campaigns.png
layout: provider
modified: '2026-06-13'
name: Zoho Campaigns
nav: Providers
network: true
overview: 'Zoho Campaigns publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Campaigns, Mailing Lists, Subscribers, and Email Templates.


  Zoho Campaigns'' developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Zoho Campaigns Plans Pricing
  plan_count: 5
  slug: zoho-campaigns-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Zoho Campaigns Rate Limits
  slug: zoho-campaigns-rate-limits
score:
  band: thin
  composite: 32.6
  delta: -3.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 36.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-campaigns/refs/heads/main/screenshots/zoho-campaigns-2026-06-20T201934.png
security:
- kind: domain-security
  name: Zoho Campaigns Domain Security
  slug: zoho-campaigns-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Campaigns Vulnerability Disclosure
  slug: zoho-campaigns-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-campaigns
tags:
- Email Marketing
- Campaigns
- Mailing Lists
- Subscribers
- Email Templates
- A/B Testing
- Campaign Analytics
- Marketing Automation
website: https://www.zoho.com/campaigns/
---
