---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Investec Agentic Access
  operation_count: 74
  slug: investec-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
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
- description: The Account Access Consents API from Investec — 2 operation(s) for account access consents.
  name: Investec Account Access Consents API
  slug: investec-account-access-consents-api
- description: The Accounts API from Investec — 2 operation(s) for accounts.
  name: Investec Accounts API
  slug: investec-accounts-api
- description: The Balances API from Investec — 2 operation(s) for balances.
  name: Investec Balances API
  slug: investec-balances-api
- description: The Beneficiaries API from Investec — 2 operation(s) for beneficiaries.
  name: Investec Beneficiaries API
  slug: investec-beneficiaries-api
- description: The Direct Debits API from Investec — 2 operation(s) for direct debits.
  name: Investec Direct Debits API
  slug: investec-direct-debits-api
- description: The Domestic Payment Consents API from Investec — 3 operation(s) for domestic payment consents.
  name: Investec Domestic Payment Consents API
  slug: investec-domestic-payment-consents-api
- description: The Domestic Payments API from Investec — 3 operation(s) for domestic payments.
  name: Investec Domestic Payments API
  slug: investec-domestic-payments-api
- description: The Domestic Scheduled Payment Consents API from Investec — 2 operation(s) for domestic scheduled payment consents.
  name: Investec Domestic Scheduled Payment Consents API
  slug: investec-domestic-scheduled-payment-consents-api
- description: The Domestic Scheduled Payments API from Investec — 3 operation(s) for domestic scheduled payments.
  name: Investec Domestic Scheduled Payments API
  slug: investec-domestic-scheduled-payments-api
- description: The Domestic Standing Order Consents API from Investec — 2 operation(s) for domestic standing order consents.
  name: Investec Domestic Standing Order Consents API
  slug: investec-domestic-standing-order-consents-api
- description: The Domestic Standing Orders API from Investec — 3 operation(s) for domestic standing orders.
  name: Investec Domestic Standing Orders API
  slug: investec-domestic-standing-orders-api
- description: The File Payment Consents API from Investec — 3 operation(s) for file payment consents.
  name: Investec File Payment Consents API
  slug: investec-file-payment-consents-api
- description: The File Payments API from Investec — 4 operation(s) for file payments.
  name: Investec File Payments API
  slug: investec-file-payments-api
- description: The Funds Confirmation Consents API from Investec — 2 operation(s) for funds confirmation consents.
  name: Investec Funds Confirmation Consents API
  slug: investec-funds-confirmation-consents-api
- description: The Funds Confirmations API from Investec — 1 operation(s) for funds confirmations.
  name: Investec Funds Confirmations API
  slug: investec-funds-confirmations-api
- description: The International Payment Consents API from Investec — 3 operation(s) for international payment consents.
  name: Investec International Payment Consents API
  slug: investec-international-payment-consents-api
- description: The International Payments API from Investec — 3 operation(s) for international payments.
  name: Investec International Payments API
  slug: investec-international-payments-api
- description: The International Scheduled Payments API from Investec — 3 operation(s) for international scheduled payments.
  name: Investec International Scheduled Payments API
  slug: investec-international-scheduled-payments-api
- description: The International Scheduled Payments Consents API from Investec — 3 operation(s) for international scheduled payments consents.
  name: Investec International Scheduled Payments Consents API
  slug: investec-international-scheduled-payments-consents-api
- description: The International Standing Orders API from Investec — 3 operation(s) for international standing orders.
  name: Investec International Standing Orders API
  slug: investec-international-standing-orders-api
- description: The International Standing Orders Consents API from Investec — 2 operation(s) for international standing orders consents.
  name: Investec International Standing Orders Consents API
  slug: investec-international-standing-orders-consents-api
- description: The Offers API from Investec — 2 operation(s) for offers.
  name: Investec Offers API
  slug: investec-offers-api
- description: The Parties API from Investec — 3 operation(s) for parties.
  name: Investec Parties API
  slug: investec-parties-api
- description: The Products API from Investec — 2 operation(s) for products.
  name: Investec Products API
  slug: investec-products-api
- description: The Scheduled Payments API from Investec — 2 operation(s) for scheduled payments.
  name: Investec Scheduled Payments API
  slug: investec-scheduled-payments-api
- description: The Standing Orders API from Investec — 2 operation(s) for standing orders.
  name: Investec Standing Orders API
  slug: investec-standing-orders-api
- description: The Statements API from Investec — 5 operation(s) for statements.
  name: Investec Statements API
  slug: investec-statements-api
- description: The Transactions API from Investec — 2 operation(s) for transactions.
  name: Investec Transactions API
  slug: investec-transactions-api
artifact_total: 38
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/investec-capability-edges.yml
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
overview: 'Investec publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account Access Consents API, Accounts API, Balances API, and 25 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Investec''s developer surface includes authentication, documentation, API reference, engineering blog, support, sandbox, getting-started guide, and 24 more developer resources.'
random_paper: 4
scopes:
- name: Investec Scopes
  scope_count: 4
  slug: investec-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 19
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 42.9
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
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
