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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Shippit Agentic Access
  operation_count: 10
  slug: shippit-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Initiate carrier bookings for orders.
  name: Shippit Book API
  slug: shippit-book-api
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Retrieve shipping labels and documents for an order.
  name: Shippit Label API
  slug: shippit-label-api
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Merchant account settings, operating hours, and webhooks.
  name: Shippit Merchant API
  slug: shippit-merchant-api
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Create, retrieve, update, and cancel shipping orders.
  name: Shippit Orders API
  slug: shippit-orders-api
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Live multi-carrier shipping quotes.
  name: Shippit Quote API
  slug: shippit-quote-api
- baseURL: https://app.shippit.com/api/3
  baseurl_source: declared
  description: Pull-based order tracking.
  name: Shippit Tracking API
  slug: shippit-tracking-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shippit Book API
  slug: open-shippit-book-api
- collection_type: open
  name: Shippit Book Label API
  slug: open-shippit-label-api
- collection_type: open
  name: Shippit Book Merchant API
  slug: open-shippit-merchant-api
- collection_type: open
  name: Shippit Book Orders API
  slug: open-shippit-orders-api
- collection_type: open
  name: Shippit Book Quote API
  slug: open-shippit-quote-api
- collection_type: open
  name: Shippit Book Tracking API
  slug: open-shippit-tracking-api
- collection_type: open
  name: Shippit API
  slug: open-shippit
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/capabilities/shippit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shippit-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/agentic-access/shippit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shippit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/security/shippit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shippit-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/authentication/shippit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shippit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippit
- group: company
  title: ''
  type: Website
  url: https://www.shippit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shippit.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/plans/shippit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shippit-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/rate-limits/shippit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shippit-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/finops/shippit-finops.yml
  title: ''
  type: FinOps
  url: finops/shippit-finops.yml
created: '2026-07-12'
description: Shippit is an Australian multi-carrier shipping and fulfillment platform for retailers and e-commerce merchants across Australia, New Zealand, and Southeast Asia. Its REST API (v3) lets merchants request live carrier quotes, create and cancel orders, book consignments with carriers, retrieve A6 shipping labels and pick slips, and track parcels via pull requests or push webhooks. Authentication is a per-merchant API key passed as an HTTP Bearer token, with a staging sandbox and a production environment.
finops:
- name: Shippit Finops
  service_category: Shipping and Logistics
  slug: shippit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippit.png
layout: provider
modified: '2026-07-12'
name: Shippit
nav: Providers
network: true
overview: 'Shippit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Book API, Label API, Merchant API, and 3 more. Tagged areas include Shipping, Logistics, Fulfillment, Australia, and Asia Pacific.


  Shippit''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Shippit Plans Pricing
  plan_count: 3
  slug: shippit-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Shippit Rate Limits
  slug: shippit-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 50.2
    developer_ergonomics: 28.6
    discoverability: 66.1
    operational_transparency: 18.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/shippit/refs/heads/main/screenshots/shippit-2026-09-02T155233.png
security:
- kind: authentication
  name: Shippit Authentication
  slug: shippit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shippit Domain Security
  slug: shippit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippit
tags:
- Shipping
- Logistics
- Fulfillment
- Australia
- Asia Pacific
- Multi-Carrier
- Labels
- Tracking
- Parcel
- E-commerce Logistics
- Software-as-a-Service
website: https://www.shippit.com
---
