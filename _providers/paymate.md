---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Legacy India API (PMXClients service). Twelve JSON-over-POST methods let a business add vendors and customers as contacts, book and approve vendor payments, raise collection requests, generate hosted '
  name: PayMate India Business Payments API
  slug: paymate-india-business-payments-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Business (KYB) onboarding, maintenance, charges and collection account setup
  name: PayMate Businesses API
  slug: paymate-businesses-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Commercial credit card enrolment and management
  name: PayMate Cards API
  slug: paymate-cards-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Payment collection requests, status and reporting
  name: PayMate Collections API
  slug: paymate-collections-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Buyer / supplier contact onboarding and maintenance
  name: PayMate Contacts API
  slug: paymate-contacts-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Vendor payment initiation, status and reporting
  name: PayMate Payments API
  slug: paymate-payments-api
- baseURL: https://api.paymate.my
  baseurl_source: declared
  description: Reference data
  name: PayMate Reference API
  slug: paymate-reference-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/paymate/capabilities/paymate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/paymate-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/paymate/security/paymate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paymate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://paymate.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.paymate.my/GlobalPartnerAPI
- group: docs
  title: ''
  type: Documentation
  url: https://paymate.in/paymateapi/APIDoc.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.paymate.my/GlobalPartnerAPI
- group: operate
  title: ''
  type: Support
  url: https://paymate.in/contactus.html
- group: company
  title: ''
  type: Blog
  url: https://paymate.in/blog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://paymate.in/Pricing_terms.html
- group: start
  title: ''
  type: Login
  url: https://paymate.in/login.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paymate.in/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paymate.in/privacy.html
- group: auth
  href: https://artifacts.apis.io/paymate/authentication/paymate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paymate-authentication.yml
- group: design
  href: https://artifacts.apis.io/paymate/conventions/paymate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paymate-conventions.yml
- group: design
  href: https://artifacts.apis.io/paymate/conventions/paymate-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/paymate-conventions.yml
- group: design
  href: https://artifacts.apis.io/paymate/errors/paymate-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/paymate-error-codes.yml
- group: commercial
  href: https://artifacts.apis.io/paymate/plans/paymate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paymate-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/paymate/rate-limits/paymate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/paymate-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/paymate/conformance/paymate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paymate-conformance.yml
- group: auth
  href: https://artifacts.apis.io/paymate/conformance/paymate-conformance.yml
  title: ''
  type: Compliance
  url: conformance/paymate-conformance.yml
- group: design
  href: https://artifacts.apis.io/paymate/lifecycle/paymate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/paymate-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/paymate/sandbox/paymate-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/paymate-sandbox.yml
- group: design
  href: https://artifacts.apis.io/paymate/data-model/paymate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paymate-data-model.yml
- group: agent
  href: https://artifacts.apis.io/paymate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/paymate/llms/paymate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paymate-llms.txt
- group: other
  href: https://artifacts.apis.io/paymate/overlays/paymate-global-partner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paymate-global-partner-api-overlay.yaml
created: '2026-08-26'
description: 'PayMate India Limited is a Mumbai-headquartered B2B payments and supply-chain finance platform that digitizes, automates and streamlines business payables and receivables. Enterprises use PayMate to pay vendors, GST and utility bills on commercial credit cards, to raise and collect invoice payment requests, to run maker/checker approval workflows, and to access working-capital credit and invoice discounting. The platform runs in India as PayMate and across Singapore, Malaysia, the UAE, Oman, Sri Lanka, Saudi Arabia, Australia and South Africa — where the Australian and South African deployments carry the DuNoMo brand. Two distinct API surfaces are published: the legacy India PayMate API (PMXClients WCF/JSON service) and the current Global Partner API, a v1 REST surface for business (KYB) onboarding, contact onboarding, commercial-card management, vendor payments, collection requests and reporting.'
finops:
- has_sources: true
  method: derived
  name: Paymate Finops
  primary_unit: subscription
  service_category: ''
  slug: paymate-finops
  template: false
image: https://paymate.in/imgs/pngs/apple-touch-icon.png
layout: provider
modified: '2026-08-26'
name: PayMate
nav: Providers
network: true
overview: 'PayMate publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Businesses API, Cards API, Collections API, and 4 more. Tagged areas include Payments, B2B Payments, Accounts Payable, Accounts Receivable, and Supply Chain Finance.


  The PayMate catalog on APIs.io includes 1 Spectral governance ruleset.


  PayMate''s developer surface includes documentation, API reference, support, engineering blog, pricing, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Paymate Plans Pricing
  plan_count: 3
  slug: paymate-plans-pricing
- name: Paymate Price Estimates
  plan_count: 0
  slug: paymate-price-estimates
random_paper: 9
rate_limits:
- limit_count: 6
  name: Paymate Rate Limits
  slug: paymate-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: PayMate API Rules
  rule_count: 64
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 3
  slug: paymate-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 31.8
    contract_quality: 53.9
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 57.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/paymate/paymate-2026-09-02T150923.png
security:
- kind: authentication
  name: Paymate Authentication
  slug: paymate-authentication
  summary_line: apiKey · 0 schemes
- kind: domain-security
  name: Paymate Domain Security
  slug: paymate-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 3
skills:
- name: paymate-collect-from-a-customer
  slug: paymate-collect-from-a-customer
- name: paymate-onboard-a-business
  slug: paymate-onboard-a-business
- name: paymate-pay-a-vendor
  slug: paymate-pay-a-vendor
slug: paymate
tags:
- Payments
- B2B Payments
- Accounts Payable
- Accounts Receivable
- Supply Chain Finance
- Invoice Discounting
- Working Capital
- Commercial Cards
- Financial Services
- India
- Fintech
- Company
website: https://paymate.in/
---
