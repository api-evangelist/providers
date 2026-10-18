---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Open Financial Agentic Access
  operation_count: 39
  slug: open-financial-agentic-access
  summary_line: 39 operations · 21 acting
api_count: 12
apis:
- description: Programmatic creation and management of virtual accounts used as transfer wallets, collection wallets, and collection tools on top of partner-bank infrastructure. Virtual accounts give platforms a uni
  name: Open Zwitch Virtual Accounts API
  slug: virtual-accounts
- description: 'Initiate single or bulk fund transfers from a virtual account to bank beneficiaries over NEFT, IMPS, or RTGS, and inspect transfer status, UTR, and settlement details. Powers vendor payouts, refunds, '
  name: Open Zwitch Transfers API
  slug: transfers
- description: 'Manage the set of bank-account beneficiaries that can be paid from a virtual account. Supports creating beneficiaries, listing, retrieving, updating, and deleting, with optional penny-drop validation '
  name: Open Zwitch Beneficiaries API
  slug: beneficiaries
- description: UPI collect requests, UPI Intent strings, and dynamic UPI QR codes for accepting customer-initiated payments on India's Unified Payments Interface rails. Includes mandate flows and webhook callbacks f
  name: Open Zwitch UPI API
  slug: upi
- description: Layer is Zwitch's hosted payment gateway. A few lines of layer.js render a fully PCI-compliant checkout pop-up that accepts net banking, UPI, credit/debit cards, and wallets. Server-side APIs create p
  name: Open Layer Payment Gateway API
  slug: layer
- description: Identity and account-validation suite used during merchant onboarding, KYB, and pre-payout checks. Endpoints cover PAN verification, name matching, bank-account validation (standard and pennyless), an
  name: Open Zwitch Verification API
  slug: verification
- description: Configure split-settlement rules so that incoming payments are automatically apportioned across multiple beneficiary accounts at settlement time. Used by marketplaces, aggregators, and platforms handl
  name: Open Zwitch Split Settlements API
  slug: settlements
- description: Real-time event delivery for payment, transfer, refund, settlement, virtual-account, and verification lifecycle events, with HMAC signature verification and configurable retry policies.
  name: Open Zwitch Webhooks
  slug: webhooks
- description: 'No-code hosted payment pages and payment links that small businesses can share over email, SMS, or WhatsApp to collect one-time or recurring payments without writing integration code. Server APIs let '
  name: Open Zwitch Payment Pages API
  slug: payment-pages
- description: Open's flagship SMB neobanking application. Connects one or more partner-bank current accounts (ICICI, SBI, Axis Bank, Yes Bank, and others) and layers on bill and invoice management, vendor payments,
  name: Open Connected Banking Platform
  slug: connected-banking
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Accounts API from Open (open.money) — 8 operation(s) for accounts.
  name: Open (open.money) Accounts API
  slug: open-financial-accounts-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Constants API from Open (open.money) — 4 operation(s) for constants.
  name: Open (open.money) Constants API
  slug: open-financial-constants-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Events API from Open (open.money) — 1 operation(s) for events.
  name: Open (open.money) Events API
  slug: open-financial-events-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Icp API from Open (open.money) — 1 operation(s) for icp.
  name: Open (open.money) Icp API
  slug: open-financial-icp-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Kycs API from Open (open.money) — 4 operation(s) for kycs.
  name: Open (open.money) Kycs API
  slug: open-financial-kycs-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Pg API from Open (open.money) — 2 operation(s) for pg.
  name: Open (open.money) Pg API
  slug: open-financial-pg-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Pg Settlements API from Open (open.money) — 2 operation(s) for pg settlements.
  name: Open (open.money) Pg Settlements API
  slug: open-financial-pg-settlements-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Refund API from Open (open.money) — 2 operation(s) for refund.
  name: Open (open.money) Refund API
  slug: open-financial-refund-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Transfers API from Open (open.money) — 4 operation(s) for transfers.
  name: Open (open.money) Transfers API
  slug: open-financial-transfers-api
- baseURL: https://api.zwitch.io/v1
  baseurl_source: declared
  description: The Verifications API from Open (open.money) — 1 operation(s) for verifications.
  name: Open (open.money) Verifications API
  slug: open-financial-verifications-api
artifact_total: 24
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/agentic-access/open-financial-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/open-financial-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/rules/open-financial-rules.yml
  title: ''
  type: Spectral
  url: rules/open-financial-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/errors/open-financial-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/open-financial-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/conformance/open-financial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/open-financial-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/llms/open-financial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/open-financial-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/well-known/open-financial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/open-financial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/hosts/open-financial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/open-financial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/vendors/open-financial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/open-financial-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.open.money/support/home
- group: company
  title: ''
  type: Newsroom
  url: https://open.money/company/press
- group: start
  title: ''
  type: Login
  url: https://app.open.money/login
- group: other
  title: ''
  type: Leadership
  url: https://open.money/company/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/authentication/open-financial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/open-financial-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/security/open-financial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/open-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.money/
- group: company
  title: ''
  type: Website
  url: https://www.zwitch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zwitch.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bankopen.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zwitch.io/reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zwitch.io/reference/authorization
- group: start
  title: ''
  type: Console
  url: https://app.zwitch.io/
- group: start
  title: ''
  type: Signup
  url: https://app.zwitch.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bankopen
- group: company
  title: ''
  type: Blog
  url: https://open.money/blog
- group: company
  title: ''
  type: Blog
  url: https://www.zwitch.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://open.money/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zwitch.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.money/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://open.money/privacy
created: '2026-05-24'
description: Open is one of India's leading SMB neobanks, pioneering "connected banking" - a unified business finance platform that layers payments, automated reconciliation, accounting, payroll, expense management, vendor payouts, and GST-compliant invoicing on top of partner-bank current accounts (ICICI, SBI, Axis Bank, Yes Bank and 20+ others). Beyond its SMB application, Open also ships an embedded-finance / Banking-as-a-Service stack branded as Zwitch (zwitch.io), which exposes the same connected-banking primitives - virtual accounts, payouts via NEFT/IMPS/RTGS, UPI collect and intent flows, the Layer hosted payment gateway, beneficiary management, PAN/bank/VPA verification, webhooks, and split settlements - as REST APIs for fintechs and platforms that want to embed account-to-account payments and Indian payment rails into their own products. Open's broader portfolio also includes BankingStack (white-label connected banking for partner banks), the Open Capital lending product, and a
  suite of e-commerce plugins (WooCommerce, Magento, OpenCart, PrestaShop, CS-Cart, WHMCS) plus PHP, Java, Node.js, iOS, and Android SDKs for the Layer payment gateway.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-financial.png
layout: provider
modified: '2026-05-24'
name: Open (open.money)
nav: Providers
network: true
overview: 'Open (open.money) publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Constants API, Events API, and 17 more. Tagged areas include Connected Banking, Neobank, Small Business, Embedded Finance, and Banking as a Service.


  The Open (open.money) catalog on APIs.io includes 1 Spectral governance ruleset.


  Open (open.money)''s developer surface includes support, authentication, documentation, getting-started guide, developer console, signup flow, GitHub presence, and 22 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Open (open.money) API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 3
  slug: open-financial-rules
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.8
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 54.8
    discoverability: 76.8
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 25.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 19.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/screenshots/open-financial-2026-06-20T190743.png
security:
- kind: authentication
  name: Open Financial Authentication
  slug: open-financial-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Open Financial Domain Security
  slug: open-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-financial
tags:
- Connected Banking
- Neobank
- Small Business
- Embedded Finance
- Banking as a Service
- Payments
- Payouts
- UPI
- Accounting
- Payroll
- Expense Management
- India
- Fintech
website: https://open.money/
---
