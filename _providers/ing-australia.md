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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ing Australia Agentic Access
  operation_count: 19
  slug: ing-australia-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: ING Australia Banking Account Balances API
  slug: ing-australia-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: ING Australia Banking Account Direct Debits API
  slug: ing-australia-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: ING Australia Banking Account Scheduled Payments API
  slug: ing-australia-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: ING Australia Banking Account Transactions API
  slug: ing-australia-banking-account-transactions-api
- description: Banking Account endpoints
  name: ING Australia Banking Accounts API
  slug: ing-australia-banking-accounts-api
- description: Banking Payee endpoints
  name: ING Australia Banking Payees API
  slug: ing-australia-banking-payees-api
- description: Banking Product endpoints
  name: ING Australia Banking Products API
  slug: ing-australia-banking-products-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ing-australia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ing-australia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ing-australia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ing-australia-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ing-australia-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ing-australia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ing-australia-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ing-australia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ing-australia-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
- group: design
  title: ''
  type: DataModel
  url: data-model/ing-australia-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ing-australia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ing-australia-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ing-australia-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.ing.com.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ing.com.au/open-banking.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.ing.com.au/pdf/CDR-policy.pdf
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: operate
  title: ''
  type: Support
  url: mailto:cdrenquiry@ing.com.au
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ing.com.au/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ing.com.au/legal.html
created: '2026-07-20'
description: ING Australia is the retail banking division of ING Bank (Australia) Limited (ABN 24 000 893 292), a wholly owned subsidiary of the Dutch multinational ING Groep N.V. headquartered in Amsterdam. Launched in 1999 as ING Direct and rebranded to ING in 2017, it is a branchless, digital-first direct bank offering everyday transaction and savings accounts, home loans, superannuation, and insurance to Australian consumers. It is not a customer-owned mutual; it is a foreign-owned Authorised Deposit-taking Institution (ADI) regulated by APRA and ASIC. As an active ADI, ING is an accredited data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes the mandatory public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards (CDS). Authenticated consumer-data sharing follows the CDR ecosystem model (OAuth2 / OIDC FAPI profile via accredited data recipients); ING does not operate a broad, self-serve public developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ing-australia.png
layout: provider
mcp_servers:
- description: ''
  name: ing-australia-mcp.yml
  slug: ing-australia-mcpyml
modified: '2026-07-21'
name: ING Australia
nav: Providers
network: true
overview: 'ING Australia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  ING Australia''s developer surface includes authentication, getting-started guide, documentation, API reference, support, and 17 more developer resources.'
random_paper: 37
scopes:
- name: Ing Australia Scopes
  scope_count: 10
  slug: ing-australia-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.2
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 45.5
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ing-australia/refs/heads/main/screenshots/ing-australia-2026-07-21T114732.png
security:
- kind: authentication
  name: Ing Australia Authentication
  slug: ing-australia-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Ing Australia Domain Security
  slug: ing-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ing-australia
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.ing.com.au/
---
