---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 12
apis:
- description: Dedicated API for PIX instant payment infrastructure in Brazil. Supports immediate charge creation via QR codes, payment receipt confirmation, and real-time notifications for PIX transactions.
  name: PagBank PIX API
  slug: pagbank-pix-api
- description: Subscription billing API for managing recurring charges. Handles subscription creation, billing cycles, payment method updates, and recurring payment indicators for installment plans.
  name: PagBank Recurring Payments API
  slug: pagbank-recurring-payments-api
- description: Boleto Bancário issuance and collection. Generates a printable / scannable boleto tied to an Order, with status callbacks once the buyer pays at a bank, lottery house, or via internet banking.
  name: PagBank Boleto API
  slug: boleto
- description: Payment-division (split) settlement for marketplaces and platforms. Splits a single charge across multiple receivers (with optional custody / release control) so each seller is settled directly by Pag
  name: PagBank Marketplace / Split API
  slug: split
- description: Electronic Data Interchange surface for downloading transaction and settlement statements for reconciliation — a structured replacement for manual CSV/PDF statement processing.
  name: PagBank EDI API
  slug: edi
- description: Issues digital certificates for mTLS authentication, layered on top of bearer-token auth for higher-trust integrations and sensitive payouts / Pix Bacen flows.
  name: PagBank Digital Certificate (mTLS) API
  slug: certificates
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Accounts API from PagBank — 2 operation(s) for accounts.
  name: PagBank Accounts API
  slug: pagbank-accounts-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Charges API from PagBank — 4 operation(s) for charges.
  name: PagBank Charges API
  slug: pagbank-charges-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Checkout API from PagBank — 4 operation(s) for checkout.
  name: PagBank Checkout API
  slug: pagbank-checkout-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Connect API from PagBank — 6 operation(s) for connect.
  name: PagBank Connect API
  slug: pagbank-connect-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Coupons API from PagBank — 2 operation(s) for coupons.
  name: PagBank Coupons API
  slug: pagbank-coupons-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Invoices API from PagBank — 2 operation(s) for invoices.
  name: PagBank Invoices API
  slug: pagbank-invoices-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Orders API from PagBank — 2 operation(s) for orders.
  name: PagBank Orders API
  slug: pagbank-orders-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Plans API from PagBank — 4 operation(s) for plans.
  name: PagBank Plans API
  slug: pagbank-plans-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Public Keys API from PagBank — 2 operation(s) for public keys.
  name: PagBank Public Keys API
  slug: pagbank-public-keys-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Refunds API from PagBank — 2 operation(s) for refunds.
  name: PagBank Refunds API
  slug: pagbank-refunds-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Subscribers API from PagBank — 3 operation(s) for subscribers.
  name: PagBank Subscribers API
  slug: pagbank-subscribers-api
- baseURL: https://api.pagseguro.com
  baseurl_source: declared
  description: The Subscriptions API from PagBank — 5 operation(s) for subscriptions.
  name: PagBank Subscriptions API
  slug: pagbank-subscriptions-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/pagbank/capabilities/pagbank-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pagbank-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/pagbank/security/pagbank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagbank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pagbank.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pagbank.com.br/docs/apis-pagbank
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pagbank.com.br/docs/primeiros-passos
- group: docs
  title: ''
  type: APIReference
  url: https://developer.pagbank.com.br/reference/introducao
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/pagseguro/
- group: company
  title: ''
  type: Blog
  url: https://developer.pagbank.com.br/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://pagbank.com.br/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pagbank.com.br/
- group: other
  title: ''
  type: X
  url: https://twitter.com/PagBank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pagbank
- group: commercial
  href: https://artifacts.apis.io/pagbank/plans/pagbank-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pagbank-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pagbank/rate-limits/pagbank-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pagbank-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pagbank/finops/pagbank-finops.yml
  title: ''
  type: FinOps
  url: finops/pagbank-finops.yml
created: '2026-06-13'
description: PagBank (formerly PagSeguro) is a Brazilian digital bank and payment platform operated by PagoSeguro Internet Instituição de Pagamento S/A, a subsidiary of Universo Online (UOL). It provides REST APIs for Pix instant transfers, credit and debit card processing, e-commerce checkout, boleto bancário, recurring payments, POS terminal integration, and financial account management. PagBank serves e-commerce merchants, SaaS platforms, and marketplaces across Brazil and supports over 29.5 million customers.
finops:
- has_sources: false
  method: generated
  name: Pagbank Finops
  primary_unit: ''
  service_category: ''
  slug: pagbank-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pagbank.png
layout: provider
modified: '2026-06-13'
name: PagBank
nav: Providers
network: true
overview: 'PagBank publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Charges API, Checkout API, and 15 more. Tagged areas include Payments, Digital Banking, Brazil, Pix, and Fintech.


  The PagBank catalog on APIs.io includes 1 Spectral governance ruleset.


  PagBank''s developer surface includes documentation, getting-started guide, API reference, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Pagbank Plans Pricing
  plan_count: 2
  slug: pagbank-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Pagbank Rate Limits
  slug: pagbank-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: PagBank API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: pagbank-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 45.3
    developer_ergonomics: 27.4
    discoverability: 71.4
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 28.4
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pagbank/pagbank-2026-06-20T191323.png
security:
- kind: domain-security
  name: Pagbank Domain Security
  slug: pagbank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pagbank
tags:
- Payments
- Digital Banking
- Brazil
- Pix
- Fintech
- E-Commerce
- Point-of-Sale
- Recurring Payments
- Boleto
website: https://pagbank.com.br/
---
