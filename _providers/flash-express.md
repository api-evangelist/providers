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
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'The FlashExpress Open API is the merchant-facing integration surface for Flash Express parcel logistics in Thailand. All calls are HTTPS POST with an application/x-www-form-urlencoded body and a JSON '
  name: FlashExpress Open API
  slug: flash-express-open-api
artifact_total: 6
asyncapis:
- description: ''
  name: Flash Express Webhooks
  slug: flash-express-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/security/flash-express-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flash-express-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashexpress.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open-docs.flashexpress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-docs.flashexpress.com/
- group: docs
  title: ''
  type: APIReference
  url: https://open-docs.flashexpress.com/#api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://open-docs.flashexpress.com/#the-basic-standard
- group: operate
  title: ''
  type: Support
  url: https://flashexpress.com/fle/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://flashexpress.com/fle/faq
- group: company
  title: ''
  type: Blog
  url: https://flashexpress.com/fle/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://flashexpress.com/fle/check-price
- group: start
  title: ''
  type: SignUp
  url: https://flashexpress.com/fle/register
- group: start
  title: ''
  type: Login
  url: https://flashexpress.com/fle/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flashexpress.com/fle/our-service/service-agreement/company-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashexpress.com/fle/our-service/service-agreement/privacy-policy
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/packages/flash-express-packages.yml
  title: ''
  type: Packages
  url: packages/flash-express-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/packages/flash-express-packages.yml
  title: ''
  type: SDKs
  url: packages/flash-express-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/authentication/flash-express-authentication.yml
  title: ''
  type: Authentication
  url: authentication/flash-express-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/conventions/flash-express-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flash-express-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/errors/flash-express-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/flash-express-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/asyncapi/flash-express-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/flash-express-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/data-model/flash-express-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flash-express-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/sandbox/flash-express-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/flash-express-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/conformance/flash-express-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flash-express-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/lifecycle/flash-express-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/flash-express-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/plans/flash-express-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flash-express-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/rate-limits/flash-express-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flash-express-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/llms/flash-express-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flash-express-llms.txt
created: '2026-08-12'
description: Flash Express is a Bangkok-headquartered express parcel delivery and e-commerce logistics operator serving Thailand, with affiliated operations in the Philippines and Laos. It runs door-to-door pickup and last-mile delivery for B2B, B2C and C2C shippers, including next-day and weekend delivery, bulky and fruit shipping, cash-on-delivery collection with daily settlement, parcel insurance, and a nationwide network of branches and drop-off points. For merchants and platform integrators Flash Express publishes the FlashExpress Open API, an HTTPS/POST, form-urlencoded, SHA256-signed interface covering warehouse and sub-account management, order creation and modification, label printing, freight-rate estimation, parcel tracking, courier pickup scheduling, and a webhook service that pushes status, weight, price, courier and route events back to the merchant.
image: https://flashexpress.com/favicon.ico
layout: provider
modified: '2026-08-12'
name: Flash Express
nav: Providers
network: true
overview: 'Flash Express publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Delivery, and Parcel Tracking.


  The Flash Express catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flash Express'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Flash Express Plans Pricing
  plan_count: 0
  slug: flash-express-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Flash Express Rate Limits
  slug: flash-express-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 34.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/flash-express/refs/heads/main/screenshots/flash-express-2026-08-17T080933.png
security:
- kind: authentication
  name: Flash Express Authentication
  slug: flash-express-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Flash Express Domain Security
  slug: flash-express-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: flash-express
tags:
- Company
- Logistics
- Shipping
- Delivery
- Parcel Tracking
- E-Commerce
- Last Mile Delivery
- Couriers
- Cash on Delivery
- Thailand
- Southeast Asia
- Webhook
website: https://flashexpress.com/en/
---
