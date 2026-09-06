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
  - '{''url'': ''https://www.octobat.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.mirakl.com/ — a different registrable domain (octobat.com -> mirakl.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Octobat Agentic Access
  operation_count: 48
  slug: octobat-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 1
apis:
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Discount coupons for invoices and subscriptions.
  name: Octobat Coupons API
  slug: octobat-coupons-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Compliant credit notes issued against invoices.
  name: Octobat Credit Notes API
  slug: octobat-credit-notes-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Customers and their billing / tax details.
  name: Octobat Customers API
  slug: octobat-customers-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Compliant invoices, their items, and lifecycle actions.
  name: Octobat Invoices API
  slug: octobat-invoices-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Settlement payouts and their balance transactions.
  name: Octobat Payouts API
  slug: octobat-payouts-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Products and their tax categorization.
  name: Octobat Products API
  slug: octobat-products-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Recurring-billing subscriptions and metered usage.
  name: Octobat Subscriptions API
  slug: octobat-subscriptions-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Real-time tax determination for customers and carts / checkouts.
  name: Octobat Tax Evidence API
  slug: octobat-tax-evidence-api
- baseURL: https://apiv2.octobat.com
  baseurl_source: declared
  description: Payments registered against invoices for reconciliation and tax reporting.
  name: Octobat Transactions API
  slug: octobat-transactions-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Octobat Coupons API
  slug: open-octobat-coupons-api
- collection_type: open
  name: Octobat Coupons Credit Notes API
  slug: open-octobat-credit-notes-api
- collection_type: open
  name: Octobat Coupons Customers API
  slug: open-octobat-customers-api
- collection_type: open
  name: Octobat Coupons Invoices API
  slug: open-octobat-invoices-api
- collection_type: open
  name: Octobat Coupons Payouts API
  slug: open-octobat-payouts-api
- collection_type: open
  name: Octobat Coupons Products API
  slug: open-octobat-products-api
- collection_type: open
  name: Octobat Coupons Subscriptions API
  slug: open-octobat-subscriptions-api
- collection_type: open
  name: Octobat Coupons Tax Evidence API
  slug: open-octobat-tax-evidence-api
- collection_type: open
  name: Octobat Coupons Transactions API
  slug: open-octobat-transactions-api
- collection_type: open
  name: Octobat API
  slug: open-octobat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octobat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octobat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octobat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0ctobat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octobat
- group: company
  title: ''
  type: Website
  url: https://www.octobat.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octobat.com
- group: commercial
  title: ''
  type: Plans
  url: plans/octobat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/octobat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/octobat-finops.yml
created: '2026-07-03'
description: Octobat is a billing, invoicing, and tax-compliance platform for online businesses. It automates the creation, delivery, and storage of legally compliant invoices, credit notes, self-billing invoices, and tax receipts for every online transaction, and provides a real-time tax (VAT / GST / sales tax) determination engine for tax-exclusive and tax-inclusive billing models. Octobat integrates with Stripe, GoCardless, and other payment providers, and exposes a Stripe-style REST API at base URL https://apiv2.octobat.com authenticated with HTTP Basic (secret key). Octobat also ships Beanie (a hosted checkout) and Plaza (marketplace / platform tax and invoicing for connected accounts). Operating status - Octobat was acquired by Mirakl in November 2021; the standalone marketing site (octobat.com) now redirects to mirakl.com, while the developer documentation at docs.octobat.com and the apiv2.octobat.com API remain available to existing integrators.
finops:
- name: Octobat Finops
  service_category: Billing and Tax Compliance
  slug: octobat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octobat.png
layout: provider
modified: '2026-07-03'
name: Octobat
nav: Providers
network: true
overview: 'Octobat publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Coupons API, Credit Notes API, Customers API, and 6 more. Tagged areas include Billing, Invoicing, Tax Compliance, VAT, and E-Commerce.


  Octobat''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Octobat Plans Pricing
  plan_count: 4
  slug: octobat-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Octobat Rate Limits
  slug: octobat-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
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
    contract_quality: 48.7
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octobat/refs/heads/main/screenshots/octobat-2026-08-07T185941.png
security:
- kind: authentication
  name: Octobat Authentication
  slug: octobat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octobat Domain Security
  slug: octobat-domain-security
  summary_line: TLSv1.3 · HSTS
slug: octobat
tags:
- Billing
- Invoicing
- Tax Compliance
- VAT
- E-Commerce
- Payments
- Fintech
website: https://www.octobat.com
---
