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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Lexoffice Agentic Access
  operation_count: 35
  slug: lexoffice-agentic-access
  summary_line: 35 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Customers and vendors.
  name: lexoffice Contacts API
  slug: lexoffice-contacts-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Credit note documents.
  name: lexoffice Credit Notes API
  slug: lexoffice-credit-notes-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Delivery note documents.
  name: lexoffice Delivery Notes API
  slug: lexoffice-delivery-notes-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Down payment invoice documents.
  name: lexoffice Down Payment Invoices API
  slug: lexoffice-down-payment-invoices-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Payment reminder documents.
  name: lexoffice Dunnings API
  slug: lexoffice-dunnings-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Webhook subscriptions for change events.
  name: lexoffice Event Subscriptions API
  slug: lexoffice-event-subscriptions-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: File upload and download for voucher receipts.
  name: lexoffice Files API
  slug: lexoffice-files-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Outgoing invoices.
  name: lexoffice Invoices API
  slug: lexoffice-invoices-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Order confirmation documents.
  name: lexoffice Order Confirmations API
  slug: lexoffice-order-confirmations-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Payment status for a voucher and payment conditions.
  name: lexoffice Payments API
  slug: lexoffice-payments-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Account profile and reference metadata.
  name: lexoffice Profile API
  slug: lexoffice-profile-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Sales quotations / offers.
  name: lexoffice Quotations API
  slug: lexoffice-quotations-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Templates that generate recurring invoices.
  name: lexoffice Recurring Templates API
  slug: lexoffice-recurring-templates-api
- baseURL: https://api.lexware.io/v1
  baseurl_source: declared
  description: Bookkeeping vouchers and the voucherlist search.
  name: lexoffice Vouchers API
  slug: lexoffice-vouchers-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts API
  slug: open-lexoffice-contacts-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Credit Notes API
  slug: open-lexoffice-credit-notes-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Delivery Notes API
  slug: open-lexoffice-delivery-notes-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Down Payment Invoices API
  slug: open-lexoffice-down-payment-invoices-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Dunnings API
  slug: open-lexoffice-dunnings-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Event Subscriptions API
  slug: open-lexoffice-event-subscriptions-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Files API
  slug: open-lexoffice-files-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Invoices API
  slug: open-lexoffice-invoices-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Order Confirmations API
  slug: open-lexoffice-order-confirmations-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Payments API
  slug: open-lexoffice-payments-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Profile API
  slug: open-lexoffice-profile-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Quotations API
  slug: open-lexoffice-quotations-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Recurring Templates API
  slug: open-lexoffice-recurring-templates-api
- collection_type: open
  name: lexoffice (lexware Office) Public Contacts Vouchers API
  slug: open-lexoffice-vouchers-api
- collection_type: open
  name: lexoffice (lexware Office) Public API
  slug: open-lexoffice
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lexoffice-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lexoffice-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lexoffice-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lexware
- group: company
  title: ''
  type: Website
  url: https://www.lexware.de/lexware-office/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lexware.io/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/lexoffice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lexoffice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lexoffice-finops.yml
created: '2026-07-12'
description: lexoffice (rebranded to "lexware Office" in 2025) is a German cloud accounting, invoicing, and bookkeeping SaaS from Lexware (Haufe Group). Its public REST API lets developers push and pull business data - contacts, invoices, quotations, order confirmations, delivery notes, credit notes, dunnings, bookkeeping vouchers, files, payments, and profile metadata - and subscribe to webhooks via event subscriptions. Authentication is a self-serve Bearer API key. The API gateway moved from api.lexoffice.io to api.lexware.io on 26 May 2025 as part of the rebrand; the legacy host remained available through December 2025.
finops:
- name: Lexoffice Finops
  service_category: Accounting and Invoicing Software
  slug: lexoffice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lexoffice.png
layout: provider
modified: '2026-07-12'
name: lexoffice
nav: Providers
network: true
overview: 'lexoffice publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Credit Notes API, Delivery Notes API, and 11 more. Tagged areas include Accounting, Invoicing, Bookkeeping, Finance, and Germany.


  lexoffice''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Lexoffice Plans Pricing
  plan_count: 4
  slug: lexoffice-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Lexoffice Rate Limits
  slug: lexoffice-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lexoffice/refs/heads/main/screenshots/lexoffice-2026-07-25T225004.png
security:
- kind: authentication
  name: Lexoffice Authentication
  slug: lexoffice-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lexoffice Domain Security
  slug: lexoffice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lexoffice
tags:
- Accounting
- Invoicing
- Bookkeeping
- Finance
- Germany
- Vouchers
- Contacts
- Software-as-a-Service
- Financial Software
website: https://www.lexware.de/lexware-office/
---
