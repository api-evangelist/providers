---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 3
apis:
- description: REST API for advertisers and agencies to manage campaigns, teasers, targeting, conversion tracking, and access detailed statistics and reporting for native advertising campaigns.
  name: MGID Advertiser API
  slug: mgid-advertiser-api
- description: REST API for publishers to retrieve widget and website performance metrics including impressions, clicks, revenue, CPM, eCPM, visibility rates, and traffic analytics broken down by date, device, count
  name: MGID Publisher API
  slug: mgid-publisher-api
- description: REST API for advertising agencies to manage client accounts, retrieve financial statistics, view expense reports by service type, and transfer funds between agency and client accounts.
  name: MGID Agency API
  slug: mgid-agency-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mgid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mgid.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.mgid.com/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mgid
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mgid-inc-
- group: company
  title: ''
  type: Blog
  url: https://www.mgid.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://help.mgid.com/mgids-pricing-and-billing-model
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mgid.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/MGID
- group: commercial
  title: ''
  type: Plans
  url: plans/mgid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mgid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mgid-finops.yml
created: '2026-06-13'
description: MGID is a native advertising platform providing a REST API for managing publishers, advertisers, and agencies. The API enables management of campaigns, ad teasers, widgets, conversion tracking, geo and device targeting, and access to detailed traffic and revenue analytics for content monetization across native, display, and video ad formats.
finops:
- name: Mgid Finops
  service_category: ''
  slug: mgid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mgid.png
jsonld:
- class_count: 23
  name: Mgid Context
  property_count: 0
  slug: mgid-context
layout: provider
modified: '2026-06-13'
name: MGID
nav: Providers
network: true
overview: 'MGID publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Native Advertising, Ad Tech, Publishers, Advertisers, and Campaigns.


  The MGID catalog on APIs.io includes 1 JSON-LD context.


  MGID''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Mgid Plans Pricing
  plan_count: 3
  slug: mgid-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 0
  name: Mgid Rate Limits
  slug: mgid-rate-limits
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mgid/refs/heads/main/screenshots/mgid-2026-06-20T185319.png
security:
- kind: domain-security
  name: Mgid Domain Security
  slug: mgid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mgid
tags:
- Native Advertising
- Ad Tech
- Publishers
- Advertisers
- Campaigns
- Content Monetization
- Programmatic
website: https://www.mgid.com
---
