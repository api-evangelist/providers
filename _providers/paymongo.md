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
  - security
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 2
  name: Paymongo Agentic Access
  operation_count: 28
  slug: paymongo-agentic-access
  summary_line: 28 operations · 15 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Checkout Sessions API from PayMongo — 3 operation(s) for checkout sessions.
  name: PayMongo Checkout Sessions API
  slug: paymongo-checkout-sessions-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Customers API from PayMongo — 2 operation(s) for customers.
  name: PayMongo Customers API
  slug: paymongo-customers-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Payment Intents API from PayMongo — 3 operation(s) for payment intents.
  name: PayMongo Payment Intents API
  slug: paymongo-payment-intents-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Payment Links API from PayMongo — 2 operation(s) for payment links.
  name: PayMongo Payment Links API
  slug: paymongo-payment-links-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Payment Methods API from PayMongo — 2 operation(s) for payment methods.
  name: PayMongo Payment Methods API
  slug: paymongo-payment-methods-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Payments API from PayMongo — 2 operation(s) for payments.
  name: PayMongo Payments API
  slug: paymongo-payments-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The QR Ph API from PayMongo — 1 operation(s) for qr ph.
  name: PayMongo QR Ph API
  slug: paymongo-qr-ph-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Refunds API from PayMongo — 2 operation(s) for refunds.
  name: PayMongo Refunds API
  slug: paymongo-refunds-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Sources API from PayMongo — 2 operation(s) for sources.
  name: PayMongo Sources API
  slug: paymongo-sources-api
- baseURL: https://api.paymongo.com/v1
  baseurl_source: declared
  description: The Webhooks API from PayMongo — 4 operation(s) for webhooks.
  name: PayMongo Webhooks API
  slug: paymongo-webhooks-api
artifact_total: 40
asyncapis:
- description: ''
  name: Paymongo Webhooks
  slug: paymongo-webhooks
collections:
- collection_type: postman
  name: PayMongo Checkout Sessions API
  slug: postman-paymongo-checkout-sessions-api
- collection_type: postman
  name: PayMongo Checkout Sessions Customers API
  slug: postman-paymongo-customers-api
- collection_type: postman
  name: PayMongo Checkout Sessions Payment Intents API
  slug: postman-paymongo-payment-intents-api
- collection_type: postman
  name: PayMongo Checkout Sessions Payment Links API
  slug: postman-paymongo-payment-links-api
- collection_type: postman
  name: PayMongo Checkout Sessions Payment Methods API
  slug: postman-paymongo-payment-methods-api
- collection_type: postman
  name: PayMongo Checkout Sessions Payments API
  slug: postman-paymongo-payments-api
- collection_type: postman
  name: PayMongo Checkout Sessions QR Ph API
  slug: postman-paymongo-qr-ph-api
- collection_type: postman
  name: PayMongo Checkout Sessions Refunds API
  slug: postman-paymongo-refunds-api
- collection_type: postman
  name: PayMongo Checkout Sessions Sources API
  slug: postman-paymongo-sources-api
- collection_type: postman
  name: PayMongo Checkout Sessions Webhooks API
  slug: postman-paymongo-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PayMongo Checkout Sessions API
  slug: open-paymongo-checkout-sessions-api
- collection_type: open
  name: PayMongo Checkout Sessions Customers API
  slug: open-paymongo-customers-api
- collection_type: open
  name: PayMongo Checkout Sessions Payment Intents API
  slug: open-paymongo-payment-intents-api
- collection_type: open
  name: PayMongo Checkout Sessions Payment Links API
  slug: open-paymongo-payment-links-api
- collection_type: open
  name: PayMongo Checkout Sessions Payment Methods API
  slug: open-paymongo-payment-methods-api
- collection_type: open
  name: PayMongo Checkout Sessions Payments API
  slug: open-paymongo-payments-api
- collection_type: open
  name: PayMongo Checkout Sessions QR Ph API
  slug: open-paymongo-qr-ph-api
- collection_type: open
  name: PayMongo Checkout Sessions Refunds API
  slug: open-paymongo-refunds-api
- collection_type: open
  name: PayMongo Checkout Sessions Sources API
  slug: open-paymongo-sources-api
- collection_type: open
  name: PayMongo Checkout Sessions Webhooks API
  slug: open-paymongo-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paymongo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paymongo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/paymongo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/paymongo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paymongo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paymongo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paymongo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paymongo
- group: company
  title: ''
  type: Website
  url: https://www.paymongo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paymongo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/paymongo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paymongo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/paymongo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.paymongo.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paymongo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paymongo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paymongo.com/docs/payment-acceptance-quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paymongo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.paymongo.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.paymongo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paymongo.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paymongo.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paymongo.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.paymongo.com/docs/older-workflows
- group: auth
  title: ''
  type: Security
  url: https://docs.paymongo.com/docs/keeping-payments-secure
- group: auth
  title: ''
  type: Compliance
  url: https://www.paymongo.com/secure
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paymongo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/paymongo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paymongo-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paymongo-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/paymongo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/paymongo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/paymongo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/paymongo-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/paymongo-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paymongo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/paymongo-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/paymongo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/paymongo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/paymongo-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paymongo-changelog.yml
created: '2026-07-17'
description: PayMongo is a Philippine payments platform that lets businesses accept online payments via cards, GCash, Maya (PayMaya), GrabPay, ShopeePay, QR Ph, BillEase buy-now-pay-later, and direct online banking. Its REST API is built around the Payment Intent / Payment Method workflow with hosted Checkout Sessions, Payment Links, Customers, Refunds, Subscriptions, and signed Webhooks. Amounts are integers in centavos and PHP is the settlement currency; PayMongo is a PCI DSS Level 1 Service Provider.
finops:
- name: Paymongo Finops
  service_category: Financial Services
  slug: paymongo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/paymongo.png
layout: provider
modified: '2026-07-17'
name: PayMongo
nav: Providers
network: true
overview: 'PayMongo publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Checkout Sessions API, Customers API, Payment Intents API, and 7 more. Tagged areas include Payments, Fintech, Philippines, Southeast Asia, and GCash.


  The PayMongo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayMongo''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Paymongo Plans Pricing
  plan_count: 4
  slug: paymongo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Paymongo Rate Limits
  slug: paymongo-rate-limits
score:
  band: exemplar
  composite: 71.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 60.1
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 64.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 78.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paymongo/refs/heads/main/screenshots/paymongo-2026-08-07T191645.png
security:
- kind: authentication
  name: Paymongo Authentication
  slug: paymongo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Paymongo Domain Security
  slug: paymongo-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: Paymongo Vulnerability Disclosure
  slug: paymongo-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Paymongo Trust Center
  slug: paymongo-trust-center
  summary_line: PCI DSS Level 1 Service Provider
slug: paymongo
tags:
- Payments
- Fintech
- Philippines
- Southeast Asia
- GCash
- E-Wallet
- Card Payments
website: https://www.paymongo.com/
---
