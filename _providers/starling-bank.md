---
access_model:
  confidence: high
  label: Free · Self-serve developer signup with sandbox
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - authentication
  - documentation
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-12'
api_count: 13
apis:
- description: Bespoke Starling Developer API for retrieving a customer's accounts, account identifiers (sort code / account number), and balances. Served over OAuth2 at the api.starlingbank.com/api/v2 host with a f
  name: Starling Accounts API
  slug: starling-accounts-api
- description: Returns account-holder profile information - the type of account holder (individual, business, joint, sole trader), name, and registered details - from the Starling bespoke Developer API.
  name: Starling Account Holder API
  slug: starling-account-holder-api
- description: The Starling transaction feed (feed items) API exposes real-time transaction activity, feed-item detail, spending categories, receipts, and attachments for an account over the bespoke Developer API.
  name: Starling Transaction Feed API
  slug: starling-transaction-feed-api
- description: Initiate and manage domestic and scheduled payments, payment orders, and standing orders from a Starling account through the bespoke Developer API, secured with OAuth2 and payment scopes.
  name: Starling Payments API
  slug: starling-payments-api
- description: Create, list, and manage payees (beneficiaries) and payee accounts used when initiating payments from a Starling account via the bespoke Developer API.
  name: Starling Payees API
  slug: starling-payees-api
- description: Create and manage Savings Goals (Spaces), add or withdraw money, and round-up transfers within a Starling account through the bespoke Developer API.
  name: Starling Savings Goals API
  slug: starling-savings-goals-api
- description: Retrieve card details and control card settings - enabling or disabling the card and per-feature controls (ATM, online, mobile wallet, magstripe, gambling) - via the Starling bespoke Developer API.
  name: Starling Cards API
  slug: starling-cards-api
- description: List and cancel direct debit mandates on a Starling account through the bespoke Developer API.
  name: Starling Mandates API
  slug: starling-mandates-api
- description: Returns the identity and token/authorising-individual context for the authenticated Starling user, including the scopes granted to the access token, via the bespoke Developer API.
  name: Starling Identity API
  slug: starling-identity-api
- description: UK Open Banking Open Data API - PUBLIC, unauthenticated reference data (personal and business current accounts, and, for banks with a physical estate, ATMs and branches) modelled on the OBIE Open Data
  name: Starling Open Data API (OBIE Standard)
  slug: starling-open-data-api
- description: UK Open Banking Read/Write Account and Transaction Information (AIS) API for accessing account, balance, transaction, and product data as an FCA-authorised ASPSP, conformant to the OBIE Read/Write sta
  name: Starling Account and Transaction Information API (AIS, OBIE Read/Write)
  slug: starling-account-transaction-api
- description: UK Open Banking Read/Write Payment Initiation (PIS) API for initiating domestic and other payments as an FCA-authorised ASPSP, conformant to the OBIE Read/Write standard and secured with FAPI OAuth2/O
  name: Starling Payment Initiation API (PIS, OBIE Read/Write)
  slug: starling-payment-initiation-api
- description: 'UK Open Banking Read/Write Confirmation of Funds (CBPII) API allowing a card-based payment instrument issuer to confirm whether funds are available, as an FCA-authorised ASPSP, conformant to the OBIE '
  name: Starling Confirmation of Funds API (CBPII, OBIE Read/Write)
  slug: starling-confirmation-of-funds-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/starling-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starling-bank-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.starlingbank.com/security/disclosure/
- group: auth
  title: ''
  type: Authentication
  url: authentication/starling-bank-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/starling-bank-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/starling-bank-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/starling-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/starling-bank-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/starling-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starling-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starling-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/starling-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starling-bank-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/starling-bank-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starling-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/starling-bank-opendata-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.starlingbank.com/docs
- group: company
  title: ''
  type: Website
  url: https://www.starlingbank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.starlingbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.starlingbank.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.starlingbank.com/docs/getting-started
- group: other
  title: ''
  type: OpenBanking
  url: https://developer.starlingbank.com/docs/open-banking
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starlingbank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/starling-bank
- group: company
  title: ''
  type: Blog
  url: https://www.starlingbank.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://starlingbank.statuspage.io/
- group: operate
  title: ''
  type: Support
  url: https://developer.starlingbank.com/community
- group: auth
  title: ''
  type: Compliance
  url: https://www.starlingbank.com/current-account/service-information/api-performance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.starlingbank.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.starlingbank.com/legal/privacy-notice/
created: '2026-07-23'
description: Starling Bank is a UK app-only digital challenger bank founded in 2014 by Anne Boden and headquartered in London, holding a full UK banking licence and authorised and regulated by the Prudential Regulation Authority and the Financial Conduct Authority (FSCS-protected, SWIFT SRLGGB2L). It is a privately held company - not a mutual and not publicly listed - backed by investors including Goldman Sachs, Fidelity, and the Qatar Investment Authority, and it also licenses its core banking platform as Software-as-a-Service under the "Engine by Starling" brand. As an FCA-authorised ASPSP it participates in UK Open Banking / PSD2, but Starling is best known for its own developer-friendly, bespoke RESTful Developer API (accounts, transaction feed, payments, payees, savings goals/spaces, cards, mandates, and identity) served over OAuth2 at api.starlingbank.com with a full sandbox, alongside its Open Banking Read/Write (AIS, PIS, CBPII) conformance to the Open Banking Implementation Entity
  (OBIE) standard secured with FAPI-grade OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Starling is a challenger bank and is not one of the nine CMA9 mandated banks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Starling Bank
nav: Providers
network: true
overview: 'Starling Bank publishes 1 API on the [APIs.io](https://apis.io/) network: Starling Open Data API (OBIE Standard). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Starling Bank''s developer surface includes authentication, sandbox, API reference, documentation, getting-started guide, engineering blog, support, and 23 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 39.6
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Starling Bank Authentication
  slug: starling-bank-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Starling Bank Domain Security
  slug: starling-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Starling Bank Vulnerability Disclosure
  slug: starling-bank-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: starling-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Fintech
- FAPI
website: https://www.starlingbank.com/
---
