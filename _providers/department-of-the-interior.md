---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Department Of The Interior Agentic Access
  operation_count: 11
  slug: department-of-the-interior-agentic-access
  summary_line: 11 operations
api_count: 3
apis:
- description: Department-wide open-data catalog at data.doi.gov, including datasets from all Interior bureaus.
  name: DOI Open Data Catalog
  slug: doi-open-data
- description: U.S. Fish and Wildlife Service data on listed species under the Endangered Species Act and the National Wildlife Refuge System.
  name: USFWS Environmental Conservation Online System (ECOS) API
  slug: usfws-environmental-conservation-api
- description: Reclamation reservoir, dam, and water-operations data for the western United States.
  name: Bureau of Reclamation Water Data
  slug: bor-water-data
- description: Office of Natural Resources Revenue datasets on royalty, rent, and bonus revenue from federal energy and mineral production.
  name: ONRR Natural Resources Revenue Data
  slug: onrr-revenue-data
- description: Park alerts and emergencies
  name: Department of the Interior Alerts API
  slug: department-of-the-interior-alerts-api
- description: News articles and releases
  name: Department of the Interior Articles API
  slug: department-of-the-interior-articles-api
- description: Campground listings
  name: Department of the Interior Campgrounds API
  slug: department-of-the-interior-campgrounds-api
- description: Event count queries
  name: Department of the Interior Counts API
  slug: department-of-the-interior-counts-api
- description: Daily statistical values
  name: Department of the Interior DailyValues API
  slug: department-of-the-interior-dailyvalues-api
- description: Park events
  name: Department of the Interior Events API
  slug: department-of-the-interior-events-api
- description: Real-time instantaneous values
  name: Department of the Interior InstantaneousValues API
  slug: department-of-the-interior-instantaneousvalues-api
- description: National parks
  name: Department of the Interior Parks API
  slug: department-of-the-interior-parks-api
- description: Water-monitoring sites
  name: Department of the Interior Sites API
  slug: department-of-the-interior-sites-api
- description: Visitor centers
  name: Department of the Interior VisitorCenters API
  slug: department-of-the-interior-visitorcenters-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: National Park Service (NPS) Data Alerts API
  slug: open-department-of-the-interior-alerts-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Articles API
  slug: open-department-of-the-interior-articles-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Campgrounds API
  slug: open-department-of-the-interior-campgrounds-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Counts API
  slug: open-department-of-the-interior-counts-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts DailyValues API
  slug: open-department-of-the-interior-dailyvalues-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Events API
  slug: open-department-of-the-interior-events-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts InstantaneousValues API
  slug: open-department-of-the-interior-instantaneousvalues-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Parks API
  slug: open-department-of-the-interior-parks-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts Sites API
  slug: open-department-of-the-interior-sites-api
- collection_type: open
  name: National Park Service (NPS) Data Alerts VisitorCenters API
  slug: open-department-of-the-interior-visitorcenters-api
- collection_type: open
  name: National Park Service (NPS) Data API
  slug: open-nps-data-api
- collection_type: open
  name: USGS Earthquake Hazards Program API
  slug: open-usgs-earthquake-api
- collection_type: open
  name: USGS Water Services API
  slug: open-usgs-water-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/department-of-the-interior-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/department-of-the-interior-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/department-of-the-interior-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doi-open-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/department-of-the-interior
- group: start
  title: ''
  type: Portal
  url: https://www.doi.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.doi.gov/developer
- group: other
  title: ''
  type: Datasets
  url: https://data.doi.gov/
created: '2024-12-25'
description: The U.S. Department of the Interior manages federal lands, water, wildlife, energy and mineral resources, and trust responsibilities to American Indian, Alaska Native, and insular communities. Interior bureaus - National Park Service, U.S. Geological Survey, Bureau of Land Management, U.S. Fish and Wildlife Service, Bureau of Reclamation, Bureau of Indian Affairs, and the Office of Natural Resources Revenue - publish a number of public APIs and open-data portals.
examples:
- key_count: 4
  name: Earthquake Example
  slug: earthquake-example
- key_count: 4
  name: Park Example
  slug: park-example
finops:
- name: Department Of The Interior Finops
  service_category: Federal Government / Public Open Data
  slug: department-of-the-interior-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
json_schemas:
- name: USGS Earthquake Feature
  property_count: 4
  slug: earthquake-feature
- name: National Park
  property_count: 16
  slug: nps-park
jsonld:
- class_count: 0
  name: Doi Context
  property_count: 4
  slug: doi-context
layout: provider
modified: '2026-07-25'
name: Department of the Interior
nav: Providers
network: true
overview: 'Department of the Interior publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Articles API, Campgrounds API, and 7 more. Tagged areas include Federal-Government, Public Lands, Natural Resources, and Geospatial.


  The Department of the Interior catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Department of the Interior''s developer surface includes authentication, developer portal, documentation, and 5 more developer resources.'
plans:
- name: Department Of The Interior Plans Pricing
  plan_count: 1
  slug: department-of-the-interior-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Department Of The Interior Rate Limits
  slug: department-of-the-interior-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Department of the Interior API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: department-of-the-interior-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: Department of the Interior API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: doi-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 58.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 31.0
    discoverability: 55.6
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/department-of-the-interior/refs/heads/main/screenshots/department-of-the-interior-2026-06-20T175924.png
security:
- kind: authentication
  name: Department Of The Interior Authentication
  slug: department-of-the-interior-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Department Of The Interior Domain Security
  slug: department-of-the-interior-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: department-of-the-interior
tags:
- Federal-Government
- Public Lands
- Natural Resources
- Geospatial
website: https://www.doi.gov/
---
