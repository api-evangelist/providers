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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Trackingmore Agentic Access
  operation_count: 9
  slug: trackingmore-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 3
apis:
- description: Track air cargo using Master Air Waybill (MAWB) numbers
  name: TrackingMore Air Waybills API
  slug: trackingmore-air-waybills-api
- description: List available couriers and detect carrier from tracking number
  name: TrackingMore Couriers API
  slug: trackingmore-couriers-api
- description: Create, retrieve, update, and delete shipment trackings
  name: TrackingMore Trackings API
  slug: trackingmore-trackings-api
artifact_total: 38
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trackingmore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trackingmore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trackingmore-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trackingmore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.trackingmore.com/docs/trackingmore/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trackingmore.com/docs/trackingmore/d5ac362fc3cda-api-quick-start-guide
- group: auth
  title: ''
  type: Authentication
  url: https://www.trackingmore.com/docs/trackingmore/zte58cee4mz0v-api-authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trackingmore.com/pricing
- group: design
  title: ''
  type: Webhooks
  url: https://www.trackingmore.com/webhook.html
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trackingmore-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trackingmore-api
- group: operate
  title: ''
  type: Support
  url: https://support.trackingmore.com/
- group: operate
  title: ''
  type: RateLimits
  url: https://support.trackingmore.com/en/article/trackingmore-api-request-rate-limit-c0ye70/
- group: commercial
  title: ''
  type: Billing
  url: https://support.trackingmore.com/en/article/trackingmore-billing-explained-credits-and-sms-fees-hychoa/
- group: company
  title: ''
  type: Blog
  url: https://www.trackingmore.com/blog/
created: '2026-06-13'
description: TrackingMore is a multi-carrier shipment tracking platform offering a unified REST API that integrates with 1,300+ global carriers including USPS, UPS, FedEx, DHL, and regional logistics providers. The platform provides real-time tracking updates, automated carrier detection, webhook notifications using HMAC-SHA256 signatures, and delivery analytics. SDKs are available for Python, Node.js, PHP, Go, Ruby, Java, and .NET. TrackingMore serves D2C merchants, ecommerce platforms, and enterprise logistics operations with 99.99% API uptime SLA and 24/7 technical support.
examples:
- key_count: 11
  name: Create Tracking Request
  slug: create-tracking-request
- key_count: 3
  name: Create Tracking Response
  slug: create-tracking-response
- key_count: 1
  name: Detect Courier Request
  slug: detect-courier-request
- key_count: 3
  name: Detect Courier Response
  slug: detect-courier-response
- key_count: 3
  name: Tracking In Transit
  slug: tracking-in-transit
features:
- 'Base URL: https://api.trackingmore.com/v4'
- 'Authentication: API key via Tracking-Api-Key header'
- Up to 4 API keys per account
- 1,300+ global carrier integrations
- 'Free plan: 50 shipments/month at $0/month'
- 'Basic plan: starting at $11/month for 200 shipments'
- 'Pro plan: $74/month for 2,000 shipments; includes tracking API and webhooks'
- 'Enterprise plan: custom pricing and custom rate limits'
- 'Overage rate: $0.04 per extra credit on Basic and Pro'
- 'Rate limit (Pro): 10 requests/second for most endpoints'
- 'Rate limit (create tracking): 3 requests/second'
- 429 error on rate limit exceeded; wait 120 seconds before retry
- 'Credit model: 1 credit per unique tracking number + courier code'
- 'Air cargo tracking (MAWB): 50 credits per track'
- 'Translation: 1 additional credit per translation'
- Webhook events via POST with HMAC-SHA256 signature verification
- 'SDKs: Python, Node.js, PHP, Go, Ruby, Java, .NET'
- 99.99% uptime SLA
- 24/7 live chat and email support
finops:
- name: Trackingmore Finops
  service_category: ''
  slug: trackingmore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trackingmore.png
json_schemas:
- name: AirWaybill
  property_count: 6
  slug: air-waybill
- name: Courier
  property_count: 6
  slug: courier
- name: Tracking
  property_count: 18
  slug: tracking
jsonld:
- class_count: 32
  name: Trackingmore Context
  property_count: 0
  slug: trackingmore-context
layout: provider
modified: '2026-06-13'
name: TrackingMore
nav: Providers
network: true
overview: 'TrackingMore publishes 3 APIs on the [APIs.io](https://apis.io/) network: Air Waybills API, Couriers API, and Trackings API. Tagged areas include Logistics, Shipping, Tracking, Parcels, and Webhooks.


  The TrackingMore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TrackingMore''s developer surface includes authentication, documentation, getting-started guide, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Trackingmore Plans
  plan_count: 4
  slug: trackingmore-plans
random_paper: 71
rate_limits:
- limit_count: 0
  name: Trackingmore Rate Limits
  slug: trackingmore-rate-limits
rules:
- name: TrackingMore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trackingmore-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.6
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.7
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trackingmore/refs/heads/main/screenshots/trackingmore-2026-06-20T195521.png
security:
- kind: authentication
  name: Trackingmore Authentication
  slug: trackingmore-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Trackingmore Domain Security
  slug: trackingmore-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: trackingmore
tags:
- Logistics
- Shipping
- Tracking
- Parcels
- Webhooks
- Ecommerce
website: https://www.trackingmore.com/
---
