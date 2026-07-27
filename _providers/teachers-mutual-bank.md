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
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Teachers Mutual Bank Banking Account Balances API
  slug: teachers-mutual-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Teachers Mutual Bank Banking Account Direct Debits API
  slug: teachers-mutual-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Teachers Mutual Bank Banking Account Scheduled Payments API
  slug: teachers-mutual-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Teachers Mutual Bank Banking Account Transactions API
  slug: teachers-mutual-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Teachers Mutual Bank Banking Accounts API
  slug: teachers-mutual-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Teachers Mutual Bank Banking Payees API
  slug: teachers-mutual-bank-banking-payees-api
- description: Banking Product endpoints
  name: Teachers Mutual Bank Banking Products API
  slug: teachers-mutual-bank-banking-products-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teachers-mutual-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/teachers-mutual-bank-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/teachers-mutual-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/teachers-mutual-bank-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/teachers-mutual-bank-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/teachers-mutual-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/teachers-mutual-bank-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/teachers-mutual-bank-scopes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/teachers-mutual-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/teachers-mutual-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teachers-mutual-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/teachers-mutual-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tmbank.com.au/open-banking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tmbank.com.au/important-information
- group: company
  title: ''
  type: Website
  url: https://www.tmbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tmbank.com.au/open-banking
- group: docs
  title: ''
  type: Documentation
  url: https://www.tmbank.com.au/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teachers-mutual-bank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tmbank.com.au/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.tmbank.com.au/security
- group: operate
  title: ''
  type: Support
  url: https://www.tmbank.com.au/contact
- group: other
  title: ''
  type: ParentOrganization
  url: https://www.tmbl.com.au/
created: '2026-07-20'
description: Teachers Mutual Bank is an Australian customer-owned mutual bank and a brand of Teachers Mutual Bank Limited (TMBL), an authorised deposit-taking institution (ADI) regulated by APRA that also operates UniBank, Firefighters Mutual Bank, Health Professionals Bank and Hiver. As a member-owned bank it returns value to members rather than external shareholders and serves teachers, education staff and the wider community. Under Australia's Consumer Data Right (CDR / Open Banking), Teachers Mutual Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, letting anyone retrieve its banking product catalogue. Consumer (account and transaction) data sharing is available to accredited data recipients through the authenticated CDR channel using the OAuth2 / OpenID Connect FAPI security profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/teachers-mutual-bank.png
layout: provider
mcp_servers:
- description: ''
  name: teachers-mutual-bank-mcp.yml
  slug: teachers-mutual-bank-mcpyml
modified: '2026-07-21'
name: Teachers Mutual Bank
nav: Providers
network: true
overview: 'Teachers Mutual Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Teachers Mutual Bank''s developer surface includes authentication, API reference, getting-started guide, documentation, support, and 20 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 2
  name: Teachers Mutual Bank Rate Limits
  slug: teachers-mutual-bank-rate-limits
scopes:
- name: Teachers Mutual Bank Scopes
  scope_count: 5
  slug: teachers-mutual-bank-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 50.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.0
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 50.4
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teachers-mutual-bank/refs/heads/main/screenshots/teachers-mutual-bank-2026-07-21T114753.png
security:
- kind: authentication
  name: Teachers Mutual Bank Authentication
  slug: teachers-mutual-bank-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Teachers Mutual Bank Domain Security
  slug: teachers-mutual-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: teachers-mutual-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.tmbank.com.au/
---
