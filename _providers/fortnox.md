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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Fortnox Agentic Access
  operation_count: 42
  slug: fortnox-agentic-access
  summary_line: 42 operations · 21 acting
api_count: 1
apis:
- description: Duplex WebSocket stream at wss://ws.fortnox.se/topics-v1 that pushes minimal change-notification events across domains (invoices, supplier-invoices, customers, articles, orders, offers, vouchers, proj
  name: Fortnox Topics WebSocket API
  slug: fortnox-topics-websocket-api
- description: Chart of accounts.
  name: Fortnox Accounts API
  slug: fortnox-accounts-api
- description: Article (product/service) register.
  name: Fortnox Articles API
  slug: fortnox-articles-api
- description: Customer register.
  name: Fortnox Customers API
  slug: fortnox-customers-api
- description: Financial (accounting) years.
  name: Fortnox Financial Years API
  slug: fortnox-financial-years-api
- description: Accounts-receivable customer invoices.
  name: Fortnox Invoices API
  slug: fortnox-invoices-api
- description: Offers (quotations).
  name: Fortnox Offers API
  slug: fortnox-offers-api
- description: Sales orders.
  name: Fortnox Orders API
  slug: fortnox-orders-api
- description: Projects for tagging and reporting.
  name: Fortnox Projects API
  slug: fortnox-projects-api
- description: Inbound accounts-payable supplier invoices.
  name: Fortnox Supplier Invoices API
  slug: fortnox-supplier-invoices-api
- description: Supplier register.
  name: Fortnox Suppliers API
  slug: fortnox-suppliers-api
- description: Accounting vouchers (journal entries).
  name: Fortnox Vouchers API
  slug: fortnox-vouchers-api
artifact_total: 33
asyncapis:
- description: AsyncAPI 2.6 description of Fortnox's **real duplex WebSocket API** at `wss://ws.fortnox.se/topics-v1` (the "Topics" service). Unlike the REST API at https://api.fortnox.se/3/, this is a genuine WebSo
  name: Fortnox Topics WebSocket API
  slug: fortnox-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts API
  slug: open-fortnox-accounts-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Articles API
  slug: open-fortnox-articles-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Customers API
  slug: open-fortnox-customers-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Financial Years API
  slug: open-fortnox-financial-years-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Invoices API
  slug: open-fortnox-invoices-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Offers API
  slug: open-fortnox-offers-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Orders API
  slug: open-fortnox-orders-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Projects API
  slug: open-fortnox-projects-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Supplier Invoices API
  slug: open-fortnox-supplier-invoices-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Suppliers API
  slug: open-fortnox-suppliers-api
- collection_type: open
  name: Fortnox REST API (Representative Subset) Accounts Vouchers API
  slug: open-fortnox-vouchers-api
- collection_type: open
  name: Fortnox REST API
  slug: open-fortnox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fortnox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortnox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fortnox-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fortnox-ab
- group: company
  title: ''
  type: Website
  url: https://www.fortnox.se
- group: docs
  title: ''
  type: Documentation
  url: https://www.fortnox.se/developer
- group: commercial
  title: ''
  type: Plans
  url: plans/fortnox-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fortnox-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fortnox-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fortnox.se/developer/blog
created: '2026-07-12'
description: Fortnox is a Swedish cloud accounting, ERP, and business-administration platform for small and medium-sized businesses and accounting bureaus. Its REST API at https://api.fortnox.se/3/ programmatically manages accounting and financial data - invoices, customers, articles, orders, offers, vouchers, accounts, suppliers, supplier invoices, projects, and financial years - authenticated with OAuth2 Authorization Code Flow. Fortnox also publishes a duplex WebSocket event stream at wss://ws.fortnox.se/topics-v1 that pushes minimal change notifications across domains so integrations can react to changes instead of polling.
finops:
- name: Fortnox Finops
  service_category: Business Applications
  slug: fortnox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fortnox.png
layout: provider
modified: '2026-07-12'
name: Fortnox
nav: Providers
network: true
overview: 'Fortnox publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Topics WebSocket API, Accounts API, Articles API, and 9 more. Tagged areas include Accounting, ERP, Invoicing, Bookkeeping, and Sweden.


  The Fortnox catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fortnox''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Fortnox Plans Pricing
  plan_count: 6
  slug: fortnox-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Fortnox Rate Limits
  slug: fortnox-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Fortnox API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: fortnox-asyncapi-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 59.4
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 21.1
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortnox/refs/heads/main/screenshots/fortnox-2026-07-25T215012.png
security:
- kind: authentication
  name: Fortnox Authentication
  slug: fortnox-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Fortnox Domain Security
  slug: fortnox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fortnox
tags:
- Accounting
- ERP
- Invoicing
- Bookkeeping
- Sweden
- Nordics
- Finance
- Vouchers
- Customers
- Software-as-a-Service
website: https://www.fortnox.se
---
