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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Pin Payments Agentic Access
  operation_count: 24
  slug: pin-payments-agentic-access
  summary_line: 24 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.pinpayments.com/1
  baseurl_source: declared
  description: Tokenize and retrieve stored card details.
  name: Pin Payments Cards API
  slug: pin-payments-cards-api
- baseURL: https://api.pinpayments.com/1
  baseurl_source: declared
  description: Create and manage charges against cards or customers.
  name: Pin Payments Charges API
  slug: pin-payments-charges-api
- baseURL: https://api.pinpayments.com/1
  baseurl_source: declared
  description: Store customer profiles with payment sources for repeat billing.
  name: Pin Payments Customers API
  slug: pin-payments-customers-api
- baseURL: https://api.pinpayments.com/1
  baseurl_source: declared
  description: Issue and inspect refunds against charges.
  name: Pin Payments Refunds API
  slug: pin-payments-refunds-api
artifact_total: 24
collections:
- collection_type: open
  name: Pin Payments Cards API
  slug: open-pin-payments-cards-api
- collection_type: open
  name: Pin Payments Cards Charges API
  slug: open-pin-payments-charges-api
- collection_type: open
  name: Pin Payments Cards Customers API
  slug: open-pin-payments-customers-api
- collection_type: open
  name: Pin Payments Cards Refunds API
  slug: open-pin-payments-refunds-api
common:
- group: auth
  href: https://artifacts.apis.io/pin-payments/well-known/pin-payments-pin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pin-payments-pin-security.txt
- group: auth
  href: https://artifacts.apis.io/pin-payments/well-known/pin-payments-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pin-payments-api-security.txt
- group: design
  href: https://artifacts.apis.io/pin-payments/rules/pin-payments-rules.yml
  title: ''
  type: Spectral
  url: rules/pin-payments-rules.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/json-ld/pin-payments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pin-payments-context.jsonld
- group: design
  href: https://artifacts.apis.io/pin-payments/vocabulary/pin-payments-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pin-payments-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pin-payments/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/data-model/pin-payments-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pin-payments-data-model.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/components/pin-payments-components.yml
  title: ''
  type: Components
  url: components/pin-payments-components.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/conventions/pin-payments-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pin-payments-conventions.yml
- group: start
  href: https://artifacts.apis.io/pin-payments/sandbox/pin-payments-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pin-payments-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/pin-payments/lifecycle/pin-payments-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/pin-payments-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/lifecycle/pin-payments-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pin-payments-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/pin-payments/errors/pin-payments-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/pin-payments-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/errors/pin-payments-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pin-payments-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pin-payments/conformance/pin-payments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pin-payments-conformance.yml
- group: other
  href: https://artifacts.apis.io/pin-payments/overlays/pin-payments-cards-errors-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pin-payments-cards-errors-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/pin-payments/well-known/pin-payments-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pin-payments-apis-security.txt
- group: agent
  href: https://artifacts.apis.io/pin-payments/well-known/pin-payments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pin-payments-well-known.yml
- group: other
  href: https://artifacts.apis.io/pin-payments/hosts/pin-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pin-payments-hosts.yml
- group: build
  href: https://artifacts.apis.io/pin-payments/integrations/pin-payments-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/pin-payments-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/pin-payments/vendors/pin-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pin-payments-vendors.yml
- group: build
  href: https://artifacts.apis.io/pin-payments/packages/pin-payments-packages.yml
  title: ''
  type: Packages
  url: packages/pin-payments-packages.yml
- group: commercial
  href: https://artifacts.apis.io/pin-payments/plans/pin-payments-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pin-payments-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/pin-payments/rate-limits/pin-payments-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pin-payments-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pin-payments/finops/pin-payments-finops.yml
  title: ''
  type: FinOps
  url: finops/pin-payments-finops.yml
- group: other
  href: https://artifacts.apis.io/pin-payments/capabilities/pin-payments-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pin-payments-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/pin-payments/agentic-access/pin-payments-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pin-payments-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/pin-payments/security/pin-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pin-payments-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/pin-payments/authentication/pin-payments-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pin-payments-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pinpayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pin-payments
- group: company
  title: ''
  type: Website
  url: https://pinpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pinpayments.com/developers/integration-guides
- group: docs
  title: ''
  type: APIReference
  url: https://pinpayments.com/developers/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pinpayments.com/developers/libraries
- group: build
  title: ''
  type: SDKs
  url: https://pinpayments.com/developers/libraries
- group: start
  title: ''
  type: GettingStarted
  url: https://pinpayments.com/support/getting-started
- group: operate
  title: ''
  type: Support
  url: https://pinpayments.com/support/contact
- group: operate
  title: ''
  type: FAQ
  url: https://pinpayments.com/support/faqs
- group: docs
  title: ''
  type: Guides
  url: https://pinpayments.com/support/guides
- group: operate
  title: ''
  type: StatusPage
  url: https://pin.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://pinpayments.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://pinpayments.com/news
- group: commercial
  title: ''
  type: Pricing
  url: https://pinpayments.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.pinpayments.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://dashboard.pinpayments.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pinpayments.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pinpayments.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://pinpayments.com/blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/pinpayments
created: '2025-02-17'
description: Pin Payments (Southern Payment Systems Pty Ltd t/a Pin Payments, ABN 46 154 451 582, Melbourne, Australia; a Fat Zebra company) is an online payment gateway for small businesses and platforms, offering ecommerce, recurring payments, payments for platforms, hosted payment pages and foreign-currency billing. The Pin Payments API enables developers to charge cards, manage customers, store payment sources, issue refunds, and run subscriptions through a RESTful JSON interface secured with HTTP Basic authentication.
finops:
- has_sources: false
  method: generated
  name: Pin Payments Finops
  primary_unit: request
  service_category: API
  slug: pin-payments-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pin-payments.png
json_schemas:
- name: CardCreate
  property_count: 12
  slug: pin-payments-card-create
- name: ChargeCreate
  property_count: 14
  slug: pin-payments-charge-create
- name: CustomerCreate
  property_count: 8
  slug: pin-payments-customer-create
jsonld:
- class_count: 3
  name: Pin Payments Context
  property_count: 31
  slug: pin-payments-context
layout: provider
modified: '2026-10-21'
name: Pin Payments
nav: Providers
network: true
overview: 'Pin Payments publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cards API, Charges API, Customers API, and 1 more. Tagged areas include Payments, Cards, Subscription, Refunds, and Payment Gateway.


  The Pin Payments catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pin Payments'' developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, FAQ, and 43 more developer resources.'
plans:
- name: Pin Payments Plans Pricing
  plan_count: 2
  slug: pin-payments-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Pin Payments Rate Limits
  slug: pin-payments-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Pin Payments API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: pin-payments-rules
score:
  band: developing
  composite: 53.8
  coverage:
    artifact_dirs: 35
    catalog_earned: 72.2
    catalog_earned_first_party: 16.0
    catalog_gap: 42.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 48.7
    contract_governance: 35.6
    contract_quality: 56.6
    developer_ergonomics: 60.1
    discoverability: 67.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/pin-payments/pin-payments-2026-06-20T191711.png
security:
- kind: authentication
  name: Pin Payments Authentication
  slug: pin-payments-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pin Payments Domain Security
  slug: pin-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: pin-payments-3d-secure-charge
  slug: pin-payments-3d-secure-charge
- name: pin-payments-authorise-and-capture
  slug: pin-payments-authorise-and-capture
- name: pin-payments-charge-a-stored-customer
  slug: pin-payments-charge-a-stored-customer
- name: pin-payments-refund-a-charge
  slug: pin-payments-refund-a-charge
- name: pin-payments-take-a-card-payment
  slug: pin-payments-take-a-card-payment
slug: pin-payments
tags:
- Payments
- Cards
- Subscription
- Refunds
- Payment Gateway
- Recurring Payments
- E-Commerce
- Australia
website: https://pinpayments.com/
---
