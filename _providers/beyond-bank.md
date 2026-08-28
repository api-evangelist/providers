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
  name: Beyond Bank Agentic Access
  operation_count: 19
  slug: beyond-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Beyond Bank Australia Banking Account Balances API
  slug: beyond-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Beyond Bank Australia Banking Account Direct Debits API
  slug: beyond-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Beyond Bank Australia Banking Account Scheduled Payments API
  slug: beyond-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Beyond Bank Australia Banking Account Transactions API
  slug: beyond-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Beyond Bank Australia Banking Accounts API
  slug: beyond-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Beyond Bank Australia Banking Payees API
  slug: beyond-bank-banking-payees-api
- description: Banking Product endpoints
  name: Beyond Bank Australia Banking Products API
  slug: beyond-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-beyond-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-beyond-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-beyond-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-beyond-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-beyond-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-beyond-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-beyond-bank-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beyond-bank-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beyond-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beyond-bank-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beyond-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beyondbank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.beyondbank.com.au/open-banking/beyond-bank-product-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.beyondbank.com.au/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#get-products
- group: start
  title: ''
  type: GettingStarted
  url: https://www.beyondbank.com.au/open-banking/product-api.html
- group: company
  title: ''
  type: Blog
  url: https://www.beyondbank.com.au/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beyond-bank-australia
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beyondbank.com.au/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beyondbank.com.au/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.beyondbank.com.au/help-and-contact/
- group: other
  title: ''
  type: Overlay
  url: overlays/beyond-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beyond-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beyond-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/beyond-bank-lookup-banking-products.md
- group: design
  title: ''
  type: Conventions
  url: conventions/beyond-bank-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beyond-bank-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beyond-bank-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beyond-bank-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beyond-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#version-control
created: '2026-07-20'
description: Beyond Bank Australia Limited (ABN 15 087 651 143, AFSL/Australian Credit Licence 237856) is one of the country's largest customer-owned (mutual) banks, owned by its members rather than shareholders, and the first bank in Australia to become a certified B Corp. It serves roughly 280,000 members from around 56 branches across South Australia, Victoria, the ACT, Western Australia, and New South Wales, with more than nine billion dollars in funds under management, offering everyday accounts, savings, term deposits, loans, insurance, and financial planning. As an Authorised Deposit-taking Institution (ADI) it participates in Australia's Consumer Data Right (CDR / Open Banking), exposing a public, unauthenticated Product Reference Data (PRD) API built to the Data Standards Body (DSB) Consumer Data Standards; consumer data sharing beyond product reference data requires accredited data recipient status and the CDR OAuth2/OIDC FAPI authorization model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beyond-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Beyond Bank Australia MCP Server
  slug: beyond-bank-australia-mcp-server
modified: '2026-07-21'
name: Beyond Bank Australia
nav: Providers
network: true
overview: 'Beyond Bank Australia publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Beyond Bank Australia''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, and 18 more developer resources.'
random_paper: 6
scopes:
- name: Beyond Bank Scopes
  scope_count: 5
  slug: beyond-bank-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 44.1
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
    score: 60.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beyond-bank/refs/heads/main/screenshots/beyond-bank-2026-07-21T114718.png
security:
- kind: authentication
  name: Beyond Bank Authentication
  slug: beyond-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Beyond Bank Domain Security
  slug: beyond-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beyond-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Customer Owned
- Product Reference Data
website: https://www.beyondbank.com.au/
---
