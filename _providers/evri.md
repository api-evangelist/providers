---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.evri.com/
- group: start
  title: ''
  type: BusinessPortal
  url: https://business.evri.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.evri.com/help-and-support/help-centre
- group: other
  title: ''
  type: BusinessAccounts
  url: https://www.evri.com/business-accounts
- group: other
  title: ''
  type: InternationalServices
  url: https://www.evri.com/international-send
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.evri.com/responsible-disclosure-policy
- group: auth
  title: ''
  type: Security
  url: https://www.evri.com/cyber-security
- group: operate
  title: ''
  type: StatusPage
  url: https://www.evri.com/service-status
- group: other
  title: ''
  type: Tracking
  url: https://www.evri.com/track-a-parcel
- group: company
  title: ''
  type: About
  url: https://www.evri.com/about-us
- group: other
  title: ''
  type: Leadership
  url: https://www.evri.com/leadership
- group: other
  title: ''
  type: AnnualReports
  url: https://www.evri.com/annual-reports
- group: company
  title: ''
  type: Press
  url: https://www.evri.com/press
created: '2026-07-30'
description: 'Evri is the United Kingdom''s largest dedicated parcel delivery company, formerly Hermes UK, headquartered in Leeds and majority owned by Apollo-managed funds. Following the CMA-cleared 2025 merger with DHL eCommerce UK, the combined group delivers more than a billion parcels a year across a courier network of 30,000+ couriers and van drivers, thousands of ParcelShops and lockers, and domestic, returns and international services for retailers and marketplace sellers. Evri sits at the last-mile end of the supply chain — the carrier a shipper, retailer or e-commerce platform hands a parcel to for final delivery in the UK. Its API posture is customer-contract portal only: Evri publishes no developer portal, no public API reference and no machine-readable specification. The host api.evri.com resolves to a live Tyk API Gateway (5.13.0) whose only publicly reachable path is an unauthenticated health check; every other probed path returns 404 and no listen path is discoverable without
  credentials. Shipment, label, ParcelShop, Print in Store and tracking credentials are issued by an Evri account manager or sales representative to contracted Corporate or Business accounts, with sandbox and production credentials handed over by email. In practice most integrators reach Evri indirectly through shipping-API aggregators such as EasyPost, ShipEngine / ShipStation, Sendcloud, AfterShip and Intersoft Sapient rather than directly.'
layout: provider
modified: '2026-07-30'
name: Evri
nav: Providers
network: true
overview: 'Evri is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, United Kingdom, Parcel, and Last Mile Delivery.


  Evri''s developer surface includes documentation and 12 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 1
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 6.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evri/refs/heads/main/screenshots/evri-2026-08-07T165054.png
slug: evri
tags:
- Logistics
- Supply Chain
- United Kingdom
- Parcel
- Last Mile Delivery
- Couriers
- Track and Trace
- Returns
- E-Commerce
- Shipping
website: https://www.evri.com/
---
