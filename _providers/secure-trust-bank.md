---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 74.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Secure Trust Bank Agentic Access
  operation_count: 86
  slug: secure-trust-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: The UK Open Banking Open Data API - a public, unauthenticated reference-data surface for ATMs, branches and product information (Personal Current Accounts, Business Current Accounts, Unsecured SME Loa
  name: Secure Trust Bank Open Data API (OBIE Standard)
  slug: open-data-api
- description: The OBIE Read/Write Account and Transaction Information (AIS) API - FAPI-secured access to account, balance, transaction, standing order, direct debit and statement data with customer consent. FAPI-gr
  name: Secure Trust Bank Account & Transaction Information API (OBIE Read/Write, AIS)
  slug: account-transaction-information-api
- description: 'The OBIE Read/Write Payment Initiation (PIS) API - FAPI-secured initiation of domestic, scheduled, standing-order, international and file payments on behalf of a consenting customer, with PSD2 strong '
  name: Secure Trust Bank Payment Initiation API (OBIE Read/Write, PIS)
  slug: payment-initiation-api
- description: The OBIE Read/Write Confirmation of Funds (CBPII) API - FAPI-secured yes/no confirmation that funds are available on an account, for card-based payment instrument issuers, under PSD2 strong customer a
  name: Secure Trust Bank Confirmation of Funds API (OBIE Read/Write, CBPII)
  slug: confirmation-of-funds-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/secure-trust-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secure-trust-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/secure-trust-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/secure-trust-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/secure-trust-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/secure-trust-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/secure-trust-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secure-trust-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secure-trust-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://standards.openbanking.org.uk/
- group: design
  title: ''
  type: DataModel
  url: data-model/secure-trust-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/secure-trust-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/secure-trust-bank-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secure-trust-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.securetrustbank.com/
- group: company
  title: ''
  type: About
  url: https://www.securetrustbank.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.securetrustbank.com/newsroom
- group: auth
  title: ''
  type: Security
  url: https://www.securetrustbank.com/security
- group: operate
  title: ''
  type: Support
  url: https://www.securetrustbank.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.securetrustbank.com/website-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.securetrustbank.com/privacy-statement
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/secure-trust-bank
- group: other
  title: ''
  type: OpenBankingStandard
  url: https://www.openbanking.org.uk/
created: '2026-07-23'
description: 'Secure Trust Bank PLC is an award-winning UK specialist bank, founded in 1952 in the West Midlands and headquartered in Solihull, providing savings accounts and specialist lending to over a million retail and business customers. It is a publicly listed company (London Stock Exchange: STB) rather than a mutual or building society, operating across Retail Finance (V12), Vehicle Finance, Real Estate Finance, Commercial Finance and personal Savings. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (FRN 204550). As a UK ASPSP under PSD2 and the CMA Open Banking framework, its account offerings sit against the Open Banking Implementation Entity (OBIE) standards - a public, unauthenticated Open Data reference surface (ATMs, branches, products) and the FAPI-secured Read/Write APIs for Account and Transaction Information, Payment Initiation and Confirmation of Funds. Secure Trust Bank is a specialist lender and not
  one of the nine CMA9-mandated banks; as of this review it publishes no public developer portal or bank-branded Open Banking developer host, so the API surfaces below reference the shared OBIE standard specifications the bank''s regulated products conform to, not proprietary Secure Trust Bank API contracts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: secure-trust-bank-mcp.yml
  slug: secure-trust-bank-mcpyml
modified: '2026-07-23'
name: Secure Trust Bank
nav: Providers
network: true
overview: 'Secure Trust Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API (OBIE Standard), Account & Transaction Information API (OBIE Read/Write, AIS), Payment Initiation API (OBIE Read/Write, PIS), and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Secure Trust Bank''s developer surface includes authentication, engineering blog, support, and 21 more developer resources.'
random_paper: 27
scopes:
- name: Secure Trust Bank Scopes
  scope_count: 3
  slug: secure-trust-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 41.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.0
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 41.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Secure Trust Bank Authentication
  slug: secure-trust-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Secure Trust Bank Domain Security
  slug: secure-trust-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: secure-trust-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Specialist Lender
- Savings
website: https://www.securetrustbank.com/
---
