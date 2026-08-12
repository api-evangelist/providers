---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Tabs Fi Agentic Access
  operation_count: 73
  slug: tabs-fi-agentic-access
  summary_line: 73 operations · 33 acting
api_count: 22
apis:
- description: REST API for the Tabs revenue automation platform that exposes the core data model of customers, contracts, items, revenue categories, obligations, invoices, payments, and usage events. The API lets f
  name: Tabs Platform API
  slug: tabs-platform-api
- description: The BillingTerms API from Tabs — 3 operation(s) for billingterms.
  name: Tabs BillingTerms API
  slug: tabs-fi-billingterms-api
- description: The Categories API from Tabs — 3 operation(s) for categories.
  name: Tabs Categories API
  slug: tabs-fi-categories-api
- description: The Commitments API from Tabs — 2 operation(s) for commitments.
  name: Tabs Commitments API
  slug: tabs-fi-commitments-api
- description: The Contracts API from Tabs — 4 operation(s) for contracts.
  name: Tabs Contracts API
  slug: tabs-fi-contracts-api
- description: The CreditMemos API from Tabs — 3 operation(s) for creditmemos.
  name: Tabs CreditMemos API
  slug: tabs-fi-creditmemos-api
- description: The Customers API from Tabs — 5 operation(s) for customers.
  name: Tabs Customers API
  slug: tabs-fi-customers-api
- description: The CustomFields API from Tabs — 1 operation(s) for customfields.
  name: Tabs CustomFields API
  slug: tabs-fi-customfields-api
- description: The Events API from Tabs — 3 operation(s) for events.
  name: Tabs Events API
  slug: tabs-fi-events-api
- description: The EventTypes API from Tabs — 2 operation(s) for eventtypes.
  name: Tabs EventTypes API
  slug: tabs-fi-eventtypes-api
- description: The Invoices API from Tabs — 4 operation(s) for invoices.
  name: Tabs Invoices API
  slug: tabs-fi-invoices-api
- description: The Items API from Tabs — 2 operation(s) for items.
  name: Tabs Items API
  slug: tabs-fi-items-api
- description: The Jobs API from Tabs — 1 operation(s) for jobs.
  name: Tabs Jobs API
  slug: tabs-fi-jobs-api
- description: The Merchant API from Tabs — 1 operation(s) for merchant.
  name: Tabs Merchant API
  slug: tabs-fi-merchant-api
- description: The Obligations API from Tabs — 4 operation(s) for obligations.
  name: Tabs Obligations API
  slug: tabs-fi-obligations-api
- description: The Payments API from Tabs — 3 operation(s) for payments.
  name: Tabs Payments API
  slug: tabs-fi-payments-api
- description: The PerformanceObligations API from Tabs — 4 operation(s) for performanceobligations.
  name: Tabs PerformanceObligations API
  slug: tabs-fi-performanceobligations-api
- description: The Renewals API from Tabs — 1 operation(s) for renewals.
  name: Tabs Renewals API
  slug: tabs-fi-renewals-api
- description: The Reports API from Tabs — 2 operation(s) for reports.
  name: Tabs Reports API
  slug: tabs-fi-reports-api
- description: The Revenue API from Tabs — 1 operation(s) for revenue.
  name: Tabs Revenue API
  slug: tabs-fi-revenue-api
- description: The System API from Tabs — 4 operation(s) for system.
  name: Tabs System API
  slug: tabs-fi-system-api
- description: The UsageEvents API from Tabs — 2 operation(s) for usageevents.
  name: Tabs UsageEvents API
  slug: tabs-fi-usageevents-api
artifact_total: 29
collections:
- collection_type: open
  name: Tabs Platform API
  slug: open-tabs-fi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tabs-fi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tabs-fi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tabs-fi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tabsplatform.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tabs.com/pricing
- group: agent
  title: ''
  type: LLMs
  url: https://docs.tabsplatform.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.tabs.com/blog
created: '2026-05-23'
description: Tabs is an AI-native revenue automation platform for B2B companies, unifying billing, collections, revenue recognition, and reporting on top of a contract-driven data model. The platform ingests executed contracts and automatically generates invoices, schedules ASC 606-compliant revenue, drives collections through AI agents, and produces real-time ARR, cash, and AR reporting. It is designed for finance teams at SaaS and B2B subscription companies who need flexibility across subscription, usage-based, metered, and hybrid billing models. Tabs exposes a REST API and integrates with ERP, CRM, payment, and tax systems so contract, billing, and revenue data can flow into the rest of the finance stack. It is SOC 2 compliant and includes a unified customer record spanning contracts, usage, payments, and terms.
finops:
- name: Tabs Fi Finops
  service_category: API
  slug: tabs-fi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tabs-fi.png
layout: provider
modified: '2026-05-23'
name: Tabs
nav: Providers
network: true
overview: 'Tabs publishes 21 APIs on the [APIs.io](https://apis.io/) network, including BillingTerms API, Categories API, Commitments API, and 18 more. Tagged areas include Tabs, Revenue, Billing, Invoicing, and Accounts Receivable.


  Tabs'' developer surface includes authentication, documentation, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Tabs Fi Plans Pricing
  plan_count: 1
  slug: tabs-fi-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 2
  name: Tabs Fi Rate Limits
  slug: tabs-fi-rate-limits
score:
  band: thin
  composite: 32.8
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tabs-fi/refs/heads/main/screenshots/tabs-fi-2026-06-20T194954.png
security:
- kind: authentication
  name: Tabs Fi Authentication
  slug: tabs-fi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tabs Fi Domain Security
  slug: tabs-fi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tabs-fi
tags:
- Tabs
- Revenue
- Billing
- Invoicing
- Accounts Receivable
- Collections
- Revenue Recognition
- Contracts
- Usage
- Payments
- Subscriptions
- Finance
- B2B
website: https://www.tabs.com/
---
