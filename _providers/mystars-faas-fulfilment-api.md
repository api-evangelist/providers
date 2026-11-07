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
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.mystars.tg
  baseurl_source: declared
  description: The MyStars FaaS — Fulfilment API API from MyStars FaaS — Fulfilment API — 0 operation(s) for mystars faas — fulfilment api.
  name: MyStars FaaS — Fulfilment API MyStars FaaS — Fulfilment API
  slug: mystars-faas-fulfilment-api-mystars-faas-fulfilment-api-api
- baseURL: https://api.mystars.tg
  baseurl_source: declared
  description: Create, inspect, list and cancel fulfilment orders.
  name: MyStars FaaS — Fulfilment API Orders API
  slug: mystars-faas-fulfilment-api-orders-api
- baseURL: https://api.mystars.tg
  baseurl_source: declared
  description: Quote a price; list supported payment currencies and products.
  name: MyStars FaaS — Fulfilment API Pricing API
  slug: mystars-faas-fulfilment-api-pricing-api
- baseURL: https://api.mystars.tg
  baseurl_source: declared
  description: Resolve a recipient and check delivery eligibility before ordering.
  name: MyStars FaaS — Fulfilment API Recipients API
  slug: mystars-faas-fulfilment-api-recipients-api
artifact_total: 15
asyncapis:
- description: ''
  name: Mystars Faas Fulfilment Api Webhooks
  slug: mystars-faas-fulfilment-api-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://mystars.tg
- group: auth
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/security/mystars-faas-fulfilment-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mystars-faas-fulfilment-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/security/mystars-faas-fulfilment-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mystars-faas-fulfilment-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/authentication/mystars-faas-fulfilment-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mystars-faas-fulfilment-api-authentication.yml
- group: build
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/packages/mystars-faas-fulfilment-api-packages.yml
  title: ''
  type: Packages
  url: packages/mystars-faas-fulfilment-api-packages.yml
- group: build
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/packages/mystars-faas-fulfilment-api-packages.yml
  title: ''
  type: SDKs
  url: packages/mystars-faas-fulfilment-api-packages.yml
- group: agent
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/well-known/mystars-faas-fulfilment-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mystars-faas-fulfilment-api-well-known.yml
- group: auth
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/well-known/mystars-faas-fulfilment-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mystars-faas-fulfilment-api-security.txt
- group: auth
  title: ''
  type: Security
  url: https://mystars.tg/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/errors/mystars-faas-fulfilment-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mystars-faas-fulfilment-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/conventions/mystars-faas-fulfilment-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mystars-faas-fulfilment-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/conventions/mystars-faas-fulfilment-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mystars-faas-fulfilment-api-conventions.yml
- group: operate
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/rate-limits/mystars-faas-fulfilment-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mystars-faas-fulfilment-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/plans/mystars-faas-fulfilment-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mystars-faas-fulfilment-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/changelog/mystars-faas-fulfilment-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mystars-faas-fulfilment-api-changelog.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/lifecycle/mystars-faas-fulfilment-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mystars-faas-fulfilment-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/conformance/mystars-faas-fulfilment-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mystars-faas-fulfilment-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/data-model/mystars-faas-fulfilment-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mystars-faas-fulfilment-api-data-model.yml
- group: design
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/asyncapi/mystars-faas-fulfilment-api-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mystars-faas-fulfilment-api-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/mystars-faas-fulfilment-api/overlays/mystars-faas-fulfilment-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mystars-faas-fulfilment-api-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mystars.tg/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mystars.tg/docs
- group: operate
  title: ''
  type: Support
  url: https://t.me/Mystars_support_bot
- group: company
  title: ''
  type: Blog
  url: https://mystars.tg/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mystars.tg/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mystars.tg/privacy
- group: start
  title: ''
  type: SignUp
  url: https://t.me/my_stars_tg_bot
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mystars-tg
created: '2026-07-12'
description: A B2B Fragment-as-a-Service (FaaS) fulfilment REST API for programmatically buying and reselling Telegram Stars and Telegram Premium, delivered to any Telegram @username, paid on-chain in TON (GRAM) or USDT (TON). Non-custodial, no KYC. Offers versioned /v1 endpoints for pricing, recipient checks, product catalog, and order lifecycle, with signed webhooks and official TypeScript and Python SDKs.
finops:
- has_sources: true
  method: derived
  name: Mystars Faas Fulfilment Api Finops
  primary_unit: ''
  service_category: ''
  slug: mystars-faas-fulfilment-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mystars-faas-fulfilment-api.png
layout: provider
modified: '2026-09-03'
name: MyStars FaaS — Fulfilment API
nav: Providers
network: true
overview: 'MyStars FaaS — Fulfilment API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including MyStars FaaS — Fulfilment API, Orders API, Pricing API, and 1 more. Tagged areas include Telegram, telegram-stars, telegram-premium, Payments, and Cryptocurrency.


  The MyStars FaaS — Fulfilment API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MyStars FaaS — Fulfilment API''s developer surface includes authentication, changelog, API reference, support, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Mystars Faas Fulfilment Api Plans Pricing
  plan_count: 0
  slug: mystars-faas-fulfilment-api-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Mystars Faas Fulfilment Api Rate Limits
  slug: mystars-faas-fulfilment-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: MyStars FaaS — Fulfilment API API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: mystars-faas-fulfilment-api-rules
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 65.3
    developer_ergonomics: 54.2
    discoverability: 73.2
    operational_transparency: 63.2
  previous_composite: 51.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mystars-faas-fulfilment-api/mystars-faas-fulfilment-api-2026-08-07T184543.png
security:
- kind: authentication
  name: Mystars Faas Fulfilment Api Authentication
  slug: mystars-faas-fulfilment-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mystars Faas Fulfilment Api Domain Security
  slug: mystars-faas-fulfilment-api-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Mystars Faas Fulfilment Api Vulnerability Disclosure
  slug: mystars-faas-fulfilment-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Buy Telegram Stars or Premium for a username
  slug: mystars-faas-fulfilment-api-buy-stars-or-premium
- name: Manage and reverse MyStars orders
  slug: mystars-faas-fulfilment-api-order-lifecycle
- name: Receive and verify MyStars order-status webhooks
  slug: mystars-faas-fulfilment-api-verify-webhooks
slug: mystars-faas-fulfilment-api
tags:
- Telegram
- telegram-stars
- telegram-premium
- Payments
- Cryptocurrency
- TON
- gram
- USDT
- Fintech
- Fulfilment
- Digital Goods
- Non-Custodial
- no-kyc
website: https://mystars.tg
---
