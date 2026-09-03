---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
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
  score: 22.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: AMP Bank Banking Account Balances API
  slug: amp-bank-banking-account-balances-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: AMP Bank Banking Account Direct Debits API
  slug: amp-bank-banking-account-direct-debits-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: AMP Bank Banking Account Scheduled Payments API
  slug: amp-bank-banking-account-scheduled-payments-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: AMP Bank Banking Account Transactions API
  slug: amp-bank-banking-account-transactions-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: AMP Bank Banking Accounts API
  slug: amp-bank-banking-accounts-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: AMP Bank Banking Payees API
  slug: amp-bank-banking-payees-api
- baseURL: https://api.cdr-api.amp.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: AMP Bank Banking Products API
  slug: amp-bank-banking-products-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-amp-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-amp-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-amp-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-amp-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-amp-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-amp-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-amp-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amp-bank-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amp-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amp-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amp.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.amp.com.au/personal-banking/open-banking/open-banking-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amp.com.au/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amp.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.amp.com.au/help-and-support
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/ampau
- group: auth
  title: ''
  type: Authentication
  url: authentication/amp-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amp-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amp-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amp-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amp-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/#versioning
- group: design
  title: ''
  type: Conformance
  url: conformance/amp-bank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amp-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amp-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amp-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amp-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amp-bank-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amp-bank-security.txt
created: '2026-07-20'
description: AMP Bank Limited is the retail and business banking arm of AMP Limited (ASX:AMP), a diversified Australian financial services group operating since 1849 and headquartered in Sydney. AMP Bank is a publicly listed (shareholder-owned, not a mutual) authorised deposit-taking institution (ADI) regulated by APRA, offering home loans, deposit and savings accounts, and the digital AMP Bank GO small-business and everyday banking brand. As an active ADI, AMP participates in Australia's Consumer Data Right (CDR / Open Banking) regime and exposes public, unauthenticated Product Reference Data (PRD) APIs conforming to the DSB Consumer Data Standards, alongside the accredited, FAPI-secured consumer data sharing surface used by authorised data recipients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amp-bank.png
layout: provider
mcp_servers:
- description: ''
  name: AMP Bank MCP Server
  slug: amp-bank-mcp-server
modified: '2026-07-21'
name: AMP Bank
nav: Providers
network: true
overview: 'AMP Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  AMP Bank''s developer surface includes documentation, getting-started guide, support, authentication, and 22 more developer resources.'
random_paper: 19
scopes:
- name: Amp Bank Scopes
  scope_count: 5
  slug: amp-bank-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 42.9
  provenance:
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amp-bank/refs/heads/main/screenshots/amp-bank-2026-07-21T114657.png
security:
- kind: authentication
  name: Amp Bank Authentication
  slug: amp-bank-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Amp Bank Domain Security
  slug: amp-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Amp Bank Vulnerability Disclosure
  slug: amp-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amp-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Product Reference Data
- ADI
website: https://www.amp.com.au/
---
