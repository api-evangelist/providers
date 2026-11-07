---
access_model:
  confidence: high
  label: Free · no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
  - '{''url'': ''https://one.ufl.edu/soc/'', ''status'': 301, ''note'': ''declared website redirects to https://one.uf.edu/soc/ — a different registrable domain (ufl.edu -> uf.edu), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The University of Florida's SAML 2.0 identity provider, entityID https://login.ufl.edu/idp/shibboleth, registered in InCommon and interfederated into eduGAIN. Signed SAML metadata is retrievable per-e
  name: UF Shibboleth Identity Provider (InCommon / eduGAIN)
  slug: identity-federation
- description: JSON datasets backing the UF interactive campus map — building footprints, bus stops, dining locations, parking lots and housing with coordinates and metadata. The host is UF's own (campusmap.ufl.edu,
  name: UF Campus Map JSON Data
  slug: campus-map
- description: The University of Florida George A. Smathers Libraries is a Crossref member, id 17357, depositing DOIs under prefix 10.32473 — 14,724 DOIs registered as of 2026-09-01. This is a registry membership, a
  name: Crossref Membership — UF George A. Smathers Libraries
  slug: crossref-membership
- description: The University of Florida's entry in the Research Organization Registry, https://ror.org/02y3ad647. A persistent identifier the institution is registered in, recorded as a membership fact. The ROR API
  name: ROR Registration — University of Florida
  slug: ror
- description: UF's learning management system is Canvas, running on Instructure's platform at the UF-specific tenant ufl.instructure.com. The Canvas REST API is present on that tenant and correctly returns HTTP 401
  name: UF Canvas LMS Tenancy
  slug: canvas-lms
- description: The UF academic catalog runs on Leepfrog's CourseLeaf platform. catalog.ufl.edu CNAMEs to ufl-public.courseleaf.com (12.175.6.47) — a vendor platform behind a UF hostname, which a hostname-only verdic
  name: UF Academic Catalog (CourseLeaf tenancy)
  slug: course-catalog-courseleaf
- description: The UF events calendar runs on LiveWhale Calendar. calendar.ufl.edu CNAMEs to ufl-prod.lwcal.com — again a vendor platform behind a UF hostname that a hostname-only verdict would credit to UF. The iCa
  name: UF Events Calendar (LiveWhale tenancy)
  slug: events-calendar-livewhale
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Public view statistics.
  name: University of Florida Analytics API
  slug: university-of-florida-analytics-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Root index and controlled vocabularies.
  name: University of Florida Discovery API
  slug: university-of-florida-discovery-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Controlled vocabularies backing the SOC search form.
  name: University of Florida Filters API
  slug: university-of-florida-filters-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: OAI-PMH and RSS harvesting surfaces.
  name: University of Florida Harvest API
  slug: university-of-florida-harvest-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Per-item citation, downloads and volume enumeration.
  name: University of Florida Item API
  slug: university-of-florida-item-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Course and section search across a UF academic term.
  name: University of Florida Schedule API
  slug: university-of-florida-schedule-api
- baseURL: https://one.ufl.edu/apix/soc
  baseurl_source: declared
  description: Full-text, exact, geospatial and page-level search.
  name: University of Florida Search API
  slug: university-of-florida-search-api
artifact_total: 27
common:
- group: company
  title: ''
  type: Website
  url: https://www.ufl.edu/
- group: company
  title: ''
  type: About
  url: https://www.ufl.edu/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UniversityofFlorida
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-florida/
- group: company
  title: ''
  type: Blog
  url: https://news.ufl.edu/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.ufl.edu/feed/
- group: operate
  title: ''
  type: Support
  url: https://helpdesk.ufl.edu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.ufl.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://lts.uflib.ufl.edu/supported-systems/uf-digital-collections/
- group: docs
  title: ''
  type: APIReference
  url: https://api.patron.uflib.ufl.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://ufdc.ufl.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uflib.ufl.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.ufl.edu/
- group: other
  href: https://artifacts.apis.io/university-of-florida/identity-federation/university-of-florida-identity-federation.yml
  title: ''
  type: IdentityFederation
  url: identity-federation/university-of-florida-identity-federation.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://rc.ufl.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.ufl.edu/
- group: build
  title: ''
  type: AITooling
  url: https://it.ufl.edu/ai/
- group: design
  href: https://artifacts.apis.io/university-of-florida/conformance/university-of-florida-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-florida-conformance.yml
- group: auth
  href: https://artifacts.apis.io/university-of-florida/authentication/university-of-florida-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-florida-authentication.yml
- group: design
  href: https://artifacts.apis.io/university-of-florida/errors/university-of-florida-errors.yml
  title: ''
  type: Errors
  url: errors/university-of-florida-errors.yml
- group: design
  href: https://artifacts.apis.io/university-of-florida/rules/university-of-florida-rules.yml
  title: ''
  type: Rules
  url: rules/university-of-florida-rules.yml
- group: design
  href: https://artifacts.apis.io/university-of-florida/vocabulary/university-of-florida-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-florida-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/university-of-florida/lifecycle/university-of-florida-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-florida-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/university-of-florida/security/university-of-florida-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-florida-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-florida/plans/university-of-florida-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-florida-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/university-of-florida/rate-limits/university-of-florida-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-florida-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-florida/finops/university-of-florida-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-florida-finops.yml
- group: other
  href: https://artifacts.apis.io/university-of-florida/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Florida (UF) is a public land-grant research university in Gainesville, Florida, United States, and a member of the Association of American Universities. UF publishes no developer portal, no API documentation, no terms of use and no versioning or changelog for anything it operates — but, unusually for this cohort, it does operate real machine-readable surfaces on its own infrastructure rather than only renting a vendor''s. Two public HTTP/JSON APIs run inside UF''s own ARIN allocation (128.227.0.0/16, NetName UFNET) under InCommon-issued certificates: the Schedule of Courses API behind ONE.UF, which serves the full course catalog for 49 terms with an AI-curriculum filter as a first-class parameter, and the Smathers Libraries Patron API behind the UF Digital Collections, a self-documenting 17-resource read API that also serves a conformant OAI-PMH 2.0 repository in Dublin Core and MODS 3.7. UF additionally runs its own Shibboleth identity provider, registered
  in InCommon and interfederated into eduGAIN with REFEDS Research & Scholarship and Sirtfi commitments. Everything else in UF''s footprint is somebody else''s engineering under a UF hostname — Canvas, CourseLeaf, LiveWhale — or is gated behind GatorLink authentication, as data.ufl.edu is.'
examples:
- key_count: 11
  name: University Of Florida Libraries Exactsearch Response
  slug: university-of-florida-libraries-exactsearch-response
- key_count: 11
  name: University Of Florida Libraries Root Index
  slug: university-of-florida-libraries-root-index
- key_count: 11
  name: University Of Florida Soc Filters Response
  slug: university-of-florida-soc-filters-response
- key_count: 11
  name: University Of Florida Soc Schedule Response
  slug: university-of-florida-soc-schedule-response
finops:
- has_sources: true
  method: generated
  name: University Of Florida Finops
  primary_unit: ''
  service_category: Education
  slug: university-of-florida-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-florida.png
json_schemas:
- name: University of Florida Libraries Patron API — response schemas
  property_count: 0
  slug: university-of-florida-libraries-patron-api
- name: University of Florida Schedule of Courses — response schemas
  property_count: 0
  slug: university-of-florida-schedule-of-courses
jsonld:
- class_count: 24
  name: University Of Florida Context
  property_count: 0
  slug: university-of-florida-context
layout: provider
modified: '2026-09-01'
name: University of Florida
nav: Providers
network: true
overview: 'University of Florida publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Discovery API, Filters API, and 11 more. Tagged areas include University, Higher Education, Education, Public Research University, and United States.


  The University of Florida catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Florida''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 23 more developer resources.'
plans:
- name: University Of Florida Plans Pricing
  plan_count: 2
  slug: university-of-florida-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: University Of Florida Rate Limits
  slug: university-of-florida-rate-limits
rules:
- authorship: derived
  effective_rule_count: 0
  extends: []
  name: University of Florida API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: university-of-florida-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 68.5
    catalog_earned_first_party: 21.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 31.6
    contract_governance: 15.2
    contract_quality: 48.9
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/university-of-florida/university-of-florida-2026-06-20T200148.png
security:
- kind: authentication
  name: University Of Florida Authentication
  slug: university-of-florida-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Florida Domain Security
  slug: university-of-florida-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-florida
tags:
- University
- Higher Education
- Education
- Public Research University
- United States
- Florida
- Association of American Universities
- Course Catalog
- Digital Collections
- Library
- Research Data
- Identity Federation
- OAI-PMH
- Research Computing
website: https://www.ufl.edu/
---
