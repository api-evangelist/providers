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
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bank Of Queensland Agentic Access
  operation_count: 19
  slug: bank-of-queensland-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bank of Queensland Banking Account Balances API
  slug: bank-of-queensland-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bank of Queensland Banking Account Direct Debits API
  slug: bank-of-queensland-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bank of Queensland Banking Account Scheduled Payments API
  slug: bank-of-queensland-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bank of Queensland Banking Account Transactions API
  slug: bank-of-queensland-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bank of Queensland Banking Accounts API
  slug: bank-of-queensland-banking-accounts-api
- description: Banking Payee endpoints
  name: Bank of Queensland Banking Payees API
  slug: bank-of-queensland-banking-payees-api
- description: Banking Product endpoints
  name: Bank of Queensland Banking Products API
  slug: bank-of-queensland-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-queensland-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-queensland-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-queensland-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-queensland-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bank-of-queensland-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bank-of-queensland-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bank-of-queensland-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bank-of-queensland-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bank-of-queensland-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bank-of-queensland-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bank-of-queensland-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bank-of-queensland-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bank-of-queensland-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.boq.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.boq.com.au/personal/banking/openbanking/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.boq.com.au/personal/banking/openbanking/developers
- group: operate
  title: ''
  type: Support
  url: https://www.boq.com.au/help-and-support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boq.com.au/personal/help-and-support/forms-and-important-information/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boq.com.au/important-information/terms-and-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-queensland
created: '2026-07-20'
description: Bank of Queensland Limited (ASX code BOQ) is one of Australia's oldest banks, founded in Brisbane in 1874, and today an APRA-regulated authorised deposit-taking institution (ADI) and ASX-listed regional retail and commercial bank - a publicly listed company, not a customer-owned mutual. Its banking group includes the ME Bank, Virgin Money Australia and BOQ Specialist brands. As an accredited Consumer Data Right (CDR) data holder, BOQ exposes a public, unauthenticated Product Reference Data (PRD) API that conforms to the Australian Consumer Data Standards, while consumer data sharing runs through the regulated CDR / Accredited Data Recipient (ADR) model with OAuth2 / OIDC (FAPI) authorization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-queensland.png
layout: provider
mcp_servers:
- description: ''
  name: bank-of-queensland-mcp.yml
  slug: bank-of-queensland-mcpyml
modified: '2026-07-21T18:00:00Z'
name: Bank of Queensland
nav: Providers
network: true
overview: 'Bank of Queensland publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bank of Queensland''s developer surface includes authentication, documentation, support, and 18 more developer resources.'
random_paper: 2
scopes:
- name: Bank Of Queensland Scopes
  scope_count: 9
  slug: bank-of-queensland-scopes
  summary_line: 9 scopes
score:
  band: developing
  composite: 46.1
  delta: 7.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.0
    developer_ergonomics: 47.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 38.8
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-queensland/refs/heads/main/screenshots/bank-of-queensland-2026-07-21T114702.png
security:
- kind: authentication
  name: Bank Of Queensland Authentication
  slug: bank-of-queensland-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Bank Of Queensland Domain Security
  slug: bank-of-queensland-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: bank-of-queensland
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.boq.com.au/
---
