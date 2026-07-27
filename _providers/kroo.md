---
access_model:
  confidence: medium
  label: TPP onboarding · FAPI-secured
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 80.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kroo Agentic Access
  operation_count: 74
  slug: kroo-agentic-access
  summary_line: 74 operations · 20 acting
api_count: 3
apis:
- description: Kroo's PSD2 Account Information Service (AIS) dedicated interface, conformant to the OBIE Read/Write Account and Transaction API Standard. Lets FCA-authorised AISP third parties retrieve, with custome
  name: Kroo Account and Transaction Information API
  slug: kroo-account-information-api
- description: 'Kroo''s PSD2 Payment Initiation Service (PIS) dedicated interface, conformant to the OBIE Read/Write Payment Initiation API Standard. Lets FCA-authorised PISP third parties initiate domestic payments, '
  name: Kroo Payment Initiation API
  slug: kroo-payment-initiation-api
- description: Kroo's PSD2 Confirmation of Funds Service (CBPII) dedicated interface, conformant to the OBIE Read/Write Confirmation of Funds API Standard. Lets FCA-authorised CBPII third parties confirm, with custo
  name: Kroo Confirmation of Funds API
  slug: kroo-confirmation-of-funds-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kroo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kroo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kroo-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kroo-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kroo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kroo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kroo.banfico.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kroo.com/open-banking-performance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kroo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.kroo.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.kroo.com/support-is-here
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kroo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kroo.com/privacy-notices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kroobank
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kroo-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kroo-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://kroo.com/.well-known/security.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/kroo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kroo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kroo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kroo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kroo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kroo-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kroo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kroo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-23'
description: Kroo Bank Ltd is a UK app-based challenger bank, founded in 2016 and granted a full UK banking licence by the PRA/FCA in 2021 (restrictions lifted in 2022), that launched its digital-only personal current account in December 2022. Independent and venture-backed rather than mutual or part of a larger group, Kroo offers a fee-free everyday current account, interest-paying balances and "Kroo Pots", fee-free spending abroad, and FSCS deposit protection up to GBP 85,000. As an FCA-authorised ASPSP under PSD2, Kroo is a regulated Open Banking provider (though not one of the nine CMA9-mandated banks and, as a branchless digital bank, it publishes no Open Data reference APIs for ATMs or branches). It exposes the UK Open Banking Implementation Entity (OBIE) Read/Write API family - Account and Transaction Information, Payment Initiation, and Confirmation of Funds - through a Banfico-hosted developer portal at developer.kroo.banfico.io, secured with FAPI-grade OAuth2/OIDC, PSD2 strong
  customer authentication implemented as a CIBA decoupled (poll-mode) flow, and mutual-TLS client authentication using OBIE/eIDAS certificates, validated with the OpenID Foundation conformance suite.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: kroo-mcp.yml
  slug: kroo-mcpyml
modified: '2026-07-23'
name: Kroo
nav: Providers
network: true
overview: 'Kroo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account and Transaction Information API, Payment Initiation API, and Confirmation of Funds API. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Kroo''s developer surface includes authentication, documentation, engineering blog, support, and 22 more developer resources.'
random_paper: 35
scopes:
- name: Kroo Scopes
  scope_count: 3
  slug: kroo-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.0
    developer_ergonomics: 50.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 48.3
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 89.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kroo/refs/heads/main/screenshots/kroo-2026-07-25T224303.png
security:
- kind: authentication
  name: Kroo Authentication
  slug: kroo-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Kroo Domain Security
  slug: kroo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kroo Vulnerability Disclosure
  slug: kroo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kroo
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
- Fintech
website: https://www.kroo.com/
---
