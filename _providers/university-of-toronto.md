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
  try_now: false
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
api_count: 1
apis:
- description: The University of Toronto's Shibboleth identity provider, entityID https://idpz.utorauth.utoronto.ca/shibboleth, serving signed SAML 2.0 metadata from the University's own utorauth.utoronto.ca host. R
  name: UTORauth Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: utorauth-shibboleth-idp
- description: OAI-PMH 2.0 harvesting endpoint for TSpace, the University of Toronto Libraries institutional research repository. The repository is the University's — Identify returns repositoryName "TSpace" with ad
  name: TSpace Institutional Repository (OAI-PMH) — tenant on Scholaris
  slug: tspace-oai-pmh
- description: 'The DSpace 8.4 HAL REST API serving TSpace. Verified live on 2026-08-19: the root document returns dspaceName "TSpace", dspaceVersion "DSpace 8.4" and a link index covering communities, collections, i'
  name: TSpace DSpace REST API — tenant on Scholaris
  slug: tspace-dspace-rest
- description: The University of Toronto's research data repository collection inside Borealis, the Canadian Dataverse Repository operated by Scholars Portal for the Ontario Council of University Libraries. Verified
  name: U of T Dataverse (Borealis) — tenant
  slug: uoft-dataverse-borealis
- baseURL: https://api.easi.utoronto.ca/ttb
  baseurl_source: declared
  description: Course, section and meeting-time retrieval.
  name: University of Toronto Courses API
  slug: university-of-toronto-courses-api
- baseURL: https://api.easi.utoronto.ca/ttb
  baseurl_source: declared
  description: Sessions, divisions, campuses and other search facets.
  name: University of Toronto Reference Data API
  slug: university-of-toronto-reference-data-api
artifact_total: 26
common:
- group: company
  title: ''
  type: Website
  url: https://www.utoronto.ca/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.utoronto.ca/llms.txt
- group: learn
  title: ''
  type: CourseCatalog
  url: https://ttb.utoronto.ca/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idpz.utorauth.utoronto.ca/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://utoronto.scholaris.ca/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://onesearch.library.utoronto.ca/
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.scinet.utoronto.ca/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.utoronto.ca/
- group: build
  title: ''
  type: AITooling
  url: https://its.utoronto.ca/ai/
- group: other
  title: ''
  type: OpenData
  url: https://data.utoronto.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://easi.its.utoronto.ca/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.utoronto.ca/privacy
- group: operate
  title: ''
  type: Status
  url: https://www.utoronto.ca/campus-status
- group: company
  title: ''
  type: Blog
  url: https://www.utoronto.ca/news
- group: operate
  title: ''
  type: Support
  url: https://www.utoronto.ca/contacts
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/utoronto
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utlib
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-toronto/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-toronto-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-toronto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-toronto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-toronto-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-toronto-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-toronto-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-toronto-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-toronto-rules.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-toronto-scopes.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ttb-course.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-toronto-timetable-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/index.yml
created: '2026-06-03'
description: 'The University of Toronto is Canada''s largest public research university, operating three campuses (St. George, Mississauga, Scarborough) and ranked in the QS World University Rankings top 25. Like almost every institution its size it is a federation of buyers rather than a producer of APIs, and this profile is deliberate about which side of that line each surface falls on. Two surfaces are genuinely institution-operated, both on utoronto.ca: the Timetable Builder API at api.easi.utoronto.ca, run by Enterprise Applications and Solutions Integration (EASI) within U of T Information Technology Services, which serves live course, section, meeting-time, enrolment and building data across all divisions with no credential required; and the UTORauth Shibboleth identity provider, which publishes SAML 2.0 metadata registered in the Canadian Access Federation with the REFEDS Research & Scholarship entity category and SIRTFI assurance. Everything else that looks like a University of
  Toronto API is a vendor or consortium contract running under the University''s name — TSpace now lives on Scholaris, the OCUL-operated DSpace service, and its OAI-PMH and REST endpoints are the platform''s engineering, not U of T''s; the U of T Dataverse is a collection inside Borealis. Those relationships are recorded here as tenant surfaces because the data is the University''s even though the contract is not. There is no developer portal, no API documentation, no terms of use for any API, no versioning scheme, no status page and no support channel for developers. The University does publish an llms.txt at its web root, which is more agent-facing provision than most of the cohort makes.'
examples:
- key_count: 2
  name: Ttb Current Session Response
  slug: ttb-current-session-response
- key_count: 2
  name: Ttb Gateway 404 Response
  slug: ttb-gateway-404-response
- key_count: 2
  name: Ttb Matching Divisions Response
  slug: ttb-matching-divisions-response
- key_count: 2
  name: Ttb No Results Response
  slug: ttb-no-results-response
- key_count: 15
  name: Ttb Pageable Courses Request
  slug: ttb-pageable-courses-request
- key_count: 3
  name: Ttb Pageable Courses Response
  slug: ttb-pageable-courses-response
- key_count: 3
  name: Ttb Reference Data Response
  slug: ttb-reference-data-response
finops:
- name: University Of Toronto Finops
  service_category: Education
  slug: university-of-toronto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-toronto.png
json_schemas:
- name: University of Toronto Timetable Builder — Course Search Request
  property_count: 15
  slug: ttb-course-search
- name: University of Toronto Timetable Builder — Course
  property_count: 8
  slug: ttb-course
- name: University of Toronto Timetable Builder — Meeting Time
  property_count: 6
  slug: ttb-meeting-time
- name: University of Toronto Timetable Builder — Section
  property_count: 19
  slug: ttb-section
jsonld:
- class_count: 10
  name: University Of Toronto Context
  property_count: 4
  slug: university-of-toronto-context
- class_count: 14
  name: University Of Toronto Timetable Context
  property_count: 8
  slug: university-of-toronto-timetable-context
layout: provider
modified: '2026-08-19'
name: University of Toronto
nav: Providers
network: true
overview: 'University of Toronto publishes 2 APIs on the [APIs.io](https://apis.io/) network: Courses API and Reference Data API. Tagged areas include University, Higher Education, Education, Canada, and U15.


  The University of Toronto catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  University of Toronto''s developer surface includes documentation, status page, engineering blog, support, code examples, and 26 more developer resources.'
plans:
- name: University Of Toronto Plans Pricing
  plan_count: 2
  slug: university-of-toronto-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: University Of Toronto Rate Limits
  slug: university-of-toronto-rate-limits
rules:
- effective_rule_count: 1
  extends: []
  name: University of Toronto API Rules
  rule_count: 1
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 1
  slug: university-of-toronto-rules
scopes:
- name: University Of Toronto Scopes
  scope_count: 0
  slug: university-of-toronto-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 52.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 23.8
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 11.4
    operational_transparency: 23.7
  previous_composite: 35.2
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
    score: 57.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-toronto/refs/heads/main/screenshots/university-of-toronto-2026-06-20T200245.png
security:
- kind: authentication
  name: University Of Toronto Authentication
  slug: university-of-toronto-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Toronto Domain Security
  slug: university-of-toronto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-toronto
tags:
- University
- Higher Education
- Education
- Canada
- U15
- Research
- Course Catalog
- Identity Federation
- Research Data
- Institutional Repository
- Library
- Public Research University
website: https://www.utoronto.ca/
---
