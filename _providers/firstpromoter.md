---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 51
  human_in_the_loop: 1
  name: Firstpromoter Agentic Access
  operation_count: 84
  slug: firstpromoter-agentic-access
  summary_line: 84 operations · 51 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Commissions API from FirstPromoter — 8 operation(s) for commissions.
  name: FirstPromoter Commissions API
  slug: firstpromoter-commissions-api
- description: The Company API from FirstPromoter — 11 operation(s) for company.
  name: FirstPromoter Company API
  slug: firstpromoter-company-api
- description: The Emails API from FirstPromoter — 8 operation(s) for emails.
  name: FirstPromoter Emails API
  slug: firstpromoter-emails-api
- description: The Payouts API from FirstPromoter — 1 operation(s) for payouts.
  name: FirstPromoter Payouts API
  slug: firstpromoter-payouts-api
- description: The Promo Codes API from FirstPromoter — 2 operation(s) for promo codes.
  name: FirstPromoter Promo Codes API
  slug: firstpromoter-promo-codes-api
- description: The Promoter Campaigns API from FirstPromoter — 5 operation(s) for promoter campaigns.
  name: FirstPromoter Promoter Campaigns API
  slug: firstpromoter-promoter-campaigns-api
- description: The Promoters API from FirstPromoter — 11 operation(s) for promoters.
  name: FirstPromoter Promoters API
  slug: firstpromoter-promoters-api
- description: The Referrals API from FirstPromoter — 7 operation(s) for referrals.
  name: FirstPromoter Referrals API
  slug: firstpromoter-referrals-api
- description: The Reports API from FirstPromoter — 6 operation(s) for reports.
  name: FirstPromoter Reports API
  slug: firstpromoter-reports-api
- description: The Track API from FirstPromoter — 4 operation(s) for track.
  name: FirstPromoter Track API
  slug: firstpromoter-track-api
- description: The Webhook Deliveries API from FirstPromoter — 3 operation(s) for webhook deliveries.
  name: FirstPromoter Webhook Deliveries API
  slug: firstpromoter-webhook-deliveries-api
- description: The Webhooks API from FirstPromoter — 4 operation(s) for webhooks.
  name: FirstPromoter Webhooks API
  slug: firstpromoter-webhooks-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/firstpromoter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/firstpromoter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/firstpromoter-authentication.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/firstpromoter-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/firstpromoter-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://firstpromoter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firstpromoter.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/firstpromoter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-promoter
- group: company
  title: ''
  type: Blog
  url: https://firstpromoter.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://firstpromoter.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/firstpromoter
- group: commercial
  title: ''
  type: Plans
  url: plans/firstpromoter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/firstpromoter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/firstpromoter-finops.yml
created: '2026-06-13'
description: Affiliate and referral tracking platform for SaaS companies with a REST API for managing promoters, tracking referrals, and handling reward distribution.
examples:
- key_count: 3
  name: Firstpromoter Create Promoter Example
  slug: firstpromoter-create-promoter-example
- key_count: 3
  name: Firstpromoter Track Sale Example
  slug: firstpromoter-track-sale-example
- key_count: 4
  name: Firstpromoter Webhook Event Example
  slug: firstpromoter-webhook-event-example
finops:
- name: Firstpromoter Finops
  service_category: ''
  slug: firstpromoter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/firstpromoter.png
json_schemas:
- name: Commission
  property_count: 11
  slug: firstpromoter-commission
- name: Promoter
  property_count: 14
  slug: firstpromoter-promoter
- name: Referral
  property_count: 10
  slug: firstpromoter-referral
jsonld:
- class_count: 37
  name: Firstpromoter Context
  property_count: 9
  slug: firstpromoter-context
layout: provider
modified: '2026-06-13'
name: FirstPromoter
nav: Providers
network: true
overview: 'FirstPromoter publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Commissions API, Company API, Emails API, and 9 more. Tagged areas include Affiliate Marketing, Referral Tracking, SaaS, Commission Management, and Reward Distribution.


  The FirstPromoter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FirstPromoter''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Firstpromoter Plans Pricing
  plan_count: 3
  slug: firstpromoter-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Firstpromoter Rate Limits
  slug: firstpromoter-rate-limits
rules:
- name: FirstPromoter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: firstpromoter-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.5
  delta: -4.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firstpromoter/refs/heads/main/screenshots/firstpromoter-2026-06-20T181244.png
security:
- kind: authentication
  name: Firstpromoter Authentication
  slug: firstpromoter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Firstpromoter Domain Security
  slug: firstpromoter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: firstpromoter
tags:
- Affiliate Marketing
- Referral Tracking
- SaaS
- Commission Management
- Reward Distribution
- Promoters
website: https://firstpromoter.com/
---
