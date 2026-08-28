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
  name: Anz Agentic Access
  operation_count: 19
  slug: anz-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 16
apis:
- description: ANZ's first-party Payments API suite on the ANZ Developer Portal, letting business and institutional customers automate and optimise payment workflows across domestic payment rails (NPP / direct entry
  name: Australia and New Zealand Banking Group (ANZ) Payments API
  slug: anz-payments-api
- description: ANZ's first-party PayTo API (also available as a file channel) for real-time account-to-account payments and PayTo mandate management over the New Payments Platform (NPP). Documented on the ANZ Develo
  name: Australia and New Zealand Banking Group (ANZ) PayTo API
  slug: anz-payto-api
- description: ANZ's first-party PayID Check API to verify that a PayID is registered before initiating a payment or collection, streamlining NPP payment and collection workflows. Documented on the ANZ Developer Por
  name: Australia and New Zealand Banking Group (ANZ) PayID Check API
  slug: anz-payid-check-api
- description: 'ANZ''s first-party Confirmation of Payee API matches a recipient''s account name against their BSB and account number to reduce mistaken and mistakenly-directed payments and help prevent scams before a '
  name: Australia and New Zealand Banking Group (ANZ) Confirmation of Payee API
  slug: anz-confirmation-of-payee-api
- description: ANZ's first-party Account Statements API provides real-time and end-of-day account statements so business and institutional customers can monitor transactions and support reconciliation. Documented on
  name: Australia and New Zealand Banking Group (ANZ) Account Statements API
  slug: anz-account-statements-api
- description: ANZ's first-party Real-Time Notification API delivers instant alerts for transaction and account events so business customers can enhance real-time reconciliation. Documented on the ANZ Developer Port
  name: Australia and New Zealand Banking Group (ANZ) Real-Time Notification API
  slug: anz-real-time-notification-api
- description: ANZ's first-party FX (Foreign Exchange) API to automate currency management and optimise foreign-exchange operations for business and institutional customers. Documented on the ANZ Developer Portal; a
  name: Australia and New Zealand Banking Group (ANZ) FX API
  slug: anz-fx-api
- description: ANZ's first-party ACMC (Accounts & Cash Management) API suite supports client-monies and cash-management use cases for institutional customers, enhancing financial management across accounts. Document
  name: Australia and New Zealand Banking Group (ANZ) ACMC (Accounts & Cash Management) API
  slug: anz-acmc-api
- description: ANZ's first-party NPP Agency API set (Agency Core, Agency PayTo Payer, Agency PayTo Biller, and Agency Confirmation of Payee) provides core payment and account-management capabilities for New Payments
  name: Australia and New Zealand Banking Group (ANZ) NPP Agency API
  slug: anz-npp-agency-api
- description: Banking Account Balance endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Account Balances API
  slug: anz-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Account Direct Debits API
  slug: anz-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Account Scheduled Payments API
  slug: anz-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Account Transactions API
  slug: anz-banking-account-transactions-api
- description: Banking Account endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Accounts API
  slug: anz-banking-accounts-api
- description: Banking Payee endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Payees API
  slug: anz-banking-payees-api
- description: Banking Product endpoints
  name: Australia and New Zealand Banking Group (ANZ) Banking Products API
  slug: anz-banking-products-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-anz-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-anz-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-anz-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-anz-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-anz-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-anz-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-anz-banking-products-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anz-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anz-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anz-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.anz/cds-au/v1/discovery/status
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/anz-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anz-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anz-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anz-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/anz-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/anz-product-reference-data.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/anz-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/anz-vdp
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: operate
  title: ''
  type: Support
  url: https://www.anz.com.au/security/
- group: company
  title: ''
  type: Website
  url: https://www.anz.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.online.anz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anz.com.au/support/legal/anz-apis/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ANZ-Bank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/anz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anz.com.au/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anz.com.au/support/help/website-terms-use/
created: '2026-07-20'
description: Australia and New Zealand Banking Group Limited (ANZ) is one of Australia's "Big Four" banks, a publicly listed company (ASX and NZX code ANZ) headquartered in Melbourne that provides retail, commercial, and institutional banking across Australia, New Zealand, and internationally. ANZ is not a mutual or customer-owned institution; it is a shareholder-owned Authorised Deposit-taking Institution (ADI) regulated by APRA. As a designated data holder under Australia's Consumer Data Right (CDR / Open Banking), ANZ exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body (DSB) Consumer Data Standards, and operates a separate CDR brand endpoint for ANZ Plus. Consumer data sharing beyond product reference data is gated behind the CDR accredited-data-recipient (ADR) model using OAuth2 / OpenID Connect FAPI security profiles.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/anz.png
layout: provider
mcp_servers:
- description: ''
  name: Australia and New Zealand Banking Group (ANZ) MCP Server
  slug: australia-and-new-zealand-banking-group-anz-mcp-server
modified: '2026-07-21'
name: Australia and New Zealand Banking Group (ANZ)
nav: Providers
network: true
overview: 'Australia and New Zealand Banking Group (ANZ) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Australia and New Zealand Banking Group (ANZ)''s developer surface includes authentication, API reference, support, documentation, and 22 more developer resources.'
random_paper: 14
scopes:
- name: Anz Scopes
  scope_count: 5
  slug: anz-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 49.7
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 46.6
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
    score: 78.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anz/refs/heads/main/screenshots/anz-2026-07-21T114652.png
security:
- kind: authentication
  name: Anz Authentication
  slug: anz-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Anz Domain Security
  slug: anz-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Anz Vulnerability Disclosure
  slug: anz-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: anz
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.anz.com.au/
---
