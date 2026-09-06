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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Codat Io Agentic Access
  operation_count: 52
  slug: codat-io-agentic-access
  summary_line: 52 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Standardized accounting data types.
  name: Codat Accounting API
  slug: codat-io-accounting-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Push transactions into accounting platforms as a bank feed.
  name: Codat Bank Feeds API
  slug: codat-io-bank-feeds-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Standardized banking data types.
  name: Codat Banking API
  slug: codat-io-banking-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Standardized commerce and point-of-sale data types.
  name: Codat Commerce API
  slug: codat-io-commerce-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Create and manage the companies (customers) you pull data for.
  name: Codat Companies API
  slug: codat-io-companies-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Manage a company's connections to accounting, banking, and commerce platforms.
  name: Codat Connections API
  slug: codat-io-connections-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Sync for Expenses - reconcile card and expense transactions.
  name: Codat Expenses API
  slug: codat-io-expenses-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Discover supported integrations and their branding.
  name: Codat Integrations API
  slug: codat-io-integrations-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Assess reports and lending metrics.
  name: Codat Lending API
  slug: codat-io-lending-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Queue data refreshes and inspect pull history and status.
  name: Codat Manage data API
  slug: codat-io-manage-data-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Sync for Payables - write bills and payments.
  name: Codat Payables API
  slug: codat-io-payables-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Sync commerce sales into accounting software.
  name: Codat Sync for Commerce API
  slug: codat-io-sync-for-commerce-api
- baseURL: https://api.codat.io
  baseurl_source: declared
  description: Manage webhook consumers for event subscriptions.
  name: Codat Webhooks API
  slug: codat-io-webhooks-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Codat Accounting API
  slug: open-codat-io-accounting-api
- collection_type: open
  name: Codat Accounting Bank Feeds API
  slug: open-codat-io-bank-feeds-api
- collection_type: open
  name: Codat Accounting Banking API
  slug: open-codat-io-banking-api
- collection_type: open
  name: Codat Accounting Commerce API
  slug: open-codat-io-commerce-api
- collection_type: open
  name: Codat Accounting Companies API
  slug: open-codat-io-companies-api
- collection_type: open
  name: Codat Accounting Connections API
  slug: open-codat-io-connections-api
- collection_type: open
  name: Codat Accounting Expenses API
  slug: open-codat-io-expenses-api
- collection_type: open
  name: Codat Accounting Integrations API
  slug: open-codat-io-integrations-api
- collection_type: open
  name: Codat Accounting Lending API
  slug: open-codat-io-lending-api
- collection_type: open
  name: Codat Accounting Manage data API
  slug: open-codat-io-manage-data-api
- collection_type: open
  name: Codat Accounting Payables API
  slug: open-codat-io-payables-api
- collection_type: open
  name: Codat Accounting Sync for Commerce API
  slug: open-codat-io-sync-for-commerce-api
- collection_type: open
  name: Codat Accounting Webhooks API
  slug: open-codat-io-webhooks-api
- collection_type: open
  name: Codat API
  slug: open-codat-io
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/codat-io-capability-edges.yml
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


  Codat''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Codat Io Plans Pricing
  plan_count: 3
  slug: codat-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Codat Io Rate Limits
  slug: codat-io-rate-limits
score:
  band: thin
  composite: 35.9
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
    contract_quality: 52.4
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.9
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
