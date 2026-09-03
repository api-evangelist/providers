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
  scored_at: '2026-09-03'
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
  title: ''
  type: Packages
  url: packages/flash-express-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flash-express-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flash-express-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flash-express-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flash-express-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flash-express-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flash-express-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flash-express-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flash-express-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flash-express-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flash-express-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flash-express-rate-limits.yml
- group: agent
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
random_paper: 5
rate_limits:
- limit_count: 0
  name: Flash Express Rate Limits
  slug: flash-express-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 34.4
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Last Mile
- Couriers
- Cash on Delivery
- Thailand
- Southeast Asia
- Webhook
website: https://flashexpress.com/en/
---
