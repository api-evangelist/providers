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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Fyle Agentic Access
  operation_count: 40
  slug: fyle-agentic-access
  summary_line: 40 operations · 25 acting
api_count: 11
apis:
- description: Advance requests raised by employees.
  name: Fyle Advances API
  slug: fyle-advances-api
- description: Expense categories, usually synced from a chart of accounts.
  name: Fyle Categories API
  slug: fyle-categories-api
- description: Enrolled corporate cards and their real-time transactions.
  name: Fyle Corporate Cards API
  slug: fyle-corporate-cards-api
- description: Cost centers mapping spend to departments or business units.
  name: Fyle Cost Centers API
  slug: fyle-cost-centers-api
- description: Employee/user records, usually synced from an HRMS.
  name: Fyle Employees API
  slug: fyle-employees-api
- description: Expenses across the organization (admin) or for the signed-in spender.
  name: Fyle Expenses API
  slug: fyle-expenses-api
- description: File records and pre-signed URLs for receipts and attachments.
  name: Fyle Files API
  slug: fyle-files-api
- description: Merchant/vendor values available to spenders.
  name: Fyle Merchants API
  slug: fyle-merchants-api
- description: Projects used to tag and allocate spend.
  name: Fyle Projects API
  slug: fyle-projects-api
- description: Expense reports submitted for approval and reimbursement.
  name: Fyle Reports API
  slug: fyle-reports-api
- description: Webhook subscriptions and scheduled callbacks.
  name: Fyle Webhooks API
  slug: fyle-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Fyle Platform API
  slug: open-fyle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fyle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fyle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fyle-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fylein
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fyle
- group: company
  title: ''
  type: Website
  url: https://www.fylehq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fylehq.com
- group: commercial
  title: ''
  type: Plans
  url: plans/fyle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fyle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fyle-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fylehq.com/blog
created: '2026-07-03'
description: Fyle (now Sage Expense Management) is a spend and expense management platform known for real-time corporate card feeds that text employees for a receipt the moment a card is swiped, then auto-code the expense. The Fyle Platform APIs expose the same objects the product runs on - expenses, expense reports, advances, categories, projects, cost centers, employees, merchants, corporate cards and their transactions, files/receipts, and webhook subscriptions - as role-scoped REST resources (admin, spender, approver, common) under https://api.fylehq.com/platform/v1. Access is authenticated with OAuth 2.0 (refresh-token grant issuing short-lived Bearer access tokens), and list endpoints use PostgREST-style filtering with mandatory offset, limit, and order pagination.
finops:
- name: Fyle Finops
  service_category: Spend and Expense Management (SaaS)
  slug: fyle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fyle.png
layout: provider
modified: '2026-07-03'
name: Fyle
nav: Providers
network: true
overview: 'Fyle publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Advances API, Categories API, Corporate Cards API, and 8 more. Tagged areas include Expense Management, Spend Management, Corporate Cards, Fintech, and Accounting.


  Fyle''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Fyle Plans Pricing
  plan_count: 3
  slug: fyle-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 3
  name: Fyle Rate Limits
  slug: fyle-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fyle/refs/heads/main/screenshots/fyle-2026-07-25T215342.png
security:
- kind: authentication
  name: Fyle Authentication
  slug: fyle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fyle Domain Security
  slug: fyle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fyle
tags:
- Expense Management
- Spend Management
- Corporate Cards
- Fintech
- Accounting
- Receipts
website: https://www.fylehq.com
---
