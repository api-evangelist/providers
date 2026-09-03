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
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 10
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
artifact_total: 11
common:
- group: auth
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
  type: LinkedIn
  url: https://www.linkedin.com/company/bankopen
- group: other
  title: ''
  type: X
  url: https://x.com/bankopen
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
overview: 'Open (open.money) publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Connected Banking, Neobank, SMB, Embedded Finance, and Banking as a Service.


  Open (open.money)''s developer surface includes documentation, getting-started guide, authentication, developer console, signup flow, GitHub presence, engineering blog, and 11 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 25.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-financial/refs/heads/main/screenshots/open-financial-2026-06-20T190743.png
security:
- kind: domain-security
  name: Open Financial Domain Security
  slug: open-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-financial
tags:
- Connected Banking
- Neobank
- SMB
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
