---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Yale Agentic Access
  operation_count: 6
  slug: yale-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: 'Search and discovery across LUX scopes, returning Linked Art OrderedCollectionPage documents in JSON-LD. LUX is Yale''s own platform: the frontend, middle tier, Varnish cache, MarkLogic backend and dat'
  name: LUX Collections Discovery — Search API
  slug: yale-search-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: Retrieves a single entity from LUX as a Linked Art JSON-LD document by type and identifier. Institution-operated on lux.collections.yale.edu.
  name: LUX Collections Discovery — Documents API
  slug: yale-documents-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: Faceted aggregation over LUX search results, returning an OrderedCollectionPage of facet values and occurrence counts. Institution-operated on lux.collections.yale.edu.
  name: LUX Collections Discovery — Facets API
  slug: yale-facets-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: Related-entity discovery across LUX, returning an OrderedCollectionPage of documents connected to a given URI. Institution-operated on lux.collections.yale.edu.
  name: LUX Collections Discovery — Related API
  slug: yale-related-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: Advanced-search configuration metadata for LUX, describing searchable terms by scope, search options and stop words. Verified 200 returning 43,502 bytes of JSON on 2026-08-19.
  name: LUX Collections Discovery — Configuration API
  slug: yale-configuration-api
- description: Yale's institution-operated developer portal documents four Portal APIs — Buildings (name and location of Yale campus buildings), Courses, Course Subjects and GatewayServiceMetrics. Yale's own page ca
  name: Yale API Portal — Portal APIs
  slug: portal
- description: Returns course-offering information for a given termCode and subjectCode — titles, descriptions, instructors, meeting times, prerequisites and distributional designations — in JSON or XML. Live and ga
  name: Yale Courses Web Service v3
  slug: courses
- description: Eleven services delivered by Yale's Integration Competency Center covering Yale identities (People Hub — PeopleService, GetPeopleService, LimitedPeopleService, SearchByIndividual, GetAppointmentServic
  name: Yale Enterprise (SOA) Services
  slug: enterprise-soa
- description: EliScholar is Yale's digital platform for scholarly publishing, and its OAI-PMH endpoint is live — Identify returned protocol version 2.0 with repositoryName "EliScholar – A Digital Platform for Schol
  name: EliScholar OAI-PMH (bepress Digital Commons tenancy)
  slug: elischolar
- description: Yale Course Search (courses.yale.edu) and the Yale University Publications bulletin (catalog.yale.edu) are the institution's public course-catalog surfaces. Both are Leepfrog CourseLeaf tenancies — co
  name: Yale Course Search and University Publications (CourseLeaf tenancy)
  slug: course-catalog
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: SAML 2.0 entity metadata
  name: Yale University Federation API
  slug: yale-federation-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: IIIF Presentation 3.0 manifests for digitized objects
  name: Yale University IIIF API
  slug: yale-iiif-api
- baseURL: https://lux.collections.yale.edu
  baseurl_source: declared
  description: Deployment identity, version and metrics
  name: Yale University Info API
  slug: yale-info-api
artifact_total: 41
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LUX Yale Collections Discovery Configuration API
  slug: open-yale-configuration-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Documents API
  slug: open-yale-documents-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Facets API
  slug: open-yale-facets-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Related API
  slug: open-yale-related-api
- collection_type: open
  name: LUX Yale Collections Discovery Configuration Search API
  slug: open-yale-search-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/project-lux/lux-middletier/blob/main/LICENSE
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/yale-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.yale.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yale.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.yale.edu/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developers.yale.edu/api-documentation/portal-apis
- group: operate
  title: ''
  type: Support
  url: https://developers.yale.edu/frequently-asked-questions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yale.edu/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://your.yale.edu/policies-procedures
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yalelibrary
- group: build
  title: ''
  type: GitHub
  url: https://github.com/yalelibrary
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/project-lux
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.yale.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://collections.library.yale.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.yale.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://auth.yale.edu/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://research.computing.yale.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.yale.edu/
- group: build
  title: ''
  type: AITooling
  url: https://poorvucenter.yale.edu/AIguidance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/yale-university/
- group: company
  title: ''
  type: Blog
  url: https://news.yale.edu/news-rss
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yale-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yale-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yale-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yale-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/yale-authentication.yml
- group: auth
  title: ''
  type: x-scopes
  url: scopes/yale-scopes.yml
- group: design
  title: ''
  type: x-errors
  url: errors/yale-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/yale-lifecycle.yml
- group: design
  title: ''
  type: x-conformance
  url: conformance/yale-domain-standards.yml
created: '2026-06-03'
description: 'Yale University is a private Ivy League research university in New Haven, Connecticut, United States, ranked #16 in the QS World University Rankings. Its programmable footprint is real but sharply bifurcated, and it is one of the few institutions in this cohort that operates its own contracts rather than only buying them. On the open side Yale runs LUX (lux.collections.yale.edu), a cross-collection discovery platform serving Linked Art JSON-LD over more than 41 million cultural-heritage records, built and published openly by Yale''s own project-lux engineering organization; Yale Dataverse (dataverse.yale.edu), a self-hosted research-data repository on Yale''s own AWS infrastructure minting DOIs under Yale''s own DataCite prefix 10.60600; IIIF Presentation 3.0 manifests from Yale University Library Digital Collections; and a signed SAML 2.0 Shibboleth identity-provider metadata document registered in InCommon. All four were probed live and answer anonymously. On the closed side,
  developers.yale.edu is a genuine institution-operated developer portal documenting eleven Enterprise (SOA) services and four Portal APIs — Buildings, Courses, Course Subjects, GatewayServiceMetrics — but Yale''s own pages describe these as internal and private: the SOA tier uses basic authentication via a provisioned service account, and a Portal API key can only be requested by someone holding a valid Yale NetID. The gateway at gw.its.yale.edu is live and answers an anonymous call with "Invalid API Key", so the surface exists and is simply not open. An earlier profile of this repository described the Courses Web Service as returning "public information"; that is corrected here. Two further surfaces carry Yale''s name but not Yale''s engineering and are recorded as tenant relationships rather than as Yale contracts: EliScholar (elischolar.library.yale.edu), whose OAI-PMH endpoint is live but whose Identify response gives an Elsevier bepress Digital Commons admin contact, and the course
  catalog at courses.yale.edu / catalog.yale.edu, which is a Leepfrog CourseLeaf tenancy. Yale publishes no open-data portal, no llms.txt and no security.txt.'
examples:
- key_count: 2
  name: Yale Dataverse Info Version Example
  slug: yale-dataverse-info-version-example
- key_count: 2
  name: Yale Dataverse Metrics Datasets Example
  slug: yale-dataverse-metrics-datasets-example
- key_count: 2
  name: Yale Dataverse Search Example
  slug: yale-dataverse-search-example
- key_count: 2
  name: Yale Getdocument Example
  slug: yale-getDocument-example
- key_count: 15
  name: Yale Iiif Manifest Example
  slug: yale-iiif-manifest-example
- key_count: 2
  name: Yale Search Example
  slug: yale-search-example
- key_count: 2
  name: Yale Searchestimate Example
  slug: yale-searchEstimate-example
finops:
- name: Yale Finops
  service_category: Education
  slug: yale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yale.png
json_schemas:
- name: LUX Linked Art Entity
  property_count: 14
  slug: yale-linkedartentity
- name: LUX OrderedCollection
  property_count: 8
  slug: yale-orderedcollection
- name: LUX OrderedCollectionPage
  property_count: 7
  slug: yale-orderedcollectionpage
json_structures:
- name: Yale Linkedartentity Structure
  property_count: 13
  slug: yale-linkedartentity-structure
- name: Yale Orderedcollectionpage Structure
  property_count: 7
  slug: yale-orderedcollectionpage-structure
jsonld:
- class_count: 10
  name: Yale Context
  property_count: 17
  slug: yale-context
layout: provider
modified: '2026-08-19'
name: Yale University
nav: Providers
network: true
overview: 'Yale University publishes 8 APIs on the [APIs.io](https://apis.io/) network, including LUX Collections Discovery — Search API, LUX Collections Discovery — Documents API, LUX Collections Discovery — Facets API, and 5 more. Tagged areas include University, Higher Education, Education, United States, and Ivy League.


  The Yale University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Yale University''s developer surface includes documentation, API reference, support, GitHub presence, engineering blog, and 27 more developer resources.'
plans:
- name: Yale Plans Pricing
  plan_count: 2
  slug: yale-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Yale Rate Limits
  slug: yale-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Yale University API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yale-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Yale University API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: yale-rules
scopes:
- name: Yale Scopes
  scope_count: 0
  slug: yale-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.4
  coverage:
    artifact_dirs: 21
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 57.6
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 53.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yale/refs/heads/main/screenshots/yale-2026-06-20T201720.png
security:
- kind: authentication
  name: Yale Authentication
  slug: yale-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Yale Domain Security
  slug: yale-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: yale
tags:
- University
- Higher Education
- Education
- United States
- Ivy League
- Research
- Research Data
- Research Repository
- Identity Federation
- Library
- Cultural Heritage
- Linked Data
- IIIF
- Course Catalog
website: https://www.yale.edu/
---
