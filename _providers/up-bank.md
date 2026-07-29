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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Up Bank Agentic Access
  operation_count: 39
  slug: up-bank-agentic-access
  summary_line: 39 operations · 9 acting
api_count: 14
apis:
- description: 'Accounts represent the underlying store used to track balances and the transactions that have occurred to modify those balances over time. Up currently has three types of account: `SAVER`—used to earn'
  name: Up Accounts API
  slug: up-bank-accounts-api
- description: Attachments represent uploaded files that are attached to transactions, these are commonly receipts.
  name: Up Attachments API
  slug: up-bank-attachments-api
- description: Banking Account Balance endpoints
  name: Up Banking Account Balances API
  slug: up-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Up Banking Account Direct Debits API
  slug: up-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Up Banking Account Scheduled Payments API
  slug: up-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Up Banking Account Transactions API
  slug: up-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Up Banking Accounts API
  slug: up-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Up Banking Payees API
  slug: up-bank-banking-payees-api
- description: Banking Product endpoints
  name: Up Banking Products API
  slug: up-bank-banking-products-api
- description: Categories enable understanding where your money goes by driving powerful insights in Up. All categories in Up are pre-defined and are automatically assigned to new purchases in most cases. A parent-c
  name: Up Categories API
  slug: up-bank-categories-api
- description: 'Tags are custom labels that can be associated with transactions on Up. Within the Up application, tags provide additional insight into spending. For example, you could have a "Take Away" tag that you '
  name: Up Tags API
  slug: up-bank-tags-api
- description: Transactions represent the movement of money into and out of an account. They have many characteristics that vary depending on the kind of transaction. Transactions may be temporarily `HELD` (pending)
  name: Up Transactions API
  slug: up-bank-transactions-api
- description: 'Some endpoints exist not to expose data, but to test the API itself. Currently there is only one endpoint in this group: ping!'
  name: Up Utility endpoints API
  slug: up-bank-utility-endpoints-api
- description: Webhooks provide a mechanism for a configured URL to receive events when transaction activity occurs on Up. You can think of webhooks as being like push notifications for your server-side application.
  name: Up Webhooks API
  slug: up-bank-webhooks-api
artifact_total: 22
asyncapis:
- description: 'Event surface for the Up Personal Banking API. Once a webhook is registered (POST /webhooks), Up delivers JSON-encoded POST callbacks to the configured URL whenever transaction activity occurs on the '
  name: Up Personal Banking Webhooks
  slug: up-bank-webhooks-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/up-bank-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/up-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/up-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.up.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.up.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.up.com.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.up.com.au/#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/up-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upbanking/
- group: company
  title: ''
  type: Blog
  url: https://up.com.au/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.up.com.au/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://up.com.au/download/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://up.com.au/terms-and-information/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.up.com.au/privacy/
- group: operate
  title: ''
  type: Support
  url: https://up.com.au/support/
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/engagements/bendigobank-vdp
- group: auth
  title: ''
  type: Authentication
  url: authentication/up-bank-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/up-bank-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/up-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/up-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/up-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/up-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.up.com.au/
- group: design
  title: ''
  type: Conformance
  url: conformance/up-bank-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/up-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/up-bank-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/up-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/up-bank-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/up-bank-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/up-bank-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/up-bank-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/up-bank-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/up-bank-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-20'
description: Up is an Australian digital-only neobank founded in 2018 as a collaboration between Melbourne software company Ferocia and Bendigo and Adelaide Bank. Up is not a mutual and is not separately licensed; it operates as a brand of ASX-listed Bendigo and Adelaide Bank, which holds the Authorised Deposit-taking Institution (ADI) licence, provides the underlying deposit products, and acquired full ownership of Ferocia and Up in 2021. Marketed as Australia's first fully cloud-hosted bank, Up serves more than one million customers through a mobile-first app with no monthly account fees, high-interest savers, and rich transaction categorisation. Up has a strong public API posture for its size - it exposes both a documented personal-banking developer API (accounts, transactions, tags, webhooks) and, as required of every Australian data holder under the Consumer Data Right (CDR / Open Banking), a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data
  Standards.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/up-bank.png
layout: provider
mcp_servers:
- description: ''
  name: up-bank-mcp.yml
  slug: up-bank-mcpyml
modified: '2026-07-22'
name: Up
nav: Providers
network: true
overview: 'Up publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Attachments API, Banking Account Balances API, and 11 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  The Up catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Up''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, support, authentication, and 27 more developer resources.'
random_paper: 70
rate_limits:
- limit_count: 0
  name: Up Bank Rate Limits
  slug: up-bank-rate-limits
scopes:
- name: Up Bank Scopes
  scope_count: 10
  slug: up-bank-scopes
  summary_line: 10 scopes
score:
  band: developing
  composite: 52.8
  delta: -3.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.7
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
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
    score: 78.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/up-bank/refs/heads/main/screenshots/up-bank-2026-07-21T115740.png
security:
- kind: authentication
  name: Up Bank Authentication
  slug: up-bank-authentication
  summary_line: http/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Up Bank Domain Security
  slug: up-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Up Bank Vulnerability Disclosure
  slug: up-bank-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: up-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Neobank
- Product Reference Data
website: https://www.up.com.au/
---
