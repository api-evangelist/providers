---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Tsb Bank Agentic Access
  operation_count: 31
  slug: tsb-bank-agentic-access
  summary_line: 31 operations · 6 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: TSB's OBIE Read/Write Account and Transaction Information (AIS) API, providing authorised third-party providers read access to account, balance, transaction, beneficiary, standing order, direct debit,
  name: TSB Account and Transaction Information API (AIS)
  slug: tsb-account-transaction-information-api
- description: TSB's OBIE Read/Write Payment Initiation (PIS) API, enabling authorised third-party providers to initiate domestic and scheduled payments and standing orders on behalf of consenting customers. FAPI-se
  name: TSB Payment Initiation API (PIS)
  slug: tsb-payment-initiation-api
- description: TSB's OBIE Read/Write Confirmation of Funds (CBPII) API, allowing authorised card-based payment instrument issuers to confirm whether funds are available on a customer account. FAPI-secured with OAuth
  name: TSB Confirmation of Funds API (CBPII)
  slug: tsb-confirmation-of-funds-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting ATM data
  name: TSB Bank ATM API
  slug: tsb-bank-atm-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: The Authorization Server APIs API from TSB Bank — 9 operation(s) for authorization server apis.
  name: TSB Bank Authorization Server APIs API
  slug: tsb-bank-authorization-server-apis-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting Business Current Account data
  name: TSB Bank BCA API
  slug: tsb-bank-bca-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting Branch data
  name: TSB Bank Branch API
  slug: tsb-bank-branch-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting Commercial Credit Card data
  name: TSB Bank CCC API
  slug: tsb-bank-ccc-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting Personal Current Account data
  name: TSB Bank PCA API
  slug: tsb-bank-pca-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: The Resource Server APIs API from TSB Bank — 2 operation(s) for resource server apis.
  name: TSB Bank Resource Server APIs API
  slug: tsb-bank-resource-server-apis-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: Endpoint for getting Unsecured SME Loan data
  name: TSB Bank SME API
  slug: tsb-bank-sme-api
- baseURL: https://apis.tsb.co.uk
  baseurl_source: declared
  description: The Token Server APIs API from TSB Bank — 3 operation(s) for token server apis.
  name: TSB Bank Token Server APIs API
  slug: tsb-bank-token-server-apis-api
artifact_total: 20
collections:
- collection_type: open
  name: Open Data API
  slug: open-obie-open-data
- collection_type: open
  name: OTK Server APIs
  slug: open-tsb-bank-oauth-server
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tsb-bank-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tsb-bank-oauth-server-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/tsb-bank-obie-open-data-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tsb-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tsb-bank-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tsb-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tsb-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tsb-bank-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/tsb-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tsb-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tsb-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tsb-bank-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tsb-bank-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tsb-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tsb.co.uk/.well-known/security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tsb-bank-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tsb-bank-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tsb-bank-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tsb-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tsb-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tsb.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.developer.tsb.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tsb.co.uk/help-and-support/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tsb-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tsb.co.uk/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tsb.co.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.tsb.co.uk/help-and-support/
created: '2026-07-23'
description: 'TSB Bank plc is a British retail and commercial bank headquartered in Edinburgh, offering current accounts, savings, mortgages, personal loans, credit cards, and insurance to personal and business customers across the United Kingdom. Spun out of Lloyds Banking Group in 2013 and listed before being acquired in 2015, TSB is a wholly owned subsidiary of the Spanish banking group Banco Sabadell. It is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the PRA. As an FCA-authorised account servicing payment service provider (ASPSP) under PSD2, TSB participates in UK Open Banking and publishes its APIs conformant to the Open Banking Implementation Entity (OBIE) standards through a public developer portal at apis.developer.tsb.co.uk. TSB is not one of the nine CMA-mandated banks (CMA9) but implements the same OBIE Open Data and Read/Write API family: unauthenticated Open Data reference APIs plus FAPI-secured Account and Transaction
  Information (AIS), Payment Initiation (PIS), and Confirmation of Funds (CBPII) services secured with OAuth2/OIDC, mutual-TLS, and PSD2 strong customer authentication.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: TSB Bank MCP Server
  slug: tsb-bank-mcp-server
modified: '2026-07-23'
name: TSB Bank
nav: Providers
network: true
overview: 'TSB Bank publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ATM API, Authorization Server APIs API, BCA API, and 6 more. Tagged areas include Financial-Services, Banking, Open Banking, PSD2, and OBIE.


  TSB Bank''s developer surface includes authentication, documentation, support, and 25 more developer resources.'
random_paper: 9
scopes:
- name: Tsb Bank Scopes
  scope_count: 9
  slug: tsb-bank-scopes
  summary_line: 9 scopes · implicit
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 37.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tsb-bank/refs/heads/main/screenshots/tsb-bank-2026-09-02T164446.png
security:
- kind: authentication
  name: Tsb Bank Authentication
  slug: tsb-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Tsb Bank Domain Security
  slug: tsb-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tsb Bank Vulnerability Disclosure
  slug: tsb-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tsb-bank
tags:
- Financial-Services
- Banking
- Open Banking
- PSD2
- OBIE
- United Kingdom
- Payments
- Account Information
- FAPI
- Fintech
website: https://www.tsb.co.uk/
---
