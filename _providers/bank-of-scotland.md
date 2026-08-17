---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: PUBLIC, unauthenticated OBIE Open Data reference API for Bank of Scotland, exposing ATM locations, branch details, personal and business current account products, unsecured SME loans, and commercial c
  name: Bank of Scotland Open Data API
  slug: bank-of-scotland-open-data-api
- description: OBIE Read/Write Account and Transaction Information (AIS) API - account details, balances, transactions, standing orders, direct debits, beneficiaries, statements, and products. FAPI-secured (OAuth2/O
  name: Bank of Scotland Account and Transaction Information API (AIS)
  slug: bank-of-scotland-account-information-api
- description: 'OBIE Read/Write Payment Initiation (PIS) API - domestic, scheduled, standing order, international, and file payment consents and orders. FAPI-secured (OAuth2/OIDC, mTLS, PSD2 SCA); requires developer '
  name: Bank of Scotland Payment Initiation API (PIS)
  slug: bank-of-scotland-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API - card-based payment instrument issuers confirm whether funds are available on an account. FAPI-secured (OAuth2/OIDC, mTLS, PSD2 SCA); requires develo
  name: Bank of Scotland Confirmation of Funds API (CBPII)
  slug: bank-of-scotland-confirmation-of-funds-api
artifact_total: 9
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-opendata-swagger
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-scotland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-scotland-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-scotland-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-scotland-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bank-of-scotland-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-scotland-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-scotland-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-scotland-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-scotland-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bank-of-scotland-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-scotland-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankofscotland.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lloydsbanking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofscotland.co.uk/aboutonline/security-and-privacy/open-banking-apis.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-scotland
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankofscotland.co.uk/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofscotland.co.uk/legal/privacy.html
created: '2026-07-23'
description: Bank of Scotland is a UK high-street retail and commercial bank, founded in 1695 and headquartered in Edinburgh, and is one of the oldest banks in the United Kingdom. It is a wholly owned subsidiary brand of Lloyds Banking Group (alongside Lloyds Bank and Halifax), authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As one of the nine mandated CMA9 account-providers, Bank of Scotland participates in the UK Open Banking regime under PSD2, publishing PUBLIC, unauthenticated Open Data reference APIs (ATMs, branches, personal and business current accounts, unsecured SME loans, and commercial credit cards) conformant to the Open Banking Implementation Entity (OBIE) Open Data Standard, plus the OBIE Read/Write API family - Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) - secured with FAPI-grade OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication,
  accessed through the Lloyds Banking Group developer platform after eIDAS/OBIE certificate onboarding.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: bank-of-scotland-mcp.yml
  slug: bank-of-scotland-mcpyml
modified: '2026-07-23'
name: Bank of Scotland
nav: Providers
network: true
overview: 'Bank of Scotland publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction Information API (AIS), Payment Initiation API (PIS), and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Bank of Scotland''s developer surface includes authentication, sandbox, documentation, and 15 more developer resources.'
random_paper: 81
scopes:
- name: Bank Of Scotland Scopes
  scope_count: 3
  slug: bank-of-scotland-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.0
    developer_ergonomics: 36.4
    discoverability: 72.2
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.3
  provenance:
    conformance: derived
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-scotland/refs/heads/main/screenshots/bank-of-scotland-2026-07-25T202339.png
security:
- kind: authentication
  name: Bank Of Scotland Authentication
  slug: bank-of-scotland-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Bank Of Scotland Domain Security
  slug: bank-of-scotland-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bank-of-scotland
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Open Data
website: https://www.bankofscotland.co.uk/
---
