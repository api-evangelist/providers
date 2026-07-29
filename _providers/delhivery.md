---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Last-mile express parcel API covering pincode serviceability, bulk and single waybill generation, order creation/manifestation, shipment tracking, order edit and cancel, shipping-charge invoicing, pac
  name: Delhivery Express Last-Mile API
  slug: delhivery-express-last-mile-api
- description: 'Self-service B2C shipping APIs exposed through the Delhivery One developer portal: pincode serviceability, fetch waybill, client warehouse creation/updation, package shipment creation/updation, shipme'
  name: Delhivery One B2C Shipping API
  slug: delhivery-one-b2c-shipping-api
- description: OS1 is Delhivery's operating-system platform for logistics; its API reference documents REST endpoints across the OS1 sandbox and production environments for building on the underlying logistics infra
  name: Delhivery OS1 Platform API
  slug: delhivery-os1-platform-api
artifact_total: 6
asyncapis:
- description: ''
  name: Delhivery Tracking Webhooks
  slug: delhivery-tracking-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.delhivery.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://one.delhivery.com/developer-portal/documents
- group: docs
  title: ''
  type: Documentation
  url: https://delhivery-express-api-doc.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://delhivery-express-api-doc.readme.io/reference/introduction-1
- group: start
  title: ''
  type: GettingStarted
  url: https://delhivery-express-api-doc.readme.io/reference/getting-started-with-your-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.delhivery.com/docs/client-developer-portal-1
- group: operate
  title: ''
  type: Support
  url: https://delhivery-express-api-doc.readme.io/reference/escalation-matrix
- group: company
  title: ''
  type: Blog
  url: https://www.delhivery.com/blog-2/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.delhivery.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://one.delhivery.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.delhivery.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.delhivery.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/delhivery
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/delhivery-tracking-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/delhivery-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/delhivery-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/delhivery-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/delhivery-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/delhivery-domain-security.yml
created: '2026-07-17'
description: Delhivery is India's largest integrated third-party logistics (3PL) service provider, offering express parcel delivery, part-truckload and full-truckload freight, warehousing, supply-chain services, cross-border logistics and shipment tracking. Its developer platform exposes REST APIs for pincode serviceability, waybill generation, order creation and manifestation, shipment tracking (pull and webhook push), shipping-cost invoicing, packing-slip and shipping-label generation, pickup requests, client-warehouse management and NDR (non-delivery report) actions. APIs are consumed with a client API token and are documented across the Delhivery One developer portal, the Express Last-Mile API reference (ReadMe) and the OS1 platform docs.
image: https://www.delhivery.com/banner/homepage.webp
layout: provider
modified: '2026-07-18'
name: Delhivery
nav: Providers
network: true
overview: 'Delhivery publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Supply Chain, and Freight.


  The Delhivery catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Delhivery''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 43.3
  delta: 6.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 36.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/delhivery/refs/heads/main/screenshots/delhivery-2026-07-25T211645.png
security:
- kind: authentication
  name: Delhivery Authentication
  slug: delhivery-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Delhivery Domain Security
  slug: delhivery-domain-security
  summary_line: TLSv1.3 · DMARC
slug: delhivery
tags:
- Company
- Logistics
- Shipping
- Supply Chain
- Freight
- Ecommerce
- Tracking
- Fulfillment
- India
website: https://www.delhivery.com
---
