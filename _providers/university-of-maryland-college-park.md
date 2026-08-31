---
access_model:
  confidence: high
  label: Free; library and repository reads keyless, campus GIS services token-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: API middleware operated by the University of Maryland Libraries that exposes today's open/closed status, current bookable-space availability, and raw LibCal space records for five UMD library location
  name: UMD Libraries Website Tools API
  slug: libraries-website-tools
- description: OAI-PMH 2.0 harvesting endpoint over UMD Libraries' Fedora-backed digital collections. Identify reports repositoryName "UMD Libraries" and adminEmail lib-ssdr@umd.edu, with records back to 2014. ListS
  name: UMD Libraries Digital Collections OAI-PMH
  slug: digital-collections-oai
- description: 'The Libraries'' Avalon Media System deployment for audio and video collections, with an OAI-PMH 2.0 endpoint (repositoryName "UMD Libraries", adminEmail lib-dpi@umd.edu), an OpenSearch 1.1 descriptor, '
  name: UMD Libraries Audio/Video Collections OAI-PMH and OpenSearch
  slug: av-collections-oai
- description: OAI-PMH 2.0 endpoint over the Libraries' ArchivesSpace instance, exposing finding aids for Special Collections and the Performing Arts collections. Identify reports adminEmail aspace-oai@umd.edu and a
  name: UMD Archival Collections OAI-PMH
  slug: archival-collections-oai
- description: The university's own Shibboleth identity provider, publishing a SAML 2.0 EntityDescriptor as InCommon entity urn:mace:incommon:umd.edu with scope umd.edu, the InCommon and REFEDS Research and Scholars
  name: UMD Shibboleth Identity Provider — SAML 2.0 Metadata
  slug: identity-federation
- description: 'IIIF Image and Presentation services operated by UMD Libraries — a Cantaloupe 5.0.5 image server and Papaya 1.2.0, the Libraries'' own IIIF Presentation API application, behind a shared service index. '
  name: UMD Libraries IIIF Services
  slug: iiif-services
- description: The university's own ArcGIS Enterprise deployment — ArcGIS Server 12.1.0 and Portal 2026.1 at gis.umd.edu — and the machine-readable backend behind the official campus map at maps.umd.edu. The service
  name: UMD Enterprise GIS — ArcGIS REST Services
  slug: enterprise-gis
- description: UMD Libraries' DSpace 7 institutional repository of UMD scholarship and research data, and the university's DOI-minting surface. UMD Libraries document a DSpace REST API, an OAI-PMH 2.0 endpoint and a
  name: DRUM — Digital Repository at the University of Maryland
  slug: drum
- description: The Office of the Registrar's public Schedule of Classes, a server-rendered web application for browsing course offerings by term and department. It is the authoritative UMD course surface and it is n
  name: Testudo Schedule of Classes
  slug: testudo-soc
- description: 'A read-only REST API over UMD course, section, professor, campus bus, building/map and major data, covering ground the university itself does not expose programmatically. It is not UMD''s. The project '
  name: umd.io — student-run University of Maryland data API
  slug: umd-io
- description: UMD's library catalog and discovery layer, delivered as Ex Libris Primo through the University System of Maryland and Affiliated Institutions (USMAI) consortium. The search experience, its APIs and it
  name: UMD Discover — library discovery layer
  slug: umd-discover
- description: UMD Libraries' web archiving programme, operated as Archive-It organization 408 at the Internet Archive. UMD Libraries document Archive-It's OpenSearch interface as an access route to their collection
  name: UMD Web Archives on Archive-It
  slug: archive-it
- description: The University of Maryland, College Park collection at the Internet Archive, documented by UMD Libraries as one of their ten Open Data services with archive.org's advancedsearch.php given as the query
  name: UMD Collection on the Internet Archive
  slug: internet-archive
- description: UMD Libraries refer researchers to Dryad for open research-data deposit and document Dryad's v2 REST API as the access route, scoped to UMD by ROR identifier https://ror.org/047s2c258. The datasets an
  name: UMD Research Data on Dryad
  slug: dryad
- description: The Big Ten Academic Alliance Geoportal, a consortium-operated discovery layer for geospatial data to which UMD Libraries contribute records. Operated by the BTAA at geo.btaa.org, not by UMD.
  name: BTAA Geoportal — UMD geospatial contributions
  slug: btaa-geoportal
- description: UMD's learning management system, an Instructure Canvas tenancy at umd.instructure.com fronted by elms.umd.edu. Requests to the tenancy redirect to UMD's own Shibboleth identity provider, which is wha
  name: ELMS-Canvas — UMD learning management system
  slug: elms-canvas
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://www.umd.edu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opendata.lib.umd.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://opendata.lib.umd.edu/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://opendata.lib.umd.edu/services/
- group: other
  title: ''
  type: OpenData
  url: https://opendata.lib.umd.edu/datasets/
- group: other
  title: ''
  type: OpenData
  url: https://opendata.umd.edu
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opendata.lib.umd.edu/services/umd-discover/
- group: other
  title: ''
  type: ResearchRepository
  url: https://opendata.lib.umd.edu/services/drum/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://app.testudo.umd.edu/soc/
- group: other
  title: ''
  type: IdentityFederation
  url: https://shib.idm.umd.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpcc.umd.edu
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.umd.edu/resources-guidelines/guidelines-for-use
- group: build
  title: ''
  type: AITooling
  url: https://terpai.umd.edu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/umd-lib
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://umd.edu/privacy-notice
- group: other
  title: ''
  type: Accessibility
  url: https://umd.edu/web-accessibility
- group: operate
  title: ''
  type: Support
  url: https://opendata.lib.umd.edu/contact/
- group: company
  title: ''
  type: Blog
  url: https://today.umd.edu/rss
- group: company
  title: ''
  type: BlogRSS
  url: https://opendata.lib.umd.edu/index.xml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-maryland/
- group: other
  title: ''
  type: Research
  url: https://research.umd.edu
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-maryland-college-park-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-maryland-college-park-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-maryland-college-park-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-maryland-college-park-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-maryland-college-park-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-maryland-college-park-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-maryland-college-park-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-maryland-college-park-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-maryland-college-park-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Maryland, College Park (UMD) is the flagship public research university of the University System of Maryland and the state''s original 1862 land-grant institution. UMD operates no central developer portal and publishes no university-wide API programme. Its entire confirmed programmable footprint is run by three offices. UMD Libraries publish an Open Data site at opendata.lib.umd.edu documenting the interfaces they operate: a keyless FastAPI service for library hours and bookable-space availability, three live OAI-PMH 2.0 endpoints over digital collections, audio/video collections and ArchivesSpace finding aids, an OpenSearch descriptor over the Avalon A/V catalog, and IIIF Image and Presentation servers. The Division of IT operates the university''s Shibboleth identity provider, which publishes SAML 2.0 metadata as InCommon entity urn:mace:incommon:umd.edu with the Research and Scholarship category and SIRTFI assurance — the most consequential machine-readable
  contract UMD runs, and one no vendor catalogues. The campus GIS office runs an ArcGIS Enterprise 12.1 deployment at gis.umd.edu whose REST service catalog, server info and portal endpoints answer keyless JSON while the fourteen service folders beneath them require a token — the machine-readable backend of the official campus map, and undocumented outside the map itself. Everything else that looks like a UMD API is somebody else''s engineering. umd.io, the widely cited course, bus and campus-map API, is a student-run independent project on a NameCheap-registered .io domain hosted at DigitalOcean that states plainly it is not the school; the library discovery layer is Ex Libris Primo through the USMAI consortium; the LMS is Instructure Canvas; web archiving is Archive-It; the open-data repository referral is Dryad. Those are recorded here as tenant relationships, not as UMD''s contracts. The DRUM institutional repository is genuinely UMD-operated and was serving a maintenance page across
  every one of its hosts throughout this review.'
examples:
- key_count: 9
  name: University Of Maryland College Park Art Details Example
  slug: university-of-maryland-college-park-art-details-example
- key_count: 9
  name: University Of Maryland College Park Mckeldin Availability Example
  slug: university-of-maryland-college-park-mckeldin-availability-example
- key_count: 9
  name: University Of Maryland College Park Mckeldin Hours Today Example
  slug: university-of-maryland-college-park-mckeldin-hours-today-example
- key_count: 9
  name: University Of Maryland College Park Stem Availability Example
  slug: university-of-maryland-college-park-stem-availability-example
finops:
- name: University Of Maryland College Park Finops
  service_category: Education
  slug: university-of-maryland-college-park-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-maryland-college-park.png
json_schemas:
- name: UMD Libraries today's open status
  property_count: 2
  slug: university-of-maryland-college-park-hours-today
- name: UMD Libraries space availability
  property_count: 2
  slug: university-of-maryland-college-park-space-availability
- name: UMD Libraries raw space records
  property_count: 0
  slug: university-of-maryland-college-park-space-details
layout: provider
modified: '2026-08-30'
name: University of Maryland College Park
nav: Providers
network: true
overview: 'University of Maryland College Park publishes 1 API on the [APIs.io](https://apis.io/) network: UMD Libraries Website Tools API. Tagged areas include University, Higher Education, Education, United States, and Maryland.


  The University of Maryland College Park catalog on APIs.io includes 1 Spectral governance ruleset.


  University of Maryland College Park''s developer surface includes API reference, documentation, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: University Of Maryland College Park Plans Pricing
  plan_count: 2
  slug: university-of-maryland-college-park-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: University Of Maryland College Park Rate Limits
  slug: university-of-maryland-college-park-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: University of Maryland College Park API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: university-of-maryland-college-park-rules
scopes:
- name: University Of Maryland College Park Scopes
  scope_count: 0
  slug: university-of-maryland-college-park-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 11.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 7.6
    contract_quality: 55.1
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 7.6
    operational_transparency: 23.7
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-maryland-college-park/refs/heads/main/screenshots/university-of-maryland-college-park-2026-06-20T200223.png
security:
- kind: authentication
  name: University Of Maryland College Park Authentication
  slug: university-of-maryland-college-park-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Maryland College Park Domain Security
  slug: university-of-maryland-college-park-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-maryland-college-park
tags:
- University
- Higher Education
- Education
- United States
- Maryland
- Public Research University
- Land Grant
- Big Ten
- Library
- Research Data
- Digital Collections
- Identity Federation
- OAI-PMH
- Open Data
- Geospatial
website: https://www.umd.edu
---
