---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 37
  human_in_the_loop: 0
  name: Chimoney Agentic Access
  operation_count: 57
  slug: chimoney-agentic-access
  summary_line: 57 operations · 37 acting
api_count: 1
apis:
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Retrieve transactions, public profiles, transfer between accounts, and issue wallet addresses.
  name: Chimoney Account API
  slug: chimoney-account-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: 'Reference lookups: supported banks, assets, exchange rates, currency conversion, and bank account verification.'
  name: Chimoney Info API
  slug: chimoney-info-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: The Interledger API from Chimoney — 5 operation(s) for interledger.
  name: Chimoney Interledger API
  slug: chimoney-interledger-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Create and manage multicurrency wallets and transfer between them.
  name: Chimoney MultiCurrency Wallets API
  slug: chimoney-multicurrency-wallets-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Initiate and verify inbound payment (collection) requests.
  name: Chimoney Payments API
  slug: chimoney-payments-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Send money to banks, mobile money, airtime, gift cards, Chimoney wallets, Interac, and Interledger wallet addresses.
  name: Chimoney Payouts API
  slug: chimoney-payouts-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Redeem issued Chimoney, airtime, gift cards, and mobile money.
  name: Chimoney Redeem API
  slug: chimoney-redeem-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: List, look up, and transfer between Chimoney wallets.
  name: Chimoney Wallet API
  slug: chimoney-wallet-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: AI Agent wallet management endpoints
  name: Chimoney Agents API
  slug: chimoney-agents-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: All AI Related Endpoints
  name: Chimoney AI API
  slug: chimoney-ai-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: Beneficiary management endpoints
  name: Chimoney Beneficiary API
  slug: chimoney-beneficiary-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: The Pass-through API from Chimoney — 5 operation(s) for pass-through.
  name: Chimoney Pass Through API
  slug: chimoney-pass-through-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: APort passport management endpoints
  name: Chimoney Passport API
  slug: chimoney-passport-api
- baseURL: https://api.chimoney.io/v0.2
  baseurl_source: declared
  description: All sub-account related endpoints.
  name: Chimoney Sub Account API
  slug: chimoney-sub-account-api
artifact_total: 31
collections:
- collection_type: open
  name: Chimoney Account API
  slug: open-chimoney-account-api
- collection_type: open
  name: Chimoney Account Info API
  slug: open-chimoney-info-api
- collection_type: open
  name: Chimoney Account Interledger API
  slug: open-chimoney-interledger-api
- collection_type: open
  name: Chimoney Account MultiCurrency Wallets API
  slug: open-chimoney-multicurrency-wallets-api
- collection_type: open
  name: Chimoney Account Payments API
  slug: open-chimoney-payments-api
- collection_type: open
  name: Chimoney Account Payouts API
  slug: open-chimoney-payouts-api
- collection_type: open
  name: Chimoney Account Redeem API
  slug: open-chimoney-redeem-api
- collection_type: open
  name: Chimoney Account SubAccount API
  slug: open-chimoney-subaccount-api
- collection_type: open
  name: Chimoney Account Wallet API
  slug: open-chimoney-wallet-api
- collection_type: open
  name: Chimoney API
  slug: open-chimoney
common:
- group: agent
  href: https://artifacts.apis.io/chimoney/agentic-access/chimoney-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chimoney-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/chimoney/security/chimoney-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chimoney-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/chimoney/authentication/chimoney-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chimoney-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chimoney
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chimoney
- group: company
  title: ''
  type: Website
  url: https://chimoney.io
- group: docs
  title: ''
  type: Documentation
  url: https://chimoney.readme.io
- group: commercial
  href: https://artifacts.apis.io/chimoney/plans/chimoney-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chimoney-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/chimoney/rate-limits/chimoney-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/chimoney-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/chimoney/finops/chimoney-finops.yml
  title: ''
  type: FinOps
  url: finops/chimoney-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://chimoney.io/blogs
created: '2026-07-12'
description: Chimoney is a developer-first global payouts and disbursement platform with deep coverage across Africa and 130+ countries. Its REST API sends money to bank accounts, mobile money wallets, airtime, gift cards, Chimoney wallets, and Interledger wallet addresses, and manages multicurrency wallets, sub-accounts, redemption, inbound payment collection, and reference lookups (supported banks, assets, exchange rates). Authentication is an API key passed in the X-API-KEY header, issued self-serve from the Chimoney developer dashboard, with a separate sandbox host for testing.
finops:
- has_sources: true
  method: generated
  name: Chimoney Finops
  primary_unit: ''
  service_category: Payments and Money Movement
  slug: chimoney-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chimoney.png
layout: provider
modified: '2026-07-12'
name: Chimoney
nav: Providers
network: true
overview: 'Chimoney publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Info API, Interledger API, and 11 more. Tagged areas include Payouts, Disbursements, Payments, Africa, and Global Payouts.


  The Chimoney catalog on APIs.io includes 1 Spectral governance ruleset.


  Chimoney''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Chimoney Plans Pricing
  plan_count: 3
  slug: chimoney-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Chimoney Rate Limits
  slug: chimoney-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Chimoney API Rules
  rule_count: 57
  severity_counts:
    error: 40
    hint: 0
    info: 5
    warn: 12
  slug: chimoney-rules
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 58.3
      total: 24
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/chimoney/chimoney-2026-07-25T205233.png
security:
- kind: authentication
  name: Chimoney Authentication
  slug: chimoney-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Chimoney Domain Security
  slug: chimoney-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chimoney
tags:
- Payouts
- Disbursements
- Payments
- Africa
- Global Payouts
- Wallets
- Multi-Currency
- Gift Cards
- Mobile Money
- Fintech
website: https://chimoney.io
---
