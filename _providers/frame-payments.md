---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: The Frame REST API for payments, payouts, accounts, KYC/identity, disputes, subscriptions, invoices, and usage-based billing. Bearer secret-key auth over HTTPS; page-based pagination; HMAC-SHA256 sign
  name: Frame API
  slug: frame-api
artifact_total: 8
asyncapis:
- description: ''
  name: Frame Payments Webhooks
  slug: frame-payments-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/frame-payments/plans/frame-payments-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frame-payments-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://framepayments.com/blog
- group: company
  title: ''
  type: Website
  url: https://framepayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.framepayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.framepayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.framepayments.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.framepayments.com/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.framepayments.com
- group: commercial
  title: ''
  type: Pricing
  url: https://framepayments.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.framepayments.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://framepayments.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://framepayments.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Frame-Payments
- group: agent
  href: https://artifacts.apis.io/frame-payments/llms/frame-payments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/frame-payments-llms.txt
- group: build
  href: https://artifacts.apis.io/frame-payments/packages/frame-payments-packages.yml
  title: ''
  type: Packages
  url: packages/frame-payments-packages.yml
- group: build
  href: https://artifacts.apis.io/frame-payments/packages/frame-payments-packages.yml
  title: ''
  type: SDKs
  url: packages/frame-payments-packages.yml
- group: build
  href: https://artifacts.apis.io/frame-payments/cli/frame-payments-cli.yml
  title: ''
  type: CLI
  url: cli/frame-payments-cli.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/components/frame-payments-components.yml
  title: ''
  type: Components
  url: components/frame-payments-components.yml
- group: auth
  href: https://artifacts.apis.io/frame-payments/authentication/frame-payments-authentication.yml
  title: ''
  type: Authentication
  url: authentication/frame-payments-authentication.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/conventions/frame-payments-conventions.yml
  title: ''
  type: Conventions
  url: conventions/frame-payments-conventions.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/conventions/frame-payments-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/frame-payments-conventions.yml
- group: start
  href: https://artifacts.apis.io/frame-payments/sandbox/frame-payments-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/frame-payments-sandbox.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/asyncapi/frame-payments-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/frame-payments-webhooks.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/errors/frame-payments-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/frame-payments-problem-types.yml
- group: build
  href: https://artifacts.apis.io/frame-payments/errors/frame-payments-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/frame-payments-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/lifecycle/frame-payments-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/frame-payments-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/frame-payments/conformance/frame-payments-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frame-payments-conformance.yml
- group: auth
  href: https://artifacts.apis.io/frame-payments/security/frame-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frame-payments-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/frame-payments/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Frame Payments is a payments and compliance platform ("operating system") for high-compliance and high-risk merchants across regulated verticals including travel, crypto, telemedicine, gaming, gambling, the creator economy, and AI businesses. The frameOS platform unifies payments, payouts, KYC/KYB, identity verification, fraud detection (Sonar), geocompliance, disputes, subscriptions, and usage-based billing behind one REST API at api.framepayments.com/v1. Frame ships backend SDKs (Node, PHP, Ruby), mobile SDKs (iOS, Android, React Native), the Frame.js browser SDK with embeddable elements, a sandbox-only CLI, and HMAC-signed webhooks. Backed by Techstars.
finops:
- has_sources: true
  method: derived
  name: Frame Payments Finops
  primary_unit: transaction
  service_category: ''
  slug: frame-payments-finops
  template: false
image: https://framerusercontent.com/images/ZuP5qavgwprrdI5GSuMK3zq6P0.jpg
layout: provider
modified: '2026-10-06'
name: Frame Payments
nav: Providers
network: true
overview: 'Frame Payments is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Financial Services, Fintech, and KYC.


  The Frame Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Frame Payments'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Frame Payments Plans Pricing
  plan_count: 8
  slug: frame-payments-plans-pricing
- name: Frame Payments Price Estimates
  plan_count: 0
  slug: frame-payments-price-estimates
random_paper: 9
score:
  band: strong
  composite: 56.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 85.7
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 48.6
  provenance:
    conformance: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/frame-payments/frame-payments-2026-07-25T215103.png
security:
- kind: authentication
  name: Frame Payments Authentication
  slug: frame-payments-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Frame Payments Domain Security
  slug: frame-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: frame-cli
  slug: frame-payments-frame-cli
slug: frame-payments
tags:
- Company
- Payments
- Financial Services
- Fintech
- KYC
- Compliance
- Fraud Prevention
- Billing
- Payouts
- Identity Verification
website: https://framepayments.com/
---
