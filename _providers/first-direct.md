---
access_model:
  confidence: medium
  label: Self-serve signup (HSBC developer portal) · public Open Data
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - open-data
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: true
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: First Direct Agentic Access
  operation_count: 86
  slug: first-direct-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: Public, unauthenticated OBIE Open Data API exposing first direct product reference data - personal current accounts and related read-only reference data - published on the shared HSBC Open Data host w
  name: first direct Open Data API
  slug: first-direct-open-data-api
- description: 'OBIE Read/Write Account and Transaction Information (AIS) API for first direct accounts, exposed through HSBC''s developer platform. FAPI-secured with OAuth2/OIDC, mutual-TLS client authentication and '
  name: first direct Account and Transaction Information API (AIS)
  slug: first-direct-account-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API for first direct accounts, exposed through HSBC's developer platform. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authentication; re
  name: first direct Payment Initiation API (PIS)
  slug: first-direct-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for first direct accounts, exposed through HSBC's developer platform. FAPI-secured with OAuth2/OIDC, mutual-TLS and PSD2 strong customer authenticatio
  name: first direct Confirmation of Funds API (CBPII)
  slug: first-direct-confirmation-of-funds-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/first-direct-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-direct-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/first-direct-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-direct-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/first-direct-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/first-direct-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/first-direct-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-direct-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/first-direct-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://standards.openbanking.org.uk/operational-guidelines/change-and-communication-management/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/first-direct-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/first-direct-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/first-direct-sandbox.yml
- group: build
  title: ''
  type: Postman
  url: https://develop.hsbc.com/knowledge-article/get-started-open-banking-apis
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-direct-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/first-direct-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-direct-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hsbc.com/.well-known/security.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-direct-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/first-direct-obie-account-info-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/first-direct-obie-payment-initiation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/first-direct-obie-confirmation-funds-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/first-direct-obie-opendata-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://develop.hsbc.com/knowledge-article/get-started-open-banking-apis
- group: start
  title: ''
  type: SignUp
  url: https://develop.hsbc.com/
- group: company
  title: ''
  type: Website
  url: https://www.firstdirect.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://develop.hsbc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.hsbc.com/knowledge-article/get-started-open-banking-apis
- group: other
  title: ''
  type: OpenBanking
  url: https://www.firstdirect.com/ways-to-bank/open-banking/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hsbc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-direct
- group: operate
  title: ''
  type: Support
  url: https://www.firstdirect.com/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.firstdirect.com/legals/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.firstdirect.com/privacy/
created: '2026-07-23'
description: first direct is a telephone- and internet-based retail bank and a division of HSBC UK Bank plc, headquartered in Leeds, England and launched in 1989. It offers personal current accounts, savings, credit cards, loans, mortgages and insurance to UK consumers with a reputation for customer service, operating with no physical branches of its own. As an HSBC brand, first direct participates in the UK Open Banking regime under HSBC UK - one of the nine CMA9 banks mandated by the Competition and Markets Authority - and is regulated by the Financial Conduct Authority (FCA) and Prudential Regulation Authority (PRA). Its Open Banking surfaces conform to the Open Banking Implementation Entity (OBIE / Open Banking Limited) standards - a public, unauthenticated Open Data API (personal current account product reference data, ATM and branch locators, published on the shared HSBC api.hsbc.com host where "first direct" appears as a distinct brand) and the FAPI-secured OBIE Read/Write APIs -
  Account and Transaction Information (AIS), Payment Initiation (PIS) and Confirmation of Funds (CBPII) - onboarded and documented through HSBC's developer portal at develop.hsbc.com, which serves the HSBC UK, first direct and M&S Bank brands.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: first direct
nav: Providers
network: true
overview: 'first direct publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Open Data API, Account and Transaction Information API (AIS), Payment Initiation API (PIS), and 1 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  first direct''s developer surface includes authentication, changelog, sandbox, getting-started guide, signup flow, documentation, support, and 28 more developer resources.'
random_paper: 8
scopes:
- name: First Direct Scopes
  scope_count: 3
  slug: first-direct-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.0
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 53.9
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-direct/refs/heads/main/screenshots/first-direct-2026-07-25T214603.png
security:
- kind: authentication
  name: First Direct Authentication
  slug: first-direct-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: First Direct Domain Security
  slug: first-direct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: First Direct Vulnerability Disclosure
  slug: first-direct-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: first-direct
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- Open Data
- HSBC
- Fintech
website: https://www.firstdirect.com/
---
