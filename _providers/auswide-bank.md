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
    agentic_access: false
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
  score: 36.3
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Auswide Bank Banking Account Balances API
  slug: auswide-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Auswide Bank Banking Account Direct Debits API
  slug: auswide-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Auswide Bank Banking Account Scheduled Payments API
  slug: auswide-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Auswide Bank Banking Account Transactions API
  slug: auswide-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Auswide Bank Banking Accounts API
  slug: auswide-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Auswide Bank Banking Payees API
  slug: auswide-bank-banking-payees-api
- description: Banking Product endpoints
  name: Auswide Bank Banking Products API
  slug: auswide-bank-banking-products-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/auswide-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/auswide-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/auswide-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/auswide-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/auswide-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/auswide-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/auswide-bank-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/auswide-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/auswide-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/auswide-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/auswide-bank-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/auswide-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/auswide-bank-product-lookup.md
- group: company
  title: ''
  type: Website
  url: https://www.auswidebank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auswidebank.com.au/help/banking-support/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auswide-bank-ltd/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auswidebank.com.au/about/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auswidebank.com.au/about/website-terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.auswidebank.com.au/about/contact-us/
created: '2026-07-20'
description: Auswide Bank Ltd is an Australian authorised deposit-taking institution (ADI) headquartered in Bundaberg, Queensland, offering home loans, savings and transaction accounts, term deposits, credit cards, and personal and business banking. Formerly Wide Bay Australia and previously ASX-listed (ABA), Auswide is now a division of MyState Bank Limited, a wholly owned subsidiary of the ASX-listed MyState Limited (ASX MYS) following the 2025 merger. As an active CDR data holder under Australia's Consumer Data Right (Open Banking), Auswide exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, alongside the accredited-data-recipient consumer data sharing channels required of every Australian bank.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auswide-bank.png
layout: provider
mcp_servers:
- description: ''
  name: auswide-bank-mcp.yml
  slug: auswide-bank-mcpyml
modified: '2026-07-21'
name: Auswide Bank
nav: Providers
network: true
overview: 'Auswide Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Auswide Bank''s developer surface includes authentication, documentation, support, and 16 more developer resources.'
random_paper: 77
scopes:
- name: Auswide Bank Scopes
  scope_count: 5
  slug: auswide-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 38.0
  delta: -4.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 50.0
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 42.3
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
    score: 60.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/auswide-bank/refs/heads/main/screenshots/auswide-bank-2026-07-21T114702.png
security:
- kind: authentication
  name: Auswide Bank Authentication
  slug: auswide-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Auswide Bank Domain Security
  slug: auswide-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: auswide-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.auswidebank.com.au/
---
