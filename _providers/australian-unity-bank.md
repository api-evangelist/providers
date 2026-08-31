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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Australian Unity Bank Agentic Access
  operation_count: 19
  slug: australian-unity-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- description: Banking Account Balance endpoints
  name: Australian Unity Bank Banking Account Balances API
  slug: australian-unity-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Australian Unity Bank Banking Account Direct Debits API
  slug: australian-unity-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Australian Unity Bank Banking Account Scheduled Payments API
  slug: australian-unity-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Australian Unity Bank Banking Account Transactions API
  slug: australian-unity-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Australian Unity Bank Banking Accounts API
  slug: australian-unity-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Australian Unity Bank Banking Payees API
  slug: australian-unity-bank-banking-payees-api
- description: Banking Product endpoints
  name: Australian Unity Bank Banking Products API
  slug: australian-unity-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-australian-unity-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-australian-unity-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-australian-unity-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-australian-unity-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-australian-unity-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-australian-unity-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-australian-unity-bank-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/australian-unity-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/australian-unity-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/australian-unity-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/australian-unity-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/australian-unity-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/australian-unity-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/australian-unity-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/australian-unity-bank-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/australian-unity-bank-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/australian-unity-bank-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/australian-unity-bank-cds-banking-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/#banking-apis
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-api
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/australian-unity-bank-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.australianunity.com.au/
- group: other
  title: ''
  type: OpenBanking
  url: https://www.australianunity.com.au/banking/open-banking
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/australian-unity/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.australianunity.com.au/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.australianunity.com.au/terms-and-conditions
created: '2026-07-20'
description: Australian Unity Bank Limited is the banking arm of Australian Unity, a member-owned Australian mutual founded in Melbourne in 1840 with origins in the friendly-societies movement and a group spanning health insurance, wealth management, aged and home care, retirement living, and banking. The bank traces to Big Sky Credit Union, which merged with Australian Unity in 2012, became Big Sky Building Society Limited, and was later renamed Australian Unity Bank Limited; it offers everyday transaction and savings accounts, term deposits, and home loans to members as an APRA-authorised deposit-taking institution (ADI) covered by the Financial Claims Scheme. On its Consumer Data Right (CDR / Open Banking) posture, Australian Unity Bank is a genuine ADI and operates a real CDR Open Banking gateway at open-banking.australianunity.com.au (CloudFront-fronted), which as a mandated data holder exposes the full DSB Consumer Data Standards (CDS) Banking API surface under the /cds-au/v1/banking
  prefix - the public Product Reference Data (PRD) endpoints plus the consumer-authorized Accounts, Balances, Transactions, Direct Debits, Scheduled Payments, and Payees endpoints. A July 2026 probe from a non-AU IP returned HTTP 403 across x-v 1-4 (typical WAF / geo / accreditation gating on CDR hosts), so payloads could not be captured verbatim, but the host resolves and responds - confirming Australian Unity as a live data-holder surface. The bank publishes no separate first-party developer portal or open-banking API documentation beyond CDR (its api.australianunity.com.au host serves only a webMethods Integration Server admin page, not documented APIs); the API contract is the shared DSB Consumer Data Standards.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/australian-unity-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Australian Unity Bank MCP Server
  slug: australian-unity-bank-mcp-server
modified: '2026-07-21'
name: Australian Unity Bank
nav: Providers
network: true
overview: 'Australian Unity Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Australian Unity Bank''s developer surface includes authentication, documentation, API reference, and 17 more developer resources.'
random_paper: 5
scopes:
- name: Australian Unity Bank Scopes
  scope_count: 9
  slug: australian-unity-bank-scopes
  summary_line: 9 scopes · authorizationCode/hybrid
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 12.4
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 70.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/australian-unity-bank/refs/heads/main/screenshots/australian-unity-bank-2026-07-21T114715.png
security:
- kind: authentication
  name: Australian Unity Bank Authentication
  slug: australian-unity-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Australian Unity Bank Domain Security
  slug: australian-unity-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: australian-unity-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Mutual
- Product Reference Data
website: https://www.australianunity.com.au/
---
