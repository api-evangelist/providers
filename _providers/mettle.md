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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mettle Agentic Access
  operation_count: 12
  slug: mettle-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- description: OBIE Read/Write Account & Transaction Information (AIS) API for Mettle business current accounts, exposing accounts, balances, transactions, and related resources to FCA-authorised third parties. FAPI
  name: Mettle Account and Transaction API
  slug: mettle-account-transaction-api
- description: OBIE Read/Write Payment Initiation Services (PIS) API for Mettle, allowing FCA-authorised third parties to initiate domestic and other payments from a customer's Mettle account with their consent. FAP
  name: Mettle Payment Initiation API
  slug: mettle-payment-initiation-api
- description: OBIE Read/Write Confirmation of Funds (CBPII) API for Mettle, letting card-based payment instrument issuers confirm whether funds are available on a customer's Mettle account. FAPI-secured with OAuth2
  name: Mettle Confirmation of Funds API
  slug: mettle-confirmation-of-funds-api
- description: Endpoint for getting ATM data
  name: Mettle ATM API
  slug: mettle-atm-api
- description: Endpoint for getting Business Current Account data
  name: Mettle BCA API
  slug: mettle-bca-api
- description: Endpoint for getting Branch data
  name: Mettle Branch API
  slug: mettle-branch-api
- description: Endpoint for getting Commercial Credit Card data
  name: Mettle CCC API
  slug: mettle-ccc-api
- description: Endpoint for getting Personal Current Account data
  name: Mettle PCA API
  slug: mettle-pca-api
- description: Endpoint for getting Unsecured SME Loan data
  name: Mettle SME API
  slug: mettle-sme-api
artifact_total: 15
collections:
- collection_type: open
  name: Open Data API
  slug: open-mettle-open-data-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mettle-capability-edges.yml
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
  name: Mettle MCP Server
  slug: mettle-mcp-server
modified: '2026-07-23'
name: Mettle
nav: Providers
network: true
overview: 'Mettle publishes 6 APIs on the [APIs.io](https://apis.io/) network, including ATM API, BCA API, Branch API, and 3 more. Tagged areas include Financial-Services, Banking, Business Banking, Open Banking, and PSD2.


  Mettle''s developer surface includes authentication, sandbox, documentation, engineering blog, support, and 23 more developer resources.'
random_paper: 0
scopes:
- name: Mettle Scopes
  scope_count: 4
  slug: mettle-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 32.7
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 39.5
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
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mettle/refs/heads/main/screenshots/mettle-2026-08-07T172804.png
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
- Financial-Services
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
