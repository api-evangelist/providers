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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Campfire Hq Agentic Access
  operation_count: 43
  slug: campfire-hq-agentic-access
  summary_line: 43 operations · 17 acting
api_count: 12
apis:
- description: The Accounts Payable API from Campfire — 2 operation(s) for accounts payable.
  name: Campfire Accounts Payable API
  slug: campfire-hq-accounts-payable-api
- description: The Accounts Receivable API from Campfire — 3 operation(s) for accounts receivable.
  name: Campfire Accounts Receivable API
  slug: campfire-hq-accounts-receivable-api
- description: The Bank Reconciliation API from Campfire — 1 operation(s) for bank reconciliation.
  name: Campfire Bank Reconciliation API
  slug: campfire-hq-bank-reconciliation-api
- description: The Cash Management API from Campfire — 2 operation(s) for cash management.
  name: Campfire Cash Management API
  slug: campfire-hq-cash-management-api
- description: The coa API from Campfire — 1 operation(s) for coa.
  name: Campfire coa API
  slug: campfire-hq-coa-api
- description: The Company Objects API from Campfire — 2 operation(s) for company objects.
  name: Campfire Company Objects API
  slug: campfire-hq-company-objects-api
- description: The Core Accounting API from Campfire — 4 operation(s) for core accounting.
  name: Campfire Core Accounting API
  slug: campfire-hq-core-accounting-api
- description: The Custom Fields API from Campfire — 1 operation(s) for custom fields.
  name: Campfire Custom Fields API
  slug: campfire-hq-custom-fields-api
- description: The Financial Statements API from Campfire — 6 operation(s) for financial statements.
  name: Campfire Financial Statements API
  slug: campfire-hq-financial-statements-api
- description: The Integrations API from Campfire — 2 operation(s) for integrations.
  name: Campfire Integrations API
  slug: campfire-hq-integrations-api
- description: The Revenue Recognition API from Campfire — 3 operation(s) for revenue recognition.
  name: Campfire Revenue Recognition API
  slug: campfire-hq-revenue-recognition-api
- description: The Settings API from Campfire — 2 operation(s) for settings.
  name: Campfire Settings API
  slug: campfire-hq-settings-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Campfire Developer APIs Accounts Payable API
  slug: open-campfire-hq-accounts-payable-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Accounts Receivable API
  slug: open-campfire-hq-accounts-receivable-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Bank Reconciliation API
  slug: open-campfire-hq-bank-reconciliation-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Cash Management API
  slug: open-campfire-hq-cash-management-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable coa API
  slug: open-campfire-hq-coa-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Company Objects API
  slug: open-campfire-hq-company-objects-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Core Accounting API
  slug: open-campfire-hq-core-accounting-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Custom Fields API
  slug: open-campfire-hq-custom-fields-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Financial Statements API
  slug: open-campfire-hq-financial-statements-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Integrations API
  slug: open-campfire-hq-integrations-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Revenue Recognition API
  slug: open-campfire-hq-revenue-recognition-api
- collection_type: open
  name: Campfire Developer APIs Accounts Payable Settings API
  slug: open-campfire-hq-settings-api
- collection_type: open
  name: Campfire Developer APIs
  slug: open-campfire-hq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/campfire-hq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/campfire-hq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/campfire-hq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meetcampfire
- group: company
  title: ''
  type: Website
  url: https://www.campfire.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.campfire.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/campfire-hq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/campfire-hq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/campfire-hq-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://campfire.ai/rss.xml
created: '2026-07-01'
description: Campfire is an AI-native ERP and accounting platform for high-growth startups and mid-market companies, unifying the general ledger, revenue recognition, accounts payable/receivable, reporting, and close management. Its "Ember" AI assistant automates transaction categorization, bank reconciliation, and revenue recognition. Campfire ships a documented REST developer API (api.meetcampfire.com) for custom accounting integrations and webhook-driven sync with tools like Stripe, Ramp, and Brex.
finops:
- name: Campfire Hq Finops
  service_category: Business Applications
  slug: campfire-hq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/campfire-hq.png
layout: provider
modified: '2026-07-01'
name: Campfire
nav: Providers
network: true
overview: 'Campfire publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Accounts Receivable API, Bank Reconciliation API, and 9 more. Tagged areas include Accounting, ERP, General Ledger, Revenue Recognition, and Fintech.


  Campfire''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Campfire Hq Plans Pricing
  plan_count: 2
  slug: campfire-hq-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Campfire Hq Rate Limits
  slug: campfire-hq-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/campfire-hq/refs/heads/main/screenshots/campfire-hq-2026-07-25T204316.png
security:
- kind: authentication
  name: Campfire Hq Authentication
  slug: campfire-hq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Campfire Hq Domain Security
  slug: campfire-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: campfire-hq
tags:
- Accounting
- ERP
- General Ledger
- Revenue Recognition
- Fintech
- Artificial Intelligence
website: https://www.campfire.ai/
---
