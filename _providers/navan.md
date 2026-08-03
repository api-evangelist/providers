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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Navan Agentic Access
  operation_count: 29
  slug: navan-agentic-access
  summary_line: 29 operations · 7 acting
api_count: 7
apis:
- description: Booking (trip) records for downstream reporting. MODELED.
  name: Navan Bookings API
  slug: navan-bookings-api
- description: Company custom fields used for cost-center / GL coding. CONFIRMED.
  name: Navan Custom Fields API
  slug: navan-custom-fields-api
- description: Fees, credit/debit adjustments, daily rebates, and disputes. CONFIRMED.
  name: Navan Fees and Adjustments API
  slug: navan-fees-and-adjustments-api
- description: Receipt URLs and downloads for expense transactions. CONFIRMED.
  name: Navan Receipts API
  slug: navan-receipts-api
- description: Expense transactions across Navan card, Connect, manual, and repayment types. CONFIRMED.
  name: Navan Transactions API
  slug: navan-transactions-api
- description: User provisioning and lifecycle under travel/v1. CONFIRMED.
  name: Navan Users API
  slug: navan-users-api
- description: Webhook subscription management for change notifications. MODELED.
  name: Navan Webhooks API
  slug: navan-webhooks-api
artifact_total: 16
collections:
- collection_type: open
  name: Navan API
  slug: open-navan
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/navan-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/navan-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/navan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/navan-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/navan-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/navan-public
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/navan
- group: company
  title: ''
  type: Website
  url: https://navan.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.navan.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/navan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/navan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/navan-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://navan.com/blog/rss.xml
created: '2026-07-03'
description: Navan (formerly TripActions, rebranded to Navan in February 2022) is a corporate travel, expense, and corporate card management platform. Its public developer surface centers on the Navan Expense API (OAuth 2.0 client-credentials) for retrieving and updating transactions, fees, adjustments, receipts, and custom fields, plus a Travel/User Management API for provisioning users and reading booking data, and webhooks for change notifications. Navan also publishes an MCP server for connecting AI assistants to Navan data. Booking (travel) is offered at no platform cost and funded by supplier commissions and per-trip fees, while Expense is a per-user subscription.
finops:
- name: Navan Finops
  service_category: Travel and Expense Management
  slug: navan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/navan.png
layout: provider
modified: '2026-07-03'
name: Navan
nav: Providers
network: true
overview: 'Navan publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Custom Fields API, Fees and Adjustments API, and 4 more. Tagged areas include Corporate Travel, Expense Management, Corporate Cards, Spend Management, and T&E.


  Navan''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Navan Plans Pricing
  plan_count: 3
  slug: navan-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 3
  name: Navan Rate Limits
  slug: navan-rate-limits
scopes:
- name: Navan Scopes
  scope_count: 6
  slug: navan-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 63.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Navan Authentication
  slug: navan-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Navan Domain Security
  slug: navan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Navan Trust Center
  slug: navan-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR, CSA STAR
slug: navan
tags:
- Corporate Travel
- Expense Management
- Corporate Cards
- Spend Management
- T&E
- Fintech
- Business Travel
website: https://navan.com
---
