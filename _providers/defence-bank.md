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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Defence Bank Agentic Access
  operation_count: 19
  slug: defence-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Defence Bank Banking Account Balances API
  slug: defence-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Defence Bank Banking Account Direct Debits API
  slug: defence-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Defence Bank Banking Account Scheduled Payments API
  slug: defence-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Defence Bank Banking Account Transactions API
  slug: defence-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Defence Bank Banking Accounts API
  slug: defence-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Defence Bank Banking Payees API
  slug: defence-bank-banking-payees-api
- description: Banking Product endpoints
  name: Defence Bank Banking Products API
  slug: defence-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-defence-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-defence-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-defence-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-defence-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-defence-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-defence-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-defence-bank-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/defence-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defence-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.defencebank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.defencebank.com.au/tools-and-advice/open-banking/
- group: company
  title: ''
  type: Blog
  url: https://www.defencebank.com.au/intel
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.defencebank.com.au/tools-and-advice/legal-and-compliance/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.defencebank.com.au/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defencebank
- group: start
  title: ''
  type: GettingStarted
  url: https://www.defencebank.com.au/tools-and-advice/open-banking/
- group: auth
  title: ''
  type: Authentication
  url: authentication/defence-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/defence-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/defence-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/defence-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/defence-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/defence-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.defencebank.com.au/tools-and-advice/open-banking/
- group: design
  title: ''
  type: DataModel
  url: data-model/defence-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/defence-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defence-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/defence-bank-cds-banking-products-overlay.yaml
created: '2026-07-20'
description: Defence Bank Limited is an Australian customer-owned (mutual) bank established in 1975 and headquartered in Melbourne, serving current and former Australian Defence Force personnel, Department of Defence employees, and their families as well as the broader community. As an APRA-regulated Authorised Deposit-taking Institution (ADI), it exists to return value to members rather than external shareholders. Under Australia's Consumer Data Right (CDR / Open Banking), Defence Bank operates as a data holder and exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards; deeper consumer-data sharing requires an accredited data recipient and the OAuth2/OIDC FAPI CDR authorization model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defence-bank.png
layout: provider
mcp_servers:
- description: Candidate MCP server surface derived from the publicly reachable Consumer Data Standards Product Reference Data operations. Defence Bank publishes no official hosted MCP server; these tools map one-to
  name: Defence Bank MCP Server
  slug: defence-bank-mcp-server
modified: '2026-07-21'
name: Defence Bank
nav: Providers
network: true
overview: 'Defence Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Defence Bank''s developer surface includes documentation, engineering blog, support, getting-started guide, authentication, and 17 more developer resources.'
random_paper: 16
scopes:
- name: Defence Bank Scopes
  scope_count: 5
  slug: defence-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 43.4
  delta: 1.4
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 30.3
    contract_quality: 49.7
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 7.9
  previous_composite: 42.0
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
    score: 62.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defence-bank/refs/heads/main/screenshots/defence-bank-2026-07-21T114721.png
security:
- kind: authentication
  name: Defence Bank Authentication
  slug: defence-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Defence Bank Domain Security
  slug: defence-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: defence-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.defencebank.com.au/
---
