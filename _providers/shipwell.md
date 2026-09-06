---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Shipwell Agentic Access
  operation_count: 19
  slug: shipwell-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.shipwell.com/v2
  baseurl_source: declared
  description: Carriers, carrier relationships, and carrier assignments. (partly confirmed)
  name: Shipwell Carriers API
  slug: shipwell-carriers-api
- baseURL: https://api.shipwell.com/v2
  baseurl_source: declared
  description: Real-time supply-chain events and webhook subscriptions. (partly confirmed)
  name: Shipwell Events and Webhooks API
  slug: shipwell-events-and-webhooks-api
- baseURL: https://api.shipwell.com/v2
  baseurl_source: declared
  description: Orders and purchase orders consolidated onto shipments. (modeled)
  name: Shipwell Orders API
  slug: shipwell-orders-api
- baseURL: https://api.shipwell.com/v2
  baseurl_source: declared
  description: Rates, quotes, RFQs, spot negotiations, and carrier bids. (modeled)
  name: Shipwell Quoting API
  slug: shipwell-quoting-api
- baseURL: https://api.shipwell.com/v2
  baseurl_source: declared
  description: Multimodal freight shipments - the central platform resource. (confirmed)
  name: Shipwell Shipments API
  slug: shipwell-shipments-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shipwell v2 Core Carriers API
  slug: open-shipwell-carriers-api
- collection_type: open
  name: Shipwell v2 Core Carriers Events and Webhooks API
  slug: open-shipwell-events-and-webhooks-api
- collection_type: open
  name: Shipwell v2 Core Carriers Orders API
  slug: open-shipwell-orders-api
- collection_type: open
  name: Shipwell v2 Core Carriers Quoting API
  slug: open-shipwell-quoting-api
- collection_type: open
  name: Shipwell v2 Core Carriers Shipments API
  slug: open-shipwell-shipments-api
- collection_type: open
  name: Shipwell v2 Core API
  slug: open-shipwell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shipwell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipwell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipwell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipwell.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipwell
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shipwell.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.shipwell.com/request-a-demo
- group: commercial
  title: ''
  type: Plans
  url: plans/shipwell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipwell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipwell-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.shipwell.com/blog
created: '2026-07-05'
description: Shipwell is an AI-powered transportation management system (TMS) and freight execution platform for shippers, brokers, and carriers. The Shipwell v2 Core API lets developers plan, rate, tender, book, track, and settle multimodal freight - parcel, LTL, truckload, intermodal, rail, and ocean - programmatically. It covers shipments, quoting and rating, carrier management, purchase orders and orders, documents, tenders, freight pay and audit, and a real-time events and webhooks surface. The production base URL is https://api.shipwell.com/v2 (the newer Orders API is served under https://api.shipwell.com without the /v2 prefix), with a fully separate sandbox at https://sandbox-api.shipwell.com/v2. Requests are authenticated with company-scoped API keys passed in the Authorization header. Access to the full platform and API is enterprise and contract-gated.
finops:
- name: Shipwell Finops
  service_category: Logistics and Supply Chain
  slug: shipwell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipwell.png
layout: provider
modified: '2026-07-05'
name: Shipwell
nav: Providers
network: true
overview: 'Shipwell publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Events and Webhooks API, Orders API, and 2 more. Tagged areas include Transportation Management, TMS, Freight, Logistics, and Shipping.


  Shipwell''s developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Shipwell Plans Pricing
  plan_count: 3
  slug: shipwell-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Shipwell Rate Limits
  slug: shipwell-rate-limits
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 22.5
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipwell/refs/heads/main/screenshots/shipwell-2026-09-02T155238.png
security:
- kind: authentication
  name: Shipwell Authentication
  slug: shipwell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shipwell Domain Security
  slug: shipwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipwell
tags:
- Transportation Management
- TMS
- Freight
- Logistics
- Shipping
- Supply Chain
website: https://www.shipwell.com/
---
