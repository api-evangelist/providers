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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Decentro Agentic Access
  operation_count: 22
  slug: decentro-agentic-access
  summary_line: 22 operations · 16 acting
api_count: 2
apis:
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: Identity verification, customer onboarding, DigiLocker integration, Aadhaar OTP, document classification, and face match.
  name: Decentro KYC & Onboarding API
  slug: kyc-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: Create and manage virtual bank accounts, balances, statements, and remitter whitelisting for collections and reconciliation.
  name: Decentro Virtual Accounts API
  slug: virtual-accounts-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Accounts API from Decentro — 2 operation(s) for accounts.
  name: Decentro Accounts API
  slug: decentro-accounts-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Forensics API from Decentro — 2 operation(s) for forensics.
  name: Decentro Forensics API
  slug: decentro-forensics-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Journals API from Decentro — 1 operation(s) for journals.
  name: Decentro Journals API
  slug: decentro-journals-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Transactions API from Decentro — 1 operation(s) for transactions.
  name: Decentro Transactions API
  slug: decentro-transactions-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Verification API from Decentro — 1 operation(s) for verification.
  name: Decentro Verification API
  slug: decentro-verification-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Auth API from Decentro — 1 operation(s) for auth.
  name: Decentro Auth API
  slug: decentro-auth-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Banking API from Decentro — 11 operation(s) for banking.
  name: Decentro Banking API
  slug: decentro-banking-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Decentro API from Decentro — 2 operation(s) for decentro.
  name: Decentro Decentro API
  slug: decentro-decentro-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Deposit Simulation API from Decentro — 1 operation(s) for deposit simulation.
  name: Decentro Deposit Simulation API
  slug: decentro-deposit-simulation-api
- baseURL: https://in.decentro.tech
  baseurl_source: declared
  description: The Payments API from Decentro — 29 operation(s) for payments.
  name: Decentro Payments API
  slug: decentro-payments-api
artifact_total: 36
collections:
- collection_type: open
  name: Decentro KYC & Onboarding Accounts API
  slug: open-decentro-accounts-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Collections API
  slug: open-decentro-collections-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Forensics API
  slug: open-decentro-forensics-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Journals API
  slug: open-decentro-journals-api
- collection_type: open
  name: Decentro & Onboarding Accounts KYC API
  slug: open-decentro-kyc-api
- collection_type: open
  name: Decentro Ledger API
  slug: open-decentro-ledger-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Mandates API
  slug: open-decentro-mandates-api
- collection_type: open
  name: Decentro Payments API
  slug: open-decentro-payments-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Payouts API
  slug: open-decentro-payouts-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Settlements API
  slug: open-decentro-settlements-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Transactions API
  slug: open-decentro-transactions-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Verification API
  slug: open-decentro-verification-api
- collection_type: open
  name: Decentro KYC & Onboarding Accounts Virtual Accounts API
  slug: open-decentro-virtual-accounts-api
common:
- group: commercial
  href: https://artifacts.apis.io/decentro/plans/decentro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/decentro-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/decentro/rate-limits/decentro-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/decentro-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/decentro/finops/decentro-finops.yml
  title: ''
  type: FinOps
  url: finops/decentro-finops.yml
- group: other
  href: https://artifacts.apis.io/decentro/capabilities/decentro-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/decentro-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/decentro/agentic-access/decentro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/decentro-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/decentro/security/decentro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decentro-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/decentro/authentication/decentro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/decentro-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decentro-in
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/decentro
- group: company
  title: ''
  type: Website
  url: https://decentro.tech/
- group: start
  title: ''
  type: Portal
  url: https://docs.decentro.tech/
- group: docs
  title: ''
  type: Reference
  url: https://docs.decentro.tech/reference
- group: company
  title: ''
  type: Blog
  url: https://decentro.tech/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://decentro.tech/pricing/
- group: design
  href: https://artifacts.apis.io/decentro/json-ld/decentro-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/decentro-context.jsonld
- group: design
  href: https://artifacts.apis.io/decentro/vocabulary/decentro-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/decentro-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.decentro.tech/llms.txt
created: '2025-02-24'
description: 'Decentro is a banking-as-a-service platform that provides businesses with seamless integration to Indian banking infrastructure - including payments (UPI, IMPS, NEFT, RTGS), virtual accounts, KYC, ledger primitives, and credit-bureau data. Decentro publishes a developer portal and Postman collection covering six API categories: KYC & Onboarding, Bytes (alternate data), Scanner (forensics), Payments, Virtual Accounts, and Ledger.'
finops:
- has_sources: true
  method: generated
  name: Decentro Finops
  primary_unit: request
  service_category: Banking-as-a-Service
  slug: decentro-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/decentro.png
json_schemas:
- name: Decentro Payout
  property_count: 10
  slug: decentro-payout
- name: Decentro Virtual Account
  property_count: 8
  slug: decentro-virtual-account
jsonld:
- class_count: 4
  name: Decentro Context
  property_count: 8
  slug: decentro-context
layout: provider
modified: '2026-05-19'
name: Decentro
nav: Providers
network: true
overview: 'Decentro publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including KYC & Onboarding API, Virtual Accounts API, Accounts API, and 9 more. Tagged areas include Banking, Banking as a Service, Fintech, India, and KYC.


  The Decentro catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Decentro''s developer surface includes authentication, developer portal, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Decentro Plans Pricing
  plan_count: 2
  slug: decentro-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Decentro Rate Limits
  slug: decentro-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Decentro — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: decentro-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Decentro — payments api rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: decentro-payments-api-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.4
    catalog_earned_first_party: 0.0
    catalog_gap: 51.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 13.2
    contract_governance: 27.3
    contract_quality: 54.0
    developer_ergonomics: 40.5
    discoverability: 73.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 29.4
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/decentro/decentro-2026-06-20T175753.png
security:
- kind: authentication
  name: Decentro Authentication
  slug: decentro-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Decentro Domain Security
  slug: decentro-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: decentro
tags:
- Banking
- Banking as a Service
- Fintech
- India
- KYC
- Ledger
- Payments
- UPI
- Virtual Accounts
website: https://decentro.tech/
---
