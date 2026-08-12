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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Refersion Agentic Access
  operation_count: 15
  slug: refersion-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 6
apis:
- description: GraphQL API providing an explorer interface for querying affiliate data, managing program configurations, and integrating with e-commerce platforms.
  name: Refersion GraphQL API
  slug: refersion-graphql-api
- description: Webhook API for receiving real-time notifications about affiliate activity, including new conversions, conversion approvals/denials, payments, affiliate status changes, and bonus tier movements.
  name: Refersion Webhooks API
  slug: refersion-webhooks-api
- description: Create, retrieve, update, search, and manage affiliate accounts and their conversion triggers.
  name: Refersion Affiliates API
  slug: refersion-affiliates-api
- description: Cancel conversions, get totals, issue manual credits, and change conversion statuses.
  name: Refersion Conversions API
  slug: refersion-conversions-api
- description: Manage offer-level configurations including SKU-specific commission rates.
  name: Refersion Offers API
  slug: refersion-offers-api
- description: Generate download links for saved reports.
  name: Refersion Reporting API
  slug: refersion-reporting-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/refersion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refersion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.refersion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.refersion.dev/reference/welcome-to-refersion
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/refersion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/refersion
- group: company
  title: ''
  type: Blog
  url: https://www.refersion.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.refersion.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.refersion.com
- group: other
  title: ''
  type: X
  url: https://x.com/refersion
- group: commercial
  title: ''
  type: Plans
  url: plans/refersion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refersion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/refersion-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/refersion-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/refersion-context.jsonld
created: '2026-06-13'
description: Affiliate marketing platform for e-commerce brands providing a REST and GraphQL API for managing affiliates, tracking referrals, processing commissions, and integrating with Shopify, BigCommerce, WooCommerce, and other platforms.
examples:
- key_count: 2
  name: Cancel Conversion Request
  slug: cancel-conversion-request
- key_count: 18
  name: New Affiliate Request
  slug: new-affiliate-request
- key_count: 3
  name: New Affiliate Response
  slug: new-affiliate-response
- key_count: 2
  name: Sku Commission Request
  slug: sku-commission-request
finops:
- name: Refersion Finops
  service_category: ''
  slug: refersion-finops
graphqls:
- description: Refersion provides a GraphQL API that supplements its REST API, enabling flexible, ad-hoc queries and data manipulation for affiliate marketing programs. The GraphQL API allows clients to request exac
  name: Refersion GraphQL API
  slug: refersion-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refersion.png
json_schemas:
- name: Affiliate
  property_count: 9
  slug: affiliate
- name: ConversionTrigger
  property_count: 4
  slug: conversion-trigger
- name: Conversion
  property_count: 13
  slug: conversion
jsonld:
- class_count: 7
  name: Refersion Context
  property_count: 68
  slug: refersion-context
layout: provider
modified: '2026-06-13'
name: Refersion
nav: Providers
network: true
overview: 'Refersion publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Affiliates API, Conversions API, Offers API, and 1 more. Tagged areas include Affiliate Marketing, Influencer Marketing, E-Commerce, Referral Tracking, and Commission Management.


  The Refersion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Refersion''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Refersion Plans Pricing
  plan_count: 3
  slug: refersion-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: Refersion Rate Limits
  slug: refersion-rate-limits
rules:
- name: Refersion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: refersion-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.5
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refersion/refs/heads/main/screenshots/refersion-2026-06-20T192744.png
security:
- kind: domain-security
  name: Refersion Domain Security
  slug: refersion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: refersion
tags:
- Affiliate Marketing
- Influencer Marketing
- E-Commerce
- Referral Tracking
- Commission Management
- Shopify
website: https://www.refersion.com/
---
