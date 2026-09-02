---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Track Pod Agentic Access
  operation_count: 73
  slug: track-pod-agentic-access
  summary_line: 73 operations · 44 acting
api_count: 1
apis:
- description: The Address API from Track-POD — 1 operation(s) for address.
  name: Track-POD Address API
  slug: track-pod-address-api
- description: The Driver API from Track-POD — 3 operation(s) for driver.
  name: Track-POD Driver API
  slug: track-pod-driver-api
- description: The Order API from Track-POD — 23 operation(s) for order.
  name: Track-POD Order API
  slug: track-pod-order-api
- description: The RejectReason API from Track-POD — 1 operation(s) for rejectreason.
  name: Track-POD RejectReason API
  slug: track-pod-rejectreason-api
- description: The Route API from Track-POD — 24 operation(s) for route.
  name: Track-POD Route API
  slug: track-pod-route-api
- description: The Test API from Track-POD — 1 operation(s) for test.
  name: Track-POD Test API
  slug: track-pod-test-api
- description: The Vehicle API from Track-POD — 2 operation(s) for vehicle.
  name: Track-POD Vehicle API
  slug: track-pod-vehicle-api
- description: The VehicleCheck API from Track-POD — 3 operation(s) for vehiclecheck.
  name: Track-POD VehicleCheck API
  slug: track-pod-vehiclecheck-api
artifact_total: 60
collections:
- collection_type: postman
  name: Track-POD Address API
  slug: postman-track-pod-address-api
- collection_type: postman
  name: Track-POD Address Driver API
  slug: postman-track-pod-driver-api
- collection_type: postman
  name: Track-POD Address Order API
  slug: postman-track-pod-order-api
- collection_type: postman
  name: Track-POD Address RejectReason API
  slug: postman-track-pod-rejectreason-api
- collection_type: postman
  name: Track-POD Address Route API
  slug: postman-track-pod-route-api
- collection_type: postman
  name: Track-POD Address Test API
  slug: postman-track-pod-test-api
- collection_type: postman
  name: Track-POD Address Vehicle API
  slug: postman-track-pod-vehicle-api
- collection_type: postman
  name: Track-POD Address VehicleCheck API
  slug: postman-track-pod-vehiclecheck-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Track-POD Address API
  slug: open-track-pod-address-api
- collection_type: open
  name: Track-POD Address Driver API
  slug: open-track-pod-driver-api
- collection_type: open
  name: Track-POD Address Order API
  slug: open-track-pod-order-api
- collection_type: open
  name: Track-POD Address RejectReason API
  slug: open-track-pod-rejectreason-api
- collection_type: open
  name: Track-POD Address Route API
  slug: open-track-pod-route-api
- collection_type: open
  name: Track-POD Address Test API
  slug: open-track-pod-test-api
- collection_type: open
  name: Track-POD Address Vehicle API
  slug: open-track-pod-vehicle-api
- collection_type: open
  name: Track-POD Address VehicleCheck API
  slug: open-track-pod-vehiclecheck-api
- collection_type: open
  name: Track-POD API
  slug: open-track-pod
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/track-pod-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/track-pod/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/track-pod-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/track-pod-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/track-pod-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.track-pod.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.track-pod.com/index.html
- group: start
  title: ''
  type: Sandbox
  url: https://api.sandbox.track-pod.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://track-pod.freshdesk.com/support/solutions/articles/103000049813-track-pod-api-integration
- group: auth
  title: ''
  type: Authentication
  url: https://track-pod.freshdesk.com/support/solutions/articles/103000049813-track-pod-api-integration
- group: commercial
  title: ''
  type: Pricing
  url: https://www.track-pod.com/pricing-delivery-app/
- group: commercial
  title: ''
  type: Plans
  url: plans/track-pod-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/track-pod-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/track-pod-finops.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.track-pod.com/blog/webhooks-api-integration/
- group: other
  title: ''
  type: Zapier
  url: https://zapier.com/apps/track-pod/integrations
- group: operate
  title: ''
  type: HelpCenter
  url: https://track-pod.freshdesk.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://www.track-pod.com/blog/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.track-pod.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.track-pod.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.track-pod.com/terms-of-service/
- group: start
  title: ''
  type: Signup
  url: https://www.track-pod.com/free-trial/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/track-pod/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/TrackPodApp
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TrackPod/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/TrackPod
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/track-pod-driver-pod-app/id1112930649
- group: other
  title: ''
  type: PlayStore
  url: https://play.google.com/store/apps/details?id=com.trackpod.android
created: '2026-05-25'
description: Track-POD is a cloud-based delivery management platform that combines route planning and optimization with electronic proof of delivery (ePOD), driver tracking, and last-mile customer notifications. The platform serves 10,000+ companies globally with a freemium model — the mobile driver app is free on iOS and Android, while the web dispatcher dashboard is sold on per-driver (Advanced, Advanced Plus, Ultimate, Enterprise) and per-order (S, M, L, XL) plans. Track-POD exposes a documented REST API (Track-POD API 2.0) with an OpenAPI 3.0 specification, JSON and XML payloads, X-API-KEY authentication, a public sandbox environment, and webhooks for ten event types covering orders, routes, and statuses. Common use cases include automated order import from e-commerce platforms (WooCommerce, Magento, Shopify, BigCommerce) and accounting/CRM systems (QuickBooks, Xero, Zoho, Microsoft Dynamics, Salesforce), real-time route dispatch and tracking, geotagged and signed proof of delivery,
  and PDF/shipping-label generation. Track-POD also ships no-code integrations via Zapier and Integrately.
examples:
- key_count: 5
  name: Track Pod Complete Order Example
  slug: track-pod-complete-order-example
- key_count: 5
  name: Track Pod Create Order Example
  slug: track-pod-create-order-example
features:
- Cloud-based delivery management for couriers, distributors, and field-service fleets
- Drag-and-drop route planning with multi-stop optimization in a single click
- Real-time driver tracking with ETA notifications to customers
- Electronic proof of delivery (ePOD) — sign-on-glass, photos, geotags, timestamps
- Barcode and QR code scanning for package and SKU verification
- Customizable delivery, collection, and service forms
- Offline-capable driver mobile app for iOS and Android with auto-sync
- REST API (Track-POD API 2.0) with JSON/XML, 58 operations across 8 resource families
- Public sandbox tenant at api.sandbox.track-pod.com for safe testing
- Webhooks for 10 events — order create/update/delete, route create/update/delete, order status change, route start/close/optimize
- Restricted API keys scoped by IP, HTTP method, and domain
- Rate limits 20 req/sec, 400 req/min, with a /Test endpoint to inspect current consumption
- Bulk order import endpoint accepting up to 500 orders per request
- PDF proof of delivery and shipping-label generation by order number or id
- Route export workflow with explicit "exported" flag and confirmation endpoints
- Vehicle inspection (VehicleCheck) endpoints for daily walk-around records
- Built-in integrations with WooCommerce, Shopify, BigCommerce, Magento, Xero, QuickBooks, Linnworks
- No-code integration via Zapier (5,000+ apps) and Integrately
- Custom integration assistance available on Advanced Plus, Ultimate, and Enterprise plans
finops:
- name: Track Pod Finops
  service_category: Logistics and Delivery Management
  slug: track-pod-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/track-pod.png
json_schemas:
- name: Track-POD Order
  property_count: 83
  slug: track-pod-order
- name: Track-POD Route
  property_count: 28
  slug: track-pod-route
- name: Track-POD Vehicle Check
  property_count: 12
  slug: track-pod-vehicle-check
json_structures:
- name: Track Pod Order Structure
  property_count: 0
  slug: track-pod-order-structure
jsonld:
- class_count: 0
  name: Track Pod Context
  property_count: 5
  slug: track-pod-context
layout: provider
modified: '2026-05-25'
name: Track-POD
nav: Providers
network: true
overview: 'Track-POD publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Address API, Driver API, Order API, and 5 more. Tagged areas include Delivery, Last Mile, Logistics, Proof of Delivery, and Electronic Proof Of Delivery.


  The Track-POD catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Track-POD''s developer surface includes authentication, documentation, sandbox, getting-started guide, pricing, engineering blog, signup flow, and 21 more developer resources.'
plans:
- name: Track Pod Plans Pricing
  plan_count: 8
  slug: track-pod-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Track Pod Rate Limits
  slug: track-pod-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Track-POD API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: track-pod-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Track-POD API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: track-pod-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 26.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 52.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/track-pod/refs/heads/main/screenshots/track-pod-2026-06-20T195516.png
security:
- kind: authentication
  name: Track Pod Authentication
  slug: track-pod-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Track Pod Domain Security
  slug: track-pod-domain-security
  summary_line: TLSv1.3 · DMARC
slug: track-pod
tags:
- Delivery
- Last Mile
- Logistics
- Proof of Delivery
- Electronic Proof Of Delivery
- EPOD
- Route Planning
- Route Optimization
- Dispatch
- Fleet Management
- Driver Tracking
- Couriers
- Field Service
- Transportation
- Shipping
website: https://www.track-pod.com
---
