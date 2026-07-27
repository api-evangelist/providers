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
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Regional Australia Bank Banking Account Balances API
  slug: regional-australia-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Regional Australia Bank Banking Account Direct Debits API
  slug: regional-australia-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Regional Australia Bank Banking Account Scheduled Payments API
  slug: regional-australia-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Regional Australia Bank Banking Account Transactions API
  slug: regional-australia-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Regional Australia Bank Banking Accounts API
  slug: regional-australia-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Regional Australia Bank Banking Payees API
  slug: regional-australia-bank-banking-payees-api
- description: Banking Product endpoints
  name: Regional Australia Bank Banking Products API
  slug: regional-australia-bank-banking-products-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regional-australia-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.regionalaustraliabank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.regionalaustraliabank.com.au/help-and-support/data-sharing
- group: operate
  title: ''
  type: Support
  url: https://www.regionalaustraliabank.com.au/help-and-support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/regional-australia-bank
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.regionalaustraliabank.com.au/help-and-support/tools-and-resources/what-is-the-consumer-data-right
- group: start
  title: ''
  type: Portal
  url: https://dashboard.cdr.regionalaustraliabank.com.au/
- group: auth
  title: ''
  type: Authentication
  url: authentication/regional-australia-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/regional-australia-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/regional-australia-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/regional-australia-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/regional-australia-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/regional-australia-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/regional-australia-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/regional-australia-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/regional-australia-bank-llms.txt
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/regional-australia-bank-lifecycle.yml
- group: company
  title: ''
  type: Blog
  url: https://www.regionalaustraliabank.com.au/the-inside-story
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.regionalaustraliabank.com.au/about-us/corporate-documents/policies-and-guides
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.regionalaustraliabank.com.au/about-us/corporate-documents/policies-and-guides
- group: start
  title: ''
  type: Login
  url: https://secure.regionalaustraliabank.com.au/
created: '2026-07-20'
description: Regional Australia Bank is a customer-owned (mutual) authorised deposit-taking institution (ADI) headquartered in Armidale and Port Macquarie, New South Wales. Founded in 1969 as New England Staff Credit Union at the University of New England, it grew through successive credit-union mergers into Community Mutual Group and rebranded as Regional Australia Bank in 2016; it is currently completing a merger with Summerland Bank. As a mutual, its customers are its owners, and it serves more than 100,000 members across regional NSW from roughly 39 locations. As an active ADI it is a designated data holder under Australia's Consumer Data Right (CDR / Open Banking), exposing a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, alongside the accredited-data-recipient consumer data sharing surface secured under the CDR OAuth2/OIDC model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/regional-australia-bank.png
layout: provider
mcp_servers:
- description: ''
  name: regional-australia-bank-mcp.yml
  slug: regional-australia-bank-mcpyml
modified: '2026-07-21'
name: Regional Australia Bank
nav: Providers
network: true
overview: 'Regional Australia Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Regional Australia Bank''s developer surface includes documentation, support, API reference, getting-started guide, developer portal, authentication, engineering blog, and 16 more developer resources.'
random_paper: 5
scopes:
- name: Regional Australia Bank Scopes
  scope_count: 5
  slug: regional-australia-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.0
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 49.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regional-australia-bank/refs/heads/main/screenshots/regional-australia-bank-2026-07-21T114749.png
security:
- kind: authentication
  name: Regional Australia Bank Authentication
  slug: regional-australia-bank-authentication
  summary_line: none/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Regional Australia Bank Domain Security
  slug: regional-australia-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: regional-australia-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Customer-Owned
- Product Reference Data
- Mutual Bank
website: https://www.regionalaustraliabank.com.au/
---
