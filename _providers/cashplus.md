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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cashplus Agentic Access
  operation_count: 74
  slug: cashplus-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 10
apis:
- description: Open Banking Account Information Service Provider (AISP) API conformant to the OBIE Read/Write API Standard, exposing account access consents, account details, balances, transactions, standing orders,
  name: Cashplus Account Information API
  slug: cashplus-account-information-api
- description: Open Banking Payment Initiation Service Provider (PISP) API conformant to the OBIE Read/Write API Standard, supporting domestic payments, domestic scheduled payments, and domestic standing orders with
  name: Cashplus Payment Initiation API
  slug: cashplus-payment-initiation-api
- description: 'Open Banking Card Based Payment Instrument Issuer (CBPII) Confirmation of Funds API conformant to the OBIE Read/Write API Standard, letting authorised providers establish a funds-confirmation consent '
  name: Cashplus Confirmation of Funds API
  slug: cashplus-confirmation-of-funds-api
- description: First-party partner API for authentication and registration against the Cashplus/Zempler developer platform, used to obtain credentials and tokens before calling the proprietary Accounts, Payments, Ap
  name: Cashplus Identity API
  slug: cashplus-identity-api
- description: First-party partner API to retrieve real-time account details and current balance for Cashplus/Zempler business and personal current accounts, for reconciliation and financial analysis. Requires a dir
  name: Cashplus Accounts API
  slug: cashplus-accounts-api
- description: First-party partner API to create applications that open new Cashplus/Zempler current accounts programmatically, enabling embedded account onboarding within partner platforms. Requires a direct commer
  name: Cashplus Applications API
  slug: cashplus-applications-api
- description: First-party partner API for running credit card eligibility checks against Cashplus/Zempler credit products. Requires a direct commercial relationship with the bank.
  name: Cashplus Eligibility API
  slug: cashplus-eligibility-api
- description: First-party partner API to initiate single and batch domestic GBP payments at low cost from Cashplus/Zempler accounts, marketed for partners as a lower-cost alternative to standard payment rails. Requ
  name: Cashplus Payments API
  slug: cashplus-payments-api
- description: First-party partner API to query the catalogue of Cashplus/Zempler banking products. Requires a direct commercial relationship with the bank.
  name: Cashplus Products API
  slug: cashplus-products-api
- description: First-party partner API to search and filter transactions on Cashplus/Zempler accounts, for reconciliation and reporting. Requires a direct commercial relationship with the bank.
  name: Cashplus Transactions API
  slug: cashplus-transactions-api
artifact_total: 18
collections:
- collection_type: open
  name: Account and Transaction API Specification
  slug: open-cashplus-account-information
- collection_type: open
  name: Confirmation of Funds API Specification
  slug: open-cashplus-confirmation-of-funds
- collection_type: open
  name: Payment Initiation API
  slug: open-cashplus-payment-initiation
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cashplus-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cashplus-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cashplus-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cashplus-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cashplus-account-information-openapi.yml
- group: company
  title: ''
  type: Website
  url: https://www.zemplerbank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zemplerbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zemplerbank.com/api-developer/
- group: other
  title: ''
  type: OpenBanking
  url: https://www.zemplerbank.com/api/
- group: other
  title: ''
  type: OpenBankingDirectory
  url: https://www.openbanking.org.uk/customers/regulated-providers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zemplerbank
- group: company
  title: ''
  type: Blog
  url: https://www.zemplerbank.com/about/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zemplerbank.com/terms-and-conditions/
- group: commercial
  title: ''
  type: Legal
  url: https://www.zemplerbank.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zemplerbank.com/policies/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.zemplerbank.com/help/
- group: operate
  title: ''
  type: Contact
  url: https://www.zemplerbank.com/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zemplerbank.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cashplus-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cashplus-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cashplus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cashplus-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cashplus-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cashplus-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cashplus-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cashplus-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cashplus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cashplus-account-information-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cashplus-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/cashplus-confirmation-of-funds-overlay.yaml
created: '2026-07-23'
description: Cashplus Bank (legal entity Advanced Payment Solutions Limited, rebranded to Zempler Bank in July 2024) is a UK challenger bank founded in 2005 that grew from a prepaid-card issuer into a fully licensed bank, receiving its UK banking licence in 2021 and regulated by the Financial Conduct Authority (FCA) and the Prudential Regulation Authority (PRA). It focuses on business current accounts, personal current accounts, credit cards, and payments for micro-enterprises, sole traders, and small-to-medium businesses. Following a 2026 acquisition it operates as a subsidiary of The Access Bank UK (part of Nigeria's Access Bank plc). As an FCA-authorised ASPSP it participates in UK Open Banking under PSD2, publishing Read/Write APIs conformant to the Open Banking Implementation Entity (OBIE) standard - Account Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) - secured with FAPI-grade OAuth2/OIDC, mutual-TLS, PSD2 strong customer authentication, and OBIE/eIDAS
  certificates. Cashplus is not one of the CMA9 mandated banks. Alongside the regulated Open Banking surface it runs a first-party partner/developer platform documenting proprietary Identity, Accounts, Applications, Eligibility, Payments, Products, and Transactions APIs for embedded and commercial integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: cashplus-mcp.yml
  slug: cashplus-mcpyml
modified: '2026-07-23'
name: Cashplus Bank
nav: Providers
network: true
overview: 'Cashplus Bank publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cashplus Account Information API, Cashplus Payment Initiation API, and Cashplus Confirmation of Funds API. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Cashplus Bank''s developer surface includes authentication, documentation, engineering blog, legal docs, support, and 26 more developer resources.'
random_paper: 122
scopes:
- name: Cashplus Scopes
  scope_count: 3
  slug: cashplus-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 43.1
  delta: 4.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 50.8
    developer_ergonomics: 39.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cashplus/refs/heads/main/screenshots/cashplus-2026-07-25T204726.png
security:
- kind: authentication
  name: Cashplus Authentication
  slug: cashplus-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Cashplus Domain Security
  slug: cashplus-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cashplus
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Business Banking
- Fintech
website: https://www.zemplerbank.com/
---
