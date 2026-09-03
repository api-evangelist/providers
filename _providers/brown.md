---
access_model:
  confidence: high
  label: Free · no key, no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://repository.library.brown.edu/api/
  baseurl_source: declared
  description: The Brown University Library's public, keyless REST API over the Brown Digital Repository — an item API, a collection API, a Solr-backed search API, and a two-key link index at /api/. Live and unauthe
  name: Brown Digital Repository (BDR) API
  slug: bdr-api
- baseURL: https://repository.library.brown.edu/iiif/
  baseurl_source: declared
  description: The BDR's IIIF surface, on the same institution-operated host. IIIF Image API 2.x (info.json reports a 6335x8560 source with a seven-step size pyramid and 512x512 tiles for the probed object) and IIIF
  name: Brown Digital Repository IIIF Image and Presentation API
  slug: bdr-iiif
- description: Brown's Shibboleth identity provider, and the strongest machine-readable contract in this profile. Brown self-publishes signed per-entity SAML metadata at the entityID itself — uncommon; most institut
  name: Brown University Identity Provider (Shibboleth / SAML 2.0)
  slug: idp
- description: Brown University Library's discovery layer. search.library.brown.edu redirects to bruknow.library.brown.edu/discovery/search?vid=01BU_INST:BROWN, an Ex Libris Primo VE instance. Brown's catalog data a
  name: BruKnow Library Discovery (Ex Libris Primo VE tenant)
  slug: bruknow
- description: Brown's course search and registration front end. It exposes a live, public, keyless JSON API at cab.brown.edu/api/ — a POST interface with page=fose routes for search and details that returned 393 co
  name: Courses@Brown (Leepfrog CourseLeaf tenant)
  slug: cab
- description: The university's academic catalog of programs, concentrations and requirements, on the same vendor as Courses@Brown but a separate deployment. Human-readable; no public JSON interface was found on it.
  name: Brown University Bulletin (Leepfrog CourseLeaf CAT tenant)
  slug: bulletin
- description: Brown's university-wide events calendar, serving a public JSON feed at /live/json/events (3,128,496 bytes on 2026-08-30) and an iCalendar feed at /live/ical/events (2,101,266 bytes, RFC 5545, PRODID /
  name: Events@Brown (LiveWhale Calendar tenant)
  slug: events
artifact_total: 33
common:
- group: company
  title: ''
  type: Website
  url: https://www.brown.edu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brown-University-Library
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brown-ccv
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Brown-University-Library/bdr_api_documentation/wiki
- group: docs
  title: ''
  type: APIReference
  url: https://repository.library.brown.edu/studio/api-docs/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.library.brown.edu/studio/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.brown.edu/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bruknow.library.brown.edu/discovery/search?vid=01BU_INST:BROWN
- group: learn
  title: ''
  type: CourseCatalog
  url: https://cab.brown.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://ccv.brown.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ccv.brown.edu/documentation
- group: other
  title: ''
  type: AIPolicy
  url: https://provost.brown.edu/committees-and-reports/generative-ai-teaching-and-learning-gaitl-committee-charge
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policy.brown.edu/policy/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.brown.edu/policy/acceptable-use-it-resources
- group: operate
  title: ''
  type: Support
  url: https://ithelp.brown.edu/
- group: company
  title: ''
  type: Blog
  url: https://www.brown.edu/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/brown-university/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/brown-bdr-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/brown-bdr-iiif-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/brown-bdr-searchresponse.json
- group: build
  title: ''
  type: Examples
  url: examples/bdr-item.json
- group: design
  title: ''
  type: Errors
  url: errors/brown-bdr-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/brown-bdr-field-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/brown-bdr-spectral-ruleset.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brown-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brown-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brown-conformance.yml
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/brown-identity-federation.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/brown-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brown-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brown-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brown-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brown-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Brown University is a private Ivy League research university in Providence, Rhode Island. Its genuinely institution-operated programmable footprint is narrow, real, and concentrated entirely in the Brown University Library. Three surfaces survive an operator check: the Brown Digital Repository (BDR) REST API, the BDR''s IIIF Image and Presentation services, and a Shibboleth SAML 2.0 identity provider. All three sit under brown.edu, and the identity provider resolves into Brown''s own ARIN allocation (BROWN-UNIV, 128.148.252.0/24) behind a Brown-procured InCommon OV certificate, so the attribution is settled by address ownership rather than by hostname. The BDR API is the substantive find: a public, keyless, Solr-backed API over 1,147,400 objects, documented by Brown Library staff in the wiki of Brown''s own GitHub repository, with 11,622 objects exposing DataCite DOIs on Brown''s prefix 10.26300. It is more than most universities in this cohort operate. It is also unversioned,
  sends no CORS headers, returns nine-byte text/html bodies on failure, silently caps results at 500 rows, and answers malformed queries with HTTP 200 and an empty result set rather than the 400 its own documentation promises. There is no OAI-PMH endpoint on any probed path — an absence worth stating, because reviewers assume an institutional repository has one. Everything else that looks like a Brown API is a vendor platform running under a Brown hostname and is recorded here as a tenant relationship, not as a Brown contract: library discovery is Ex Libris Primo VE (bruknow.library.brown.edu terminates on Ex Libris (USA) Inc address space), the course catalog and bulletin are Leepfrog CourseLeaf (cab.brown.edu and bulletin.brown.edu CNAME to courseleaf.com), and the events calendar is LiveWhale (events.brown.edu CNAMEs to lwcal.com). Two of those tenant platforms expose genuinely useful public JSON — Courses@Brown returns full section, meeting-time and instructor data with no key, and Events@Brown
  serves a 3MB JSON feed and an iCal feed — but that engineering is the vendor''s. No central developer portal, no open data portal, and no institution-operated course or registrar API exist; the one that did, the student-built api.students.brown.edu, has been 404 since before this profile was first written.'
examples:
- key_count: 12
  name: Bdr Api Root
  slug: bdr-api-root
- key_count: 12
  name: Bdr Collections Top Level
  slug: bdr-collections-top-level
- key_count: 12
  name: Bdr Iiif Image Info
  slug: bdr-iiif-image-info
- key_count: 12
  name: Bdr Iiif Presentation Manifest
  slug: bdr-iiif-presentation-manifest
- key_count: 12
  name: Bdr Item
  slug: bdr-item
- key_count: 12
  name: Bdr Search Filtered
  slug: bdr-search-filtered
- key_count: 12
  name: Bdr Search Malformed Query
  slug: bdr-search-malformed-query
finops:
- name: Brown Finops
  service_category: Education
  slug: brown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brown.png
json_schemas:
- name: ApiRoot
  property_count: 2
  slug: brown-bdr-apiroot
- name: Collection
  property_count: 4
  slug: brown-bdr-collection
- name: CollectionList
  property_count: 1
  slug: brown-bdr-collectionlist
- name: CollectionRef
  property_count: 9
  slug: brown-bdr-collectionref
- name: Document
  property_count: 5
  slug: brown-bdr-document
- name: ImageInfo
  property_count: 7
  slug: brown-bdr-imageinfo
- name: Item
  property_count: 11
  slug: brown-bdr-item
- name: ItemLinks
  property_count: 4
  slug: brown-bdr-itemlinks
- name: Manifest
  property_count: 6
  slug: brown-bdr-manifest
- name: Relations
  property_count: 13
  slug: brown-bdr-relations
- name: SearchResponse
  property_count: 3
  slug: brown-bdr-searchresponse
jsonld:
- class_count: 18
  name: Brown Context
  property_count: 7
  slug: brown-context
layout: provider
modified: '2026-08-30'
name: Brown University
nav: Providers
network: true
overview: 'Brown University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Brown Digital Repository (BDR) API and Brown Digital Repository IIIF Image and Presentation API. Tagged areas include Education, Higher Education, University, United States, and Ivy League.


  The Brown University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Brown University''s developer surface includes documentation, API reference, support, engineering blog, code examples, authentication, and 28 more developer resources.'
plans:
- name: Brown Plans Pricing
  plan_count: 2
  slug: brown-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Brown Rate Limits
  slug: brown-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Brown University API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: brown-bdr-lint-report
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Brown University API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: brown-bdr-spectral-ruleset
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 50.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 17.4
    contract_quality: 27.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 17.4
    operational_transparency: 10.5
  previous_composite: 34.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brown/refs/heads/main/screenshots/brown-2026-06-20T173721.png
security:
- kind: authentication
  name: Brown Authentication
  slug: brown-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Brown Domain Security
  slug: brown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brown
tags:
- Education
- Higher Education
- University
- United States
- Ivy League
- Research
- Research Repository
- Digital Repository
- Library
- IIIF
- Identity Federation
- Course Catalog
- Research Computing
website: https://www.brown.edu
---
