---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-03'
api_count: 4
apis:
- baseURL: https://geoservices.tamu.edu/Api/Geocode/V5/
  baseurl_source: declared
  description: Free geocoding, address normalisation and standardisation, census intersection and reverse geocoding from Texas A&M GeoServices. Version 5.0.0 returns up to 172 output fields; an API key from a free s
  name: Texas A&M GeoServices Geocoding API
  slug: geoservices-geocode
- baseURL: https://api.aggiemap.tamu.edu
  baseurl_source: declared
  description: Read-only GeoJSON feed of Texas A&M campus dining locations with live open/closed state, status message, street address and an occupancy signal, served from the university's own Aggie Map backend. Ver
  name: Aggie Map Dining Locations API
  slug: aggiemap-dining
- baseURL: https://veoride.geoservices.tamu.edu
  baseurl_source: declared
  description: Live positions of shared micromobility vehicles on and around campus as GeoJSON, served from veoride.geoservices.tamu.edu inside Texas A&M's own geoservices estate. Verified 200 on 2026-09-01 returnin
  name: Campus Micromobility Vehicle Positions API
  slug: campus-micromobility
- description: Public Esri ArcGIS Server operated by Texas A&M IT, serving campus base maps, ADA routes, construction, department search, transit lots, bike maps and event pedestrian/vehicle flow layers. The service
  name: Texas A&M IT ArcGIS REST Services
  slug: gis-arcgis-rest
- description: 'OAI-PMH 2.0 harvesting endpoint for OAKTrust, the Texas A&M University Libraries institutional repository. Verified 200 on 2026-09-01: repositoryName "OAKTrust", repositoryIdentifier oaktrust.library.'
  name: OAKTrust Institutional Repository — OAI-PMH
  slug: oaktrust-oaipmh
- baseURL: https://idp.tamu.edu/idp/shibboleth
  baseurl_source: declared
  description: SAML 2.0 metadata for Texas A&M University's own Shibboleth Identity Provider, published unauthenticated from idp.tamu.edu. Verified 200 with content-type application/xml on 2026-09-01; the entityID s
  name: Texas A&M Shibboleth Identity Provider Metadata
  slug: identity-federation
- description: Texas A&M University's registration in the InCommon identity federation, resolvable through InCommon's per-entity Metadata Query service under entityID urn:mace:incommon:tamu.edu. Verified 200 as appl
  name: InCommon Federation Registration
  slug: incommon-registration
- description: 'Texas A&M University System enterprise API to search, verify, create and update Universal Identification Numbers. Gated: access requires registering an application, subscribing to UIN Proxy Services v'
  name: UIN Services API
  slug: uin-services
- description: The Texas A&M academic catalog runs on Leepfrog CourseLeaf at catalog.tamu.edu. Its machine-readable course-detail route answered 200 as text/xml on 2026-09-01 for /ribbit/?page=getcourse.rjs&code=ENG
  name: Texas A&M Course Catalog (CourseLeaf)
  slug: course-catalog
- description: 'Texas A&M''s learning management system is Instructure Canvas: canvas.tamu.edu is a CNAME to texasam-vanity.instructure.com. The tenancy is a real institutional fact and is recorded here; the Canvas RE'
  name: Canvas Learning Management System (tenancy)
  slug: canvas-lms
- description: Texas A&M Libraries is a DataCite consortium organization (provider CXAU) whose record carries Texas A&M University's own ROR id, https://ror.org/01f5ytq51, and which owns the repository client TDL.TA
  name: DataCite Registrant — Texas A&M Libraries
  slug: datacite-membership
- description: Texas A&M University Libraries is Crossref member 14385, holding DOI prefix 10.21423 with 7,464 registered DOIs (706 current, 6,758 backfile) as of 2026-09-01. The same prefix is registered at DataCit
  name: Crossref Member — Texas A&M University Libraries
  slug: crossref-membership
- description: 'Texas A&M University is registered in the Research Organization Registry as https://ror.org/01f5ytq51, with domain tamu.edu, established 1876, types education and funder, and cross-references to GRID '
  name: ROR Registration
  slug: ror-registration
artifact_total: 26
common:
- group: company
  title: ''
  type: Website
  url: https://www.tamu.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-doc.sea.system.tamus.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://geoservices.tamu.edu/Services/Geocode/WebService/Details/
- group: docs
  title: ''
  type: APIReference
  url: https://it.tamus.edu/uinmanager/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geoservices.tamu.edu/About/Legal/TermsOfUse.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tamu.edu/statements/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://it.tamu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tamu-edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/tamu-edu
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TAMULib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/texas-a-m-university/
- group: other
  title: ''
  type: ResearchRepository
  url: https://oaktrust.library.tamu.edu/server/oai/request?verb=Identify
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.tamu.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.tamu.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Atamu.edu
- group: other
  title: ''
  type: ResearchComputing
  url: https://hprc.tamu.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.tamu.edu/teach-with-ai/use-guidelines-and-ethics.html
- group: build
  title: ''
  type: AITooling
  url: https://it.tamu.edu/ai-services/index.html
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/texas-a-m-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/texas-a-m-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/texas-a-m-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/texas-a-m-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/texas-a-m-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/texas-a-m-university-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/texas-a-m-university-errors.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/texas-a-m-university-domain-standards.yml
created: '2026-06-03'
description: 'Texas A&M University is a public land-grant research university in College Station, Texas, the flagship of the Texas A&M University System, and ranked #154 in the QS World University Rankings 2025. Unlike most institutions in this cohort it is not a pure buyer: several of the surfaces recorded here are Texas A&M''s own engineering on Texas A&M''s own hosts, and each one below was fetched and given a status code before it was written down. The genuinely institution-operated tier is four contracts wide. Texas A&M GeoServices (geoservices.tamu.edu) publishes a documented, free, self-service geocoding and address normalisation API at version 5.0.0 that returns up to 172 output fields — a research product of the university''s geospatial group and the strongest institution-authored API in the higher-education catalog. The Aggie Map application backend (api.aggiemap.tamu.edu) serves campus dining locations with live open/closed state as GeoJSON, and a companion feed on geoservices.tamu.edu
  serves live shared-micromobility vehicle positions; both are undocumented, unauthenticated backends rather than offered products, and are recorded as such. Texas A&M IT runs a public Esri ArcGIS Server (gis.it.tamu.edu, mirrored at gis.tamu.edu) whose services directory answers anonymously across seven folders of campus base maps, construction, transit and event-flow layers. Two further institution-operated surfaces are protocol surfaces rather than REST APIs. The university''s Shibboleth Identity Provider publishes SAML 2.0 metadata unauthenticated from idp.tamu.edu and is registered in InCommon as urn:mace:incommon:tamu.edu, which carries it into eduGAIN — the surface class this cohort was most completely missing. The OAKTrust institutional repository exposes a working OAI-PMH 2.0 endpoint whose Identify response names Texas A&M Libraries'' own help desk and no vendor at all, which is rare in this cohort. Against that, the enterprise tier is closed. The Texas A&M University System API
  Developer Portal (api-doc.sea.system.tamus.edu) is live but renders nothing without a sponsored System account; the UIN Services API is documented in prose and gated behind subscription approval by the System Enterprise Applications DevOps group, so no base URL and no specification is published. There is no open-data portal — data.tamu.edu resolves in DNS but every HTTPS connection times out — no llms.txt, and no student-facing course or registrar API. The course catalog is a Leepfrog CourseLeaf tenancy and the LMS is an Instructure Canvas tenancy; both are real relationships and neither is Texas A&M''s contract. Texas A&M Libraries holds DOI prefix 10.21423 as a registrant at both DataCite and Crossref, and the university carries ROR id 01f5ytq51.'
examples:
- key_count: 2
  name: Texas A M University Arcgis Services Catalog Example
  slug: texas-a-m-university-arcgis-services-catalog-example
- key_count: 3
  name: Texas A M University Dining Locations Geojson Example
  slug: texas-a-m-university-dining-locations-geojson-example
- key_count: 2
  name: Texas A M University Geocode Apikeymissing Example
  slug: texas-a-m-university-geocode-apikeymissing-example
- key_count: 3
  name: Texas A M University Micromobility Vehicles Geojson Example
  slug: texas-a-m-university-micromobility-vehicles-geojson-example
finops:
- name: Texas A M University Finops
  service_category: Education
  slug: texas-a-m-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/texas-a-m-university.png
json_schemas:
- name: Texas A&M Aggie Map Dining Location
  property_count: 2
  slug: texas-a-m-university-dining-location
- name: Texas A&M Campus Micromobility Vehicle Positions
  property_count: 2
  slug: texas-a-m-university-micromobility-vehicles
jsonld:
- class_count: 11
  name: Texas A M University Context
  property_count: 0
  slug: texas-a-m-university-context
layout: provider
modified: '2026-09-01'
name: Texas A&M University
nav: Providers
network: true
overview: 'Texas A&M University publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Texas A&M GeoServices Geocoding API, Aggie Map Dining Locations API, Campus Micromobility Vehicle Positions API, and 1 more. Tagged areas include University, Higher Education, Education, United States, and Texas.


  The Texas A&M University catalog on APIs.io includes 1 JSON-LD context.


  Texas A&M University''s developer surface includes documentation, API reference, support, GitHub presence, and 23 more developer resources.'
plans:
- name: Texas A M University Plans Pricing
  plan_count: 2
  slug: texas-a-m-university-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Texas A M University Rate Limits
  slug: texas-a-m-university-rate-limits
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 44.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/texas-a-m-university/refs/heads/main/screenshots/texas-a-m-university-2026-06-20T195203.png
security:
- kind: authentication
  name: Texas A M University Authentication
  slug: texas-a-m-university-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Texas A M University Domain Security
  slug: texas-a-m-university-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Texas A M University Vulnerability Disclosure
  slug: texas-a-m-university-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: texas-a-m-university
tags:
- University
- Higher Education
- Education
- United States
- Texas
- Public Research University
- Land Grant
- Research
- Research Data
- Research Repository
- Identity Federation
- Geospatial
- Geocoding
- Open Data
- Library
- Course Catalog
- Campus Life
- Research Computing
website: https://www.tamu.edu
---
