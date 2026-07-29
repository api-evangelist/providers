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
  name: Bankvic Agentic Access
  operation_count: 19
  slug: bankvic-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: BankVic Banking Account Balances API
  slug: bankvic-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: BankVic Banking Account Direct Debits API
  slug: bankvic-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: BankVic Banking Account Scheduled Payments API
  slug: bankvic-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: BankVic Banking Account Transactions API
  slug: bankvic-banking-account-transactions-api
- description: Banking Account endpoints
  name: BankVic Banking Accounts API
  slug: bankvic-banking-accounts-api
- description: Banking Payee endpoints
  name: BankVic Banking Payees API
  slug: bankvic-banking-payees-api
- description: Banking Product endpoints
  name: BankVic Banking Products API
  slug: bankvic-banking-products-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'For an accredited Data Recipient (ADR) holding an active consumer consent: list the member''s accounts, read one account''s current balance, then page its transactions. Requires the CDR OIDC/FAPI 2.0 au'
  name: BankVic consented account data overview
  slug: bankvic-account-data-overview
- description: Discover BankVic's public product catalogue then drill into one product's full terms via the unauthenticated CDR Product Reference Data (PRD) surface. Runnable as-is against the live endpoint (no cons
  name: BankVic product discovery
  slug: bankvic-product-discovery
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bankvic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bankvic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bankvic-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bankvic-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bankvic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bankvic-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://uat.bankvic.com.au/documents/95c3605a8cf64a12ae35608ca0188c73.pdf
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bankvic-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bankvic-product-discovery.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bankvic-account-data-overview.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bankvic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/bankvic-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bankvic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bankvic-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bankvic-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bankvic-product-reference-data.md
- group: company
  title: ''
  type: Website
  url: https://www.bankvic.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankvic.com.au/get-help/open-banking/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankvic.com.au/get-help/open-banking/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bankvic.com.au/get-help/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api_get-products
- group: operate
  title: ''
  type: Support
  url: https://www.bankvic.com.au/get-help/
- group: start
  title: ''
  type: SignUp
  url: https://www.bankvic.com.au/join-bankvic/
- group: start
  title: ''
  type: Login
  url: https://ib.bankvic.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.intelligencebank.com/au/share/NZw2/RVzr/yzJw/original/BankVic+Terms+%26+Conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.intelligencebank.com/au/share/NZw2/19DD/6daB/original/Privacy+Policy
created: '2026-07-20'
description: BankVic is an Australian customer-owned mutual bank and the trading name of Police Financial Services Limited, an authorised deposit-taking institution (ADI) founded in 1974 and headquartered in Melbourne, Victoria. Member-owned rather than shareholder-driven, it has served Victoria's police, health, and emergency-services communities and the broader Victorian public under a "people before profits" ethos for more than fifty years, offering everyday accounts, home and personal loans, term deposits, credit cards, and insurance. As a regulated ADI, BankVic participates in Australia's Consumer Data Right (CDR / Open Banking) regime and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, alongside its consented, ADR-mediated consumer data-sharing surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bankvic.png
layout: provider
mcp_servers:
- description: ''
  name: bankvic-mcp.yml
  slug: bankvic-mcpyml
modified: '2026-07-21'
name: BankVic
nav: Providers
network: true
overview: 'BankVic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  BankVic''s developer surface includes authentication, documentation, getting-started guide, API reference, support, signup flow, and 21 more developer resources.'
random_paper: 14
scopes:
- name: Bankvic Scopes
  scope_count: 9
  slug: bankvic-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: developing
  composite: 47.9
  delta: -4.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 50.0
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 7.9
  previous_composite: 51.9
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
    score: 67.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bankvic/refs/heads/main/screenshots/bankvic-2026-07-21T114709.png
security:
- kind: authentication
  name: Bankvic Authentication
  slug: bankvic-authentication
  summary_line: none-public/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Bankvic Domain Security
  slug: bankvic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bankvic
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.bankvic.com.au/
---
