---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Treasury Services API family covering payments (USD clearing, global ACH, RTP, wires, Pay by Bank), liquidity, cash management, trade finance, and FX, exposed to corporate and financial-institution cl
  name: BNY Treasury Services API
  slug: treasury-services-api
- description: Asset Servicing API family for custody, fund accounting, middle-office, and transfer-agency operations, published through the BNY Developer Marketplace. API reference is gated behind Nexen single sign
  name: BNY Asset Servicing API
  slug: asset-servicing-api
- description: Markets API family spanning FX, securities finance, fixed income, and equities, published through the BNY Developer Marketplace. API reference is gated behind Nexen single sign-on; no OpenAPI is publi
  name: BNY Markets API
  slug: markets-api
- description: Pershing API family for clearing, custody, and the NetX360+ / Wove wealth platforms serving broker-dealers and RIAs, published through the BNY Developer Marketplace. API reference is gated behind Nexe
  name: BNY Pershing API
  slug: pershing-api
- description: Public, smart-contract-only product that broadcasts BNY-attested fund accounting data to public blockchains for on-chain and off-chain consumers (first implementation is the BlackRock USD Digital Liqu
  name: BNY Data On-Chain
  slug: data-on-chain
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bnymellon/bny-data-on-chain/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/BNYMellon/bny-data-on-chain/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.bny.com/corporate/global/en/about-us/trust-center.html
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bny-mellon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bny.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bny.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bny.com/app/open/apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bnymellon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-bank-of-new-york-mellon-corporation
- group: operate
  title: ''
  type: Support
  url: https://developer.bny.com/app/open/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bny.com/corporate/global/en/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bny.com/corporate/global/en/data-privacy.html
- group: company
  title: ''
  type: About
  url: https://www.bny.com/corporate/global/en/about-us.html
- group: start
  title: ''
  type: Login
  url: https://developer.bny.com/login
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bny-mellon-sandbox.yml
created: '2026-07-23'
description: BNY Mellon (legal parent The Bank of New York Mellon Corporation, rebranded to "BNY" in 2024) is a US money-center bank and the world's largest custodian, overseeing roughly $50 trillion in assets under custody and/or administration. Its principal banking subsidiary, The Bank of New York Mellon, is a nationally chartered bank (OCC-supervised) headquartered in New York City, operating across Securities Services, Market & Wealth Services, and Investment & Wealth Management with brand families including Pershing, Eagle Investment Systems, and BNY Markets. On open finance, BNY runs a genuine first-party developer program — the BNY Developer Marketplace at developer.bny.com (formerly marketplace.bnymellon.com) — publishing Treasury Services (payments, liquidity, cash management, trade finance, FX), Asset Servicing, Markets, and Pershing API families to corporate, fintech, and financial-institution clients. Registration and full API reference are gated behind Nexen single sign-on,
  and no OpenAPI/Swagger is publicly downloadable. BNY also ships a public, smart-contract-only "Data On-Chain" product that broadcasts fund accounting data to Ethereum. Consumer/business-banking account data is reached primarily through aggregators such as Plaid rather than a first-party consumer data API. No FDX participation or CFPB 1033 posture is publicly documented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: BNY Mellon
nav: Providers
network: true
overview: 'BNY Mellon publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Custody Bank, and Treasury Services.


  BNY Mellon''s developer surface includes documentation, support, sandbox, and 12 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bny-mellon/refs/heads/main/screenshots/bny-mellon-2026-07-25T203518.png
security:
- kind: domain-security
  name: Bny Mellon Domain Security
  slug: bny-mellon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bny-mellon
tags:
- Financial-Services
- Banking
- United States
- Custody Bank
- Treasury Services
- Payments
- Digital Assets
- Open Finance
website: https://www.bny.com
---
