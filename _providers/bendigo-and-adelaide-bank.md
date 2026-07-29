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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
api_count: 14
apis:
- description: 'Accounts represent the underlying store used to track balances and the transactions that have occurred to modify those balances over time. Up currently has three types of account: `SAVER`—used to earn'
  name: Bendigo and Adelaide Bank Accounts API
  slug: bendigo-and-adelaide-bank-accounts-api
- description: Attachments represent uploaded files that are attached to transactions, these are commonly receipts.
  name: Bendigo and Adelaide Bank Attachments API
  slug: bendigo-and-adelaide-bank-attachments-api
- description: Banking Account Balance endpoints
  name: Bendigo and Adelaide Bank Banking Account Balances API
  slug: bendigo-and-adelaide-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bendigo and Adelaide Bank Banking Account Direct Debits API
  slug: bendigo-and-adelaide-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bendigo and Adelaide Bank Banking Account Scheduled Payments API
  slug: bendigo-and-adelaide-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bendigo and Adelaide Bank Banking Account Transactions API
  slug: bendigo-and-adelaide-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bendigo and Adelaide Bank Banking Accounts API
  slug: bendigo-and-adelaide-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Bendigo and Adelaide Bank Banking Payees API
  slug: bendigo-and-adelaide-bank-banking-payees-api
- description: Banking Product endpoints
  name: Bendigo and Adelaide Bank Banking Products API
  slug: bendigo-and-adelaide-bank-banking-products-api
- description: Categories enable understanding where your money goes by driving powerful insights in Up. All categories in Up are pre-defined and are automatically assigned to new purchases in most cases. A parent-c
  name: Bendigo and Adelaide Bank Categories API
  slug: bendigo-and-adelaide-bank-categories-api
- description: 'Tags are custom labels that can be associated with transactions on Up. Within the Up application, tags provide additional insight into spending. For example, you could have a "Take Away" tag that you '
  name: Bendigo and Adelaide Bank Tags API
  slug: bendigo-and-adelaide-bank-tags-api
- description: Transactions represent the movement of money into and out of an account. They have many characteristics that vary depending on the kind of transaction. Transactions may be temporarily `HELD` (pending)
  name: Bendigo and Adelaide Bank Transactions API
  slug: bendigo-and-adelaide-bank-transactions-api
- description: 'Some endpoints exist not to expose data, but to test the API itself. Currently there is only one endpoint in this group: ping!'
  name: Bendigo and Adelaide Bank Utility endpoints API
  slug: bendigo-and-adelaide-bank-utility-endpoints-api
- description: Webhooks provide a mechanism for a configured URL to receive events when transaction activity occurs on Up. You can think of webhooks as being like push notifications for your server-side application.
  name: Bendigo and Adelaide Bank Webhooks API
  slug: bendigo-and-adelaide-bank-webhooks-api
artifact_total: 20
asyncapis:
- description: Real-time webhook event callbacks delivered by Up to a subscriber-configured HTTPS URL when transaction activity occurs on an Up account. Each delivery carries an X-Up-Authenticity-Signature header (S
  name: Up Developer API Webhooks
  slug: bendigo-and-adelaide-bank-up-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bendigo-and-adelaide-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bendigo-and-adelaide-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bendigobank.com.au/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://www.bendigoadelaide.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bendigoadelaide.com.au/banking-products-api/
- group: start
  title: ''
  type: Portal
  url: https://developer.up.com.au/
- group: other
  title: ''
  type: ConsumerDataRight
  url: https://www.bendigobank.com.au/cdr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bendigoadelaide.com.au/banking-products-api/
- group: other
  title: ''
  type: APIStandards
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bendigobank.com.au/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bendigobank.com.au/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bendigobank.com.au/contact-us/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.bendigoadelaide.com.au/investor-centre/
- group: company
  title: ''
  type: Blog
  url: https://www.bendigoadelaide.com.au/media-centre/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bendigoadelaide
- group: auth
  title: ''
  type: Authentication
  url: authentication/bendigo-and-adelaide-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bendigo-and-adelaide-bank-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bendigo-and-adelaide-bank-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bendigo-and-adelaide-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bendigo-and-adelaide-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bendigo-and-adelaide-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/bendigo-and-adelaide-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bendigo-and-adelaide-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bendigo-and-adelaide-bank-cds-banking-products-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/bendigo-and-adelaide-bank-up-developer-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/bendigo-and-adelaide-bank-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bendigo-and-adelaide-bank-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bendigo-and-adelaide-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bendigobank.com.au/security/
created: '2026-07-20'
description: Bendigo and Adelaide Bank Limited (ASX:BEN) is one of Australia's largest retail banks, formed by the 2007 merger of the community-focused Bendigo Bank and the wholesale-strong Adelaide Bank, and headquartered in Bendigo, Victoria. The group serves millions of customers through the Bendigo Bank, Adelaide Bank, Rural Bank, and Up (neobank) brands, with a distinctive Community Bank branch-franchise model. As an authorised deposit-taking institution and accredited Consumer Data Right (CDR) data holder, the bank exposes public, unauthenticated Product Reference Data (PRD) APIs conforming to the Australian Consumer Data Standards, alongside the authenticated CDR consumer data-sharing surface governed by the ACCC/DSB rules.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bendigo-and-adelaide-bank.png
layout: provider
mcp_servers:
- description: ''
  name: bendigo-and-adelaide-bank-mcp.yml
  slug: bendigo-and-adelaide-bank-mcpyml
modified: '2026-07-21'
name: Bendigo and Adelaide Bank
nav: Providers
network: true
overview: 'Bendigo and Adelaide Bank publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Banking Account Balances API, and 11 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  The Bendigo and Adelaide Bank catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bendigo and Adelaide Bank''s developer surface includes developer portal, documentation, support, engineering blog, authentication, and 26 more developer resources.'
random_paper: 21
scopes:
- name: Bendigo And Adelaide Bank Scopes
  scope_count: 10
  slug: bendigo-and-adelaide-bank-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.5
  delta: -4.2
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.5
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 68.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bendigo-and-adelaide-bank/refs/heads/main/screenshots/bendigo-and-adelaide-bank-2026-07-21T114715.png
security:
- kind: authentication
  name: Bendigo And Adelaide Bank Authentication
  slug: bendigo-and-adelaide-bank-authentication
  summary_line: none/openIdConnect/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Bendigo And Adelaide Bank Domain Security
  slug: bendigo-and-adelaide-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bendigo And Adelaide Bank Vulnerability Disclosure
  slug: bendigo-and-adelaide-bank-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bendigo-and-adelaide-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
website: https://www.bendigobank.com.au/
---
