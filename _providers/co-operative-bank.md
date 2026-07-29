---
access_model:
  confidence: medium
  label: TPP onboarding (manual)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - documentation
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Co Operative Bank Agentic Access
  operation_count: 12
  slug: co-operative-bank-agentic-access
  summary_line: 12 operations
api_count: 4
apis:
- description: 'OBIE Read/Write Account & Transaction Information (AISP) API for The Co-operative Bank and smile brands — account-access consents, accounts, balances, transactions, direct debits, standing orders and '
  name: The Co-operative Bank Account Information API (AIS)
  slug: account-information-api
- description: 'OBIE Read/Write Payment Initiation (PISP) API for The Co-operative Bank and smile brands — domestic payments, domestic scheduled payments and domestic standing orders, with their associated consents. '
  name: The Co-operative Bank Payment Initiation API (PIS)
  slug: payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII / Card-Based Payment Instrument) API — funds-confirmation consent and funds-confirmation checks for The Co-operative Bank and smile brands. FAPI-secured (O
  name: The Co-operative Bank Confirmation of Funds API (CBPII)
  slug: confirmation-of-funds-api
- description: Public, unauthenticated OBIE Open Data reference data (ATMs, Branches, Personal & Business Current Accounts, Unsecured SME Loans, Commercial Credit Cards). Represented here against the shared OBIE Ope
  name: The Co-operative Bank Open Data API (OBIE standard)
  slug: open-data-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/co-operative-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/co-operative-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/co-operative-bank-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.co-operativebank.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developer.co-operativebank.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.developer.co-operativebank.co.uk/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.developer.co-operativebank.co.uk/get-started/
- group: auth
  title: ''
  type: Authentication
  url: https://www.developer.co-operativebank.co.uk/apis/general-specifications/
- group: start
  title: ''
  type: Sandbox
  url: https://www.developer.co-operativebank.co.uk/help-and-support/sandbox-environment/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.developer.co-operativebank.co.uk/help-and-support/service-status/
- group: operate
  title: ''
  type: Support
  url: https://www.developer.co-operativebank.co.uk/help-and-support/frequently-asked-questions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.developer.co-operativebank.co.uk/help-and-support/privacy-cookie-policies/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-co-operative-bank
- group: start
  title: ''
  type: SignUp
  url: https://www.developer.co-operativebank.co.uk/get-started/
- group: auth
  title: ''
  type: Authentication
  url: authentication/co-operative-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/co-operative-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/co-operative-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/co-operative-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/co-operative-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/co-operative-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/co-operative-bank-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/co-operative-bank-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/co-operative-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/co-operative-bank-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.co-operativebank.co.uk/help-and-support/fraud-and-security/responsible-security-disclosure/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/co-operative-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/co-operative-bank-open-data-overlay.yaml
created: '2026-07-23'
description: The Co-operative Bank plc is a UK high-street retail and commercial bank, headquartered in Manchester and long known for its customer-led ethical banking policy. Following its 2013-2017 recapitalisation it was owned by institutional bondholders, and in January 2025 it completed its acquisition by Coventry Building Society, becoming part of the member-owned Coventry Building Society Group; it also operates the online-only "smile" brand. Authorised by the PRA and regulated by the FCA and PRA, it is an FCA-authorised ASPSP under PSD2 and the UK Open Banking regime. While it is not one of the nine CMA-mandated banks (CMA9), it implements the Open Banking Implementation Entity (OBIE) Read/Write API Standard (v3.1) and publishes a public developer portal at developer.co-operativebank.co.uk exposing Account Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) APIs for both the Co-operative Bank and smile brands, secured with FAPI-grade OAuth2/OIDC, mutual-TLS
  client authentication using Open Banking directory certificates, and PSD2 strong customer authentication, with a manual TPP onboarding process and a sandbox for testing before production.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: The Co-operative Bank
nav: Providers
network: true
overview: 'The Co-operative Bank publishes 1 API on the [APIs.io](https://apis.io/) network: Open Data API (OBIE standard). Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  The Co-operative Bank''s developer surface includes documentation, getting-started guide, authentication, sandbox, support, signup flow, and 21 more developer resources.'
random_paper: 67
scopes:
- name: Co Operative Bank Scopes
  scope_count: 6
  slug: co-operative-bank-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 43.3
  delta: -0.7
  facets:
    commercial_clarity: 23.7
    contract_quality: 32.3
    developer_ergonomics: 50.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 73.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/co-operative-bank/refs/heads/main/screenshots/co-operative-bank-2026-07-25T205806.png
security:
- kind: authentication
  name: Co Operative Bank Authentication
  slug: co-operative-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Co Operative Bank Domain Security
  slug: co-operative-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Co Operative Bank Vulnerability Disclosure
  slug: co-operative-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: co-operative-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Confirmation of Funds
- Fintech
website: https://www.co-operativebank.co.uk/
---
