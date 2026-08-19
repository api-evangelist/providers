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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: Banking Account Balance endpoints
  name: MyState Bank Banking Account Balances API
  slug: mystate-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: MyState Bank Banking Account Direct Debits API
  slug: mystate-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: MyState Bank Banking Account Scheduled Payments API
  slug: mystate-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: MyState Bank Banking Account Transactions API
  slug: mystate-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: MyState Bank Banking Accounts API
  slug: mystate-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: MyState Bank Banking Payees API
  slug: mystate-bank-banking-payees-api
- description: Banking Product endpoints
  name: MyState Bank Banking Products API
  slug: mystate-bank-banking-products-api
- description: The Products API from MyState Bank — 2 operation(s) for products.
  name: MyState Bank Products API
  slug: mystate-bank-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-mystate-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-mystate-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-mystate-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-mystate-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-mystate-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-mystate-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-mystate-bank-banking-products-api
- collection_type: open
  name: CDR Banking Banking Account Balances Products API
  slug: open-mystate-bank-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mystate-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mystate.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mystate-limited
- group: company
  title: ''
  type: InvestorRelations
  url: https://mystatelimited.com.au/
- group: docs
  title: ''
  type: ProductReferenceData
  url: https://public.cdr.mystate.com.au/cds-au/v1/banking/products
- group: other
  title: ''
  type: Standards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: operate
  title: ''
  type: Support
  url: https://mystate.com.au/help-centre/open-banking-help/
- group: docs
  title: ''
  type: Documentation
  url: https://mystate.com.au/help-centre/open-banking-help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mystate.com.au/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mystate.com.au/legal/
- group: design
  title: ''
  type: Conventions
  url: conventions/mystate-bank-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mystate-bank-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mystate-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mystate-bank-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mystate-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/mystate-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mystate-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mystate-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/mystate-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: MyState Bank is an Australian retail bank headquartered in Hobart, Tasmania, and the principal banking brand of ASX-listed MyState Limited (ASX:MYS). It traces its origins to a Tasmanian credit union serving teachers, police and nurses, formed its current group in the 2009 merger of Tasmanian Perpetual Trustees and MyState Financial, was authorised to use the MyState Bank name in 2014, and in February 2025 completed a merger with Queensland regional lender Auswide Bank to create one of Australia's larger regional banking groups. As an authorised deposit-taking institution (ADI) it is a regulated data holder under the Australian Consumer Data Right (CDR / Open Banking) and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards (CDS). Consumer data sharing beyond PRD is protected under the CDR's accredited-data-recipient model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mystate-bank.png
layout: provider
mcp_servers:
- description: ''
  name: mystate-bank-mcp.yml
  slug: mystate-bank-mcpyml
modified: '2026-07-21'
name: MyState Bank
nav: Providers
network: true
overview: 'MyState Bank publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 5 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  MyState Bank''s developer surface includes support, documentation, authentication, and 18 more developer resources.'
random_paper: 40
score:
  band: thin
  composite: 33.8
  delta: 0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 50.7
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 33.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mystate-bank/refs/heads/main/screenshots/mystate-bank-2026-07-21T130910.png
security:
- kind: authentication
  name: Mystate Bank Authentication
  slug: mystate-bank-authentication
  summary_line: none/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Mystate Bank Domain Security
  slug: mystate-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mystate-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
website: https://www.mystate.com.au/
---
