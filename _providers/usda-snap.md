---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Usda Snap Agentic Access
  operation_count: 3
  slug: usda-snap-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Query SNAP retailer location records.
  name: USDA SNAP Retailer Locator Retailers API
  slug: usda-snap-retailers-api
- description: Feature service and layer metadata.
  name: USDA SNAP Retailer Locator Service API
  slug: usda-snap-service-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SNAP Retailer Location Data Retailers API
  slug: open-usda-snap-retailers-api
- collection_type: open
  name: SNAP Retailer Location Data Retailers Service API
  slug: open-usda-snap-service-api
- collection_type: open
  name: USDA SNAP Retailer Location Data API
  slug: open-usda-snap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/usda-snap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/usda-snap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fna.usda.gov/snap/retailer-locator
- group: docs
  title: ''
  type: Documentation
  url: https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/usda-snap-rate-limits.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-03'
description: The USDA Food and Nutrition Administration (FNA) - renamed from the Food and Nutrition Service (FNS) on June 1, 2026 - publishes an open, public geospatial API for the Supplemental Nutrition Assistance Program (SNAP) Retailer Locator. The data is hosted as an Esri ArcGIS Feature Service (snap_retailer_location_data) rather than a bespoke fns.usda.gov or api.fns.usda.gov endpoint, and is embedded directly in the public retailer locator tool at fna.usda.gov/snap/retailer-locator. It exposes point-in-time location records - name, address, city, state, zip, county, store type, latitude/longitude, and Healthy Incentive Program participation - for every currently authorized SNAP retailer nationwide (roughly a quarter million records as of the review date), queryable anonymously over REST with no API key, in JSON, GeoJSON, or PBF, with CSV/Shapefile/KML export also available through the ArcGIS Hub item page. Data is refreshed on a recurring basis by FNA; the service is read-only (Query
  only - no write capabilities).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/usda-snap.png
layout: provider
modified: '2026-07-03'
name: USDA SNAP Retailer Locator
nav: Providers
network: true
overview: 'USDA SNAP Retailer Locator publishes 2 APIs on the [APIs.io](https://apis.io/) network: Retailers API and Service API. Tagged areas include SNAP, USDA, Food and Nutrition Administration, FNA, and FNS.


  USDA SNAP Retailer Locator''s developer surface includes documentation and 5 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 3
  name: Usda Snap Rate Limits
  slug: usda-snap-rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 24.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Usda Snap Domain Security
  slug: usda-snap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: usda-snap
tags:
- SNAP
- USDA
- Food and Nutrition Administration
- FNA
- FNS
- Retailer Locator
- Open Data
- ArcGIS
- GIS
- Government Data
- Food Assistance
website: https://www.fna.usda.gov/snap/retailer-locator
---
