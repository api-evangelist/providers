---
access_model:
  confidence: medium
  label: Self-serve signup · Open Data public
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - open-data
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Danske Bank Uk Agentic Access
  operation_count: 81
  slug: danske-bank-uk-agentic-access
  summary_line: 81 operations · 26 acting
api_count: 11
apis:
- description: Public, unauthenticated UK Open Banking Open Data API (OBIE Open Data v2.2) publishing reference data for Danske Bank (UK) - ATM and branch locations, personal and business current accounts, unsecured
  name: Danske Bank (UK) Open Data API
  slug: danske-bank-uk-open-data-api
- description: OBIE Read/Write Account and Transaction Information API (AIS, v4.0) for accessing account details, balances, transactions, beneficiaries, standing orders, direct debits, and statements. FAPI-secured w
  name: Danske Bank (UK) Account and Transaction API
  slug: danske-bank-uk-account-transaction-api
- description: OBIE Read/Write Payment Initiation API (PIS, v4.0) for initiating domestic, scheduled, standing-order, file, and international payments. FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong cust
  name: Danske Bank (UK) Payment Initiation API
  slug: danske-bank-uk-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds API (CBPII, v4.0) for card-based payment instrument issuers to confirm the availability of funds on an account. FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD
  name: Danske Bank (UK) Confirmation of Funds API
  slug: danske-bank-uk-confirmation-of-funds-api
- description: OBIE Read/Write Variable Recurring Payments API (VRP, v4.0) for setting up domestic VRP consents and executing recurring payments within agreed parameters. FAPI-secured with OAuth2/OIDC, mutual-TLS, a
  name: Danske Bank (UK) Variable Recurring Payments API
  slug: danske-bank-uk-variable-recurring-payments-api
- description: OBIE Read/Write Event Notification API (v4.0) delivering real-time notifications on account and payment activities to registered TPPs. FAPI-secured with OAuth2/OIDC and mutual-TLS; requires TPP onboar
  name: Danske Bank (UK) Events API
  slug: danske-bank-uk-events-api
- description: Premium first-party corporate API providing real-time access to account transactions and balances, published on the Danske Bank developer portal and served from the corporate API host with a public mo
  name: Danske Bank (UK) Account Transaction & Balance API
  slug: danske-bank-uk-account-transaction-balance-api
- description: Premium first-party corporate API for initiating and managing collection (direct debit style) payment services, published on the Danske Bank developer portal with a public mock sandbox.
  name: Danske Bank (UK) Payment Collection API
  slug: danske-bank-uk-payment-collection-api
- description: Premium first-party corporate payment initiation API for submitting and managing corporate payment orders, published on the Danske Bank developer portal with a public mock sandbox.
  name: Danske Bank (UK) Premium Payment Initiation API
  slug: danske-bank-uk-premium-payment-initiation-api
- description: 'Premium first-party API providing access to open and historical FX trade reports with date-range filtering, counterpart filtering, and pagination, published on the Danske Bank developer portal with a '
  name: Danske Bank (UK) FX Trade Report API
  slug: danske-bank-uk-fx-trade-report-api
- description: Premium first-party API for executing FX trades against existing quotes, published on the Danske Bank developer portal with a public mock sandbox.
  name: Danske Bank (UK) FX Trade Execution API
  slug: danske-bank-uk-fx-trade-execution-api
artifact_total: 17
asyncapis:
- description: ''
  name: Danske Bank Uk Events Webhooks
  slug: danske-bank-uk-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/danske-bank-uk-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/danske-bank-uk-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/danske-bank-uk-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/danske-bank-uk-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/danske-bank-uk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/danske-bank-uk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/danske-bank-uk-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/danske-bank-uk-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/danske-bank-uk-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/danske-bank-uk-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/danske-bank-uk-events-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/danske-bank-uk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/danske-bank-uk-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/danske-bank-uk-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/danske-bank-uk-account-transaction-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.danskebank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.danskebank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.danskebank.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://danskebank.co.uk/important-information/open-banking/third-party-providers
- group: other
  title: ''
  type: OpenBanking
  url: https://danskebank.co.uk/important-information/open-banking
- group: auth
  title: ''
  type: Compliance
  url: https://danskebank.co.uk/important-information/open-banking/api-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/danske-bank
- group: company
  title: ''
  type: Blog
  url: https://danskebank.co.uk/about-us/news-and-insights
- group: operate
  title: ''
  type: Support
  url: https://www.danskebank.co.uk/personal/help/useful-numbers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.danskebank.co.uk/personal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.danskebank.co.uk/personal/privacy-notice
- group: other
  title: ''
  type: Cookies
  url: https://www.danskebank.co.uk/personal/help/cookie-policy
created: '2026-07-23'
description: 'Danske Bank (UK) is the trading name of Northern Bank Limited, a retail and commercial bank headquartered in Belfast and the largest bank in Northern Ireland. It is a wholly owned subsidiary of Denmark''s Danske Bank Group and is authorised by the UK Prudential Regulation Authority and regulated by the Financial Conduct Authority and PRA. As "Northern Bank Limited t/a Danske Bank" it is one of the CMA9 - the nine largest current-account providers mandated by the UK Competition and Markets Authority to implement the Open Banking standard - and an FCA-authorised ASPSP under PSD2. It publishes the UK Open Banking (OBIE) API family: a public, unauthenticated Open Data API (ATMs, branches, personal and business current accounts, unsecured SME loans, commercial credit cards) and the FAPI-secured Read/Write APIs for Account and Transaction Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), Variable Recurring Payments (VRP), and Events, alongside a suite of
  premium corporate APIs (account transaction and balance reporting, payment collection, corporate payment initiation, and FX trade reporting and execution) exposed through the Danske Bank developer portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: danske-bank-uk-mcp.yml
  slug: danske-bank-uk-mcpyml
modified: '2026-07-23'
name: Danske Bank (UK)
nav: Providers
network: true
overview: 'Danske Bank (UK) publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction API, Payment Initiation API, and 8 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  The Danske Bank (UK) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Danske Bank (UK)''s developer surface includes authentication, sandbox, documentation, getting-started guide, engineering blog, support, and 22 more developer resources.'
random_paper: 76
scopes:
- name: Danske Bank Uk Scopes
  scope_count: 4
  slug: danske-bank-uk-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 45.4
  delta: -6.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 67.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/danske-bank-uk/refs/heads/main/screenshots/danske-bank-uk-2026-07-25T211205.png
security:
- kind: authentication
  name: Danske Bank Uk Authentication
  slug: danske-bank-uk-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Danske Bank Uk Domain Security
  slug: danske-bank-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: danske-bank-uk
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Northern Ireland
- Payments
- Account Information
- FAPI
- Fintech
website: https://www.danskebank.co.uk/
---
