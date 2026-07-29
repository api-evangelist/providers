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
    well_known_catalog: true
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-07-28'
api_count: 14
apis:
- description: The Accounts API from Newcastle Permanent Building Society — 6 operation(s) for accounts.
  name: Newcastle Permanent Building Society Accounts API
  slug: newcastle-permanent-accounts-api
- description: Banking Account Balance endpoints
  name: Newcastle Permanent Building Society Banking Account Balances API
  slug: newcastle-permanent-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Newcastle Permanent Building Society Banking Account Direct Debits API
  slug: newcastle-permanent-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Newcastle Permanent Building Society Banking Account Scheduled Payments API
  slug: newcastle-permanent-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Newcastle Permanent Building Society Banking Account Transactions API
  slug: newcastle-permanent-banking-account-transactions-api
- description: Banking Account endpoints
  name: Newcastle Permanent Building Society Banking Accounts API
  slug: newcastle-permanent-banking-accounts-api
- description: The Banking API from Newcastle Permanent Building Society — 14 operation(s) for banking.
  name: Newcastle Permanent Building Society Banking API
  slug: newcastle-permanent-banking-api
- description: Banking Payee endpoints
  name: Newcastle Permanent Building Society Banking Payees API
  slug: newcastle-permanent-banking-payees-api
- description: Banking Product endpoints
  name: Newcastle Permanent Building Society Banking Products API
  slug: newcastle-permanent-banking-products-api
- description: The Common API from Newcastle Permanent Building Society — 2 operation(s) for common.
  name: Newcastle Permanent Building Society Common API
  slug: newcastle-permanent-common-api
- description: The Customer API from Newcastle Permanent Building Society — 2 operation(s) for customer.
  name: Newcastle Permanent Building Society Customer API
  slug: newcastle-permanent-customer-api
- description: The Direct Debits API from Newcastle Permanent Building Society — 2 operation(s) for direct debits.
  name: Newcastle Permanent Building Society Direct Debits API
  slug: newcastle-permanent-direct-debits-api
- description: The Payees API from Newcastle Permanent Building Society — 2 operation(s) for payees.
  name: Newcastle Permanent Building Society Payees API
  slug: newcastle-permanent-payees-api
- description: The Scheduled Payments API from Newcastle Permanent Building Society — 2 operation(s) for scheduled payments.
  name: Newcastle Permanent Building Society Scheduled Payments API
  slug: newcastle-permanent-scheduled-payments-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newcastle-permanent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.newcastlepermanent.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.newcastlepermanent.com.au/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.newcastlepermanent.com.au/public/apis
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api
- group: other
  title: ''
  type: Email
  url: mailto:OpenBankingSupport@newcastlepermanent.com.au
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newcastle-permanent
- group: start
  title: ''
  type: Sandbox
  url: https://developer.newcastlepermanent.com.au/
- group: auth
  title: ''
  type: Authentication
  url: authentication/newcastle-permanent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/newcastle-permanent-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/newcastle-permanent-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/newcastle-permanent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/newcastle-permanent-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/newcastle-permanent-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/newcastle-permanent-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://openbank.newcastlepermanent.com.au/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: DataModel
  url: data-model/newcastle-permanent-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/newcastle-permanent-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/newcastle-permanent-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/newcastle-permanent-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/newcastle-permanent-browse-products.md
- group: auth
  title: ''
  type: Compliance
  url: https://www.newcastlepermanent.com.au/cdr-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.newcastlepermanent.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.newcastlepermanent.com.au/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.newcastlepermanent.com.au/contact-us
- group: other
  title: ''
  type: OpenBanking
  url: https://www.newcastlepermanent.com.au/tools-and-services/digital-banking/open-banking
created: '2026-07-20'
description: Newcastle Permanent Building Society is a customer-owned Australian authorised deposit-taking institution (ADI) founded in 1903 and headquartered in Newcastle, New South Wales. As a mutual, it is owned by its members rather than shareholders, and it provides retail banking, home loans, savings, term deposits, and insurance to communities across NSW. In March 2023 it merged with Greater Bank to form Newcastle Greater Mutual Group (NGM Group), one of Australia's largest customer-owned banks, while Newcastle Permanent continues to operate as a consumer brand. As a regulated ADI it is a data holder under Australia's Consumer Data Right (CDR / Open Banking) and exposes a live, public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body Consumer Data Standards, alongside an NPBS Innovation Sandbox and Marketplace developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newcastle-permanent.png
layout: provider
mcp_servers:
- description: ''
  name: newcastle-permanent-mcp.yml
  slug: newcastle-permanent-mcpyml
modified: '2026-07-21'
name: Newcastle Permanent Building Society
nav: Providers
network: true
overview: 'Newcastle Permanent Building Society publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Banking Account Balances API, Banking Account Direct Debits API, and 11 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Newcastle Permanent Building Society''s developer surface includes getting-started guide, documentation, API reference, sandbox, authentication, support, and 22 more developer resources.'
random_paper: 37
scopes:
- name: Newcastle Permanent Scopes
  scope_count: 12
  slug: newcastle-permanent-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 49.1
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.4
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 52.6
  provenance:
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
    score: 77.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newcastle-permanent/refs/heads/main/screenshots/newcastle-permanent-2026-07-21T115738.png
security:
- kind: authentication
  name: Newcastle Permanent Authentication
  slug: newcastle-permanent-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Newcastle Permanent Domain Security
  slug: newcastle-permanent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: newcastle-permanent
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Building Society
- Mutual
- Australia
website: https://www.newcastlepermanent.com.au/
---
