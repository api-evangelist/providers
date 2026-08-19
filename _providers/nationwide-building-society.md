---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: Public, unauthenticated OBIE Open Data API listing the location, accessibility, supported currencies, and services of Nationwide ATMs across the UK. Confirmed live (HTTP 200, application/json) at v2.2
  name: Nationwide ATM Locator API
  slug: nationwide-atm-locator-api
- description: Public, unauthenticated OBIE Open Data API listing Nationwide branch locations, opening hours, accessibility, and services. Documented Open Data type on the developer portal (the v2.2 branches path re
  name: Nationwide Branch Locator API
  slug: nationwide-branch-locator-api
- description: Public, unauthenticated OBIE Open Data API publishing reference data for Nationwide personal current account products, features, fees, and eligibility. Confirmed live (HTTP 200, application/json) at v
  name: Nationwide Personal Current Accounts API
  slug: nationwide-personal-current-accounts-api
- description: OBIE Read/Write Account and Transaction Information (AIS) API providing consented access to Nationwide account, balance, and transaction data for authorised third-party providers. FAPI-secured (OAuth2
  name: Nationwide Account and Transaction Information API (AIS)
  slug: nationwide-account-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API allowing authorised third-party providers to initiate domestic and other payments from Nationwide accounts with customer consent. FAPI-secured (OAuth2/OIDC
  name: Nationwide Payment Initiation API (PIS)
  slug: nationwide-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) utility API letting a consented card-based payment instrument issuer check whether funds are available on a Nationwide account. FAPI-secured (OAuth2/OIDC,
  name: Nationwide Confirmation of Funds API (CBPII)
  slug: nationwide-confirmation-of-funds-api
- description: OBIE Read/Write Variable Recurring Payments (VRP) API enabling consented sweeping and recurring payment mandates from Nationwide accounts. FAPI-secured (OAuth2/OIDC, mutual-TLS, PSD2 SCA); endpoints u
  name: Nationwide Variable Recurring Payments API (VRP)
  slug: nationwide-variable-recurring-payments-api
artifact_total: 15
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-atm-locator
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-branch-locator
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data-personal-current-accounts
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nationwide-building-society-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nationwide-building-society-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nationwide.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nationwide.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nationwide.co.uk/open-banking
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nationwide.co.uk/open-banking/open-data-apis
- group: operate
  title: ''
  type: Support
  url: https://developer.nationwide.co.uk/open-banking/support/faq
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.nationwide.co.uk/open-banking/support/known-issues
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nationwide-building-society
- group: company
  title: ''
  type: About
  url: https://www.nationwide.co.uk/about-us
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.nationwide.co.uk/open-banking
- group: start
  title: ''
  type: SignUp
  url: https://developer.nationwide.co.uk/
- group: auth
  title: ''
  type: Security
  url: https://www.nationwide.co.uk/help/fraud-and-security/report-security-vulnerability
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nationwide-building-society-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nationwide-building-society-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nationwide-building-society-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nationwide-building-society-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nationwide-building-society-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/nationwide-building-society-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nationwide-building-society-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nationwide-building-society-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nationwide-building-society-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nationwide-building-society-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nationwide-building-society-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nationwide-building-society-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nationwide-building-society-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nationwide-building-society-open-data-discovery.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nationwide-building-society-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/nationwide-building-society-atm-locator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nationwide-building-society-branch-locator-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nationwide-building-society-personal-current-accounts-overlay.yaml
created: '2026-07-23'
description: Nationwide Building Society is the world's largest building society and one of the UK's biggest retail financial services providers, headquartered in Swindon, England. As a mutual it is owned by and run for the benefit of its members rather than external shareholders, offering current accounts, mortgages, savings, and personal loans across a large branch and digital network. Nationwide is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As one of the CMA9 - the nine largest current-account providers mandated by the UK Competition and Markets Authority to deliver Open Banking - Nationwide operates a public developer portal that publishes UK Open Banking APIs conformant to the Open Banking Implementation Entity (OBIE) standards - public, unauthenticated Open Data APIs (ATM and branch locators, personal and business current account product reference data) and FAPI-secured Read/Write APIs for Account and Transaction
  Information (AIS), Payment Initiation (PIS), Confirmation of Funds (CBPII), and Variable Recurring Payments (VRP), secured with OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication using OBIE/eIDAS certificates.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: nationwide-building-society-mcp.yml
  slug: nationwide-building-society-mcpyml
modified: '2026-07-23'
name: Nationwide Building Society
nav: Providers
network: true
overview: 'Nationwide Building Society publishes 3 APIs on the [APIs.io](https://apis.io/) network: Nationwide ATM Locator API, Nationwide Branch Locator API, and Nationwide Personal Current Accounts API. Tagged areas include Financial Services, Banking, Building Society, Open Banking, and PSD2.


  Nationwide Building Society''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, and 26 more developer resources.'
random_paper: 96
scopes:
- name: Nationwide Building Society Scopes
  scope_count: 4
  slug: nationwide-building-society-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.6
  delta: 4.8
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 30.3
    contract_quality: 38.0
    developer_ergonomics: 49.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 40.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
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
    score: 68.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nationwide-building-society/refs/heads/main/screenshots/nationwide-building-society-2026-08-07T184659.png
security:
- kind: authentication
  name: Nationwide Building Society Authentication
  slug: nationwide-building-society-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Nationwide Building Society Domain Security
  slug: nationwide-building-society-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nationwide Building Society Vulnerability Disclosure
  slug: nationwide-building-society-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nationwide-building-society
tags:
- Financial Services
- Banking
- Building Society
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
website: https://www.nationwide.co.uk/
---
