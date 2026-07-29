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
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Us Agentic Access
  operation_count: 19
  slug: bank-of-us-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bank of us Banking Account Balances API
  slug: bank-of-us-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bank of us Banking Account Direct Debits API
  slug: bank-of-us-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bank of us Banking Account Scheduled Payments API
  slug: bank-of-us-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bank of us Banking Account Transactions API
  slug: bank-of-us-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bank of us Banking Accounts API
  slug: bank-of-us-banking-accounts-api
- description: Banking Payee endpoints
  name: Bank of us Banking Payees API
  slug: bank-of-us-banking-payees-api
- description: Banking Product endpoints
  name: Bank of us Banking Products API
  slug: bank-of-us-banking-products-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-us-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-us-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-us-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-us-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-us-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-us-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-of-us-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-us-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-us-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-us-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-us-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-of-us-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bank-of-us-product-lookup.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bank-of-us-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bank-of-us-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bank-of-us-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-us-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://bankofus.com.au/.well-known/security.txt
- group: company
  title: ''
  type: Website
  url: https://www.bankofus.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://bankofus.com.au/open-banking
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bankofus.com.au/open-banking
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#consumer-data-standards-banking-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-us/
- group: company
  title: ''
  type: Blog
  url: https://www.bankofus.com.au/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofus.com.au/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.bankofus.com.au/contact
created: '2026-07-20'
description: Bank of us is Tasmania's only customer-owned bank, a mutual authorised deposit-taking institution (ADI) trading as B&E Ltd (brand "BNE LTD") and headquartered in Launceston, Tasmania. Formed from the former Bass & Equitable Building Society and rebranded to Bank of us in 2016, it is owned by its members rather than shareholders and offers home loans, personal and business banking, savings, and term deposits. As a regulated ADI it participates in Australia's Consumer Data Right (CDR / Open Banking) as a data holder, exposing a public, unauthenticated Product Reference Data (PRD) API that conforms to the Data Standards Body (DSB) Consumer Data Standards, and enabling customers to share account and transaction data with accredited data recipients under ACCC oversight.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-us.png
layout: provider
mcp_servers:
- description: ''
  name: bank-of-us-mcp.yml
  slug: bank-of-us-mcpyml
modified: '2026-07-21'
name: Bank of us
nav: Providers
network: true
overview: 'Bank of us publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of us'' developer surface includes authentication, documentation, API reference, engineering blog, support, and 21 more developer resources.'
random_paper: 23
scopes:
- name: Bank Of Us Scopes
  scope_count: 5
  slug: bank-of-us-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 40.6
  delta: -4.9
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 63.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-us/refs/heads/main/screenshots/bank-of-us-2026-07-21T114712.png
security:
- kind: authentication
  name: Bank Of Us Authentication
  slug: bank-of-us-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Bank Of Us Domain Security
  slug: bank-of-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bank Of Us Vulnerability Disclosure
  slug: bank-of-us-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bank-of-us
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Tasmania
- Mutual
- Product Reference Data
website: https://www.bankofus.com.au/
---
