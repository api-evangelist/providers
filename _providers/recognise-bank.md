---
access_model:
  confidence: high
  label: No public developer API confirmed
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - website
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 39.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Shared UK Open Banking Open Data standard for public, unauthenticated reference data (ATMs, branches, personal and business current accounts, unsecured SME loans, commercial credit cards). Included as
  name: UK Open Banking Open Data API (OBIE Standard)
  slug: uk-open-banking-open-data-api
- description: Shared OBIE Read/Write Account & Transaction Information (AIS) standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication. Included as the OBIE v4.0 standard specific
  name: UK Open Banking Account & Transaction Information API (OBIE Standard)
  slug: uk-open-banking-account-information-api
- description: Shared OBIE Read/Write Payment Initiation (PIS) standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 SCA. Included as the OBIE v4.0 standard specification, not a confirmed Recognise Bank cont
  name: UK Open Banking Payment Initiation API (OBIE Standard)
  slug: uk-open-banking-payment-initiation-api
- description: Shared OBIE Read/Write Confirmation of Funds (CBPII) standard, FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 SCA. Included as the OBIE v4.0 standard specification, not a confirmed Recognise Bank
  name: UK Open Banking Confirmation of Funds API (OBIE Standard)
  slug: uk-open-banking-confirmation-of-funds-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recognise-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://recognisebank.co.uk/responsible-disclosure-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recognise-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/recognise-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/recognise-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recognise-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/recognise-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recognise-bank-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recognise-bank-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recognise-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://recognisebank.co.uk/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recognisebank/
- group: company
  title: ''
  type: Blog
  url: https://recognisebank.co.uk/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://recognisebank.co.uk/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recognisebank.co.uk/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recognisebank.co.uk/privacy-notice/
created: '2026-07-23'
description: Recognise Bank Limited is a UK challenger bank focused on the SME sector and the personal and business savings markets, offering fixed-rate, notice, and easy-access savings accounts alongside secured SME lending such as bridging loans and commercial mortgages. Formed out of AIM-listed City of London Group and now majority owned by Gibraltar-based Parasol V27 Limited (the Ruth Parasol family office), it is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority under FRN 849404, with deposits protected by the FSCS. As a deposit-and-lending institution that does not offer payment/current accounts, Recognise Bank is not one of the CMA9 and publishes no dedicated developer portal, Open Banking Open Data endpoint, or Read/Write API surface at review time; the UK Open Banking (OBIE / PSD2) API families are represented here as the shared industry standard the bank would conform to if it exposed regulated account and payment interfaces, not
  as confirmed Recognise-operated endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Recognise Bank
nav: Providers
network: true
overview: 'Recognise Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including UK Open Banking Open Data API (OBIE Standard), UK Open Banking Account & Transaction Information API (OBIE Standard), UK Open Banking Payment Initiation API (OBIE Standard), and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Recognise Bank''s developer surface includes authentication, engineering blog, and 14 more developer resources.'
random_paper: 39
scopes:
- name: Recognise Bank Scopes
  scope_count: 3
  slug: recognise-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.7
  delta: -3.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.6
    developer_ergonomics: 13.0
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 10.5
  previous_composite: 40.3
  provenance:
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
    score: 78.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Recognise Bank Authentication
  slug: recognise-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Recognise Bank Domain Security
  slug: recognise-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recognise Bank Vulnerability Disclosure
  slug: recognise-bank-vulnerability-disclosure
  summary_line: contact published
slug: recognise-bank
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Savings
- SME Lending
- Fintech
- Account Information
website: https://recognisebank.co.uk/
---
