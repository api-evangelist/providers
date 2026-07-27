---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
api_count: 9
apis:
- description: First-party Westpac payment API (beyond CDR). PayWay is Westpac's merchant payment platform; its public REST API v1 processes real-time credit-card and bank-account payments, refunds, pre-authorisatio
  name: Westpac PayWay REST API
  slug: westpac-payway-rest-api
- description: First-party Westpac payment API (beyond CDR). QuickStream is Westpac's online payment gateway; its public REST API v1 exposes Transactions, Customers, Accounts, Credit Cards, Recurring Payments, PayID
  name: Westpac QuickStream REST API
  slug: westpac-quickstream-rest-api
- description: Banking Account Balance endpoints
  name: Westpac Banking Corporation Banking Account Balances API
  slug: westpac-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Westpac Banking Corporation Banking Account Direct Debits API
  slug: westpac-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Westpac Banking Corporation Banking Account Scheduled Payments API
  slug: westpac-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Westpac Banking Corporation Banking Account Transactions API
  slug: westpac-banking-account-transactions-api
- description: Banking Account endpoints
  name: Westpac Banking Corporation Banking Accounts API
  slug: westpac-banking-accounts-api
- description: Banking Payee endpoints
  name: Westpac Banking Corporation Banking Payees API
  slug: westpac-banking-payees-api
- description: Banking Product endpoints
  name: Westpac Banking Corporation Banking Products API
  slug: westpac-banking-products-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/westpac-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/westpac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.westpac.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.westpac.com.au/about-westpac/innovation/open-banking/
- group: docs
  title: ''
  type: Documentation
  url: https://www.westpac.com.au/about-westpac/innovation/open-banking/product-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/westpac
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/westpac
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westpac.com.au/privacy/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westpac.com.au/content/dam/public/wbc/documents/pdf/aw/WBC_CDR_Policy.pdf
- group: auth
  title: ''
  type: Security
  url: https://www.westpac.com.au/security/how-to-report/responsible-disclosure.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/westpac-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/westpac-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/westpac-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/westpac-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/westpac-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/westpac-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/westpac-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/westpac-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/westpac-browse-products.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/westpac-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/westpac-quickstream-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/westpac-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/westpac-components.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/westpac-decline-codes.yml
- group: auth
  title: ''
  type: Compliance
  url: https://quickstream.westpac.com.au/docs/general/pci-compliance/
- group: start
  title: ''
  type: GettingStarted
  url: https://quickstream.westpac.com.au/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://quickstream.westpac.com.au/docs/quickstreamapi/v1/
created: '2026-07-20'
description: Westpac Banking Corporation is Australia's oldest bank and company, founded in 1817 as the Bank of New South Wales, and is one of the country's "Big Four" banks. Headquartered in Sydney, it is a publicly listed company on the Australian Securities Exchange (ASX:WBC), not a customer-owned mutual, and operates a multi-brand group that includes St.George, BankSA, Bank of Melbourne, and RAMS. As an authorised deposit-taking institution (ADI) regulated by APRA, Westpac is a designated data holder under Australia's Consumer Data Right (CDR / Open Banking) regime and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards. Consumer and account data sharing beyond product reference data is available only to accredited data recipients through the CDR's authenticated, consent-driven channels.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/westpac.png
layout: provider
mcp_servers:
- description: ''
  name: westpac-mcp.yml
  slug: westpac-mcpyml
modified: '2026-07-21'
name: Westpac Banking Corporation
nav: Providers
network: true
overview: 'Westpac Banking Corporation publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Westpac Banking Corporation''s developer surface includes documentation, authentication, changelog, sandbox, getting-started guide, API reference, and 21 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.6
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 51.7
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/westpac/refs/heads/main/screenshots/westpac-2026-07-21T114757.png
security:
- kind: authentication
  name: Westpac Authentication
  slug: westpac-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Westpac Domain Security
  slug: westpac-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Westpac Vulnerability Disclosure
  slug: westpac-vulnerability-disclosure
  summary_line: Bugcrowd
slug: westpac
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.westpac.com.au/
---
