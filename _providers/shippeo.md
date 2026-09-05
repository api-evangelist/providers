---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
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
  score: 24.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Shippeo Agentic Access
  operation_count: 11
  slug: shippeo-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.shippeo.com
  baseurl_source: declared
  description: Retrieve predictive ETAs, statuses, and milestone events (Events-out, pull).
  name: Shippeo ETA and Status API
  slug: shippeo-eta-and-status-api
- baseURL: https://api.shippeo.com
  baseurl_source: declared
  description: Manage webhook subscriptions for real-time Events-out notifications.
  name: Shippeo Event Subscriptions API
  slug: shippeo-event-subscriptions-api
- baseURL: https://api.shippeo.com
  baseurl_source: declared
  description: Feed and retrieve geolocation positions for tracked transports.
  name: Shippeo Positions API
  slug: shippeo-positions-api
- baseURL: https://api.shippeo.com
  baseurl_source: declared
  description: Submit and manage transport orders (tours) for real-time tracking.
  name: Shippeo Transport Orders API
  slug: shippeo-transport-orders-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility ETA and Status API
  slug: open-shippeo-eta-and-status-api
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility ETA and Status Event Subscriptions API
  slug: open-shippeo-event-subscriptions-api
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility ETA and Status Positions API
  slug: open-shippeo-positions-api
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility ETA and Status Transport Orders API
  slug: open-shippeo-transport-orders-api
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility API
  slug: open-shippeo
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shippeo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shippeo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shippeo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shippeo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shippeo.com
- group: start
  title: ''
  type: SignUp
  url: https://developers.shippeo.com
- group: operate
  title: ''
  type: StatusPage
  url: https://shippeo.statuspage.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippeo
- group: commercial
  title: ''
  type: Plans
  url: plans/shippeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shippeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shippeo-finops.yml
created: '2026-07-12'
description: Shippeo is a real-time transportation and multimodal supply-chain visibility platform, giving shippers, carriers, and logistics teams predictive and real-time information for all their deliveries across road, rail, sea, and air. Through its developer portal (developers.shippeo.com) Shippeo exposes REST APIs and webhooks so TMS, ERP, and control-tower systems can submit transport orders (tours) for tracking, feed GPS positions, retrieve predictive ETAs, statuses, and milestone events, and subscribe to real-time "Events-out" notifications. API access is enterprise and customer-provisioned - applications and OAuth2 client IDs are created in the portal after contracting with Shippeo.
finops:
- name: Shippeo Finops
  service_category: Supply Chain Visibility
  slug: shippeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippeo.png
layout: provider
modified: '2026-07-12'
name: Shippeo
nav: Providers
network: true
overview: 'Shippeo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ETA and Status API, Event Subscriptions API, Positions API, and 1 more. Tagged areas include Supply Chain, Transportation Visibility, Real-Time Visibility, Logistics, and Shipment Tracking.


  Shippeo''s developer surface includes authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Shippeo Plans Pricing
  plan_count: 1
  slug: shippeo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Shippeo Rate Limits
  slug: shippeo-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 13.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shippeo/refs/heads/main/screenshots/shippeo-2026-09-02T155227.png
security:
- kind: authentication
  name: Shippeo Authentication
  slug: shippeo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Shippeo Domain Security
  slug: shippeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippeo
tags:
- Supply Chain
- Transportation Visibility
- Real-Time Visibility
- Logistics
- Shipment Tracking
- ETA
- Freight
- Supply Chain Visibility
- Software-as-a-Service
website: https://www.shippeo.com
---
