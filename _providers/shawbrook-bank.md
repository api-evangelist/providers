---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Shawbrook Bank Agentic Access
  operation_count: 86
  slug: shawbrook-bank-agentic-access
  summary_line: 86 operations · 20 acting
api_count: 4
apis:
- description: UK Open Banking Open Data API — the PUBLIC, unauthenticated reference-data surface (ATM locations, branches, personal and business current accounts, unsecured SME loans, commercial credit cards) defin
  name: Shawbrook Open Data API (OBIE Standard, Unverified)
  slug: shawbrook-open-data-api
- description: UK Open Banking Read/Write Account & Transaction Information API (AISP) as defined by the OBIE Account and Transaction API Specification v4.0.1 (OpenAPI 3.0.0). FAPI-secured — OAuth2/OIDC authorizatio
  name: Shawbrook Account & Transaction Information API (AIS, OBIE Standard, Unverified)
  slug: shawbrook-account-transaction-api
- description: 'UK Open Banking Read/Write Payment Initiation API (PISP) as defined by the OBIE Payment Initiation API Specification v4.0.1 (OpenAPI 3.0.0). FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong '
  name: Shawbrook Payment Initiation API (PIS, OBIE Standard, Unverified)
  slug: shawbrook-payment-initiation-api
- description: 'UK Open Banking Read/Write Confirmation of Funds API (CBPII) as defined by the OBIE Confirmation of Funds API Specification v4.0.1 (OpenAPI 3.0.0). FAPI-secured with OAuth2/OIDC, mutual-TLS, and PSD2 '
  name: Shawbrook Confirmation of Funds API (CBPII, OBIE Standard, Unverified)
  slug: shawbrook-confirmation-of-funds-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shawbrook-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shawbrook-bank-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shawbrook-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shawbrook-bank-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shawbrook-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shawbrook-bank-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shawbrook-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shawbrook-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shawbrook-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shawbrook-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shawbrook-bank-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shawbrook-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/shawbrook-bank-account-info-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.shawbrook.co.uk/
- group: company
  title: ''
  type: About
  url: https://www.shawbrook.co.uk/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.shawbrook.co.uk/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.shawbrook.co.uk/help/
- group: operate
  title: ''
  type: Contact
  url: https://www.shawbrook.co.uk/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shawbrook.co.uk/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shawbrook-bank/
created: '2026-07-23'
description: 'Shawbrook Bank Limited is a specialist UK savings and lending bank (trading as Shawbrook, part of Shawbrook Group plc, which listed on the London Stock Exchange in October 2025 after being owned by a consortium led by BC Partners and Pollen Street Capital since 2017). It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA, and its deposits are protected by the Financial Services Compensation Scheme. Shawbrook focuses on personal and business savings and specialist lending (property finance, SME and asset finance, and consumer lending) rather than personal current accounts, so it is not one of the nine CMA-mandated banks (CMA9). As an FCA-authorised deposit-taker it operates within the UK Open Banking / PSD2 framework: it consumes Open Banking (using account verification via Consents.Online to confirm customers'' linked nominated accounts) more than it publishes ASPSP surfaces. As of this review Shawbrook does not
  operate a public developer portal, and no Shawbrook Open Data (ATM/branch/product) endpoint or bank-specific Read/Write API host could be confirmed live; the OBIE Open Data and Read/Write API families are represented here as the shared Open Banking standard that an FCA-authorised ASPSP conforms to, not as verified Shawbrook contracts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Shawbrook Bank
nav: Providers
network: true
overview: 'Shawbrook Bank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Shawbrook Open Data API (OBIE Standard, Unverified), Shawbrook Account & Transaction Information API (AIS, OBIE Standard, Unverified), Shawbrook Payment Initiation API (PIS, OBIE Standard, Unverified), and 1 more. Tagged areas include Financial Services, Banking, Savings, Specialist Lending, and Open Banking.


  Shawbrook Bank''s developer surface includes authentication, engineering blog, support, and 18 more developer resources.'
random_paper: 47
scopes:
- name: Shawbrook Bank Scopes
  scope_count: 3
  slug: shawbrook-bank-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 33.9
  delta: -1.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.6
    developer_ergonomics: 19.0
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Shawbrook Bank Authentication
  slug: shawbrook-bank-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Shawbrook Bank Domain Security
  slug: shawbrook-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shawbrook-bank
tags:
- Financial Services
- Banking
- Savings
- Specialist Lending
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
website: https://www.shawbrook.co.uk/
---
