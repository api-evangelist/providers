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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bonneville Power Administration Agentic Access
  operation_count: 8
  slug: bonneville-power-administration-agentic-access
  summary_line: 8 operations
api_count: 2
apis:
- description: The BPA GIS Data Hub provides publicly available geospatial data from Bonneville Power Administration. The hub is built on ArcGIS and supports data downloads in multiple formats including CSV, KML, Ge
  name: BPA GIS Data Hub API
  slug: gis-data-api
- description: BPA publishes real-time and historical wind and solar generation data for the Balancing Authority area. Data includes total wind generation, total solar generation, net generation, and load data avail
  name: BPA Wind and Solar Generation Data
  slug: wind-solar-data
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: declared
  description: The Customers API from Bonneville Power Administration — 3 operation(s) for customers.
  name: Bonneville Power Administration Customers API
  slug: bonneville-power-administration-customers-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: declared
  description: The Hydrology API from Bonneville Power Administration — 1 operation(s) for hydrology.
  name: Bonneville Power Administration Hydrology API
  slug: bonneville-power-administration-hydrology-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: declared
  description: The Right of Way API from Bonneville Power Administration — 1 operation(s) for right of way.
  name: Bonneville Power Administration Right of Way API
  slug: bonneville-power-administration-right-of-way-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: declared
  description: The Service Area API from Bonneville Power Administration — 1 operation(s) for service area.
  name: Bonneville Power Administration Service Area API
  slug: bonneville-power-administration-service-area-api
- baseURL: https://services3.arcgis.com/Iz3chmSt4P7oOoZy/arcgis/rest
  baseurl_source: declared
  description: The Transmission API from Bonneville Power Administration — 2 operation(s) for transmission.
  name: Bonneville Power Administration Transmission API
  slug: bonneville-power-administration-transmission-api
- baseURL: https://data-bpagis.hub.arcgis.com
  baseurl_source: declared
  description: BPA's ArcGIS Hub site publishes a real OGC API Records catalog search over the agency's open geospatial data — 17 operations across collections, items, queryables, related and connected records, aggre
  name: Bonneville Power Administration Data Search API
  slug: bonneville-power-administration-data-search-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers API
  slug: open-bonneville-power-administration-customers-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Hydrology API
  slug: open-bonneville-power-administration-hydrology-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Right of Way API
  slug: open-bonneville-power-administration-right-of-way-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Service Area API
  slug: open-bonneville-power-administration-service-area-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub Customers Transmission API
  slug: open-bonneville-power-administration-transmission-api
- collection_type: open
  name: Bonneville Power Administration GIS Hub API
  slug: open-bonneville-power-administration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bonneville-power-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bonneville-power-administration-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bpa.gov/rss-feeds/news-feed-no-cp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bonnevillepower
- group: company
  title: ''
  type: Website
  url: https://www.bpa.gov
- group: company
  title: ''
  type: About
  url: https://www.bpa.gov/about/
- group: other
  title: ''
  type: OpenData
  url: https://data-bpagis.hub.arcgis.com
- group: other
  title: ''
  type: DataDownload
  url: https://transmission.bpa.gov/business/operations/Wind/
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.bpa.gov/energy-and-services/
- group: operate
  title: ''
  type: Contact
  url: https://www.bpa.gov/about/who-we-are/contact-form
- group: auth
  title: ''
  type: Authentication
  url: authentication/bonneville-power-administration-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bonneville-power-administration-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bonneville-power-administration-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bonneville-power-administration-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bonneville-power-administration-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bonneville-power-administration-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bonneville-power-administration-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bonneville-power-administration-mcp.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bonneville-power-administration-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bonneville-power-administration-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bonneville-power-administration-finops.yml
- group: auth
  title: ''
  type: Security
  url: security/bonneville-power-administration-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bonneville-power-administration-vulnerability-disclosure.yml
- group: other
  title: ''
  type: DataCatalog
  url: https://data-bpagis.hub.arcgis.com/data.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bonneville-power-administration-dcat-us-catalog.json
- group: docs
  title: ''
  type: Documentation
  url: https://data-bpagis.hub.arcgis.com
- group: docs
  title: ''
  type: APIReference
  url: https://data-bpagis.hub.arcgis.com/api/search/definition/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bpa.gov/about/who-we-are/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.bpa.gov/about/who-we-are/contact-form
created: '2024-11-25'
description: The Bonneville Power Administration (BPA) is a federal agency within the U.S. Department of Energy that markets wholesale electrical power from federal hydroelectric projects in the Pacific Northwest. BPA also operates and maintains about three-quarters of the high-voltage transmission in the Pacific Northwest. The agency provides publicly available GIS data, energy statistics, and operational data through its data hub and web services.
features:
- features:
  - ArcGIS REST API
  - GeoJSON Export
  - CSV Export
  - KML Export
  - GeoTIFF Export
  - Web Map Service (WMS)
  - Web Feature Service (WFS)
  name: GeoServices API
  url: https://data-bpagis.hub.arcgis.com
- features:
  - CSV Download
  - JSON Download
  - GeoJSON Download
  - Shapefile Download
  - KML Download
  name: Open Data Downloads
  url: https://data-bpagis.hub.arcgis.com
finops:
- name: Bonneville Power Administration Finops
  service_category: API
  slug: bonneville-power-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bonneville-power-administration.png
layout: provider
modified: '2026-09-06'
name: Bonneville Power Administration
nav: Providers
network: true
overview: 'Bonneville Power Administration publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Hydrology API, Right of Way API, and 3 more. Tagged areas include Energy, Federal-Government, GIS, Hydroelectric, and Pacific Northwest.


  Bonneville Power Administration''s developer surface includes engineering blog, authentication, documentation, API reference, support, and 25 more developer resources.'
plans:
- name: Bonneville Power Administration Plans Pricing
  plan_count: 0
  slug: bonneville-power-administration-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Bonneville Power Administration Rate Limits
  slug: bonneville-power-administration-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 47.1
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 54.1
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/bonneville-power-administration/refs/heads/main/screenshots/bonneville-power-administration-2026-06-20T173608.png
security:
- kind: authentication
  name: Bonneville Power Administration Authentication
  slug: bonneville-power-administration-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bonneville Power Administration Domain Security
  slug: bonneville-power-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bonneville Power Administration Vulnerability Disclosure
  slug: bonneville-power-administration-vulnerability-disclosure
  summary_line: Hackerone
slug: bonneville-power-administration
tags:
- Energy
- Federal-Government
- GIS
- Hydroelectric
- Pacific Northwest
- Power
- Transmission
- Wind
use_cases:
- features:
  - Geospatial Data Download
  - Map Visualization
  - Service Area Data
  - Transmission Infrastructure Mapping
  - Energy Facility Locations
  name: GIS Data Analysis
  url: https://data-bpagis.hub.arcgis.com
- features:
  - Wind Generation Data
  - Solar Generation Data
  - Real-Time Generation Monitoring
  - Historical Data Access
  - Grid Load Tracking
  name: Renewable Energy Monitoring
  url: https://transmission.bpa.gov/business/operations/Wind/
- features:
  - Transmission Availability
  - Hourly Firm Data
  - System Load Monitoring
  - Grid Operations Data
  name: Transmission System Monitoring
  url: https://www.bpa.gov/energy-and-services/transmission/
website: https://www.bpa.gov
---
