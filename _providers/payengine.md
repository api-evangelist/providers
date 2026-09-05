---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for merchant onboarding, card and ACH transaction processing (auth, sale, capture, void, refund, offline and device sale), card and bank-account tokenization, gateway orchestration, hosted pa
  name: PayEngine Platform API
  slug: payengine-platform-api
artifact_total: 7
asyncapis:
- description: ''
  name: Payengine Webhooks
  slug: payengine-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payengine-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payengine-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.payengine.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.payengine.co/developer-docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.payengine.co/developer-docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs-api.payengine.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.payengine.co/developer-docs/getting-started-1/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.payengine.co/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.payengine.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payengine
- group: commercial
  title: ''
  type: Pricing
  url: https://www.payengine.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.payengine.co/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payengine.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payengine.co/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.payengine.co/
- group: auth
  title: ''
  type: Security
  url: https://www.payengine.co/security
- group: auth
  title: ''
  type: Compliance
  url: conformance/payengine-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payengine-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/payengine-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/payengine-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payengine-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/payengine-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payengine-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payengine-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/payengine-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payengine-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payengine-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/payengine-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payengine-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/payengine-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/payengine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payengine-rate-limits.yml
created: '2026-08-26'
description: 'PayEngine is an embedded-payments and payment-facilitation platform for vertical market SaaS companies, operated by Platform Factory, Inc. It lets a software company offer payments to its own customers without building an acquiring stack: PayEngine handles merchant onboarding and underwriting, PCI-scoped card and bank-account capture through hosted SecureFields and a <pay-engine> web-component library, card and ACH processing with 3-D Secure, AVS and Level 2/Level 3 interchange data, network tokenization, Tap to Pay and cloud-connected terminals, hosted payment links, subscriptions, disputes, settlement and payouts. A gateway-orchestration layer routes across multiple processors. The platform is a PCI DSS Level 1 certified Service Provider, listed in Visa''s Global Registry under Platform Factory, Inc. Integration is REST plus a signed webhook surface of 37 documented events; the REST reference itself requires a partner login.'
image: https://cdn.prod.website-files.com/64cc25b62ffdab8b077809ed/64f2c783505aa955d658014b_payengine-opengrpah.jpg
layout: provider
modified: '2026-08-26'
name: PayEngine
nav: Providers
network: true
overview: 'PayEngine publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Embedded Payments, Payment Facilitation, Merchant Onboarding, and Payment Gateway.


  The PayEngine catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayEngine''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Payengine Plans Pricing
  plan_count: 0
  slug: payengine-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Payengine Rate Limits
  slug: payengine-rate-limits
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 48.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payengine/refs/heads/main/screenshots/payengine-2026-09-02T150922.png
security:
- kind: authentication
  name: Payengine Authentication
  slug: payengine-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Payengine Domain Security
  slug: payengine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payengine Vulnerability Disclosure
  slug: payengine-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: payengine
tags:
- Payments
- Embedded Payments
- Payment Facilitation
- Merchant Onboarding
- Payment Gateway
- Financial-Services
- ACH
- Tokenization
- Webhook
- Fintech
- Company
website: https://www.payengine.co/
---
