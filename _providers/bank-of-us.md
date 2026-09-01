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
    agentic_access: derived
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
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Us Agentic Access
  operation_count: 19
  slug: bank-of-us-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-bank-of-us-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-bank-of-us-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-bank-of-us-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-bank-of-us-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-bank-of-us-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-bank-of-us-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-bank-of-us-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bank-of-us-capability-edges.yml
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
  name: Bank of us MCP Server
  slug: bank-of-us-mcp-server
modified: '2026-07-21'
name: Bank of us
nav: Providers
network: true
overview: 'Bank of us publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of us'' developer surface includes authentication, documentation, API reference, engineering blog, support, and 22 more developer resources.'
random_paper: 2
scopes:
- name: Bank Of Us Scopes
  scope_count: 5
  slug: bank-of-us-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.3
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
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 63.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
