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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bankwest Agentic Access
  operation_count: 19
  slug: bankwest-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 7
apis:
- description: Banking Account Balance endpoints
  name: Bankwest Banking Account Balances API
  slug: bankwest-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Bankwest Banking Account Direct Debits API
  slug: bankwest-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Bankwest Banking Account Scheduled Payments API
  slug: bankwest-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Bankwest Banking Account Transactions API
  slug: bankwest-banking-account-transactions-api
- description: Banking Account endpoints
  name: Bankwest Banking Accounts API
  slug: bankwest-banking-accounts-api
- description: Banking Payee endpoints
  name: Bankwest Banking Payees API
  slug: bankwest-banking-payees-api
- description: Banking Product endpoints
  name: Bankwest Banking Products API
  slug: bankwest-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-bankwest-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-bankwest-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-bankwest-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-bankwest-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-bankwest-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-bankwest-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-bankwest-banking-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bankwest-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bankwest-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bankwest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bankwest-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bankwest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bankwest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bankwest-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bankwest.com.au/support/payments/payment-services-availability
- group: design
  title: ''
  type: Conformance
  url: conformance/bankwest-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bankwest-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bankwest-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bankwest-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bankwest-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankwest.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bankwest.com.au/support/open-banking/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankwest.com.au/support/open-banking
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#cdr-banking-apis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bankwest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankwest.com.au/legal-stuff/bankwest-privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankwest.com.au/legal-stuff/website-terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.bankwest.com.au/support
created: '2026-07-20'
description: Bankwest is an Australian retail and business bank headquartered in Perth, Western Australia. Founded in 1895 as the Agricultural Bank of Western Australia and later the Bank of Western Australia, it has operated as a wholly owned subsidiary of Commonwealth Bank of Australia (CBA) since CBA's December 2008 acquisition. In March 2024 Bankwest announced it would close its remaining branch network and become a digital-only bank, retaining the Bankwest brand for personal and business customers nationally. As an authorised deposit-taking institution brand operating under Australia's Consumer Data Right (CDR / Open Banking) regime, Bankwest exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body Consumer Data Standards; consumer data sharing beyond PRD requires ACCC accreditation and customer consent under the CDR authorisation model.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bankwest.png
layout: provider
mcp_servers:
- description: ''
  name: Bankwest MCP Server
  slug: bankwest-mcp-server
modified: '2026-07-21T12:00:00Z'
name: Bankwest
nav: Providers
network: true
overview: 'Bankwest publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Bankwest''s developer surface includes authentication, documentation, API reference, support, and 18 more developer resources.'
random_paper: 2
scopes:
- name: Bankwest Scopes
  scope_count: 5
  slug: bankwest-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 41.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 51.0
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 41.4
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bankwest/refs/heads/main/screenshots/bankwest-2026-07-21T114718.png
security:
- kind: authentication
  name: Bankwest Authentication
  slug: bankwest-authentication
  summary_line: none/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Bankwest Domain Security
  slug: bankwest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bankwest
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- Digital Bank
website: https://www.bankwest.com.au/
---
