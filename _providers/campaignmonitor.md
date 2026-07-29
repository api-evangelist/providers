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
- description: REST API for managing email campaigns, subscriber lists, transactional emails, segments, journeys, templates, and campaign performance analytics.
  name: Campaign Monitor API
  slug: campaign-monitor-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/campaignmonitor-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/campaignmonitor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campaignmonitor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.campaignmonitor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.campaignmonitor.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/campaignmonitor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/campaign-monitor
- group: company
  title: ''
  type: Blog
  url: https://www.campaignmonitor.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.campaignmonitor.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.campaignmonitor.com/
- group: other
  title: ''
  type: X
  url: https://x.com/campaignmonitor
- group: commercial
  title: ''
  type: Plans
  url: plans/campaignmonitor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/campaignmonitor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/campaignmonitor-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/campaignmonitor-context.jsonld
created: '2026-06-13'
description: Email marketing platform with a REST API for managing campaigns, subscriber lists, transactional emails, segments, and accessing campaign performance analytics.
finops:
- name: Campaignmonitor Finops
  service_category: ''
  slug: campaignmonitor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campaignmonitor.png
jsonld:
- class_count: 18
  name: Campaignmonitor Context
  property_count: 1
  slug: campaignmonitor-context
layout: provider
modified: '2026-06-13'
name: Campaign Monitor
nav: Providers
network: true
overview: 'Campaign Monitor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Email Marketing, Campaigns, Subscribers, Transactional Email, and Segments.


  The Campaign Monitor catalog on APIs.io includes 1 JSON-LD context.


  Campaign Monitor''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Campaignmonitor Plans Pricing
  plan_count: 5
  slug: campaignmonitor-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 2
  name: Campaignmonitor Rate Limits
  slug: campaignmonitor-rate-limits
score:
  band: thin
  composite: 36.5
  delta: -3.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 40.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campaignmonitor/refs/heads/main/screenshots/campaignmonitor-2026-06-20T173912.png
security:
- kind: domain-security
  name: Campaignmonitor Domain Security
  slug: campaignmonitor-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Campaignmonitor Vulnerability Disclosure
  slug: campaignmonitor-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Campaignmonitor Trust Center
  slug: campaignmonitor-trust-center
  summary_line: SOC 2, GDPR
slug: campaignmonitor
tags:
- Email Marketing
- Campaigns
- Subscribers
- Transactional Email
- Segments
- Newsletters
- Automation
website: https://www.campaignmonitor.com/
---
