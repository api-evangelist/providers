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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Sevdesk Agentic Access
  operation_count: 30
  slug: sevdesk-agentic-access
  summary_line: 30 operations · 13 acting
api_count: 1
apis:
- description: Bank and clearing check accounts.
  name: sevdesk CheckAccount API
  slug: sevdesk-checkaccount-api
- description: Transactions booked against a check account.
  name: sevdesk CheckAccountTransaction API
  slug: sevdesk-checkaccounttransaction-api
- description: Contacts - customers, suppliers, and other business partners.
  name: sevdesk Contact API
  slug: sevdesk-contact-api
- description: Credit notes issued to contacts.
  name: sevdesk CreditNote API
  slug: sevdesk-creditnote-api
- description: Outgoing invoices and their lifecycle.
  name: sevdesk Invoice API
  slug: sevdesk-invoice-api
- description: Orders, quotations, and packing lists.
  name: sevdesk Order API
  slug: sevdesk-order-api
- description: Parts / articles with stock (inventory).
  name: sevdesk Part API
  slug: sevdesk-part-api
- description: Tags and tag relations used to label resources.
  name: sevdesk Tag API
  slug: sevdesk-tag-api
- description: Vouchers (receipts) used for expense and revenue bookkeeping.
  name: sevdesk Voucher API
  slug: sevdesk-voucher-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: sevdesk CheckAccount API
  slug: open-sevdesk-checkaccount-api
- collection_type: open
  name: sevdesk CheckAccount CheckAccountTransaction API
  slug: open-sevdesk-checkaccounttransaction-api
- collection_type: open
  name: sevdesk CheckAccount Contact API
  slug: open-sevdesk-contact-api
- collection_type: open
  name: sevdesk CheckAccount CreditNote API
  slug: open-sevdesk-creditnote-api
- collection_type: open
  name: sevdesk CheckAccount Invoice API
  slug: open-sevdesk-invoice-api
- collection_type: open
  name: sevdesk CheckAccount Order API
  slug: open-sevdesk-order-api
- collection_type: open
  name: sevdesk CheckAccount Part API
  slug: open-sevdesk-part-api
- collection_type: open
  name: sevdesk CheckAccount Tag API
  slug: open-sevdesk-tag-api
- collection_type: open
  name: sevdesk CheckAccount Voucher API
  slug: open-sevdesk-voucher-api
- collection_type: open
  name: sevdesk API
  slug: open-sevdesk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sevdesk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sevdesk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sevdesk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sevdesk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sevdesk
- group: company
  title: ''
  type: Website
  url: https://sevdesk.de
- group: docs
  title: ''
  type: Documentation
  url: https://api.sevdesk.de/
- group: commercial
  title: ''
  type: Plans
  url: plans/sevdesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sevdesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sevdesk-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://tech.sevdesk.com/
created: '2026-07-12'
description: sevdesk is a German cloud accounting, invoicing, and bookkeeping platform for freelancers and small businesses. Its RESTful API (base https://my.sevdesk.de/api/v1) exposes everything the web application does - contacts, invoices, orders, credit notes, vouchers (receipts), bank check accounts and transactions, parts (inventory), tags, plus DATEV and CSV exports - authenticated with a per-administrator API token passed in the Authorization header. Nested resources can be pulled in with the embed query parameter.
finops:
- name: Sevdesk Finops
  service_category: Business Software - Accounting and Invoicing
  slug: sevdesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sevdesk.png
layout: provider
modified: '2026-07-12'
name: sevdesk
nav: Providers
network: true
overview: 'sevdesk publishes 9 APIs on the [APIs.io](https://apis.io/) network, including CheckAccount API, CheckAccountTransaction API, Contact API, and 6 more. Tagged areas include Accounting, Invoicing, Bookkeeping, Finance, and Germany.


  sevdesk''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sevdesk Plans Pricing
  plan_count: 5
  slug: sevdesk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Sevdesk Rate Limits
  slug: sevdesk-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Sevdesk Authentication
  slug: sevdesk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sevdesk Domain Security
  slug: sevdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sevdesk
tags:
- Accounting
- Invoicing
- Bookkeeping
- Finance
- Germany
- Vouchers
- Contacts
- Software-as-a-Service
- ERP
- Financial Software
website: https://sevdesk.de
---
