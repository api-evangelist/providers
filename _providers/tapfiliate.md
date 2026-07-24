---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Tapfiliate Agentic Access
  operation_count: 77
  slug: tapfiliate-agentic-access
  summary_line: 77 operations · 41 acting
api_count: 10
apis:
- description: Manage affiliate groups
  name: Tapfiliate Affiliate Groups API
  slug: tapfiliate-affiliate-groups-api
- description: Manage affiliate prospects (pending applicants)
  name: Tapfiliate Affiliate Prospects API
  slug: tapfiliate-affiliate-prospects-api
- description: Manage affiliates, their groups, notes, and payout methods
  name: Tapfiliate Affiliates API
  slug: tapfiliate-affiliates-api
- description: View affiliate balances
  name: Tapfiliate Balances API
  slug: tapfiliate-balances-api
- description: Track and manage clicks
  name: Tapfiliate Clicks API
  slug: tapfiliate-clicks-api
- description: Manage individual commissions
  name: Tapfiliate Commissions API
  slug: tapfiliate-commissions-api
- description: Track and manage conversions and commissions
  name: Tapfiliate Conversions API
  slug: tapfiliate-conversions-api
- description: Manage customers and their metadata
  name: Tapfiliate Customers API
  slug: tapfiliate-customers-api
- description: Manage affiliate payments
  name: Tapfiliate Payments API
  slug: tapfiliate-payments-api
- description: Manage affiliate programs and program affiliates
  name: Tapfiliate Programs API
  slug: tapfiliate-programs-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tapfiliate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tapfiliate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tapfiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tapfiliate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tapfiliate.com
- group: docs
  title: ''
  type: Documentation
  url: https://tapfiliate.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Tapfiliate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tapfiliate/
- group: company
  title: ''
  type: Blog
  url: https://tapfiliate.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tapfiliate.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tapfiliate.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/tapfiliate
- group: commercial
  title: ''
  type: Plans
  url: plans/tapfiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tapfiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tapfiliate-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tapfiliate-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/tapfiliate-context.jsonld
created: 2026-06-13
description: Tapfiliate is an affiliate tracking and management platform with a REST API for creating affiliate programs, managing affiliates, tracking conversions, and handling commission payouts. The API is versioned at V1.6 and uses API key authentication via the X-Api-Key header.
examples:
- key_count: 4
  name: Tapfiliate Create Affiliate Example
  slug: tapfiliate-create-affiliate-example
- key_count: 4
  name: Tapfiliate Create Conversion Example
  slug: tapfiliate-create-conversion-example
finops:
- name: Tapfiliate Finops
  service_category: ''
  slug: tapfiliate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tapfiliate.png
json_schemas:
- name: Affiliate
  property_count: 10
  slug: tapfiliate-affiliate
- name: Commission
  property_count: 7
  slug: tapfiliate-commission
- name: Conversion
  property_count: 8
  slug: tapfiliate-conversion
- name: Customer
  property_count: 6
  slug: tapfiliate-customer
jsonld:
- class_count: 54
  name: Tapfiliate Context
  property_count: 0
  slug: tapfiliate-context
layout: provider
modified: 2026-06-13
name: Tapfiliate
nav: Providers
network: true
overview: 'Tapfiliate publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Affiliate Groups API, Affiliate Prospects API, Affiliates API, and 7 more. Tagged areas include Affiliate Marketing, Affiliate Tracking, Commission Management, Conversion Tracking, and Partner Programs.


  The Tapfiliate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tapfiliate''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Tapfiliate Plans Pricing
  plan_count: 3
  slug: tapfiliate-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 0
  name: Tapfiliate Rate Limits
  slug: tapfiliate-rate-limits
rules:
- name: Tapfiliate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tapfiliate-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 54.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tapfiliate/refs/heads/main/screenshots/tapfiliate-2026-06-20T194920.png
security:
- kind: authentication
  name: Tapfiliate Authentication
  slug: tapfiliate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tapfiliate Domain Security
  slug: tapfiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tapfiliate Vulnerability Disclosure
  slug: tapfiliate-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tapfiliate
tags:
- Affiliate Marketing
- Affiliate Tracking
- Commission Management
- Conversion Tracking
- Partner Programs
- Referral Programs
- Influencer Marketing
website: https://tapfiliate.com
---
