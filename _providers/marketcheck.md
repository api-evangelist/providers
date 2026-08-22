---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Marketcheck Agentic Access
  operation_count: 27
  slug: marketcheck-agentic-access
  summary_line: 27 operations
api_count: 15
apis:
- description: Decode 17-digit VINs to extract year, make, model, trim, installed equipment, and full vehicle specifications. Available in Basic and NeoVIN Enhanced tiers for comprehensive build-level data.
  name: MarketCheck VIN Decoder API
  slug: marketcheck-vin-decoder-api
- description: Access complete price history, odometer readings, and full listing details for vehicles up to six years back by VIN, enabling market analysis and vehicle valuation insights.
  name: MarketCheck Vehicle History API
  slug: marketcheck-vehicle-history-api
- description: 'Predict market prices and retrieve MSRP for used vehicles. Three tiers available: Base (predicted price + MSRP), Premium (adds comparable vehicles), and Premium Plus (adds full NeoVIN decode).'
  name: MarketCheck Price API
  slug: marketcheck-price-api
- description: Search individual dealerships or locate multiple dealerships in a geographic area by radius. Access dealer profiles, inventory counts, and dealership group information.
  name: MarketCheck Dealer API
  slug: marketcheck-dealer-api
- description: Obtain Market Days Supply (MDS) values, sales statistics, and popular vehicle data to understand supply and demand dynamics across the automotive market.
  name: MarketCheck Market Insights API
  slug: marketcheck-market-insights-api
- description: Search incentive programs from 30+ car manufacturers by make, zip code, and other criteria to surface OEM financing, rebate, and lease offers.
  name: MarketCheck OEM Incentives API
  slug: marketcheck-oem-incentives-api
- description: Search recreational vehicle (RV) inventory and dealer listings across the US and Canada. Supports filtering by price, options, photos, and equipment details.
  name: MarketCheck RV API
  slug: marketcheck-rv-api
- description: Dealer search and information
  name: MarketCheck Dealer API
  slug: marketcheck-dealer-api
- description: Search facets for filtering
  name: MarketCheck Facets API
  slug: marketcheck-facets-api
- description: Plot data for visualizations
  name: MarketCheck Graphs API
  slug: marketcheck-graphs-api
- description: Vehicle listing history
  name: MarketCheck History API
  slug: marketcheck-history-api
- description: Dealer inventory operations
  name: MarketCheck Inventory API
  slug: marketcheck-inventory-api
- description: Search and retrieve active car listings
  name: MarketCheck Listings API
  slug: marketcheck-listings-api
- description: Market analytics, trends, and pricing insights
  name: MarketCheck Market API
  slug: marketcheck-market-api
- description: VIN decoding and vehicle specifications
  name: MarketCheck VIN Decoder API
  slug: marketcheck-vin-decoder-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MarketCheck Cars Dealer API
  slug: open-marketcheck-dealer-api
- collection_type: open
  name: MarketCheck Cars Dealer Facets API
  slug: open-marketcheck-facets-api
- collection_type: open
  name: MarketCheck Cars Dealer Graphs API
  slug: open-marketcheck-graphs-api
- collection_type: open
  name: MarketCheck Cars Dealer History API
  slug: open-marketcheck-history-api
- collection_type: open
  name: MarketCheck Cars Dealer Inventory API
  slug: open-marketcheck-inventory-api
- collection_type: open
  name: MarketCheck Cars Dealer Listings API
  slug: open-marketcheck-listings-api
- collection_type: open
  name: MarketCheck Cars Dealer Market API
  slug: open-marketcheck-market-api
- collection_type: open
  name: MarketCheck Cars Dealer VIN Decoder API
  slug: open-marketcheck-vin-decoder-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marketcheck-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketcheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marketcheck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.marketcheck.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/MarketcheckCarsInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marketcheckdata
- group: company
  title: ''
  type: Blog
  url: https://www.marketcheck.com/category/automotive-api/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marketcheck.com/apis/pricing/
- group: other
  title: ''
  type: X
  url: https://x.com/MarketCheckCars
- group: commercial
  title: ''
  type: Plans
  url: plans/marketcheck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketcheck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marketcheck-finops.yml
created: '2026-06-13'
description: MarketCheck is an automotive market data platform providing REST APIs for accessing new and used vehicle listings, VIN decoding, market valuations, dealer inventory, and vehicle history data. The platform aggregates billions of data points from over 44,000 US and 3,500 Canadian dealerships, offering daily-updated inventory search, price prediction, market days supply, OEM incentives, auction listings, and third-party integrations for recalls, title checks, and plate-to-VIN lookups.
examples:
- key_count: 3
  name: Search Response Example
  slug: search-response-example
- key_count: 16
  name: Vin Decode Response Example
  slug: vin-decode-response-example
finops:
- name: Marketcheck Finops
  service_category: ''
  slug: marketcheck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketcheck.png
json_schemas:
- name: MarketCheck Listing
  property_count: 25
  slug: marketcheck-listing
- name: MarketCheck Search Response
  property_count: 4
  slug: marketcheck-search-response
jsonld:
- class_count: 9
  name: Marketcheck Context
  property_count: 68
  slug: marketcheck-context
layout: provider
modified: '2026-06-13'
name: MarketCheck
nav: Providers
network: true
overview: 'MarketCheck publishes 10 APIs on the [APIs.io](https://apis.io/) network, including VIN Decoder API, Dealer API, and 8 more. Tagged areas include Automotive, Vehicle Data, VIN Decoder, Car Inventory, and Market Data.


  The MarketCheck catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MarketCheck''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Marketcheck Plans Pricing
  plan_count: 4
  slug: marketcheck-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Marketcheck Rate Limits
  slug: marketcheck-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: MarketCheck API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: marketcheck-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  delta: -7.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 2.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/marketcheck/refs/heads/main/screenshots/marketcheck-2026-06-20T184954.png
security:
- kind: domain-security
  name: Marketcheck Domain Security
  slug: marketcheck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: marketcheck
tags:
- Automotive
- Vehicle Data
- VIN Decoder
- Car Inventory
- Market Data
- Dealer Inventory
- Vehicle Valuation
- Vehicle History
- Price Analytics
- Automotive Intelligence
website: https://www.marketcheck.com/
---
