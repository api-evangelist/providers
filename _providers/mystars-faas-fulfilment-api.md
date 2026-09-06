---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST/HTTP API for pricing, recipient eligibility checks, product catalog, and Telegram Stars/Premium order lifecycle, with X-Api-Key auth and signed webhooks. OpenAPI contract and llms.txt are adverti
  name: MyStars FaaS Fulfilment API
  slug: mystars-faas-fulfilment-api
artifact_total: 7
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
  title: ''
  type: VulnerabilityDisclosure
  url: security/mystars-faas-fulfilment-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mystars-faas-fulfilment-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mystars-faas-fulfilment-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/mystars-faas-fulfilment-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mystars-faas-fulfilment-api-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mystars-faas-fulfilment-api-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mystars-faas-fulfilment-api-security.txt
- group: auth
  title: ''
  type: Security
  url: https://mystars.tg/.well-known/security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mystars-faas-fulfilment-api-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mystars-faas-fulfilment-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mystars-faas-fulfilment-api-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mystars-faas-fulfilment-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mystars-faas-fulfilment-api-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mystars-faas-fulfilment-api-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mystars-faas-fulfilment-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mystars-faas-fulfilment-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mystars-faas-fulfilment-api-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mystars-faas-fulfilment-api-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
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
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mystars-faas-fulfilment-api.png
layout: provider
modified: '2026-09-03'
name: MyStars FaaS — Fulfilment API
nav: Providers
network: true
overview: 'MyStars FaaS — Fulfilment API publishes 1 API on the [APIs.io](https://apis.io/) network: MyStars FaaS Fulfilment API. Tagged areas include Telegram, telegram-stars, telegram-premium, Payments, and Crypto.


  The MyStars FaaS — Fulfilment API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MyStars FaaS — Fulfilment API''s developer surface includes authentication, changelog, API reference, support, engineering blog, signup flow, and 23 more developer resources.'
plans:
- name: Mystars Faas Fulfilment Api Plans Pricing
  plan_count: 0
  slug: mystars-faas-fulfilment-api-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Mystars Faas Fulfilment Api Rate Limits
  slug: mystars-faas-fulfilment-api-rate-limits
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 49.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mystars-faas-fulfilment-api/refs/heads/main/screenshots/mystars-faas-fulfilment-api-2026-08-07T184543.png
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
slug: mystars-faas-fulfilment-api
tags:
- Telegram
- telegram-stars
- telegram-premium
- Payments
- Crypto
- TON
- gram
- USDT
- Fintech
- fulfilment
- Digital Goods
- Non-Custodial
- no-kyc
website: https://mystars.tg
---
