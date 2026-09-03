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
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Australian Military Bank Banking Account Balances API
  slug: australian-military-bank-banking-account-balances-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Australian Military Bank Banking Account Direct Debits API
  slug: australian-military-bank-banking-account-direct-debits-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Australian Military Bank Banking Account Scheduled Payments API
  slug: australian-military-bank-banking-account-scheduled-payments-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Australian Military Bank Banking Account Transactions API
  slug: australian-military-bank-banking-account-transactions-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Australian Military Bank Banking Accounts API
  slug: australian-military-bank-banking-accounts-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Australian Military Bank Banking Payees API
  slug: australian-military-bank-banking-payees-api
- baseURL: https://public.open.australianmilitarybank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Australian Military Bank Banking Products API
  slug: australian-military-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-australian-military-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-australian-military-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-australian-military-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-australian-military-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-australian-military-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-australian-military-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-australian-military-bank-banking-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/australian-military-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.australianmilitarybank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.australianmilitarybank.com.au/consumer-data-right
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/australian-military-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.australianmilitarybank.com.au/disclosuredocuments
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.australianmilitarybank.com.au/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.australianmilitarybank.com.au/securityhub
- group: operate
  title: ''
  type: Support
  url: https://www.australianmilitarybank.com.au/contact
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#get-products
- group: auth
  title: ''
  type: Authentication
  url: authentication/australian-military-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/australian-military-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/australian-military-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/australian-military-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/australian-military-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.australianmilitarybank.com.au/consumer-data-right
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/australian-military-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/australian-military-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/australian-military-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/australian-military-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/australian-military-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/australian-military-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: Australian Military Bank Ltd (ABN 48 087 649 741, AFSL/Australian Credit Licence 237988, BSB 642170) is a customer-owned mutual authorised deposit-taking institution (ADI) that has served the Australian Defence Force community, veterans, and their families since 1959, making it one of Australia's longest-serving Defence financial institutions. As an active ADI it participates in Australia's Consumer Data Right (CDR) open banking regime, and its only public, unauthenticated API surface is the mandated Product Reference Data (PRD) API built to the Data Standards Body (DSB) Consumer Data Standards. Consumer data sharing (accounts, balances, transactions) is available only to accredited data recipients through the CDR's authenticated, FAPI-profiled OAuth2/OIDC flows; the bank does not publish a broader self-serve developer portal or proprietary API program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/australian-military-bank.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the public, unauthenticated CDR Product Reference Data endpoints. Australian Military Bank publishes no official hosted MCP server; these tools map 1:1 to the t
  name: Australian Military Bank MCP Server
  slug: australian-military-bank-mcp-server
modified: '2026-07-21'
name: Australian Military Bank
nav: Providers
network: true
overview: 'Australian Military Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Australian Military Bank''s developer surface includes support, API reference, authentication, and 19 more developer resources.'
random_paper: 17
scopes:
- name: Australian Military Bank Scopes
  scope_count: 0
  slug: australian-military-bank-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 12.4
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 36.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
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
    score: 77.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/australian-military-bank/refs/heads/main/screenshots/australian-military-bank-2026-07-21T120337.png
security:
- kind: authentication
  name: Australian Military Bank Authentication
  slug: australian-military-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Australian Military Bank Domain Security
  slug: australian-military-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: australian-military-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual
- Defence
website: https://www.australianmilitarybank.com.au/
---
