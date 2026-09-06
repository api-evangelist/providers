---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Fyle Agentic Access
  operation_count: 40
  slug: fyle-agentic-access
  summary_line: 40 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Advance requests raised by employees.
  name: Fyle Advances API
  slug: fyle-advances-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Expense categories, usually synced from a chart of accounts.
  name: Fyle Categories API
  slug: fyle-categories-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Enrolled corporate cards and their real-time transactions.
  name: Fyle Corporate Cards API
  slug: fyle-corporate-cards-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Cost centers mapping spend to departments or business units.
  name: Fyle Cost Centers API
  slug: fyle-cost-centers-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Employee/user records, usually synced from an HRMS.
  name: Fyle Employees API
  slug: fyle-employees-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Expenses across the organization (admin) or for the signed-in spender.
  name: Fyle Expenses API
  slug: fyle-expenses-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: File records and pre-signed URLs for receipts and attachments.
  name: Fyle Files API
  slug: fyle-files-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Merchant/vendor values available to spenders.
  name: Fyle Merchants API
  slug: fyle-merchants-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Projects used to tag and allocate spend.
  name: Fyle Projects API
  slug: fyle-projects-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Expense reports submitted for approval and reimbursement.
  name: Fyle Reports API
  slug: fyle-reports-api
- baseURL: https://api.fylehq.com/platform/v1/admin
  baseurl_source: declared
  description: Webhook subscriptions and scheduled callbacks.
  name: Fyle Webhooks API
  slug: fyle-webhooks-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fyle Platform Advances API
  slug: open-fyle-advances-api
- collection_type: open
  name: Fyle Platform Advances Categories API
  slug: open-fyle-categories-api
- collection_type: open
  name: Fyle Platform Advances Corporate Cards API
  slug: open-fyle-corporate-cards-api
- collection_type: open
  name: Fyle Platform Advances Cost Centers API
  slug: open-fyle-cost-centers-api
- collection_type: open
  name: Fyle Platform Advances Employees API
  slug: open-fyle-employees-api
- collection_type: open
  name: Fyle Platform Advances Expenses API
  slug: open-fyle-expenses-api
- collection_type: open
  name: Fyle Platform Advances Files API
  slug: open-fyle-files-api
- collection_type: open
  name: Fyle Platform Advances Merchants API
  slug: open-fyle-merchants-api
- collection_type: open
  name: Fyle Platform Advances Projects API
  slug: open-fyle-projects-api
- collection_type: open
  name: Fyle Platform Advances Reports API
  slug: open-fyle-reports-api
- collection_type: open
  name: Fyle Platform Advances Webhooks API
  slug: open-fyle-webhooks-api
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
random_paper: 12
rate_limits:
- limit_count: 3
  name: Fyle Rate Limits
  slug: fyle-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
