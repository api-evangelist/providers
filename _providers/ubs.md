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
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: 'UBS''s EU PSD2-compliant open banking API set covering Account Information Services (AIS), Payment Initiation Services (PIS), and Confirmation of Funds (CoF). Used by licensed third-party providers to '
  name: UBS PSD2 API
  slug: psd2
- description: 'The UBS key4 mortgages API lets property platforms and brokers embed Swiss mortgage origination, affordability checks, and indicative financing into their own customer journeys. Reference integration '
  name: UBS key4 Mortgages API
  slug: key4-mortgages
- description: A free programmatic QR-bill creation service supporting the Swiss QR payment standard. Returns QR bills in multiple output formats for invoicing and accounts-receivable use cases.
  name: UBS QR Portal API
  slug: qr-portal
- description: UBS integration with TWINT, the Swiss mobile payment scheme, exposing merchant and consumer payment flows for in-app and point-of-sale checkout.
  name: UBS TWINT API
  slug: twint
- description: bLink is the open banking platform for UBS corporate clients, exposing account information, transaction history, and payment submission so ERPs, accounting software, and treasury management systems ca
  name: UBS bLink API
  slug: blink
- description: UBS Partner and KeyPort form the enterprise integration surface used by partner banks, external asset managers (EAMs), and corporate clients to embed UBS wealth-management, custody, and banking capabi
  name: UBS Partner / KeyPort API
  slug: partner-keyport
- description: The umbrella UBS Banking Ecosystem exposes APIs around the broader retail and private banking surface, covering account, transaction, and product-data services beyond the dedicated mortgage, QR, PSD2,
  name: UBS Banking Ecosystem API
  slug: banking-ecosystem
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubs-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UBS-AG
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubs
- group: company
  title: ''
  type: Website
  url: https://www.ubs.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.ubs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ubs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ubs.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://developer.ubs.com/blog
- group: operate
  title: ''
  type: Support
  url: https://developer.ubs.com/support
created: '2026-05-05'
description: A Swiss multinational investment bank and financial services company and the world's largest wealth manager. UBS exposes a multi-ecosystem developer platform at developer.ubs.com covering retail banking, mortgages, QR billing, EU PSD2 open banking, Swiss TWINT payments, corporate bLink connectivity, and the enterprise UBS Partner / KeyPort offering.
features:
- description: Seven distinct API ecosystems on developer.ubs.com covering retail banking, mortgages, QR bills, PSD2 open banking, TWINT, corporate bLink, and Partner/KeyPort
  name: Multi-Ecosystem Developer Platform
- description: EU PSD2-compliant Account Information, Payment Initiation, and Confirmation of Funds services for licensed third-party providers
  name: PSD2 Compliance
- description: Free programmatic creation of Swiss QR bills in multiple output formats
  name: Swiss QR-Bill Generation
- description: key4 mortgage APIs allow property platforms to embed Swiss home financing journeys
  name: Embedded Mortgage Origination
- description: bLink connects ERPs and treasury systems directly to UBS corporate accounts
  name: Corporate ERP Connectivity
- description: Swiss mobile payment integration for merchants and consumers
  name: TWINT Mobile Payments
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubs.png
integrations:
- description: Reference property-portal integration of the key4 mortgages API
  name: Homegate.ch
- description: bLink connects to SAP, Abacus, Bexio, and similar Swiss ERP/accounting stacks
  name: ERP and Accounting Systems
- description: Integrations with the TWINT mobile payment scheme for Swiss merchants
  name: TWINT Acceptance
layout: provider
modified: '2026-05-16'
name: UBS
nav: Providers
network: true
overview: 'UBS publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, Wealth Management, Investment Banking, and Open Banking.


  UBS''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, and 4 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubs/refs/heads/main/screenshots/ubs-2026-06-20T195946.png
security:
- kind: domain-security
  name: Ubs Domain Security
  slug: ubs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ubs
tags:
- Financial
- Banks
- Wealth Management
- Investment Banking
- Open Banking
use_cases:
- description: Third-party providers aggregate UBS account data into personal finance and wealth aggregation apps under PSD2
  name: Open Banking Aggregation
- description: Property listing sites embed key4 mortgage affordability checks and pre-qualification
  name: Embedded Mortgages on Property Portals
- description: Accounting and invoicing platforms generate compliant Swiss QR bills via the QR Portal API
  name: Invoicing Automation
- description: Treasury systems consume bLink to view balances and initiate corporate payments
  name: Corporate Cash Management
- description: Partner banks and EAMs use UBS Partner / KeyPort to offer UBS-backed services under their own brand
  name: White-Label Wealth Management
website: https://www.ubs.com/
---
