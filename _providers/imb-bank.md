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
  score: 34.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Imb Bank Agentic Access
  operation_count: 19
  slug: imb-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: IMB Bank Banking Account Balances API
  slug: imb-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: IMB Bank Banking Account Direct Debits API
  slug: imb-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: IMB Bank Banking Account Scheduled Payments API
  slug: imb-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: IMB Bank Banking Account Transactions API
  slug: imb-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: IMB Bank Banking Accounts API
  slug: imb-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: IMB Bank Banking Payees API
  slug: imb-bank-banking-payees-api
- description: Banking Product endpoints
  name: IMB Bank Banking Products API
  slug: imb-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-imb-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-imb-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-imb-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-imb-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-imb-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-imb-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-imb-bank-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imb-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imb-bank-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/imb-bank-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imb-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/imb-bank-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/imb-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.imb.com.au/pdfs/consumer-data-right-policy
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imb-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/imb-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.imb.com.au/help-centre/banking-help/service-updates
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/imb-bank-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/imb-bank-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/imb-bank-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imb-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/imb-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imb-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/imb-bank-browse-products.md
- group: company
  title: ''
  type: Website
  url: https://www.imb.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.openbanking.imb.com.au/public/apis
- group: docs
  title: ''
  type: Documentation
  url: https://www.imb.com.au/openbanking
- group: docs
  title: ''
  type: APIReference
  url: https://developer.openbanking.imb.com.au/public/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.openbanking.imb.com.au/public/apis
- group: start
  title: ''
  type: SignUp
  url: https://developer.openbanking.imb.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imb.com.au/important-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imb.com.au/important-information/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.imb.com.au/help-centre
- group: company
  title: ''
  type: About
  url: https://www.imb.com.au/about-us
created: '2026-07-20'
description: IMB Bank (IMB Ltd, ABN 92 087 651 974) is a member-owned Australian mutual bank founded in 1880 as the Illawarra Mutual Building Society in Wollongong, New South Wales. It is an authorised deposit-taking institution (ADI) regulated by APRA and ASIC, offering home loans, personal and business banking, deposits, cards and insurance to members across NSW, Victoria and the ACT. As a mutual, IMB is owned by its members rather than external shareholders. Under Australia's Consumer Data Right (CDR / Open Banking), IMB operates as a data holder and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Consumer Data Standards, alongside an accredited data recipient (ADR) consent flow for sharing member banking data. IMB also runs a public developer sandbox and marketplace at developer.openbanking.imb.com.au.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imb-bank.png
layout: provider
mcp_servers:
- description: ''
  name: imb-bank-mcp.yml
  slug: imb-bank-mcpyml
modified: '2026-07-21'
name: IMB Bank
nav: Providers
network: true
overview: 'IMB Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  IMB Bank''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, support, and 21 more developer resources.'
random_paper: 24
scopes:
- name: Imb Bank Scopes
  scope_count: 12
  slug: imb-bank-scopes
  summary_line: 12 scopes
score:
  band: developing
  composite: 47.3
  delta: -1.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 51.0
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 23.7
  previous_composite: 49.1
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
    score: 77.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imb-bank/refs/heads/main/screenshots/imb-bank-2026-07-21T114727.png
security:
- kind: authentication
  name: Imb Bank Authentication
  slug: imb-bank-authentication
  summary_line: none/openIdConnect/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Imb Bank Domain Security
  slug: imb-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imb-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.imb.com.au/
---
