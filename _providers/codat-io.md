---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Codat Io Agentic Access
  operation_count: 52
  slug: codat-io-agentic-access
  summary_line: 52 operations · 16 acting
api_count: 13
apis:
- description: Standardized accounting data types.
  name: Codat Accounting API
  slug: codat-io-accounting-api
- description: Push transactions into accounting platforms as a bank feed.
  name: Codat Bank Feeds API
  slug: codat-io-bank-feeds-api
- description: Standardized banking data types.
  name: Codat Banking API
  slug: codat-io-banking-api
- description: Standardized commerce and point-of-sale data types.
  name: Codat Commerce API
  slug: codat-io-commerce-api
- description: Create and manage the companies (customers) you pull data for.
  name: Codat Companies API
  slug: codat-io-companies-api
- description: Manage a company's connections to accounting, banking, and commerce platforms.
  name: Codat Connections API
  slug: codat-io-connections-api
- description: Sync for Expenses - reconcile card and expense transactions.
  name: Codat Expenses API
  slug: codat-io-expenses-api
- description: Discover supported integrations and their branding.
  name: Codat Integrations API
  slug: codat-io-integrations-api
- description: Assess reports and lending metrics.
  name: Codat Lending API
  slug: codat-io-lending-api
- description: Queue data refreshes and inspect pull history and status.
  name: Codat Manage data API
  slug: codat-io-manage-data-api
- description: Sync for Payables - write bills and payments.
  name: Codat Payables API
  slug: codat-io-payables-api
- description: Sync commerce sales into accounting software.
  name: Codat Sync for Commerce API
  slug: codat-io-sync-for-commerce-api
- description: Manage webhook consumers for event subscriptions.
  name: Codat Webhooks API
  slug: codat-io-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Codat API
  slug: open-codat-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codat-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codat-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codat-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codatio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codat
- group: company
  title: ''
  type: Website
  url: https://www.codat.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codat.io
- group: commercial
  title: ''
  type: Plans
  url: plans/codat-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codat-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codat-io-finops.yml
created: '2026-07-01'
description: Codat provides a business data API that connects small-business accounting, banking, and commerce platforms to lenders, fintechs, and B2B software providers. A single integration to api.codat.io standardizes data from QuickBooks, Xero, Sage, NetSuite, FreshBooks, and 30+ other systems - and can write bills, payments, and expenses back into them - powering underwriting, reconciliation, payables, and spend products.
finops:
- name: Codat Io Finops
  service_category: Financial Data and Analytics
  slug: codat-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codat-io.png
layout: provider
modified: '2026-07-01'
name: Codat
nav: Providers
network: true
overview: 'Codat publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Bank Feeds API, Banking API, and 10 more. Tagged areas include Business Data, Accounting, Banking, Commerce, and Fintech.


  Codat''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Codat Io Plans Pricing
  plan_count: 3
  slug: codat-io-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 3
  name: Codat Io Rate Limits
  slug: codat-io-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codat-io/refs/heads/main/screenshots/codat-io-2026-07-25T205918.png
security:
- kind: authentication
  name: Codat Io Authentication
  slug: codat-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codat Io Domain Security
  slug: codat-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codat-io
tags:
- Business Data
- Accounting
- Banking
- Commerce
- Fintech
- Lending
- Financial Data
website: https://www.codat.io
---
