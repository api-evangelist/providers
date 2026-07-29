---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Gb Bank Agentic Access
  operation_count: 86
  slug: gb-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: UK Open Banking Open Data API (OBIE standard, v1.3) - the public, unauthenticated reference-data surface for ATMs, Branches, Personal Current Accounts, Business Current Accounts, Unsecured SME Loans a
  name: GB Bank Open Data API
  slug: gb-bank-open-data-api
- description: UK Open Banking Read/Write Account & Transaction Information API (AISP) - the OBIE standard for accessing account, balance, transaction and statement data with customer consent. FAPI-secured (OAuth2/O
  name: GB Bank Account and Transaction Information API (AIS)
  slug: gb-bank-account-transaction-information-api
- description: UK Open Banking Read/Write Payment Initiation API (PISP) - the OBIE standard for initiating domestic, scheduled, standing-order, international and file payments with customer consent. FAPI-secured (OA
  name: GB Bank Payment Initiation API (PIS)
  slug: gb-bank-payment-initiation-api
- description: UK Open Banking Read/Write Confirmation of Funds API (CBPII) - the OBIE standard for confirming whether funds are available on a payment account with customer consent. FAPI-secured (OAuth2/OIDC, mTLS,
  name: GB Bank Confirmation of Funds API (CBPII)
  slug: gb-bank-confirmation-of-funds-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gb-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gb-bank-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gb-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gb-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gb-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gb-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gb-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gb-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gb-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gb-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.gbbank.co.uk/
- group: other
  title: ''
  type: Savings
  url: https://www.gbbank.co.uk/savings
- group: other
  title: ''
  type: MobileApp
  url: https://www.gbbank.co.uk/gb-bank-mobile-app
- group: operate
  title: ''
  type: Support
  url: https://www.gbbank.co.uk/help-and-support/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.gbbank.co.uk/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gbbank.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gbbank.co.uk/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thegbb
- group: other
  title: ''
  type: Standard
  url: https://github.com/OpenBankingUK/opendata-api-spec-compiled
- group: other
  title: ''
  type: Standard
  url: https://standards.openbanking.org.uk/
created: '2026-07-23'
description: GB Bank Limited is a UK challenger bank headquartered in Middlesbrough (2 Centre Square) with a London office (73 Brook Street, Mayfair). Wholly owned and privately backed rather than a mutual building society, it secured its full UK banking licence in 2022 and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA (Financial Services Register number 850286). GB Bank funds SME regional property developers and investors with development finance, buy-to-let and bridging loans (typically between £26k and £5m across underserved UK regions) and funds that lending with retail deposits - fixed-rate bonds, notice accounts and easy-access savings accounts protected by the FSCS up to £85,000, managed through an online portal and a GB Bank mobile app. As a small, non-CMA9 FCA-authorised bank focused on savings and secured lending, GB Bank does not operate a public developer portal or a documented UK Open Banking (OBIE / PSD2) API
  surface; the Open Banking API families listed here are represented as the shared industry standard the bank would conform to as an FCA-authorised ASPSP, and are unverified for GB Bank pending a confirmed developer portal or Open Data endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: GB Bank
nav: Providers
network: true
overview: 'GB Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction Information API (AIS), Payment Initiation API (PIS), and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  GB Bank''s developer surface includes authentication, support, engineering blog, and 17 more developer resources.'
random_paper: 26
scopes:
- name: Gb Bank Scopes
  scope_count: 3
  slug: gb-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 35.2
  delta: -2.7
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.6
    developer_ergonomics: 17.4
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gb-bank/refs/heads/main/screenshots/gb-bank-2026-07-25T215509.png
security:
- kind: authentication
  name: Gb Bank Authentication
  slug: gb-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Gb Bank Domain Security
  slug: gb-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gb-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Savings
- Property Finance
- SME Lending
- Fintech
website: https://www.gbbank.co.uk/
---
