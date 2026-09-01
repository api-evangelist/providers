---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The MyStars FaaS — Fulfilment API API from MyStars FaaS — 0 operation(s) for mystars faas — fulfilment api.
  name: MyStars FaaS MyStars FaaS — Fulfilment API
  slug: mystars-mystars-faas-fulfilment-api-api
- description: Create, inspect, list and cancel fulfilment orders.
  name: MyStars FaaS Orders API
  slug: mystars-orders-api
- description: Quote a price; list supported payment currencies and products.
  name: MyStars FaaS Pricing API
  slug: mystars-pricing-api
- description: Resolve a recipient and check delivery eligibility before ordering.
  name: MyStars FaaS Recipients API
  slug: mystars-recipients-api
artifact_total: 10
asyncapis:
- description: ''
  name: Mystars Webhooks
  slug: mystars-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mystars-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mystars-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mystars-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/mystars-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mystars.tg/developers
- group: docs
  title: ''
  type: Documentation
  url: https://mystars.tg/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mystars.tg/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://mystars.tg/developers
- group: operate
  title: ''
  type: Support
  url: https://t.me/Mystars_support_bot
- group: company
  title: ''
  type: Blog
  url: https://mystars.tg/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MyStars-tg
- group: commercial
  title: ''
  type: Pricing
  url: https://mystars.tg/developers
- group: start
  title: ''
  type: SignUp
  url: https://t.me/my_stars_tg_bot
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mystars.tg/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mystars.tg/privacy
- group: build
  title: ''
  type: Packages
  url: packages/mystars-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mystars-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mystars-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mystars-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mystars-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mystars-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/mystars-faas-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/mystars-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mystars-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/mystars-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mystars-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mystars-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mystars-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mystars-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mystars-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mystars-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/mystars-examples.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mystars-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mystars-rate-limits.yml
created: '2026-07-12'
description: MyStars FaaS is a public B2B fulfilment API for buying and reselling Telegram Stars and Telegram Premium, delivered to any Telegram @username and settled on-chain in GRAM (ex TON) or USDT on the TON network. Integrators quote an all-in price, check that a recipient can receive the item, create an idempotent order, and pay the returned treasury address with the order id as the transfer memo; MyStars fulfils the delivery through Fragment and confirms it with an HMAC-signed webhook. The model is non-custodial and no-KYC — there is no prepaid balance and no card processor, and a flat 5% margin is already included in every quote. Official TypeScript and Python SDKs, plus a CLI, ship on npm and PyPI.
image: https://mystars.tg/icon.png
layout: provider
modified: '2026-08-27'
name: MyStars FaaS
nav: Providers
network: true
overview: 'MyStars FaaS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including MyStars FaaS — Fulfilment API, Orders API, Pricing API, and 1 more. Tagged areas include Telegram, telegram-stars, telegram-premium, Payments, and Crypto.


  The MyStars FaaS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MyStars FaaS''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 28 more developer resources.'
plans:
- name: Mystars Plans Pricing
  plan_count: 0
  slug: mystars-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Mystars Rate Limits
  slug: mystars-rate-limits
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 62.2
    developer_ergonomics: 78.6
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 62.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Mystars Authentication
  slug: mystars-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mystars Domain Security
  slug: mystars-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Mystars Vulnerability Disclosure
  slug: mystars-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mystars
tags:
- Telegram
- telegram-stars
- telegram-premium
- Payments
- Crypto
- TON
- fulfilment
- Blockchain
- Digital Goods
- reseller-api
website: https://mystars.tg/developers
---
