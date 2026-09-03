---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  - '{''url'': ''https://www.finicity.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.mastercard.com/us/en/business/open-finance.html — a different registrable domain (finicity.com -> mastercard.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-03'
api_count: 1
apis:
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
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Micro entries and account verification
  name: Finicity Account Validation Assistance API
  slug: finicity-account-validation-assistance-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch or refresh customer accounts
  name: Finicity Accounts API
  slug: finicity-accounts-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch simple customer accounts
  name: Finicity Accounts (Simple) API
  slug: finicity-accounts-simple-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Register and assign apps to customers
  name: Finicity App Registration API
  slug: finicity-app-registration-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate authentication tokens and manage credentials
  name: Finicity Authentication API
  slug: finicity-authentication-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Balance Analytics for businesses
  name: Finicity Balance Analytics API
  slug: finicity-balance-analytics-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch account statements and generate reports asynchronously
  name: Finicity Bank Statements API
  slug: finicity-bank-statements-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Create and manage business associated with customers in order to use Balance Analytics or Cash Flow Analytics
  name: Finicity Businesses API
  slug: finicity-businesses-api-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Cash Flow Analytics for business
  name: Finicity Cash Flow Analytics API
  slug: finicity-cash-flow-analytics-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate cash flow reports asynchronously
  name: Finicity Cash Flow API
  slug: finicity-cash-flow-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Allow customers to log into their financial institutions and grant Finicity authorization
  name: Finicity Connect API
  slug: finicity-connect-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Allow customers to log into their financial institutions and grant Finicity authorization
  name: Finicity Connect Components API
  slug: finicity-connect-components-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate consumer foresight analytics reports
  name: Finicity Consumer Foresight API
  slug: finicity-consumer-foresight-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Create and manage consumers associated with customers in order to use report services
  name: Finicity Consumers API
  slug: finicity-consumers-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: APIs to retrieve customer authorization details
  name: Finicity Customer Authorization Details API
  slug: finicity-customer-authorization-details-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Enroll and manage customers
  name: Finicity Customers API
  slug: finicity-customers-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Manage data sharing consents
  name: Finicity Data Sharing Consent API
  slug: finicity-data-sharing-consent-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Match the request details to the Institution account holder details
  name: Finicity Identity API
  slug: finicity-identity-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Search and fetch financial institutions
  name: Finicity Institutions API
  slug: finicity-institutions-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Upload pay statements
  name: Finicity Pay Statements API
  slug: finicity-pay-statements-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Any or all of the Payments endpoints in one API call
  name: Finicity Payment Enablement Bundle API
  slug: finicity-payment-enablement-bundle-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Payment History Report for business
  name: Finicity Payment History Report API
  slug: finicity-payment-history-report-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Predict a transaction's likelihood to settle
  name: Finicity Payment Success Indicator API
  slug: finicity-payment-success-indicator-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch ACH details and account balances
  name: Finicity Payments API
  slug: finicity-payments-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate portfolios of the most recent reports
  name: Finicity Portfolios API
  slug: finicity-portfolios-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch generated reports when ready
  name: Finicity Reports API
  slug: finicity-reports-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch merchant location matches and generate reports
  name: Finicity Small Business Credit Analytics API
  slug: finicity-small-business-credit-analytics-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate and manage access keys for other partners
  name: Finicity Third Party Access API
  slug: finicity-third-party-access-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Enhance the transaction data set
  name: Finicity Transaction Data Enrichment API
  slug: finicity-transaction-data-enrichment-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch customer and account transactions and generate reports asynchronously
  name: Finicity Transactions API
  slug: finicity-transactions-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Fetch details of the deposit and bill pay switches
  name: Finicity Transfer API
  slug: finicity-transfer-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Manage TxPush subscriptions
  name: Finicity Tx Push API
  slug: finicity-txpush-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate asset reports asynchronously
  name: Finicity Verify Assets API
  slug: finicity-verify-assets-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: Generate income and employment reports asynchronously
  name: Finicity Verify Income and Employment API
  slug: finicity-verify-income-and-employment-api
- baseURL: https://api.finicity.com
  baseurl_source: declared
  description: APIs for Managing Partner Webhook Event Subscriptions
  name: Finicity Webhook Subscription API
  slug: finicity-webhook-subscription-api
artifact_total: 44
asyncapis:
- description: ''
  name: Finicity Webhooks
  slug: finicity-webhooks
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/mastercard/
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/finicity-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-23'
name: Finicity
nav: Providers
network: true
overview: 'Finicity publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Account Validation Assistance API, Accounts API, Accounts (Simple) API, and 32 more. Tagged areas include Financial-Services, Data Aggregation, Open Finance, Open Banking, and FDX.


  The Finicity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finicity''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 24 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 65.6
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fdx
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 41.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Financial-Services
- Data Aggregation
- Open Finance
- Open Banking
- FDX
- United States
- Payments
- Financial Data
website: https://www.finicity.com/
---
