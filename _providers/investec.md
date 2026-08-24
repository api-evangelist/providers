---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Investec Agentic Access
  operation_count: 74
  slug: investec-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 9
apis:
- description: First-party Programmable Banking API to retrieve data and perform actions on your own or your business's Investec Private Banking account, including accounts, balances, transactions, transfers, and pa
  name: Investec Private Bank API
  slug: investec-private-bank-api
- description: First-party Programmable Banking API to retrieve data and perform actions on Investec business and commercial banking accounts.
  name: Investec Business & Commercial Banking API
  slug: investec-business-commercial-banking-api
- description: First-party Programmable Banking API to retrieve data and perform actions on behalf of your clients, including forex quoting and trading.
  name: Investec Intermediaries API
  slug: investec-intermediaries-api
- description: First-party Programmable Banking API for Balance of Payments (BOP) reporting and foreign-exchange information retrieval on behalf of your clients.
  name: Investec Intermediaries Forex API
  slug: investec-intermediaries-forex-api
- description: First-party Programmable Banking Card API to retrieve card data and programmatically attach rules that run before and after transactions on Investec programmable cards.
  name: Investec Card API
  slug: investec-card-api
- description: First-party OAuth2 authorisation endpoint that generates and refreshes the access tokens authorising calls to the Investec Programmable Banking APIs.
  name: Investec Authorisation API (OAuth)
  slug: investec-authorisation-api
- description: UK Open Banking Account Information Service (AISP) interface for accessing account, balance, transaction, and product data. Investec Bank plc conforms to the OBIE Read/Write API Standard (v3.1); the h
  name: Investec Account and Transaction Information API (AIS)
  slug: investec-account-transaction-information-api
- description: 'UK Open Banking Payment Initiation Service (PISP) interface for initiating domestic and other payments. Investec Bank plc conforms to the OBIE Read/Write API Standard (v3.1); the harvested OpenAPI is '
  name: Investec Payment Initiation API (PIS)
  slug: investec-payment-initiation-api
- description: UK Open Banking Confirmation of Funds (CBPII) interface for checking whether funds are available on an account. Investec Bank plc conforms to the OBIE Read/Write API Standard (v3.1); the harvested Ope
  name: Investec Confirmation of Funds API (CBPII)
  slug: investec-confirmation-of-funds-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/investec-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/investec-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/investec-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/investec-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.investec.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.investec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.investec.com/api-reference
- group: docs
  title: ''
  type: APIReference
  url: https://developer.investec.com/api-products
- group: company
  title: ''
  type: Blog
  url: https://investec.gitbook.io/programmable-banking-community-wiki
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/investec
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/investec
- group: operate
  title: ''
  type: Support
  url: https://developer.investec.com/support
- group: build
  title: ''
  type: Packages
  url: packages/investec-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/investec-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/investec-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/investec-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/investec-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/investec-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/investec-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/investec-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/investec-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/investec-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/investec-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/investec-confirmation-funds-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/investec-retrieve-accounts-and-transactions.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/investec-initiate-domestic-payment.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/investec-confirm-funds.md
- group: start
  title: ''
  type: GettingStarted
  url: https://investec.gitbook.io/programmable-banking-community-wiki/get-started/get-started-overview
- group: start
  title: ''
  type: SignUp
  url: https://developer.investec.com/individuals
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/investec-open-api/workspace/programmable-banking
created: '2026-07-23'
description: Investec is an international specialist bank and wealth manager, dual-listed on the London Stock Exchange and Johannesburg Stock Exchange and operating through Investec plc (UK) and Investec Limited (South Africa). In the United Kingdom, Investec Bank plc is authorised by the PRA and regulated by the FCA and PRA and is an FCA-registered Account Servicing Payment Service Provider (ASPSP) under UK Open Banking, exposing Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) interfaces built to the Open Banking Implementation Entity (OBIE) Read/Write API Standard (v3.1), secured with FAPI-grade OAuth2/OIDC, PSD2 strong customer authentication, and mutual-TLS using OBIE/eIDAS certificates. Investec is a specialist private bank and wealth manager rather than a mass-market retail bank, so it is not one of the CMA9 and does not operate a branch or ATM network. Alongside Open Banking, Investec runs a first-party Programmable Banking /
  Open API developer platform at openapi.investec.com offering Private Bank, Business & Commercial Banking, Intermediaries, Intermediaries Forex, and Card APIs secured with OAuth2 client credentials, published through the Investec Developer Portal at developer.investec.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Investec
nav: Providers
network: true
overview: 'Investec publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API (AIS), Payment Initiation API (PIS), and Confirmation of Funds API (CBPII). Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Investec''s developer surface includes authentication, documentation, API reference, engineering blog, support, sandbox, getting-started guide, and 23 more developer resources.'
random_paper: 4
scopes:
- name: Investec Scopes
  scope_count: 4
  slug: investec-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 44.8
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/investec/refs/heads/main/screenshots/investec-2026-07-25T222744.png
security:
- kind: authentication
  name: Investec Authentication
  slug: investec-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Investec Domain Security
  slug: investec-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: investec
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Specialist Bank
- Wealth Management
- FAPI
- Programmable Banking
website: https://www.investec.com/
---
