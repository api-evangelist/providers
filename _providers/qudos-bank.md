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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Qudos Bank Agentic Access
  operation_count: 19
  slug: qudos-bank-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 1
apis:
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Balance endpoints
  name: Qudos Bank Banking Account Balances API
  slug: qudos-bank-banking-account-balances-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Direct Debit endpoints
  name: Qudos Bank Banking Account Direct Debits API
  slug: qudos-bank-banking-account-direct-debits-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Scheduled Payment endpoints
  name: Qudos Bank Banking Account Scheduled Payments API
  slug: qudos-bank-banking-account-scheduled-payments-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account Transaction endpoints
  name: Qudos Bank Banking Account Transactions API
  slug: qudos-bank-banking-account-transactions-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Account endpoints
  name: Qudos Bank Banking Accounts API
  slug: qudos-bank-banking-accounts-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Payee endpoints
  name: Qudos Bank Banking Payees API
  slug: qudos-bank-banking-payees-api
- baseURL: https://public.cdr.qudosbank.com.au/cds-au/v1/banking/products
  baseurl_source: declared
  description: Banking Product endpoints
  name: Qudos Bank Banking Products API
  slug: qudos-bank-banking-products-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CDR Banking Banking Account Balances API
  slug: open-qudos-bank-banking-account-balances-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Direct Debits API
  slug: open-qudos-bank-banking-account-direct-debits-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Scheduled Payments API
  slug: open-qudos-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Account Transactions API
  slug: open-qudos-bank-banking-account-transactions-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Accounts API
  slug: open-qudos-bank-banking-accounts-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Payees API
  slug: open-qudos-bank-banking-payees-api
- collection_type: open
  name: CDR Banking Banking Account Balances Banking Products API
  slug: open-qudos-bank-banking-products-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/qudos-bank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qudos-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qudos-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qudos-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qudos-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qudos-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qudos-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qudos-bank-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qudos-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.qudosbank.com.au/support/open-banking
- group: design
  title: ''
  type: DataModel
  url: data-model/qudos-bank-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qudos-bank-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qudos-bank-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/qudos-bank-cds-banking-products-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qudos-bank-list-products.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qudos-bank-get-product-detail.md
- group: company
  title: ''
  type: Website
  url: https://www.qudosbank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.qudosbank.com.au/support/open-banking
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.qudosbank.com.au/support/open-banking
- group: company
  title: ''
  type: Blog
  url: https://www.qudosbank.com.au/news-tools-tips/news-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qudosbank.com.au/support/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qudosbank.com.au/support/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.qudosbank.com.au/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qudos-bank
created: '2026-07-20'
description: Qudos Bank is an Australian customer-owned (mutual) bank that has been 100% customer-owned since 1959, serving members with everyday transaction and savings accounts, term deposits, credit cards, home and personal loans, and offset accounts. Following its 2025 merger it now operates as a division of Bank Australia Limited (ABN 21 087 651 607, trading as Qudos Bank), one of the largest customer-owned banks in the country. As an Australian authorised deposit-taking institution and a designated data holder under the Consumer Data Right (CDR / Open Banking), Qudos Bank exposes a public, unauthenticated Product Reference Data (PRD) API conforming to the Data Standards Body Consumer Data Standards, and supports authenticated CDR consumer data sharing with accredited data recipients under the ACCC / FAPI security profile.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qudos-bank.png
layout: provider
modified: '2026-07-21'
name: Qudos Bank
nav: Providers
network: true
overview: 'Qudos Bank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Banking Account Balances API, Banking Account Direct Debits API, Banking Account Scheduled Payments API, and 4 more. Tagged areas include Financial, Banks, Open Banking, CDR, and Consumer Banking.


  Qudos Bank''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, and 19 more developer resources.'
random_paper: 5
scopes:
- name: Qudos Bank Scopes
  scope_count: 5
  slug: qudos-bank-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 44.8
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
    score: 77.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qudos-bank/refs/heads/main/screenshots/qudos-bank-2026-07-21T114742.png
security:
- kind: authentication
  name: Qudos Bank Authentication
  slug: qudos-bank-authentication
  summary_line: none/oauth2/openIdConnect/mutualTLS · 2 schemes
- kind: domain-security
  name: Qudos Bank Domain Security
  slug: qudos-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qudos-bank
tags:
- Financial
- Banks
- Open Banking
- CDR
- Consumer Banking
- Australia
- Customer Owned
- Mutual Bank
- Product Reference Data
website: https://www.qudosbank.com.au/
---
