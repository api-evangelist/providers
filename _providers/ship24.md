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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ship24 Agentic Access
  operation_count: 11
  slug: ship24-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 1
apis:
- description: 'The **Tracking API (Per-call Plans)** is a specific product and associated endpoint on which usage is measured per API Call made. Each API call is synchronously fetching data from couriers which make '
  name: Ship24 ➕ API for per-call plans API
  slug: ship24-api-for-per-call-plans-api
- description: The 🚚 Couriers API from Ship24 — 1 operation(s) for 🚚 couriers.
  name: Ship24 🚚 Couriers API
  slug: ship24-couriers-api
- description: The 📦 Trackers API from Ship24 — 7 operation(s) for 📦 trackers.
  name: Ship24 📦 Trackers API
  slug: ship24-trackers-api
- description: The Ship24 Tracking API API from Ship24 — 0 operation(s) for ship24 tracking api.
  name: Ship24 Ship24 Tracking API
  slug: ship24-ship24-tracking-api-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ship24 Tracking ➕ API for per-call plans ➕ API for per-call plans ➕ API for per-call plans API
  slug: open-ship24-api-for-per-call-plans-api
- collection_type: open
  name: Ship24 Tracking ➕ API for per-call plans ➕ API for per-call plans 🚚 Couriers API
  slug: open-ship24-couriers-api
- collection_type: open
  name: Ship24 Tracking ➕ API for per-call plans ➕ API for per-call plans 📦 Trackers API
  slug: open-ship24-trackers-api
- collection_type: open
  name: Ship24 Tracking API
  slug: open-ship24-tracking-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ship24-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ship24-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ship24-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ship24-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ship24.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ship24.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ship24.com/tracking-api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ship24.com/getting-started
- group: design
  title: ''
  type: Webhooks
  url: https://docs.ship24.com/webhooks
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.ship24.com/rate-limiter
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ship24.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://dashboard.ship24.com/register
- group: start
  title: ''
  type: Login
  url: https://dashboard.ship24.com/
- group: auth
  title: ''
  type: Authentication
  url: https://dashboard.ship24.com/integrations/api-keys
- group: operate
  title: ''
  type: Status
  url: https://status.ship24.com
- group: company
  title: ''
  type: Blog
  url: https://www.ship24.com/blog
- group: operate
  title: ''
  type: ContactUs
  url: https://www.ship24.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ship24.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ship24.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ship24/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ship24
- group: other
  title: ''
  type: ShopifyApp
  url: https://apps.shopify.com/ship24
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Ship24/n8n-nodes-ship24
created: '2026-05-25'
description: Ship24 is a universal shipment tracking platform that consolidates 1,500+ couriers and marketplaces into a single API, dashboard, and post-purchase customer experience. It is operated as an enterprise tracking aggregator with reported coverage of over a billion shipments tracked, a Shopify app, branded tracking pages, email and SMS delivery notifications, a tracking widget, and an IOSS fiscal intermediary service for EU VAT compliance on inbound parcels. The developer surface is a single REST tracking API delivering normalized status codes and webhook events designed to reduce WISMO ("where is my order?") support load for ecommerce, 3PL, and marketplace operators.
examples:
- key_count: 2
  name: Ship24 Create Tracker Example
  slug: ship24-create-tracker-example
- key_count: 2
  name: Ship24 Tracking Result Example
  slug: ship24-tracking-result-example
features:
- 1,500+ couriers worldwide (USPS, UPS, FedEx, DHL, Royal Mail, La Poste, China Post, Japan Post, India Post, Correios, Yodel, Hermes, GLS, Canada Post, Australia Post, etc.)
- Universal tracking REST API at api.ship24.com over HTTPS
- Bearer token (API key) authentication issued from the Ship24 dashboard
- Automatic courier auto-detection from tracking number patterns
- Bulk tracker creation in a single request
- Normalized shipment status codes across heterogeneous courier feeds
- Webhook delivery of tracking events with signed payloads
- Webhook resend / replay endpoint for missed events
- Branded customer tracking pages on custom domain (Pro plan and above)
- Email and SMS delivery notifications
- Tracking widget embeddable in storefronts
- Shopify app integration with automated post-purchase workflows
- Per-shipment and per-API-call commercial plans
- 99.9% uptime SLA target
- GDPR-compliant data processing
- IOSS fiscal intermediary service for EU VAT compliance on cross-border ecommerce parcels
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ship24.png
json_schemas:
- name: Ship24 Tracker
  property_count: 10
  slug: ship24-tracker
- name: Ship24 Tracking Result
  property_count: 4
  slug: ship24-tracking-result
json_structures:
- name: Ship24 Tracker Structure
  property_count: 0
  slug: ship24-tracker-structure
jsonld:
- class_count: 22
  name: Ship24 Context
  property_count: 2
  slug: ship24-context
layout: provider
modified: '2026-05-25'
name: Ship24
nav: Providers
network: true
overview: 'Ship24 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ➕ API for per-call plans API, 🚚 Couriers API, 📦 Trackers API, and 1 more. Tagged areas include Tracking, Logistics, Shipping, Couriers, and Parcels.


  The Ship24 catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ship24''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, status page, and 16 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 5
  extends: []
  name: Ship24 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ship24-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Ship24 API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: ship24-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 28.8
    contract_quality: 67.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 2.6
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ship24/refs/heads/main/screenshots/ship24-2026-06-20T193813.png
security:
- kind: authentication
  name: Ship24 Authentication
  slug: ship24-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ship24 Domain Security
  slug: ship24-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ship24
tags:
- Tracking
- Logistics
- Shipping
- Couriers
- Parcels
- Webhook
- E-Commerce
- Post-Purchase
website: https://www.ship24.com
---
