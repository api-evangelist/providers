---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Verification-as-a-Service. A single POST /v1/verifications call declares which verification modules to run — organization_identity, individual_identity, payment_method and payee_qualification (PQS) — '
  name: Verituity Verification API
  slug: verituity-verification-api
artifact_total: 7
asyncapis:
- description: ''
  name: Verituity Webhooks
  slug: verituity-webhooks
common:
- group: company
  title: ''
  type: Blog
  url: https://verituity.com/blog
- group: auth
  href: https://artifacts.apis.io/verituity/security/verituity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verituity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verituity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://verituity.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://verituity.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://verituity.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://verituity.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verituity.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verituity.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://verituity.com/developers
- group: start
  href: https://artifacts.apis.io/verituity/sandbox/verituity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/verituity-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/verituity/authentication/verituity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/verituity-authentication.yml
- group: design
  href: https://artifacts.apis.io/verituity/conventions/verituity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/verituity-conventions.yml
- group: design
  href: https://artifacts.apis.io/verituity/conventions/verituity-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/verituity-conventions.yml
- group: design
  href: https://artifacts.apis.io/verituity/errors/verituity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/verituity-problem-types.yml
- group: build
  href: https://artifacts.apis.io/verituity/errors/verituity-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/verituity-decline-codes.yml
- group: operate
  href: https://artifacts.apis.io/verituity/rate-limits/verituity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/verituity-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/verituity/plans/verituity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/verituity-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/verituity/examples/verituity-verification-examples.yml
  title: ''
  type: Examples
  url: examples/verituity-verification-examples.yml
- group: design
  href: https://artifacts.apis.io/verituity/data-model/verituity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/verituity-data-model.yml
- group: design
  href: https://artifacts.apis.io/verituity/conformance/verituity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/verituity-conformance.yml
- group: auth
  href: https://artifacts.apis.io/verituity/conformance/verituity-conformance.yml
  title: ''
  type: Compliance
  url: conformance/verituity-conformance.yml
- group: design
  href: https://artifacts.apis.io/verituity/lifecycle/verituity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/verituity-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/verituity/packages/verituity-packages.yml
  title: ''
  type: Packages
  url: packages/verituity-packages.yml
- group: agent
  href: https://artifacts.apis.io/verituity/llms/verituity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/verituity-llms.txt
created: '2026-09-02'
description: Verituity is a McLean, Virginia payment integrity platform that verifies the file, the payee, the account and the payment instruction at the moment of authorization, before money moves, across any payment rail. The platform is organized as six services — Connect (ingest any batch file or REST call and normalize it to ISO 20022), Detect (duplicate and out-of-pattern screening), Eligibility (payee qualification against OFAC, SAM and payer-private lists), Verify (identity and bank account ownership verification), Pay (rail optionality and orchestration across ACH, RTP, wire, push-to-card, virtual card, PayPal, Zelle, Venmo, check and cross-border) and Explain (evidence and lineage on every decision). Its developer-facing product is Verification-as-a-Service, a single POST /v1/verifications call that runs four verification modules and returns one normalized decision/tier/reason_code response regardless of which underlying data source answered.
finops:
- has_sources: true
  method: derived
  name: Verituity Finops
  primary_unit: inquiry
  service_category: ''
  slug: verituity-finops
  template: false
image: https://verituity.com/img/og-default.png
layout: provider
modified: '2026-10-06'
name: Verituity
nav: Providers
network: true
overview: 'Verituity is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payouts, Disbursements, Identity Verification, and Account Verification.


  The Verituity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Verituity''s developer surface includes engineering blog, documentation, API reference, getting-started guide, pricing, sandbox, authentication, and 18 more developer resources.'
plans:
- name: Verituity Plans Pricing
  plan_count: 4
  slug: verituity-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Verituity Rate Limits
  slug: verituity-rate-limits
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 45.3
    developer_ergonomics: 59.5
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 41.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 28.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verituity/verituity-2026-10-11T132903.png
security:
- kind: authentication
  name: Verituity Authentication
  slug: verituity-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Verituity Domain Security
  slug: verituity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verituity
tags:
- Payments
- Payouts
- Disbursements
- Identity Verification
- Account Verification
- Fraud Prevention
- Payment Integrity
- Banking
- Financial Services
- Public Sector
- ISO 20022
- Compliance
- Company
website: https://verituity.com/
---
