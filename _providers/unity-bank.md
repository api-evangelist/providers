---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Unity Bank Agentic Access
  operation_count: 19
  slug: unity-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- description: Banking Account Balance endpoints
  name: Unity Bank Banking Account Balances API
  slug: unity-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Unity Bank Banking Account Direct Debits API
  slug: unity-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Unity Bank Banking Account Scheduled Payments API
  slug: unity-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Unity Bank Banking Account Transactions API
  slug: unity-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Unity Bank Banking Accounts API
  slug: unity-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Unity Bank Banking Payees API
  slug: unity-bank-banking-payees-api
- description: Banking Product endpoints
  name: Unity Bank Banking Products API
  slug: unity-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-unity-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-unity-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-unity-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-unity-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-unity-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-unity-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-unity-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/unity-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/unity-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unity-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unity-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unity-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unity-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unity-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unity-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/unity-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unity-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unity-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unity-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/unity-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.unitybank.com.au/
- group: start
  title: ''
  type: Portal
  url: https://www.unitybank.com.au/about-us/corporate-information/public-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.unity.bank/about-us/corporate-information/open-banking/
- group: company
  title: ''
  type: Blog
  url: https://www.unitybank.com.au/latest-news-blog/articles/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unitybank.com.au/help/rates-fees/view-all-rates-fees/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unitybank.com.au/about-us/corporate-information/disclosure-documents/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unitybank.com.au/about-us/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.unitybank.com.au/talk-to-us/contact-us/
created: '2026-07-20'
description: Unity Bank Limited (ABN 72 087 650 637, AFSL & Australian Credit Licence 238311, BSB 659 000) is an Australian member-owned mutual bank that consolidated the Unity Bank and Reliance Bank brands under a single Unity Bank identity. As an authorised deposit-taking institution (ADI) it offers transaction and savings accounts, term deposits, home loans, personal loans, credit cards, business banking, and wealth services to its members across Australia. Under the Australian Consumer Data Right (CDR / open banking), Unity Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, served on a shared CDR platform (ibank.gcmutualbank.com.au) and documented on the bank's public APIs page. Broader consumer data sharing follows the CDR Accredited Data Recipient (ADR) model and is out of scope of the public PRD surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unity-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Unity Bank MCP Server
  slug: unity-bank-mcp-server
modified: '2026-07-21'
name: Unity Bank
nav: Providers
network: true
overview: 'Unity Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  Unity Bank''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, support, and 17 more developer resources.'
random_paper: 18
scopes:
- name: Unity Bank Scopes
  scope_count: 5
  slug: unity-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 40.6
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
    score: 53.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unity-bank/refs/heads/main/screenshots/unity-bank-2026-07-21T114754.png
security:
- kind: authentication
  name: Unity Bank Authentication
  slug: unity-bank-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Unity Bank Domain Security
  slug: unity-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: unity-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Mutual Bank
- Product Reference Data
website: https://www.unitybank.com.au/
---
