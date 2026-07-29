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
  name: Gc Mutual Bank Agentic Access
  operation_count: 19
  slug: gc-mutual-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: G&C Mutual Bank Banking Account Balances API
  slug: gc-mutual-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: G&C Mutual Bank Banking Account Direct Debits API
  slug: gc-mutual-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: G&C Mutual Bank Banking Account Scheduled Payments API
  slug: gc-mutual-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: G&C Mutual Bank Banking Account Transactions API
  slug: gc-mutual-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: G&C Mutual Bank Banking Accounts API
  slug: gc-mutual-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: G&C Mutual Bank Banking Payees API
  slug: gc-mutual-bank-banking-payees-api
- description: Banking Product endpoints
  name: G&C Mutual Bank Banking Products API
  slug: gc-mutual-bank-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gc-mutual-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gc-mutual-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gc-mutual-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gc-mutual-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gc-mutual-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gc-mutual-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gc-mutual-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gc-mutual-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gc-mutual-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gc-mutual-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/gc-mutual-bank-cds-banking-products-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/gc-mutual-bank-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://unity.bank/
- group: docs
  title: ''
  type: Documentation
  url: https://unity.bank/about-us/corporate-information/open-banking/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unity.bank/about-us/privacy/
- group: operate
  title: ''
  type: Support
  url: https://unity.bank/talk-to-us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://unity.bank/latest-news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unity-bank
created: '2026-07-20'
description: G&C Mutual Bank is an Australian customer-owned mutual bank and authorised deposit-taking institution (ADI) providing retail and business banking to its members, including home loans, transaction and savings accounts, and credit cards. It merged with Unity Bank effective 7 March 2025, with the combined entity renamed Unity Bank Limited from 1 July 2025; the G&C Mutual Bank brand and its digital banking host (gcmutualbank.com.au) remain operational during the multi-brand consolidation, while the public website gcmutual.bank now redirects to unity.bank. Under Australia's Consumer Data Right (CDR / Open Banking) the bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, alongside the authenticated consumer-data (accounts and transactions) surface that is restricted to accredited data recipients under the CDR ADR model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gc-mutual-bank.png
layout: provider
mcp_servers:
- description: ''
  name: gc-mutual-bank-mcp.yml
  slug: gc-mutual-bank-mcpyml
modified: '2026-07-21T00:00:00Z'
name: G&C Mutual Bank
nav: Providers
network: true
overview: 'G&C Mutual Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  G&C Mutual Bank''s developer surface includes authentication, documentation, support, engineering blog, and 15 more developer resources.'
random_paper: 8
scopes:
- name: Gc Mutual Bank Scopes
  scope_count: 9
  slug: gc-mutual-bank-scopes
  summary_line: 9 scopes
score:
  band: thin
  composite: 35.5
  delta: -3.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.0
    developer_ergonomics: 29.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.7
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
    score: 65.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gc-mutual-bank/refs/heads/main/screenshots/gc-mutual-bank-2026-07-21T114725.png
security:
- kind: authentication
  name: Gc Mutual Bank Authentication
  slug: gc-mutual-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Gc Mutual Bank Domain Security
  slug: gc-mutual-bank-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gc-mutual-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Mutual Bank
- Australia
website: https://unity.bank/
---
