---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
api_count: 7
apis:
- description: Consumer-permissioned account and transaction aggregation across banks, credit unions, cards, loans and investment accounts, delivering account details, balances and categorized transactions.
  name: Finicity Aggregation (Accounts & Transactions) API
  slug: finicity-aggregation-api
- description: Hosted, embeddable account-linking experience that lets a consumer authenticate to their financial institution and permission data sharing, returning the linked accounts to the partner application.
  name: Finicity Connect
  slug: finicity-connect
- description: Generates a consumer-permissioned Verification of Assets report from aggregated account and balance data for mortgage, lending and underwriting workflows, an FCRA-regulated consumer report product.
  name: Finicity Verification of Assets (VoA) API
  slug: finicity-verification-of-assets-api
- description: Derives income streams and employment signals from permissioned transaction and payroll data to produce Verification of Income and Verification of Employment reports for lending decisions.
  name: Finicity Verification of Income & Employment (VoIE) API
  slug: finicity-verification-of-income-employment-api
- description: Analyzes permissioned transaction history to produce cash-flow, income and expense insights used for prequalification, credit decisioning and financial-health scoring.
  name: Finicity Transaction Analysis (Cash Flow) API
  slug: finicity-transaction-analysis-api
- description: Validates account ownership and status for ACH and account-funding flows, returning account, routing and owner verification signals to reduce returned payments and fraud.
  name: Finicity Payments (Account Validation) API
  slug: finicity-payments-account-validation-api
- description: FDX-aligned, consumer-permissioned open-banking data-access surface through which Finicity, as a founding Financial Data Exchange participant, shares financial data on behalf of connected institutions
  name: Finicity Open Banking Data Access (FDX)
  slug: finicity-open-banking-data-access
artifact_total: 11
asyncapis:
- description: ''
  name: Finicity Webhooks
  slug: finicity-webhooks
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/finicity-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finicity-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/finicity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/finicity-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/finicity-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finicity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finicity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/finicity-openbanking-us-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/finicity-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finicity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finicity-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.mastercard.com/open-banking-us/documentation/status/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/finicity-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finicity-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/finicity-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/finicity-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finicity-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/finicity-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.finicity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mastercard.com/open-banking-us/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mastercard.com/open-banking-us/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mastercard.com/open-banking-us/documentation/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mastercard.com/open-banking-us/documentation/test-the-apis/
- group: build
  title: ''
  type: Postman
  url: https://github.com/Mastercard/open-banking-us-postman
- group: operate
  title: ''
  type: Support
  url: https://developer.mastercard.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://developer.mastercard.com/product/open-banking/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mastercard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finicity/
created: '2026-07-23'
description: Finicity, LLC is a Utah-based financial-data aggregator and open-finance technology provider acquired by Mastercard in 2020 and now operating as Mastercard Open Banking (US) within Mastercard Open Finance. It is not a chartered bank but a consumer-permissioned data-access and decisioning platform (and an FCRA-regulated consumer reporting agency for its verification products), providing account and transaction aggregation, Verification of Assets, Income and Employment, transaction and cash-flow analysis, statements, and account validation for ACH payments. Finicity runs a first-party developer portal (developer.mastercard.com/open-banking-us, formerly developer.finicity.com and docs.finicity.com, both of which now redirect) over the live api.finicity.com host, is a founding participant in the Financial Data Exchange (FDX) with FDX-aligned data-sharing APIs, and positions its platform as an enabler of CFPB Section 1033 personal financial data rights. Public product documentation
  is openly reachable, but the full API reference and any machine-readable OpenAPI specification are partner-gated behind Mastercard Developers credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: finicity-mcp.yml
  slug: finicity-mcpyml
modified: '2026-07-23'
name: Finicity
nav: Providers
network: true
overview: 'Finicity publishes 1 API on the [APIs.io](https://apis.io/) network: Aggregation (Accounts & Transactions) API. Tagged areas include Financial Services, Data Aggregation, Open Finance, Open Banking, and FDX.


  The Finicity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finicity''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 118
score:
  band: developing
  composite: 52.1
  delta: 6.6
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 68.5
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 45.5
  provenance:
    conformance: derived
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
    score: 41.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/finicity/refs/heads/main/screenshots/finicity-2026-07-25T214523.png
security:
- kind: authentication
  name: Finicity Authentication
  slug: finicity-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Finicity Domain Security
  slug: finicity-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: finicity
tags:
- Financial Services
- Data Aggregation
- Open Finance
- Open Banking
- FDX
- United States
- Payments
- Financial Data
website: https://www.finicity.com/
---
