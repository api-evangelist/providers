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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Banksa Agentic Access
  operation_count: 19
  slug: banksa-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: BankSA Banking Account Balances API
  slug: banksa-banking-account-balances-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: BankSA Banking Account Direct Debits API
  slug: banksa-banking-account-direct-debits-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: BankSA Banking Account Scheduled Payments API
  slug: banksa-banking-account-scheduled-payments-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: BankSA Banking Account Transactions API
  slug: banksa-banking-account-transactions-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: BankSA Banking Accounts API
  slug: banksa-banking-accounts-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: BankSA Banking Payees API
  slug: banksa-banking-payees-api
- baseURL: https://digital-api.banksa.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: BankSA Banking Products API
  slug: banksa-banking-products-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-banksa-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-banksa-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-banksa-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-banksa-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-banksa-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-banksa-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-banksa-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/banksa-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/banksa-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/banksa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.banksa.com.au/online-services/security-centre
- group: auth
  title: ''
  type: DomainSecurity
  url: security/banksa-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/banksa-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/banksa-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/banksa-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/banksa-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/banksa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/banksa-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/banksa-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/banksa-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/banksa-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/banksa-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/banksa-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.banksa.com.au/
- group: other
  title: ''
  type: OpenBanking
  url: https://www.banksa.com.au/online-services/open-banking
- group: docs
  title: ''
  type: APIReference
  url: https://www.banksa.com.au/online-services/open-banking/product-api
- group: design
  title: ''
  type: ErrorMapping
  url: https://www.banksa.com.au/online-services/open-banking/error-mapping
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banksa.com.au/privacy/privacy-statement
- group: auth
  title: ''
  type: DomainSecurity
  url: https://www.banksa.com.au/security
- group: operate
  title: ''
  type: Support
  url: https://www.banksa.com.au/help
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-sa
- group: docs
  title: ''
  type: Documentation
  url: https://consumerdatastandardsaustralia.github.io/standards/
created: '2026-07-20'
description: BankSA is a South Australian retail and business banking brand operating as a division of Westpac Banking Corporation (ABN 33 007 457 141, AFSL and Australian credit licence 233714). It is not a mutual or independent ADI - it shares the Westpac Group core banking platform alongside sibling brands St.George and Bank of Melbourne. Under Australia's Consumer Data Right (CDR / Open Banking) regime, BankSA exposes a live, public, unauthenticated Product Reference Data (PRD) API conforming to the DSB Consumer Data Standards, hosted at digital-api.banksa.com.au. Consumer and account data sharing beyond product reference data runs on the accredited-data-recipient (ADR) model with OAuth2 / OpenID Connect (FAPI) authorization; BankSA does not publish an open self-service developer portal for third-party integration outside the CDR channel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/banksa.png
layout: provider
mcp_servers:
- description: ''
  name: BankSA MCP Server
  slug: banksa-mcp-server
modified: '2026-07-21'
name: BankSA
nav: Providers
network: true
overview: 'BankSA publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Data Right.


  BankSA''s developer surface includes authentication, API reference, support, documentation, and 22 more developer resources.'
random_paper: 15
scopes:
- name: Banksa Scopes
  scope_count: 9
  slug: banksa-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 38.4
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
    jurisdictions:
    - jurisdiction: AU
      standard: cdr-consumer-data-standards
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 73.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/banksa/refs/heads/main/screenshots/banksa-2026-07-21T114709.png
security:
- kind: authentication
  name: Banksa Authentication
  slug: banksa-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Banksa Domain Security
  slug: banksa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Banksa Vulnerability Disclosure
  slug: banksa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: banksa
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Data Right
- Consumer Banking
- Australia
- Product Reference Data
website: https://www.banksa.com.au/
---
