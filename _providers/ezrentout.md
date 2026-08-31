---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Ezrentout Agentic Access
  operation_count: 71
  slug: ezrentout-agentic-access
  summary_line: 71 operations · 40 acting
api_count: 1
apis:
- description: Serialized fixed (rentable) assets and GPS location tracking.
  name: EZRentOut Assets API
  slug: ezrentout-assets-api
- description: Booked dates and per-location quantity for scheduling.
  name: EZRentOut Availability API
  slug: ezrentout-availability-api
- description: Reusable kits of assets and inventory rented together.
  name: EZRentOut Bundles API
  slug: ezrentout-bundles-api
- description: Customers, businesses, and business contacts, with addresses.
  name: EZRentOut Customers API
  slug: ezrentout-customers-api
- description: Volatile assets (inventory) and asset stock, with per-location stock.
  name: EZRentOut Inventory API
  slug: ezrentout-inventory-api
- description: Warehouses / branches that hold assets and inventory.
  name: EZRentOut Locations API
  slug: ezrentout-locations-api
- description: Service records and work orders (tasks) to keep equipment serviceable.
  name: EZRentOut Maintenance API
  slug: ezrentout-maintenance-api
- description: Staff members (users) of the rental account.
  name: EZRentOut Members API
  slug: ezrentout-members-api
- description: Rental orders, called baskets - draft, reserve, check out, and check in.
  name: EZRentOut Orders API
  slug: ezrentout-orders-api
- description: Order payments, taxes, coupons, and damage charges (invoicing).
  name: EZRentOut Payments API
  slug: ezrentout-payments-api
- description: Procurement - purchase orders and vendors.
  name: EZRentOut Purchase Orders API
  slug: ezrentout-purchase-orders-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EZRentOut Assets API
  slug: open-ezrentout-assets-api
- collection_type: open
  name: EZRentOut Assets Availability API
  slug: open-ezrentout-availability-api
- collection_type: open
  name: EZRentOut Assets Bundles API
  slug: open-ezrentout-bundles-api
- collection_type: open
  name: EZRentOut Assets Customers API
  slug: open-ezrentout-customers-api
- collection_type: open
  name: EZRentOut Assets Inventory API
  slug: open-ezrentout-inventory-api
- collection_type: open
  name: EZRentOut Assets Locations API
  slug: open-ezrentout-locations-api
- collection_type: open
  name: EZRentOut Assets Maintenance API
  slug: open-ezrentout-maintenance-api
- collection_type: open
  name: EZRentOut Assets Members API
  slug: open-ezrentout-members-api
- collection_type: open
  name: EZRentOut Assets Orders API
  slug: open-ezrentout-orders-api
- collection_type: open
  name: EZRentOut Assets Payments API
  slug: open-ezrentout-payments-api
- collection_type: open
  name: EZRentOut Assets Purchase Orders API
  slug: open-ezrentout-purchase-orders-api
- collection_type: open
  name: EZRentOut API
  slug: open-ezrentout
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ezrentout-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezrentout-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ezrentout-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezrentout-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezrentout-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ezrentout/
- group: company
  title: ''
  type: Website
  url: https://ezo.io/ezrentout/
- group: docs
  title: ''
  type: Documentation
  url: https://ezo.io/ezrentout/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/ezrentout-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ezrentout-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ezrentout-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ezo.io/ezrentout/blog/feed/
created: '2026-07-03'
description: EZRentOut is cloud-based equipment rental management software from EZO (the company behind EZOfficeInventory) for rental businesses to manage orders, fixed and inventory assets, bundles, customers, members, locations, purchase orders, and maintenance. Its REST API is made available to paying customers for custom integrations - each request is authenticated with a per-company access token sent in a token header over HTTPS, endpoints are namespaced with a .api suffix, and calls are scoped to the customer's own {subdomain}.ezrentout.com tenant. The API covers orders (baskets), assets, inventory and stock assets, bundles, customers and businesses, members, locations, availability, payments and invoicing, purchase orders, and service/work-order maintenance.
finops:
- name: Ezrentout Finops
  service_category: Business Application Software (Rental Management)
  slug: ezrentout-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ezrentout.png
layout: provider
modified: '2026-07-03'
name: EZRentOut
nav: Providers
network: true
overview: 'EZRentOut publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Availability API, Bundles API, and 8 more. Tagged areas include Equipment Rental, Rental Management, Asset Tracking, Inventory, and Order Management.


  EZRentOut''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ezrentout Plans Pricing
  plan_count: 5
  slug: ezrentout-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Ezrentout Rate Limits
  slug: ezrentout-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezrentout/refs/heads/main/screenshots/ezrentout-2026-07-25T214101.png
security:
- kind: authentication
  name: Ezrentout Authentication
  slug: ezrentout-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ezrentout Domain Security
  slug: ezrentout-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Ezrentout Trust Center
  slug: ezrentout-trust-center
  summary_line: SOC 2, ISO 27001, CSA STAR
slug: ezrentout
tags:
- Equipment Rental
- Rental Management
- Asset Tracking
- Inventory
- Order Management
- EZO
website: https://ezo.io/ezrentout/
---
