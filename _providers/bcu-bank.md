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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bcu Bank Agentic Access
  operation_count: 19
  slug: bcu-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: BCU Bank Banking Account Balances API
  slug: bcu-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: BCU Bank Banking Account Direct Debits API
  slug: bcu-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: BCU Bank Banking Account Scheduled Payments API
  slug: bcu-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: BCU Bank Banking Account Transactions API
  slug: bcu-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: BCU Bank Banking Accounts API
  slug: bcu-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: BCU Bank Banking Payees API
  slug: bcu-bank-banking-payees-api
- description: Banking Product endpoints
  name: BCU Bank Banking Products API
  slug: bcu-bank-banking-products-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bcu-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bcu-bank-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bcu-bank-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: well-known/bcu-bank-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bcu-bank-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bcu-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bcu-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bcu-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bcu-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bcu-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bcu-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bcu.com.au/consumer-data-right-policy/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bcu-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bcu-bank-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bcu-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bcu-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bcu-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bcu-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bcu-bank-lookup-products.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bcu-bank-retrieve-accounts-and-transactions.md
- group: company
  title: ''
  type: Website
  url: https://www.bcu.com.au/
- group: company
  title: ''
  type: About
  url: https://www.bcu.com.au/about/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bcu.com.au/help-centre/open-banking/bcu-bank-products-api/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bcu
- group: company
  title: ''
  type: Blog
  url: https://www.bcu.com.au/news-and-media/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bcu.com.au/important-information/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bcu.com.au/important-information/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bcu.com.au/help-centre/
- group: operate
  title: ''
  type: Contact
  url: https://www.bcu.com.au/contact/
created: '2026-07-20'
description: BCU Bank is a customer-owned banking brand operated by Police & Nurses Limited (ABN 69 087 651 876), the mutual bank formed when Bananacoast Community Credit Union merged into the P&N Group. Headquartered on the New South Wales north coast, BCU serves retail and business members with everyday accounts, savings, home and personal lending, and cards. As an Authorised Deposit-taking Institution, BCU is a Consumer Data Right (CDR) Data Holder that exposes a public, unauthenticated Product Reference Data (PRD) API under the DSB Consumer Data Standards, and supports consumer data sharing to accredited data recipients through the CDR consent and Open Banking model. BCU does not run a general-purpose developer portal; its programmatic surface is the standards-based CDR banking API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bcu-bank.png
layout: provider
mcp_servers:
- description: ''
  name: bcu-bank-mcp.yml
  slug: bcu-bank-mcpyml
modified: '2026-07-21'
name: BCU Bank
nav: Providers
network: true
overview: 'BCU Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  BCU Bank''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 25 more developer resources.'
random_paper: 93
scopes:
- name: Bcu Bank Scopes
  scope_count: 5
  slug: bcu-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.3
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 46.4
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
    score: 84.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bcu-bank/refs/heads/main/screenshots/bcu-bank-2026-07-21T114720.png
security:
- kind: authentication
  name: Bcu Bank Authentication
  slug: bcu-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Bcu Bank Domain Security
  slug: bcu-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bcu Bank Vulnerability Disclosure
  slug: bcu-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bcu-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Mutual Bank
- Australia
website: https://www.bcu.com.au/
---
