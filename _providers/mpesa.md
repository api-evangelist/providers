---
access_model:
  confidence: high
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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Mpesa Agentic Access
  operation_count: 14
  slug: mpesa-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 1
apis:
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Account Balance API from M-Pesa (Safaricom Daraja) — 1 operation(s) for account balance.
  name: M-Pesa (Safaricom Daraja) Account Balance API
  slug: mpesa-account-balance-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Authorization API from M-Pesa (Safaricom Daraja) — 1 operation(s) for authorization.
  name: M-Pesa (Safaricom Daraja) Authorization API
  slug: mpesa-authorization-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The B2C API from M-Pesa (Safaricom Daraja) — 1 operation(s) for b2c.
  name: M-Pesa (Safaricom Daraja) B2C API
  slug: mpesa-b2c-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The C2B API from M-Pesa (Safaricom Daraja) — 2 operation(s) for c2b.
  name: M-Pesa (Safaricom Daraja) C2B API
  slug: mpesa-c2b-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Dynamic QR API from M-Pesa (Safaricom Daraja) — 1 operation(s) for dynamic qr.
  name: M-Pesa (Safaricom Daraja) Dynamic QR API
  slug: mpesa-dynamic-qr-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The M-Pesa Express API from M-Pesa (Safaricom Daraja) — 2 operation(s) for m-pesa express.
  name: M-Pesa (Safaricom Daraja) M-Pesa Express API
  slug: mpesa-m-pesa-express-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Reversal API from M-Pesa (Safaricom Daraja) — 1 operation(s) for reversal.
  name: M-Pesa (Safaricom Daraja) Reversal API
  slug: mpesa-reversal-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Standing Order API from M-Pesa (Safaricom Daraja) — 1 operation(s) for standing order.
  name: M-Pesa (Safaricom Daraja) Standing Order API
  slug: mpesa-standing-order-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Tax Remittance API from M-Pesa (Safaricom Daraja) — 1 operation(s) for tax remittance.
  name: M-Pesa (Safaricom Daraja) Tax Remittance API
  slug: mpesa-tax-remittance-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The Transaction Status API from M-Pesa (Safaricom Daraja) — 1 operation(s) for transaction status.
  name: M-Pesa (Safaricom Daraja) Transaction Status API
  slug: mpesa-transaction-status-api
- baseURL: https://api.safaricom.co.ke
  baseurl_source: declared
  description: The B2B API from M-Pesa (Safaricom Daraja) — 2 operation(s) for b2b.
  name: M-Pesa (Safaricom Daraja) B2B API
  slug: mpesa-b2-b-api
artifact_total: 47
asyncapis:
- description: The asynchronous callback (webhook) surface of the M-Pesa Daraja API. Daraja delivers the real outcome of collections and funds-movement operations by POSTing JSON to caller-hosted HTTPS endpoints. Th
  name: M-Pesa Daraja Callbacks
  slug: mpesa-callbacks-asyncapi
collections:
- collection_type: postman
  name: M-Pesa Daraja Account Balance API
  slug: postman-mpesa-account-balance-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Authorization API
  slug: postman-mpesa-authorization-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance B2B API
  slug: postman-mpesa-b2b-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance B2C API
  slug: postman-mpesa-b2c-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance C2B API
  slug: postman-mpesa-c2b-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Dynamic QR API
  slug: postman-mpesa-dynamic-qr-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance M-Pesa Express API
  slug: postman-mpesa-m-pesa-express-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Reversal API
  slug: postman-mpesa-reversal-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Standing Order API
  slug: postman-mpesa-standing-order-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Tax Remittance API
  slug: postman-mpesa-tax-remittance-api
- collection_type: postman
  name: M-Pesa Daraja Account Balance Transaction Status API
  slug: postman-mpesa-transaction-status-api
- collection_type: open
  name: M-Pesa Daraja Account Balance API
  slug: open-mpesa-account-balance-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Authorization API
  slug: open-mpesa-authorization-api
- collection_type: open
  name: M-Pesa Daraja Account Balance B2B API
  slug: open-mpesa-b2b-api
- collection_type: open
  name: M-Pesa Daraja Account Balance B2C API
  slug: open-mpesa-b2c-api
- collection_type: open
  name: M-Pesa Daraja Account Balance C2B API
  slug: open-mpesa-c2b-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Dynamic QR API
  slug: open-mpesa-dynamic-qr-api
- collection_type: open
  name: M-Pesa Daraja Account Balance M-Pesa Express API
  slug: open-mpesa-m-pesa-express-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Reversal API
  slug: open-mpesa-reversal-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Standing Order API
  slug: open-mpesa-standing-order-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Tax Remittance API
  slug: open-mpesa-tax-remittance-api
- collection_type: open
  name: M-Pesa Daraja Account Balance Transaction Status API
  slug: open-mpesa-transaction-status-api
common:
- group: other
  href: https://artifacts.apis.io/mpesa/capabilities/mpesa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mpesa-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/m-pesa-safaricom-daraja/overview
- group: agent
  href: https://artifacts.apis.io/mpesa/agentic-access/mpesa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mpesa-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/security/mpesa-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mpesa-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/security/mpesa-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mpesa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/security/mpesa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mpesa-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/authentication/mpesa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mpesa-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/safaricom
- group: company
  title: ''
  type: Website
  url: https://developer.safaricom.co.ke/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.safaricom.co.ke/APIs
- group: commercial
  href: https://artifacts.apis.io/mpesa/plans/mpesa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mpesa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mpesa/rate-limits/mpesa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mpesa-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mpesa/finops/mpesa-finops.yml
  title: ''
  type: FinOps
  url: finops/mpesa-finops.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/security/mpesa-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mpesa-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mpesa/security/mpesa-trust-center.yml
  title: ''
  type: Compliance
  url: security/mpesa-trust-center.yml
- group: design
  href: https://artifacts.apis.io/mpesa/conformance/mpesa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mpesa-conformance.yml
- group: build
  href: https://artifacts.apis.io/mpesa/packages/mpesa-packages.yml
  title: ''
  type: Packages
  url: packages/mpesa-packages.yml
- group: agent
  href: https://artifacts.apis.io/mpesa/mcp/mpesa-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mpesa-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mpesa/llms/mpesa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mpesa-llms.txt
- group: other
  href: https://artifacts.apis.io/mpesa/overlays/mpesa-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mpesa-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/mpesa/errors/mpesa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mpesa-problem-types.yml
- group: build
  href: https://artifacts.apis.io/mpesa/errors/mpesa-result-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/mpesa-result-codes.yml
- group: design
  href: https://artifacts.apis.io/mpesa/lifecycle/mpesa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mpesa-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mpesa/conventions/mpesa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mpesa-conventions.yml
- group: design
  href: https://artifacts.apis.io/mpesa/conventions/mpesa-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mpesa-conventions.yml
- group: start
  href: https://artifacts.apis.io/mpesa/sandbox/mpesa-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mpesa-sandbox.yml
- group: design
  href: https://artifacts.apis.io/mpesa/data-model/mpesa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mpesa-data-model.yml
- group: docs
  href: https://artifacts.apis.io/mpesa/asyncapi/mpesa-callbacks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/mpesa-callbacks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/mpesa/asyncapi/mpesa-callbacks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/mpesa-callbacks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/mpesa/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.safaricom.co.ke/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.safaricom.co.ke/APIs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.safaricom.co.ke/
- group: operate
  title: ''
  type: Support
  url: https://developer.safaricom.co.ke/faqs
- group: start
  title: ''
  type: SignUp
  url: https://developer.safaricom.co.ke/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.safaricom.co.ke/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.safaricom.co.ke/data-privacy-statements
- group: build
  href: https://artifacts.apis.io/mpesa/collections/mpesa.postman_collection.json
  title: ''
  type: Postman
  url: collections/mpesa.postman_collection.json
created: '2026-07-17'
description: M-Pesa is Safaricom's mobile-money platform for Kenya, exposed to developers through the Daraja API. The Daraja REST APIs let businesses collect payments (M-Pesa Express / STK Push, C2B), disburse funds (B2C, B2B), query transactions and balances, reverse payments, generate dynamic QR codes, and run standing orders — authorized with OAuth bearer tokens minted from Basic credentials, priced in Kenyan Shillings (KES).
finops:
- has_sources: true
  method: generated
  name: Mpesa Finops
  primary_unit: ''
  service_category: Payments and Financial Services
  slug: mpesa-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mpesa.png
layout: provider
modified: '2026-07-17'
name: M-Pesa (Safaricom Daraja)
nav: Providers
network: true
overview: 'M-Pesa (Safaricom Daraja) publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Balance API, Authorization API, B2C API, and 8 more. Tagged areas include Mobile Money, Payments, Fintech, Kenya, and Africa.


  The M-Pesa (Safaricom Daraja) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  M-Pesa (Safaricom Daraja)''s developer surface includes authentication, documentation, sandbox, API reference, getting-started guide, support, signup flow, and 31 more developer resources.'
plans:
- name: Mpesa Plans Pricing
  plan_count: 3
  slug: mpesa-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Mpesa Rate Limits
  slug: mpesa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: M-Pesa (Safaricom Daraja) API Rules
  rule_count: 59
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 1
  slug: mpesa-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 51.9
    developer_ergonomics: 48.2
    discoverability: 66.1
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - kenya
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mpesa/mpesa-2026-08-07T184414.png
security:
- kind: authentication
  name: Mpesa Authentication
  slug: mpesa-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Mpesa Domain Security
  slug: mpesa-domain-security
  summary_line: HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mpesa Vulnerability Disclosure
  slug: mpesa-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Mpesa Trust Center
  slug: mpesa-trust-center
  summary_line: PCI DSS v4, ISO/IEC 27001, ISO/IEC 27701, GDPR-aligned / Kenya Data Protection Act 2019
skill_count: 4
skills:
- name: Collect a payment with M-Pesa Express (STK Push)
  slug: mpesa-collect-stk-payment
- name: Disburse funds to a customer (B2C)
  slug: mpesa-disburse-b2c
- name: Register C2B callbacks and receive customer payments
  slug: mpesa-register-c2b-and-receive
- name: Check transaction status and reverse a payment
  slug: mpesa-status-and-reversal
slug: mpesa
tags:
- Mobile Money
- Payments
- Fintech
- Kenya
- Africa
- M-PESA
website: https://developer.safaricom.co.ke/
---
