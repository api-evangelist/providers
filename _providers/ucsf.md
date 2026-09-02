---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 28.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: UCSF's Shibboleth SAML 2.0 identity provider, registered in the InCommon Federation and re-exported to eduGAIN. Signed, versioned, publicly retrievable federation metadata describing SingleSignOnServi
  name: UCSF Identity Provider (Shibboleth / InCommon)
  slug: incommon-idp
- description: Publicly readable REST content API behind the Industry Documents Library website, exposing 320 editorial pages — collection guides, curated document sets, field-name references, dataset listings, poli
  name: UCSF Industry Documents Library Content API
  slug: idl-content-api
- description: 'UCSF''s institutional research-data repository, delivered on the Dryad platform. 1,306 DataCite DOIs carry a UCSF publisher string. Dryad operates a public REST API, but it is Dryad''s contract serving '
  name: UCSF DataShare (Dryad)
  slug: datashare-dryad
- description: UCSF's open-access scholarly output is harvestable as a named OAI-PMH set on the University of California's eScholarship repository, returning oai_dc records with ark:/13030/ identifiers. This satisfi
  name: UCSF scholarly output via eScholarship OAI-PMH
  slug: escholarship-oai
- description: UCSF Library's discovery layer, delivered on Ex Libris Primo. No UCSF-operated catalog API was found; the Primo and Alma APIs are Ex Libris products and are not attributed to UCSF. Recorded to make th
  name: UCSF Library Discovery (Ex Libris Primo)
  slug: library-discovery
- description: 'The 2026–27 UCSF course catalog, published through Leepfrog''s CourseLeaf. No public course, timetable or registrar API exists — the CourseLeaf JSON endpoints that some institutions leave open are not '
  name: UCSF Course Catalog (CourseLeaf)
  slug: course-catalog
- description: Query the IDL document corpus by identifier or by Solr query syntax.
  name: University of California, San Francisco Documents API
  slug: ucsf-documents-api
- description: Look up a UCSF person's public research profile.
  name: University of California, San Francisco Profiles API
  slug: ucsf-profiles-api
artifact_total: 22
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucsf.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://profilesdeveloper.ucsf.edu/json-api
- group: docs
  title: ''
  type: APIReference
  url: https://profilesdeveloper.ucsf.edu/json-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://profilesdeveloper.ucsf.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UCSF
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsf-ckm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ucsf/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucsf.edu/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ucsf.edu/website-privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://profilesdeveloper.ucsf.edu/contact-and-support
- group: company
  title: ''
  type: Blog
  url: https://www.ucsf.edu/news
- group: other
  title: ''
  type: OpenData
  url: https://data.ucsf.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://datashare.ucsf.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.ucsf.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://coursecatalog.ucsf.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucsf.edu
- group: other
  title: ''
  type: ResearchComputing
  url: https://wynton.ucsf.edu/hpc/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.ucsf.edu/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ucsf-profiles-json-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/ucsf-industry-documents-solr-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ucsf-profile.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ucsf-industry-document.json
- group: build
  title: ''
  type: Examples
  url: examples/README.md
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ucsf-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucsf-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/ucsf-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/ucsf-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ucsf-education-standards-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ucsf-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/ucsf-governance-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucsf-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsf-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsf-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsf-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsf-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of California, San Francisco (UCSF) is a public health-sciences university and the only UC campus dedicated exclusively to graduate and health professions education, biomedical research, and patient care. Unlike most universities in this cohort, UCSF operates two genuinely institution-owned public APIs rather than renting them from a platform vendor: the UCSF Profiles JSON API, run by the UCSF Clinical and Translational Science Institute over 8,000+ researcher records, and the UCSF Industry Documents Library Solr API, run by the UCSF Library Center for Knowledge Management over 28.2 million internal industry documents produced in tobacco, drug, chemical, food, fossil fuel and opioid litigation. Both are anonymous, read-only, and documented by UCSF itself. UCSF also operates a Shibboleth identity provider registered in the InCommon Federation as urn:mace:incommon:ucsf.edu. Everything else in UCSF''s machine-readable footprint is a vendor platform running under
  a UCSF name — Dryad for research data, Ex Libris Primo for library discovery, CourseLeaf for the course catalog, and the California Digital Library''s eScholarship for OAI-PMH harvesting — and is recorded here as a tenant relationship, not as UCSF engineering. There is no central UCSF developer portal: the developer.ucsf.edu host recorded in the June 2026 profile does not resolve on any public DNS resolver and has never been archived, and UCSF''s API gateway at unified-api.ucsf.edu answers only with a Citrix challenge. UCSF publishes no OpenAPI, no changelog, and no status feed for either API it does run.'
examples:
- key_count: 3
  name: Ucsf Industry Documents Search Response
  slug: ucsf-industry-documents-search-response
- key_count: 3
  name: Ucsf Industry Documents Single Document
  slug: ucsf-industry-documents-single-document
- key_count: 3
  name: Ucsf Profiles Json Api Response
  slug: ucsf-profiles-json-api-response
finops:
- name: Ucsf Finops
  service_category: Education
  slug: ucsf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsf.png
json_schemas:
- name: UCSF Industry Documents Library Document
  property_count: 26
  slug: ucsf-industry-document
- name: UCSF Profiles Person
  property_count: 31
  slug: ucsf-profile
jsonld:
- class_count: 42
  name: Ucsf Context
  property_count: 3
  slug: ucsf-context
- class_count: 20
  name: Ucsf Industry Documents Context
  property_count: 2
  slug: ucsf-industry-documents-context
layout: provider
modified: '2026-08-19'
name: University of California, San Francisco
nav: Providers
network: true
overview: 'University of California, San Francisco publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Profiles API. Tagged areas include University, Higher Education, Education, United States, and California.


  The University of California, San Francisco catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  University of California, San Francisco''s developer surface includes documentation, API reference, GitHub presence, support, engineering blog, code examples, authentication, and 29 more developer resources.'
plans:
- name: Ucsf Plans Pricing
  plan_count: 2
  slug: ucsf-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Ucsf Rate Limits
  slug: ucsf-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of California, San Francisco API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ucsf-governance-rules
scopes:
- name: Ucsf Scopes
  scope_count: 0
  slug: ucsf-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 29.3
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 3.8
    operational_transparency: 23.7
  previous_composite: 41.1
  provenance:
    conformance: first-party
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
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ucsf Authentication
  slug: ucsf-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ucsf Domain Security
  slug: ucsf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucsf
tags:
- University
- Higher Education
- Education
- United States
- California
- UC System
- Public Research University
- Health Sciences
- Research
- Researcher Profiles
- Research Data
- Open Data
- Library
- Digital Archive
- Identity Federation
- Research Computing
website: https://www.ucsf.edu/
---
