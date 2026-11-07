---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Mono Co Agentic Access
  operation_count: 30
  slug: mono-co-agentic-access
  summary_line: 30 operations · 9 acting
api_count: 6
apis:
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Account details and balance for a linked account.
  name: Mono Account Information API
  slug: mono-co-account-information-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Initiate Connect account linking and exchange a code for an account id.
  name: Mono Account Linking API
  slug: mono-co-account-linking-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Customers, mandates, balance inquiry, and recurring debits.
  name: Mono Direct Debit API
  slug: mono-co-direct-debit-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: One-time bank-to-bank payments.
  name: Mono DirectPay API
  slug: mono-co-directpay-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Identity verification and income signals for a linked account.
  name: Mono Identity and Income API
  slug: mono-co-identity-and-income-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Transactions and bank statements for a linked account.
  name: Mono Transactions and Statements API
  slug: mono-co-transactions-and-statements-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Affordability and credit-decisioning analysis.
  name: Mono Creditworthiness API
  slug: mono-co-creditworthiness-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Read financial data from a linked account.
  name: Mono Financial Data API
  slug: mono-co-financial-data-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Investment holdings for a linked account.
  name: Mono Investment API
  slug: mono-co-investment-api
- baseURL: https://api.withmono.com
  baseurl_source: declared
  description: Identity and data verification for KYC/KYB.
  name: Mono Lookup API
  slug: mono-co-lookup-api
artifact_total: 25
collections:
- collection_type: open
  name: Mono API
  slug: open-mono-africa
- collection_type: open
  name: Mono Account Information API
  slug: open-mono-co-account-information-api
- collection_type: open
  name: Mono Account Information Account Linking API
  slug: open-mono-co-account-linking-api
- collection_type: open
  name: Mono Account Information Direct Debit API
  slug: open-mono-co-direct-debit-api
- collection_type: open
  name: Mono Account Information DirectPay API
  slug: open-mono-co-directpay-api
- collection_type: open
  name: Mono Account Information Identity and Income API
  slug: open-mono-co-identity-and-income-api
- collection_type: open
  name: Mono Account Information Transactions and Statements API
  slug: open-mono-co-transactions-and-statements-api
- collection_type: open
  name: Mono API
  slug: open-mono-co
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://mono.co/pricing
- group: other
  href: https://artifacts.apis.io/mono-co/capabilities/mono-co-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mono-co-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mono-co/agentic-access/mono-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mono-co-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mono-co/security/mono-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mono-co-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mono-co/authentication/mono-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mono-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmono
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mono-hq
- group: company
  title: ''
  type: Website
  url: https://mono.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mono.co
- group: commercial
  href: https://artifacts.apis.io/mono-co/plans/mono-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mono-co-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mono-co/rate-limits/mono-co-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mono-co-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mono-co/finops/mono-co-finops.yml
  title: ''
  type: FinOps
  url: finops/mono-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mono.co/blog
created: '2026-06-21'
description: Mono is an African open-banking platform that lets businesses access bank and financial data and collect recurring payments through a single API. The Mono REST API at api.withmono.com covers account linking (Connect), transactions, statements, identity, income, and balance, plus DirectPay one-time payments and Direct Debit mandates, secured with a mono-sec-key header.
finops:
- has_sources: true
  method: generated
  name: Mono Co Finops
  primary_unit: ''
  service_category: Financial Services
  slug: mono-co-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mono-co.png
layout: provider
modified: '2026-06-21'
name: Mono
nav: Providers
network: true
overview: 'Mono publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Information API, Account Linking API, Direct Debit API, and 7 more. Tagged areas include Open Banking, Financial Data, Payments, Direct Debit, and Africa.


  The Mono catalog on APIs.io includes 1 Spectral governance ruleset.


  Mono''s developer surface includes pricing, authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Mono Co Plans Pricing
  plan_count: 7
  slug: mono-co-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Mono Co Rate Limits
  slug: mono-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Mono API Rules
  rule_count: 66
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 3
  slug: mono-co-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 38.3
    developer_ergonomics: 32.1
    discoverability: 71.4
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 40.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 9.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mono-co/mono-co-2026-08-07T184212.png
security:
- kind: authentication
  name: Mono Co Authentication
  slug: mono-co-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mono Co Domain Security
  slug: mono-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mono-co
tags:
- Open Banking
- Financial Data
- Payments
- Direct Debit
- Africa
website: https://mono.co
---
