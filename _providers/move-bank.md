---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://www.movebank.com.au/'', ''status'': 301, ''note'': ''declared website redirects to https://move.bank/ — a different registrable domain (movebank.com.au -> move.bank), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Move Bank Agentic Access
  operation_count: 19
  slug: move-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: MOVE Bank Banking Account Balances API
  slug: move-bank-banking-account-balances-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: MOVE Bank Banking Account Direct Debits API
  slug: move-bank-banking-account-direct-debits-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: MOVE Bank Banking Account Scheduled Payments API
  slug: move-bank-banking-account-scheduled-payments-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: MOVE Bank Banking Account Transactions API
  slug: move-bank-banking-account-transactions-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: MOVE Bank Banking Accounts API
  slug: move-bank-banking-accounts-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: MOVE Bank Banking Payees API
  slug: move-bank-banking-payees-api
- baseURL: https://openbanking.movebank.com.au/OpenBanking/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: MOVE Bank Banking Products API
  slug: move-bank-banking-products-api
arazzos:
- description: List MOVE Bank's public CDR banking products then fetch full detail for the first one — an unauthenticated, forkable Product Reference Data walkthrough.
  name: Discover MOVE Bank banking products
  slug: move-bank-discover-products
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-move-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-move-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-move-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-move-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-move-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-move-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-move-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/move-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/move-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/move-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/move-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/move-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/move-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/move-bank-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/move-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.movebank.com.au/reusable-documents/important-documents/cdr-policy/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/move-bank-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/move-bank-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/move-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/move-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/move-bank-cds-banking-products-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/move-bank-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/move-bank-discover-products.md
- group: design
  title: ''
  type: Arazzo
  url: arazzo/move-bank-discover-products.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.movebank.com.au/about-us/corporate-information/open-banking/
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: company
  title: ''
  type: Website
  url: https://www.movebank.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openbanking.movebank.com.au/OpenBanking
- group: docs
  title: ''
  type: Documentation
  url: https://www.movebank.com.au/about-us/corporate-information/open-banking/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/movebanksocial
- group: company
  title: ''
  type: Blog
  url: https://www.movebank.com.au/about-us/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.movebank.com.au/about-us/corporate-information/privacy-policy-summary/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.movebank.com.au/about-us/corporate-information/conditions-of-use/
created: '2026-07-20'
description: MOVE Bank is a 100% customer-owned Australian mutual bank operated by MoveBank Ltd (ABN 91 087 651 090, AFSL/Australian credit licence 234 536), headquartered in Brisbane, Queensland. Founded in 1968 as Railways Credit Union to serve railway workers and their families, it rebranded to MOVE Bank in 2018 to serve the broader transport and logistics community nationally, and today manages more than $750 million in assets across transaction and savings accounts, term deposits, home and personal loans, and insurance. As an authorised deposit-taking institution, MOVE Bank participates in Australia's Consumer Data Right (CDR / Open Banking) as a data holder, exposing a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body's Consumer Data Standards, alongside the accredited, consent-based consumer data sharing surface governed by the CDR security profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/move-bank.png
layout: provider
modified: '2026-07-21'
name: MOVE Bank
nav: Providers
network: true
overview: 'MOVE Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  MOVE Bank''s developer surface includes authentication, getting-started guide, API reference, documentation, engineering blog, and 21 more developer resources.'
random_paper: 14
scopes:
- name: Move Bank Scopes
  scope_count: 9
  slug: move-bank-scopes
  summary_line: 9 scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 49.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 30.6
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
    score: 50.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/move-bank/refs/heads/main/screenshots/move-bank-2026-07-21T114734.png
security:
- kind: authentication
  name: Move Bank Authentication
  slug: move-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 0 schemes
- kind: domain-security
  name: Move Bank Domain Security
  slug: move-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: move-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Mutual Bank
- Australia
- Product Reference Data
website: https://www.movebank.com.au/
---
