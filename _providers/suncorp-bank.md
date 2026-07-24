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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Suncorp Bank Agentic Access
  operation_count: 19
  slug: suncorp-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 8
apis:
- description: Suncorp Bank's merchant payment gateway, a Suncorp-branded instance of Mastercard Payment Gateway Services (MPGS). It offers merchants a REST/JSON (and NVP) API plus hosted checkout, hosted batch, and
  name: Suncorp Bank Gateway (Mastercard) Payments API
  slug: suncorp-bank-gateway-payments-api
- description: Banking Account Balance endpoints
  name: Suncorp Bank Banking Account Balances API
  slug: suncorp-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Suncorp Bank Banking Account Direct Debits API
  slug: suncorp-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Suncorp Bank Banking Account Scheduled Payments API
  slug: suncorp-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Suncorp Bank Banking Account Transactions API
  slug: suncorp-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Suncorp Bank Banking Accounts API
  slug: suncorp-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Suncorp Bank Banking Payees API
  slug: suncorp-bank-banking-payees-api
- description: Banking Product endpoints
  name: Suncorp Bank Banking Products API
  slug: suncorp-bank-banking-products-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suncorp-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suncorp-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/suncorp-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/suncorp-bank-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/suncorp-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/suncorp-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cdr.gov.au/find-a-provider
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/suncorp-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/suncorp-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cdr.gov.au/performance
- group: operate
  title: ''
  type: Deprecation
  url: https://www.suncorpbank.com.au/variation
- group: design
  title: ''
  type: Conventions
  url: conventions/suncorp-bank-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/suncorp-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/suncorp-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/suncorp-bank-cds-banking-products-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/suncorp-bank-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/suncorp-bank-product-reference-data.md
- group: company
  title: ''
  type: Website
  url: https://www.suncorpbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.suncorpbank.com.au/help-support/open-banking.html
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/suncorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suncorp/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suncorpbank.com.au/about-us/legal/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suncorpbank.com.au/about-us/legal.html
- group: operate
  title: ''
  type: Support
  url: https://www.suncorpbank.com.au/help-support/open-banking.html
created: '2026-07-20'
description: Suncorp Bank is an Australian retail and business bank headquartered in Brisbane, Queensland, offering transaction and savings accounts, home and personal lending, credit cards, and business banking. Formerly the banking arm of Suncorp Group, it was acquired by Australia and New Zealand Banking Group (ANZ) on 31 July 2024 and now operates as a division of ANZ while retaining the Suncorp Bank brand under a multi-year transition. As an authorised deposit-taking institution (ADI) it is a data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards, powered by the Frollo PRD portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suncorp-bank.png
layout: provider
mcp_servers:
- description: ''
  name: suncorp-bank-mcp.yml
  slug: suncorp-bank-mcpyml
modified: '2026-07-21'
name: Suncorp Bank
nav: Providers
network: true
overview: 'Suncorp Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Suncorp Bank''s developer surface includes authentication, documentation, support, and 22 more developer resources.'
random_paper: 11
scopes:
- name: Suncorp Bank Scopes
  scope_count: 10
  slug: suncorp-bank-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 49.6
  delta: 6.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.8
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 43.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/suncorp-bank/refs/heads/main/screenshots/suncorp-bank-2026-07-21T114752.png
security:
- kind: authentication
  name: Suncorp Bank Authentication
  slug: suncorp-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Suncorp Bank Domain Security
  slug: suncorp-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: suncorp-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- Consumer Data Right
website: https://www.suncorpbank.com.au/
---
