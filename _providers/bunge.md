---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: 'Bunge operates customer-facing portals for industrial and food-service customers to manage orders, contracts, shipment tracking, and account information for oilseed, grain, and oil product purchases. '
  name: Bunge Customer Portal
  slug: bunge-customer-portal
- description: Bunge operates digital tools for grain origination relationships with farmers, enabling contract management, pricing, scale-ticket access, and settlement information for delivered grain. Access is res
  name: Bunge Farmer Portal
  slug: bunge-farmer-portal
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bunge-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bunge
- group: company
  title: ''
  type: Website
  url: https://www.bunge.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.bunge.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.bunge.com/sustainability
created: '2026-05-05'
description: Bunge Global SA is a multinational agribusiness and food company connecting farmers to consumers by sourcing, processing, and supplying oilseed and grain products. Operates across grain origination, oilseed processing, refined and specialty oils, milling, sugarcane and biofuel production, and fertilizer sales. In 2025 Bunge completed its merger with Viterra to create a major global agricultural trading and processing platform.
features:
- description: Sourcing oilseeds and grains from major growing regions worldwide.
  name: Grain Origination
- description: Crushing oilseeds to produce meal for livestock and oil for food and biofuels.
  name: Oilseed Processing
- description: Manufacturing bottled oils, margarines, and food-service oil products.
  name: Refined and Specialty Oils
- description: Wheat, corn, and rice milling for food and industrial customers.
  name: Milling
- description: Sugarcane processing for sugar and ethanol biofuel production.
  name: Sugar and Bioenergy
- description: Manufacturing and distributing fertilizer to South American farmers.
  name: Fertilizer
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bunge.png
integrations:
- description: 2025 merger combining Bunge and Viterra global grain trading operations.
  name: Viterra
- description: Subsidiary specialty oils and fats manufacturer for food industry.
  name: IOI Loders Croklaan
- description: Subsidiary supporting oilseed processing operations.
  name: Central Soya
- description: Specialty fats and margarine subsidiary.
  name: Walter Rau
layout: provider
modified: '2026-05-16'
name: Bunge
nav: Providers
network: true
overview: Bunge publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agribusiness, Food, Manufacturing, Commodities, and Oilseeds.
random_paper: 4
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bunge/refs/heads/main/screenshots/bunge-2026-06-20T173759.png
security:
- kind: domain-security
  name: Bunge Domain Security
  slug: bunge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bunge
tags:
- Agribusiness
- Food
- Manufacturing
- Commodities
- Oilseeds
- Grain
- Biofuels
use_cases:
- description: Supplying food manufacturers with vegetable oils, flour, and ingredients.
  name: Food Manufacturing Supply
- description: Providing oilseed meal to livestock and poultry feed producers.
  name: Animal Feed Supply
- description: Supplying oilseed-derived feedstock to biodiesel and renewable diesel producers.
  name: Biofuel Feedstock
- description: Trading grains globally between origin and destination markets.
  name: Grain Trading
- description: Bottled oils, margarines, and shortenings sold via retail brands.
  name: Consumer Cooking Oils
website: https://www.bunge.com/
---
