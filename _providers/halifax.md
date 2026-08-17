---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: Public, unauthenticated OBIE Open Data API returning the location and details of every Halifax cashpoint (ATM) in the UK. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data ATM Locator API
  slug: halifax-open-data-atm-locator-api
- description: Public, unauthenticated OBIE Open Data API returning a directory of all Halifax branches in the UK. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data Branch Locator API
  slug: halifax-open-data-branch-locator-api
- description: Public, unauthenticated OBIE Open Data API publishing personal current account product reference data. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data Personal Current Accounts API
  slug: halifax-open-data-personal-current-accounts-api
- description: Public, unauthenticated OBIE Open Data API publishing business current account product reference data. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data Business Current Accounts API
  slug: halifax-open-data-business-current-accounts-api
- description: Public, unauthenticated OBIE Open Data API publishing unsecured SME loan product reference data. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data Unsecured SME Loans API
  slug: halifax-open-data-unsecured-sme-loans-api
- description: Public, unauthenticated OBIE Open Data API publishing commercial credit card product reference data. Confirmed live (HTTP 200, JSON) at the v2.2 base.
  name: Halifax Open Data Commercial Credit Cards API
  slug: halifax-open-data-commercial-credit-cards-api
- description: OBIE Read/Write Account and Transaction Information (AIS) API for authorised AISPs. FAPI-secured (OAuth2/OIDC, PSD2 SCA, mTLS, OBIE/eIDAS certificates); onboarded via the Lloyds Banking Group Develope
  name: Halifax Account and Transaction Information API (AIS)
  slug: halifax-account-transaction-information-api
- description: OBIE Read/Write Payment Initiation (PIS) API for authorised PISPs. FAPI-secured (OAuth2/OIDC, PSD2 SCA, mTLS, OBIE/eIDAS certificates); onboarded via the Lloyds Banking Group Developer Portal. Base pa
  name: Halifax Payment Initiation API (PIS)
  slug: halifax-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for authorised CBPIIs. FAPI-secured (OAuth2/OIDC, PSD2 SCA, mTLS, OBIE/eIDAS certificates); onboarded via the Lloyds Banking Group Developer Portal. B
  name: Halifax Confirmation of Funds API (CBPII)
  slug: halifax-confirmation-of-funds-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Data API
  slug: open-openbanking-opendata-standard-swagger
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/halifax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.halifax.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lloydsbanking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lloydsbanking.com/prod01/lbg/opendata_halifax
- group: operate
  title: ''
  type: Support
  url: https://developer.lloydsbanking.com/prod01/lbg/lbg-support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/halifax
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.halifax.co.uk/aboutonline/legal-information.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.halifax.co.uk/aboutonline/security-and-privacy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lloydsbanking.com/prod01/lbg/get-started
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.lloydsbanking.com/prod01/lbg/home
- group: auth
  title: ''
  type: Authentication
  url: authentication/halifax-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/halifax-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/halifax-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/halifax-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/halifax-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/halifax-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/halifax-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/halifax-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/halifax-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/halifax-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/halifax-opendata-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/halifax-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-23'
description: 'Halifax is a major British high-street banking brand serving personal and business customers with current accounts, savings, mortgages, credit cards, loans, and insurance. It operates as a trading division of Bank of Scotland plc, a wholly owned subsidiary of Lloyds Banking Group, and is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As one of the UK Open Banking CMA9 mandated ASPSPs, Halifax publishes the full Open Banking Implementation Entity (OBIE) API surface: a set of PUBLIC, unauthenticated Open Data APIs (ATM and branch locators plus personal current account, business current account, unsecured SME loan, and commercial credit card product reference data) served live at api.halifax.co.uk, and the FAPI-secured OBIE Read/Write APIs for Account and Transaction Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII). Read/Write access is delivered through the shared Lloyds Banking Group
  Developer Portal that also covers the Lloyds Bank and Bank of Scotland brands, secured with OAuth2/OIDC, PSD2 strong customer authentication, mutual-TLS, and OBIE/eIDAS certificates.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: halifax-mcp.yml
  slug: halifax-mcpyml
modified: '2026-07-24'
name: Halifax
nav: Providers
network: true
overview: 'Halifax publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Open Data ATM Locator API, Open Data Branch Locator API, Open Data Personal Current Accounts API, and 3 more. Tagged areas include Financial Services, Banking, Open Banking, PSD2, and OBIE.


  Halifax''s developer surface includes documentation, support, getting-started guide, authentication, sandbox, and 18 more developer resources.'
random_paper: 137
scopes:
- name: Halifax Scopes
  scope_count: 4
  slug: halifax-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 39.6
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 41.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/halifax/refs/heads/main/screenshots/halifax-2026-07-25T220540.png
security:
- kind: authentication
  name: Halifax Authentication
  slug: halifax-authentication
  summary_line: none/oauth2/mutualTLS · 4 schemes
- kind: domain-security
  name: Halifax Domain Security
  slug: halifax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: halifax
tags:
- Financial Services
- Banking
- Open Banking
- PSD2
- OBIE
- CMA9
- United Kingdom
- Payments
- Account Information
- Open Data
website: https://www.halifax.co.uk/
---
