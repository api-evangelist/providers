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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Sydney Agentic Access
  operation_count: 19
  slug: bank-of-sydney-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bank of Sydney Banking Account Balances API
  slug: bank-of-sydney-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bank of Sydney Banking Account Direct Debits API
  slug: bank-of-sydney-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bank of Sydney Banking Account Scheduled Payments API
  slug: bank-of-sydney-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bank of Sydney Banking Account Transactions API
  slug: bank-of-sydney-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bank of Sydney Banking Accounts API
  slug: bank-of-sydney-banking-accounts-api
- description: Banking Payee endpoints
  name: Bank of Sydney Banking Payees API
  slug: bank-of-sydney-banking-payees-api
- description: Banking Product endpoints
  name: Bank of Sydney Banking Products API
  slug: bank-of-sydney-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-sydney-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-sydney-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.banksyd.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.banksyd.com.au/tools-support/open-banking/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.banksyd.com.au/tools-support/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-products
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-sydney
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-sydney-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-sydney-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-sydney-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-sydney-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-sydney-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bank-of-sydney-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-sydney-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-sydney-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-of-sydney-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-sydney-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-sydney-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bank-of-sydney-product-reference-data.md
created: '2026-07-20'
description: Bank of Sydney Ltd is an Australian authorised deposit-taking institution (ADI) headquartered in Sydney, New South Wales, offering personal and business banking, home loans, deposits, and everyday accounts. It is a wholly owned subsidiary of Lebanon-based Bank of Beirut and operates a national branch and digital footprint across Australia. As a regulated ADI, Bank of Sydney participates in Australia's Consumer Data Right (CDR) / Open Banking regime, exposing a public, unauthenticated Product Reference Data (PRD) API that conforms to the Data Standards Body (DSB) Consumer Data Standards. Consumer-facing account and transaction data sharing is delivered to Accredited Data Recipients (ADRs) under the CDR authorisation model, backed by OAuth2/OIDC.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-sydney.png
layout: provider
mcp_servers:
- description: ''
  name: bank-of-sydney-mcp.yml
  slug: bank-of-sydney-mcpyml
modified: '2026-07-21'
name: Bank of Sydney
nav: Providers
network: true
overview: 'Bank of Sydney publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of Sydney''s developer surface includes documentation, getting-started guide, API reference, authentication, and 15 more developer resources.'
random_paper: 74
scopes:
- name: Bank Of Sydney Scopes
  scope_count: 5
  slug: bank-of-sydney-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 36.0
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.0
    developer_ergonomics: 40.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 50.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-sydney/refs/heads/main/screenshots/bank-of-sydney-2026-07-21T130910.png
security:
- kind: authentication
  name: Bank Of Sydney Authentication
  slug: bank-of-sydney-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Bank Of Sydney Domain Security
  slug: bank-of-sydney-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bank-of-sydney
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.banksyd.com.au/
---
