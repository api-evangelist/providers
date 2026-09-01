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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-regional-australia-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-regional-australia-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-regional-australia-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-regional-australia-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-regional-australia-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-regional-australia-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-regional-australia-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/regional-australia-bank-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/regional-australia-bank-cds-banking-products-overlay.yaml
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
  name: Regional Australia Bank MCP Server
  slug: regional-australia-bank-mcp-server
modified: '2026-07-21'
name: Regional Australia Bank
nav: Providers
network: true
overview: 'Regional Australia Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Regional Australia Bank''s developer surface includes documentation, support, API reference, getting-started guide, developer portal, authentication, engineering blog, and 18 more developer resources.'
random_paper: 7
scopes:
- name: Regional Australia Bank Scopes
  scope_count: 5
  slug: regional-australia-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 44.9
  provenance:
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
    score: 70.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Customer Owned
- Product Reference Data
- Mutual Bank
website: https://www.regionalaustraliabank.com.au/
---
