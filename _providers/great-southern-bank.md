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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 34.7
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Great Southern Bank Banking Account Balances API
  slug: great-southern-bank-banking-account-balances-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Great Southern Bank Banking Account Direct Debits API
  slug: great-southern-bank-banking-account-direct-debits-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Great Southern Bank Banking Account Scheduled Payments API
  slug: great-southern-bank-banking-account-scheduled-payments-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Great Southern Bank Banking Account Transactions API
  slug: great-southern-bank-banking-account-transactions-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Great Southern Bank Banking Accounts API
  slug: great-southern-bank-banking-accounts-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Great Southern Bank Banking Payees API
  slug: great-southern-bank-banking-payees-api
- baseURL: https://api.open-banking.greatsouthernbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Great Southern Bank Banking Products API
  slug: great-southern-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-great-southern-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-great-southern-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-great-southern-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-great-southern-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-great-southern-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-great-southern-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-great-southern-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/great-southern-bank-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/great-southern-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/great-southern-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/great-southern-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/great-southern-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/great-southern-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/great-southern-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/great-southern-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/great-southern-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/great-southern-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/great-southern-bank-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/great-southern-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/great-southern-bank-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/great-southern-bank-openid-configuration.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/great-southern-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/great-southern-bank-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/great-southern-bank-lookup-products.md
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/#consumer-data-standards-banking-apis
- group: start
  title: ''
  type: Portal
  url: https://www.greatsouthernbank.com.au/open-banking
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.greatsouthernbank.com.au/open-banking
- group: company
  title: ''
  type: Website
  url: https://www.greatsouthernbank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.greatsouthernbank.com.au/consumer-data-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/great-southern-bank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greatsouthernbank.com.au/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greatsouthernbank.com.au/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.greatsouthernbank.com.au/help-and-contact/support
- group: company
  title: ''
  type: Blog
  url: https://www.greatsouthernbank.com.au/about/news
created: '2026-07-20'
description: Great Southern Bank is one of Australia's largest customer-owned (mutual) banks, operating as a business name of Credit Union Australia Ltd (ABN 44 087 650 959, AFSL and Australian Credit Licence 238317). Formerly known as Credit Union Australia (CUA) before rebranding to Great Southern Bank in 2021, it is owned by its customers rather than shareholders and serves retail and small-business members with transaction accounts, savings, term deposits, home loans, credit cards, and insurance. As an Australian authorised deposit-taking institution (ADI) it participates in the Consumer Data Right (CDR / Open Banking) as a data holder, exposing public, unauthenticated Product Reference Data (PRD) APIs for both its retail and Business+ brands that conform to the Data Standards Body (DSB) Consumer Data Standards (CDS). Authenticated consumer data sharing is available only to accredited data recipients (ADRs) via the CDR ecosystem; the bank does not operate a self-serve public developer
  portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/great-southern-bank.png
layout: provider
mcp_servers:
- description: ''
  name: Great Southern Bank MCP Server
  slug: great-southern-bank-mcp-server
modified: '2026-07-22'
name: Great Southern Bank
nav: Providers
network: true
overview: 'Great Southern Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Great Southern Bank''s developer surface includes authentication, API reference, developer portal, documentation, support, engineering blog, and 21 more developer resources.'
random_paper: 10
scopes:
- name: Great Southern Bank Scopes
  scope_count: 13
  slug: great-southern-bank-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
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
    score: 67.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/great-southern-bank/refs/heads/main/screenshots/great-southern-bank-2026-07-21T114729.png
security:
- kind: authentication
  name: Great Southern Bank Authentication
  slug: great-southern-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 4 schemes
- kind: domain-security
  name: Great Southern Bank Domain Security
  slug: great-southern-bank-domain-security
  summary_line: TLSv1.3 · DMARC
slug: great-southern-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Customer Owned
- Product Reference Data
website: https://www.greatsouthernbank.com.au/
---
