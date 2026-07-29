---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Royal Mail Agentic Access
  operation_count: 14
  slug: royal-mail-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 10
apis:
- description: 'A fully RESTful service enabling account customers to create domestic and international shipments, produce shipping labels, print customs documents, manifest shipments, pre-allocate tracking numbers, '
  name: Royal Mail API Shipping V2 (REST)
  slug: royal-mail-api-shipping-v2-rest
- description: Allows account customers to receive track-and-trace information for mail items, including current status, delivery history, and proof of delivery for single or multiple items. Intended for server-side
  name: Royal Mail Tracking V2 (REST)
  slug: royal-mail-tracking-v2-rest
- description: A RESTful web service that enables API consumers to request a pre-allocated range of Royal Mail barcodes for offline use in shipping processes. No usage costs to customers; development costs are cover
  name: Royal Mail Barcode Allocation V1 (REST)
  slug: royal-mail-barcode-allocation-v1-rest
- description: Enables customers to benefit from Click and Collect delivery options by retrieving current lists of participating Post Offices and Royal Mail Customer Service Points where tracked and special delivery
  name: Royal Mail Local Collect V3 (REST)
  slug: royal-mail-local-collect-v3-rest
- description: Enables Royal Mail customers to obtain details of the delivery office dedicated to a provided postcode, including location name, address, available facilities, and opening hours.
  name: Royal Mail Delivery Office Finder V1 (REST)
  slug: royal-mail-delivery-office-finder-v1-rest
- description: The Labels API from Royal Mail — 1 operation(s) for labels.
  name: Royal Mail Labels API
  slug: royal-mail-labels-api
- description: The Manifests API from Royal Mail — 3 operation(s) for manifests.
  name: Royal Mail Manifests API
  slug: royal-mail-manifests-api
- description: The Orders API from Royal Mail — 5 operation(s) for orders.
  name: Royal Mail Orders API
  slug: royal-mail-orders-api
- description: Reserved for OBA customers only.
  name: Royal Mail Returns API
  slug: royal-mail-returns-api
- description: The Version API from Royal Mail — 1 operation(s) for version.
  name: Royal Mail Version API
  slug: royal-mail-version-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/royal-mail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/royal-mail-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/royal-mail-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.royalmail.net/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.royalmail.net/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.royalmail.net/start
- group: operate
  title: ''
  type: Support
  url: https://developer.royalmail.net/help
- group: commercial
  title: ''
  type: Plans
  url: https://developer.royalmail.net/product
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.royalmail.net/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.royalmail.net/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.royalmail.net/start
- group: operate
  title: ''
  type: Contact
  url: https://developer.royalmail.net/help
created: '2026-06-13'
description: Royal Mail provides a suite of REST APIs for businesses to integrate shipping, tracking, label generation, barcode allocation, and Click & Drop order management directly into their fulfilment systems. APIs cover domestic and international shipment creation, label printing, manifest submission, pre-allocated tracking numbers, offline barcode ranges, local collect options, and delivery office lookup.
examples:
- key_count: 4
  name: Create Order
  slug: create-order
- key_count: 4
  name: Create Return
  slug: create-return
- key_count: 5
  name: Manifest Orders
  slug: manifest-orders
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/royal-mail.png
json_schemas:
- name: CreateOrderRequest
  property_count: 19
  slug: create-order-request
- name: CreateOrdersResponse
  property_count: 4
  slug: create-order-response
jsonld:
- class_count: 25
  name: Royal Mail Context
  property_count: 12
  slug: royal-mail
layout: provider
modified: '2026-06-13'
name: Royal Mail
nav: Providers
network: true
overview: 'Royal Mail publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Labels API, Manifests API, Orders API, and 2 more. Tagged areas include Shipping, Postal Services, Labels, Tracking, and Logistics.


  The Royal Mail catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Royal Mail''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 55
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Royal Mail API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: royal-mail-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: -6.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/royal-mail/refs/heads/main/screenshots/royal-mail-2026-06-20T193236.png
security:
- kind: authentication
  name: Royal Mail Authentication
  slug: royal-mail-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Royal Mail Domain Security
  slug: royal-mail-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: royal-mail
tags:
- Shipping
- Postal Services
- Labels
- Tracking
- Logistics
- Barcodes
- Click and Drop
- UK
website: https://developer.royalmail.net/
---
