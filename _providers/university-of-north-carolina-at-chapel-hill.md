---
access_model:
  confidence: high
  label: Free · keyless public read endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: Public, keyless JSON API behind the Carolina Digital Repository, UNC Libraries' institutional repository for digitized special collections, theses, dissertations and research output. GET /services/api
  name: Carolina Digital Repository Services API (box-c)
  slug: cdr-services-api
- description: The UNC University Library catalog answers machine-readable search over its full bibliographic index at /catalog.json, the Blacklight JSON response format, with query, search_field, facet and paginati
  name: UNC Libraries Catalog Search API (TRLN Discovery / Blacklight)
  slug: library-catalog-search
- description: 'Machine-readable search across the finding aids of the Wilson Special Collections Library, served at /catalog.json in Blacklight''s JSON:API form — a `links` object with self/next/last, a `meta.pages` '
  name: UNC Finding Aids Search API (Blacklight JSON:API)
  slug: finding-aids-search
- description: OAI-PMH 2.0 harvesting endpoint for the UNC Dataverse research data repository, operated by the Odum Institute / Institute for Research in Social Science. Identify reports repositoryName "UNC Datavers
  name: UNC Dataverse OAI-PMH Archive
  slug: dataverse-oai-pmh
- description: UNC's Onyen single sign-on is a Shibboleth Identity Provider that publishes SAML 2.0 metadata at its canonical /idp/shibboleth location — an EntityDescriptor with an IDPSSODescriptor and HTTP-POST, HT
  name: UNC Shibboleth Identity Provider (SAML 2.0 / InCommon)
  slug: shibboleth-idp
- description: REST API for the Space Planning and Occupancy Tracking System run by UNC Facilities Services, the campus system of record for building and room space data. The documentation page resolves (200) but it
  name: Facilities SPOTS REST API
  slug: facilities-spots
- description: UNC Dataverse, the Odum Institute's research data repository, runs Dataverse 6.8 and exposes the Dataverse Native REST API at /api. GET /api/info/version is keyless and returned {"version":"6.8","buil
  name: UNC Dataverse Native REST API (Dataverse deployment)
  slug: dataverse-native-api
- description: The University Catalog exposes a keyless JSON course-search API at /course-search/api/?page=fose&route=search. A POST carrying a criteria array returns {"srcdb","count","results":[{"key","code","srcdb
  name: UNC Catalog Course Search API (CourseLeaf)
  slug: course-catalog-search
- description: UNC-Chapel Hill's campus open-data site for geospatial and institutional datasets, published through ArcGIS Hub. The DCAT-US 1.1 catalog feed at /api/feed/dcat-us/1.1.json returned 48,189 bytes of app
  name: UNC GIS Open Data Hub (ArcGIS Hub DCAT-US)
  slug: gis-opendata
- description: '"Search the Special Collections", UNC University Library''s discovery layer over its digitized special collections. A WordPress front at the root fronts an OCLC CONTENTdm 6.10 installation that handles'
  name: UNC Digital Collections Search (OCLC CONTENTdm)
  slug: digital-collections
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.unc.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/UNC-Libraries/box-c
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UNC-Libraries
- group: other
  title: ''
  type: ResearchRepository
  url: https://dcr.lib.unc.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.unc.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.lib.unc.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.unc.edu/
- group: other
  title: ''
  type: OpenData
  url: https://gisdata-uncadmin.opendata.arcgis.com/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.unc.edu/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn:mace:incommon:unc.edu
- group: other
  title: ''
  type: ResearchComputing
  url: https://help.rc.unc.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.unc.edu/ai-guidance-for-faculty/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.unc.edu/staff-generative-ai-usage-guidance/
- group: build
  title: ''
  type: AITooling
  url: https://ai.unc.edu/tools/
- group: auth
  title: ''
  type: Authentication
  url: https://sso.unc.edu/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.unc.edu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unc.edu/about/privacy-statement/
- group: operate
  title: ''
  type: Support
  url: https://help.unc.edu/
- group: company
  title: ''
  type: Blog
  url: https://www.unc.edu/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/unc-chapel-hill/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-north-carolina-at-chapel-hill-education-standards-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-north-carolina-at-chapel-hill-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-north-carolina-at-chapel-hill-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-north-carolina-at-chapel-hill-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-north-carolina-at-chapel-hill-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of North Carolina at Chapel Hill is a public research university in Chapel Hill, North Carolina, a member of the Association of American Universities and the flagship of the seventeen-campus University of North Carolina System. It operates no central developer portal, no API gateway, and publishes no OpenAPI of its own — but it does run several genuinely institution-engineered machine-readable surfaces. The strongest is the Carolina Digital Repository services API at dcr.lib.unc.edu, including IIIF Presentation 3.0 and Image 3.0 endpoints, served by box-c, a repository application UNC Libraries writes and maintains in the open on GitHub. Alongside it are two Blacklight JSON search APIs on UNC''s own hardware (the TRLN Discovery library catalog and the Wilson Library finding aids), an OAI-PMH 2.0 archive on UNC Dataverse advertising DataCite metadata, and UNC''s own Shibboleth/InCommon SAML 2.0 metadata. The rest of the programmable footprint is tenant relationships
  rather than UNC engineering: the UNC Dataverse native REST API is the Dataverse product''s contract, the course-catalog search API is Leepfrog CourseLeaf''s, the GIS open-data hub is Esri ArcGIS Hub''s, and the Digital Collections search at dc.lib.unc.edu is OCLC CONTENTdm. The Facilities SPOTS REST API is institution-operated but its documentation is entirely Onyen-gated and could not be read.'
finops:
- name: University Of North Carolina At Chapel Hill Finops
  service_category: Education
  slug: university-of-north-carolina-at-chapel-hill-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-north-carolina-at-chapel-hill.png
layout: provider
modified: '2026-08-30'
name: University of North Carolina at Chapel Hill
nav: Providers
network: true
overview: 'University of North Carolina at Chapel Hill publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Public Research University, and United States.


  University of North Carolina at Chapel Hill''s developer surface includes documentation, authentication, support, engineering blog, and 22 more developer resources.'
plans:
- name: University Of North Carolina At Chapel Hill Plans Pricing
  plan_count: 2
  slug: university-of-north-carolina-at-chapel-hill-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: University Of North Carolina At Chapel Hill Rate Limits
  slug: university-of-north-carolina-at-chapel-hill-rate-limits
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 9.3
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-north-carolina-at-chapel-hill/refs/heads/main/screenshots/university-of-north-carolina-at-chapel-hill-2026-06-20T200208.png
security:
- kind: domain-security
  name: University Of North Carolina At Chapel Hill Domain Security
  slug: university-of-north-carolina-at-chapel-hill-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-north-carolina-at-chapel-hill
tags:
- Education
- Higher Education
- University
- Public Research University
- United States
- North Carolina
- University of North Carolina System
- Association of American Universities
- Research Data
- Open Data
- Digital Library
- Library
- Course Catalog
- Identity Federation
- Geospatial
- Open-Source
website: https://www.unc.edu/
---
