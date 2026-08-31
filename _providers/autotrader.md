---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 13
apis:
- description: 'Provides VRM and VIN lookups, MOT history, vehicle features, valuations, and retail metrics for individual vehicles. Enables dealers and partners to retrieve comprehensive vehicle data for appraisals '
  name: Autotrader Vehicles API
  slug: autotrader-vehicles-api
- description: Provides structured data for vehicle makes, models, generations, and derivatives. Used to build consistent vehicle classification and search facets across automotive systems.
  name: Autotrader Taxonomy API
  slug: autotrader-taxonomy-api
- description: Enables retailers to manage their forecourt inventory programmatically. Supports creating, updating, and deleting vehicle adverts in the Autotrader marketplace from third-party dealer management syste
  name: Autotrader Stock API
  slug: autotrader-stock-api
- description: CDN-backed image storage and management API for vehicle adverts. Allows partners to upload, retrieve, and manage vehicle photography via Autotrader's content delivery network.
  name: Autotrader Images API
  slug: autotrader-images-api
- description: Provides filtered and sorted access to consumer vehicle adverts on the Autotrader marketplace. Enables partners to build consumer-facing search and browsing applications with Autotrader inventory.
  name: Autotrader Search API
  slug: autotrader-search-api
- description: Delivers current UK market vehicle valuation data based on real-time Autotrader marketplace signals. Provides dealers and partners with trusted pricing intelligence for retail decisions.
  name: Autotrader Valuations API
  slug: autotrader-valuations-api
- description: Provides supply, demand, and pricing intelligence metrics to help retailers understand market positioning. Includes retail rating, average days to sell, and competitor analysis data.
  name: Autotrader Vehicle Metrics API
  slug: autotrader-vehicle-metrics-api
- description: Returns predicted vehicle valuations for a specified future date, enabling dealers to forecast vehicle depreciation and make forward-looking pricing and acquisition decisions.
  name: Autotrader Future Valuations API
  slug: autotrader-future-valuations-api
- description: Provides access to historical vehicle valuation data, enabling trend analysis and retrospective pricing research across the UK automotive market.
  name: Autotrader Historic Valuations API
  slug: autotrader-historic-valuations-api
- description: Manages the full deal lifecycle between buyers and dealers on the Autotrader platform. Supports deal creation, status updates, and notifications including DEAL_CREATE and DEAL_UPDATE events.
  name: Autotrader Deals API
  slug: autotrader-deals-api
- description: Manages part-exchange vehicle transactions allowing dealers to appraise and accept trade-in vehicles as part of the deal flow integrated with Autotrader's Deal Builder product.
  name: Autotrader Part Exchange API
  slug: autotrader-part-exchange-api
- description: AI-powered API that generates vehicle advert descriptions and optimizes image ordering for vehicle listings. Enables dealers to produce high-quality, consistent content at scale through integration wi
  name: Autotrader Co-Driver API
  slug: autotrader-co-driver-api
- description: Beta API supporting finance application and quote management for vehicle purchases. Enables integration of motor finance products into the Autotrader deal flow and partner platforms.
  name: Autotrader Finance API
  slug: autotrader-finance-api
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autotrader-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autotrader.co.uk
- group: company
  title: ''
  type: PartnerSite
  url: https://www.autotrader.co.uk/partners/retailer/platform/autotrader-connect
- group: docs
  title: ''
  type: Documentation
  url: https://developers.autotrader.co.uk/api
- group: company
  title: ''
  type: Blog
  url: https://engineering.autotrader.co.uk
- group: operate
  title: ''
  type: StatusPage
  url: https://status.autotrader.co.uk
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/auto-trader-uk
- group: other
  title: ''
  type: X
  url: https://twitter.com/AutoTrader_UK
- group: operate
  title: ''
  type: Support
  url: https://help.autotrader.co.uk/hc/en-gb
- group: commercial
  title: ''
  type: Plans
  url: plans/autotrader-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autotrader-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/autotrader-finops.yml
created: 2026-06-13
description: Autotrader is the UK's largest digital automotive marketplace, providing REST APIs through the Autotrader Connect platform for vehicle listings, dealer stock management, VIN and VRM lookups, vehicle valuations, retail metrics, taxonomy, images, deals, and consumer-facing search. The platform enables technology partners and retailers to integrate automotive data and marketplace functionality into their systems in real time.
finops:
- name: Autotrader Finops
  service_category: ''
  slug: autotrader-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autotrader.png
layout: provider
modified: 2026-06-13
name: Autotrader
nav: Providers
network: true
overview: 'Autotrader publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Vehicles, Marketplace, Dealer, and Listings.


  Autotrader''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
plans:
- name: Autotrader Plans Pricing
  plan_count: 1
  slug: autotrader-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Autotrader Rate Limits
  slug: autotrader-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 22.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autotrader/refs/heads/main/screenshots/autotrader-2026-06-20T172717.png
security:
- kind: domain-security
  name: Autotrader Domain Security
  slug: autotrader-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autotrader
tags:
- Automotive
- Vehicles
- Marketplace
- Dealer
- Listings
- Valuations
- VIN
- VRM
- Inventory
- Car Buying
- Car Selling
website: https://www.autotrader.co.uk
---
