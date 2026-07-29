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
- description: REST API for programmatically managing campaigns, affiliates, referrals, commissions, payouts, and webhooks within a Rewardful account.
  name: Rewardful REST API
  slug: rewardful-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rewardful-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rewardful.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.rewardful.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rewardful
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rewardful/
- group: company
  title: ''
  type: Blog
  url: https://www.rewardful.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rewardful.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rewardful.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getrewardful
- group: commercial
  title: ''
  type: Plans
  url: plans/rewardful-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rewardful-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rewardful-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rewardful-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rewardful-vocabulary.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: SaaS affiliate and referral tracking platform with a REST API for managing campaigns, affiliates, referrals, and Stripe-integrated commission payouts.
finops:
- name: Rewardful Finops
  service_category: ''
  slug: rewardful-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rewardful.png
jsonld:
- class_count: 15
  name: Rewardful Context
  property_count: 59
  slug: rewardful-context
layout: provider
modified: '2026-06-13'
name: Rewardful
nav: Providers
network: true
overview: 'Rewardful publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Affiliate Tracking, Referral Programs, SaaS, Stripe, and Commissions.


  The Rewardful catalog on APIs.io includes 1 JSON-LD context.


  Rewardful''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Rewardful Plans Pricing
  plan_count: 3
  slug: rewardful-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Rewardful Rate Limits
  slug: rewardful-rate-limits
score:
  band: thin
  composite: 34.6
  delta: -4.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 21.1
  previous_composite: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/screenshots/rewardful-2026-06-20T193058.png
security:
- kind: domain-security
  name: Rewardful Domain Security
  slug: rewardful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rewardful
tags:
- Affiliate Tracking
- Referral Programs
- SaaS
- Stripe
- Commissions
- Payouts
website: https://www.rewardful.com/
---
