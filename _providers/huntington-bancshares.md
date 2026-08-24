---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Huntington Bancshares Agentic Access
  operation_count: 4
  slug: huntington-bancshares-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 3
apis:
- description: Account information and balances
  name: Huntington Bancshares Accounts API
  slug: huntington-bancshares-accounts-api
- description: Payment initiation and management
  name: Huntington Bancshares Payments API
  slug: huntington-bancshares-payments-api
- description: Transaction reporting and history
  name: Huntington Bancshares Transactions API
  slug: huntington-bancshares-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Huntington Bank Treasury Management Accounts API
  slug: open-huntington-bancshares-accounts-api
- collection_type: open
  name: Huntington Bank Treasury Management Accounts Payments API
  slug: open-huntington-bancshares-payments-api
- collection_type: open
  name: Huntington Bank Treasury Management Accounts Transactions API
  slug: open-huntington-bancshares-transactions-api
- collection_type: open
  name: Huntington Bank Treasury Management API
  slug: open-huntington-bank-treasury-management-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/huntington-bancshares-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/huntington-bancshares-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/huntington-bancshares-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/huntington-bancshares-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huntington-national-bank
- group: start
  title: ''
  type: Portal
  url: https://hnbdevportal.huntington.com/
- group: company
  title: ''
  type: Website
  url: https://www.huntington.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.huntington.com/privacy
created: '2026-03-21'
description: Huntington Bancshares is a regional bank holding company that provides full-service consumer and business banking, insurance, investment, mortgage, equipment leasing, and commercial banking services. Huntington operates a developer portal at hnbdevportal.huntington.com built on Apigee X, offering API-first treasury management solutions with over 500 interfaces that process more than 10 million transaction events daily.
finops:
- name: Huntington Bancshares Finops
  service_category: Banking & Treasury Management
  slug: huntington-bancshares-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/huntington-bancshares.png
layout: provider
modified: '2026-05-19'
name: Huntington Bancshares
nav: Providers
network: true
overview: 'Huntington Bancshares publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Payments API, and Transactions API. Tagged areas include Banking, ERP Integration, Open Banking, Payments, and Treasury.


  Huntington Bancshares'' developer surface includes authentication, developer portal, and 6 more developer resources.'
plans:
- name: Huntington Bancshares Plans Pricing
  plan_count: 2
  slug: huntington-bancshares-plans-pricing
press:
- date: '2026-05-25'
  title: Huntington Launches Huntington Heads Up® with AI to ...
  url: https://ir.huntington.com/news-presentations/press-releases/detail/172/huntington-launches-huntington-heads-up-with-ai-to-improve-customers-digital-banking-experience
- date: '2026-05-25'
  title: Huntington Bank Announces Treasury Management ...
  url: https://www.prnewswire.com/news-releases/huntington-bank-announces-treasury-management-connectivity-ecosystem-to-empower-businesses-with-more-sophisticated-personalized-financial-intelligence-302593271.html
- date: '2026-05-25'
  title: BANK INVESTMENT AIMS TO IMPROVE REVENUE ...
  url: https://ir.huntington.com/news-presentations/press-releases/detail/854/bank-investment-aims-to-improve-revenue-cycle-for-healthcare-industry
- date: '2026-05-25'
  title: Veuu Announces Partnership with Huntington Bancshares ...
  url: https://www.nasdaq.com/press-release/veuu-announces-partnership-with-huntington-bancshares-inc.-to-enhance-health-care
- date: '2026-05-25'
  title: Huntington Launches Huntington Heads Up® with AI to ...
  url: https://www.prnewswire.com/news-releases/huntington-launches-huntington-heads-up-with-ai-to-improve-customers-digital-banking-experience-300794687.html
random_paper: 13
rate_limits:
- limit_count: 2
  name: Huntington Bancshares Rate Limits
  slug: huntington-bancshares-rate-limits
scopes:
- name: Huntington Bancshares Scopes
  scope_count: 3
  slug: huntington-bancshares-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 33.2
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 41.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/huntington-bancshares/refs/heads/main/screenshots/huntington-bancshares-2026-06-20T182949.png
security:
- kind: authentication
  name: Huntington Bancshares Authentication
  slug: huntington-bancshares-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Huntington Bancshares Domain Security
  slug: huntington-bancshares-domain-security
  summary_line: TLSv1.3 · DMARC
slug: huntington-bancshares
tags:
- Banking
- ERP Integration
- Open Banking
- Payments
- Treasury
- Fortune 1000
website: https://www.huntington.com/
---
