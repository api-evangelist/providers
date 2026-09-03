---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Cashplus Agentic Access
  operation_count: 74
  slug: cashplus-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: First-party partner API for authentication and registration against the Cashplus/Zempler developer platform, used to obtain credentials and tokens before calling the proprietary Accounts, Payments, Ap
  name: Cashplus Identity API
  slug: cashplus-identity-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: First-party partner API to retrieve real-time account details and current balance for Cashplus/Zempler business and personal current accounts, for reconciliation and financial analysis. Requires a dir
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
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: First-party partner API to query the catalogue of Cashplus/Zempler banking products. Requires a direct commercial relationship with the bank.
  name: Cashplus Products API
  slug: cashplus-products-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: First-party partner API to search and filter transactions on Cashplus/Zempler accounts, for reconciliation and reporting. Requires a direct commercial relationship with the bank.
  name: Cashplus Transactions API
  slug: cashplus-transactions-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Account Access API from Cashplus Bank — 2 operation(s) for account access.
  name: Cashplus Bank Account Access API
  slug: cashplus-account-access-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Accounts API from Cashplus Bank — 2 operation(s) for accounts.
  name: Cashplus Bank Accounts API
  slug: cashplus-accounts-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Balances API from Cashplus Bank — 2 operation(s) for balances.
  name: Cashplus Bank Balances API
  slug: cashplus-balances-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Beneficiaries API from Cashplus Bank — 2 operation(s) for beneficiaries.
  name: Cashplus Bank Beneficiaries API
  slug: cashplus-beneficiaries-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Direct Debits API from Cashplus Bank — 2 operation(s) for direct debits.
  name: Cashplus Bank Direct Debits API
  slug: cashplus-direct-debits-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Payments API from Cashplus Bank — 5 operation(s) for domestic payments.
  name: Cashplus Bank Domestic Payments API
  slug: cashplus-domestic-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Scheduled Payments API from Cashplus Bank — 4 operation(s) for domestic scheduled payments.
  name: Cashplus Bank Domestic Scheduled Payments API
  slug: cashplus-domestic-scheduled-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Domestic Standing Orders API from Cashplus Bank — 4 operation(s) for domestic standing orders.
  name: Cashplus Bank Domestic Standing Orders API
  slug: cashplus-domestic-standing-orders-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The File Payments API from Cashplus Bank — 6 operation(s) for file payments.
  name: Cashplus Bank File Payments API
  slug: cashplus-file-payments-api
- baseURL: /open-banking/v3.1/cbpii
  baseurl_source: spec
  description: The Funds Confirmations API from Cashplus Bank — 3 operation(s) for funds confirmations.
  name: Cashplus Bank Funds Confirmations API
  slug: cashplus-funds-confirmations-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Payments API from Cashplus Bank — 5 operation(s) for international payments.
  name: Cashplus Bank International Payments API
  slug: cashplus-international-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Scheduled Payments API from Cashplus Bank — 5 operation(s) for international scheduled payments.
  name: Cashplus Bank International Scheduled Payments API
  slug: cashplus-international-scheduled-payments-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The International Standing Orders API from Cashplus Bank — 4 operation(s) for international standing orders.
  name: Cashplus Bank International Standing Orders API
  slug: cashplus-international-standing-orders-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Offers API from Cashplus Bank — 2 operation(s) for offers.
  name: Cashplus Bank Offers API
  slug: cashplus-offers-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Parties API from Cashplus Bank — 3 operation(s) for parties.
  name: Cashplus Bank Parties API
  slug: cashplus-parties-api
- baseURL: /open-banking/v3.1/pisp
  baseurl_source: spec
  description: The Payment Details API from Cashplus Bank — 7 operation(s) for payment details.
  name: Cashplus Bank Payment Details API
  slug: cashplus-payment-details-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Products API from Cashplus Bank — 2 operation(s) for products.
  name: Cashplus Bank Products API
  slug: cashplus-products-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Scheduled Payments API from Cashplus Bank — 2 operation(s) for scheduled payments.
  name: Cashplus Bank Scheduled Payments API
  slug: cashplus-scheduled-payments-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Standing Orders API from Cashplus Bank — 2 operation(s) for standing orders.
  name: Cashplus Bank Standing Orders API
  slug: cashplus-standing-orders-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Statements API from Cashplus Bank — 4 operation(s) for statements.
  name: Cashplus Bank Statements API
  slug: cashplus-statements-api
- baseURL: /open-banking/v3.1/aisp
  baseurl_source: spec
  description: The Transactions API from Cashplus Bank — 3 operation(s) for transactions.
  name: Cashplus Bank Transactions API
  slug: cashplus-transactions-api
artifact_total: 36
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cashplus-capability-edges.yml
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
  name: Cashplus Bank MCP Server
  slug: cashplus-bank-mcp-server
modified: '2026-07-23'
name: Cashplus Bank
nav: Providers
network: true
overview: 'Cashplus Bank publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Cashplus Accounts API, Cashplus Products API, Cashplus Transactions API, and 21 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  Cashplus Bank''s developer surface includes authentication, documentation, engineering blog, legal docs, support, and 27 more developer resources.'
random_paper: 6
scopes:
- name: Cashplus Scopes
  scope_count: 3
  slug: cashplus-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.3
    developer_ergonomics: 47.0
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
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
    score: 70.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Financial-Services
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
