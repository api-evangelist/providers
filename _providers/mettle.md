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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mettle Agentic Access
  operation_count: 12
  slug: mettle-agentic-access
  summary_line: 12 operations
api_count: 4
apis:
- description: 'Mettle''s public, unsecured UK Open Banking Open Data (Product) API, exposing reference information about the business current accounts Mettle offers to sole traders and limited companies. Conforms to '
  name: Mettle Open Data Product API
  slug: mettle-open-data-product-api
- description: OBIE Read/Write Account & Transaction Information (AIS) API for Mettle business current accounts, exposing accounts, balances, transactions, and related resources to FCA-authorised third parties. FAPI
  name: Mettle Account and Transaction API
  slug: mettle-account-transaction-api
- description: OBIE Read/Write Payment Initiation Services (PIS) API for Mettle, allowing FCA-authorised third parties to initiate domestic and other payments from a customer's Mettle account with their consent. FAP
  name: Mettle Payment Initiation API
  slug: mettle-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for Mettle, letting card-based payment instrument issuers confirm whether funds are available on a customer's Mettle account. FAPI-secured with OAuth2
  name: Mettle Confirmation of Funds API
  slug: mettle-confirmation-of-funds-api
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mettle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mettle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mettle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mettle-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mettle-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bankofapis.com/products/natwest-group-open-banking
- group: design
  title: ''
  type: Conventions
  url: conventions/mettle-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mettle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mettle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mettle-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.bankofapis.com/products/natwest-group-open-banking
- group: design
  title: ''
  type: DataModel
  url: data-model/mettle-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mettle-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mettle-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mettle-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/mettle-open-data-api-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: https://developer.sandbox.natwest.com/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.mettle.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankofapis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankofapis.com/products/natwest-group-open-banking/products-and-locations/documentation/mettle
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankofapis.com/performance/service-interruptions
- group: company
  title: ''
  type: Blog
  url: https://www.mettle.co.uk/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/join-mettle
- group: operate
  title: ''
  type: Support
  url: https://www.mettle.co.uk/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mettle.co.uk/docs/terms-and-conditions/1.5.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mettle.co.uk/privacy-notice/
created: '2026-07-23'
description: Mettle is a digital-only business bank account brand for UK sole traders, freelancers, and small limited companies, wholly owned by NatWest Group and originally built with Capco. It has no physical branches and is run on separate technology from the core NatWest bank, offering an app-based current account with a UK sort code and account number, invoicing, bookkeeping, tax tools, and a free FreeAgent accounting integration. As a NatWest Group brand, Mettle participates in UK Open Banking through NatWest Group's "Bank of APIs" developer platform, publishing PSD2 / OBIE-conformant APIs - a public, unsecured Open Data (Product) API describing its business current accounts, plus the FAPI-secured Read/Write family (Account & Transaction Information, Payment Initiation, and Confirmation of Funds). Read/Write access runs against a live production gateway (api.openbanking.prd-mettle.co.uk) secured with OAuth2/OIDC, mutual-TLS client authentication, and PSD2 strong customer authentication
  using OBIE/eIDAS certificates, onboarded via the Bank of APIs portal. Mettle is delivered under NatWest Group's FCA-authorised banking group and is a challenger/digital proposition rather than one of the CMA9 mandated brands.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: mettle-mcp.yml
  slug: mettle-mcpyml
modified: '2026-07-23'
name: Mettle
nav: Providers
network: true
overview: 'Mettle publishes 1 API on the [APIs.io](https://apis.io/) network: Open Data Product API. Tagged areas include Financial Services, Banking, Business Banking, Open Banking, and PSD2.


  Mettle''s developer surface includes authentication, sandbox, documentation, engineering blog, support, and 22 more developer resources.'
random_paper: 35
scopes:
- name: Mettle Scopes
  scope_count: 4
  slug: mettle-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.6
  delta: -3.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
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
    score: 77.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mettle Authentication
  slug: mettle-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Mettle Domain Security
  slug: mettle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mettle
tags:
- Financial Services
- Banking
- Business Banking
- Open Banking
- PSD2
- OBIE
- FAPI
- United Kingdom
- Payments
- Account Information
- Challenger Bank
- Fintech
website: https://www.mettle.co.uk/
---
