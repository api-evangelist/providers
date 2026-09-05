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
  - rate-limits
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: University Of Waterloo Agentic Access
  operation_count: 48
  slug: university-of-waterloo-agentic-access
  summary_line: 48 operations · 2 acting
api_count: 1
apis:
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The AcademicOrganizations API from University of Waterloo — 2 operation(s) for academicorganizations.
  name: University of Waterloo AcademicOrganizations API
  slug: university-of-waterloo-academicorganizations-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Account API from University of Waterloo — 5 operation(s) for account.
  name: University of Waterloo Account API
  slug: university-of-waterloo-account-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The ClassSchedules API from University of Waterloo — 3 operation(s) for classschedules.
  name: University of Waterloo ClassSchedules API
  slug: university-of-waterloo-classschedules-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Courses API from University of Waterloo — 5 operation(s) for courses.
  name: University of Waterloo Courses API
  slug: university-of-waterloo-courses-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The ExamSchedules API from University of Waterloo — 2 operation(s) for examschedules.
  name: University of Waterloo ExamSchedules API
  slug: university-of-waterloo-examschedules-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The FoodServices API from University of Waterloo — 6 operation(s) for foodservices.
  name: University of Waterloo FoodServices API
  slug: university-of-waterloo-foodservices-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The HolidayDates API from University of Waterloo — 3 operation(s) for holidaydates.
  name: University of Waterloo HolidayDates API
  slug: university-of-waterloo-holidaydates-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The ImportantDates API from University of Waterloo — 2 operation(s) for importantdates.
  name: University of Waterloo ImportantDates API
  slug: university-of-waterloo-importantdates-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Locations API from University of Waterloo — 6 operation(s) for locations.
  name: University of Waterloo Locations API
  slug: university-of-waterloo-locations-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Subjects API from University of Waterloo — 3 operation(s) for subjects.
  name: University of Waterloo Subjects API
  slug: university-of-waterloo-subjects-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Terms API from University of Waterloo — 3 operation(s) for terms.
  name: University of Waterloo Terms API
  slug: university-of-waterloo-terms-api
- baseURL: https://openapi.data.uwaterloo.ca/v3/
  baseurl_source: declared
  description: The Wcms API from University of Waterloo — 8 operation(s) for wcms.
  name: University of Waterloo Wcms API
  slug: university-of-waterloo-wcms-api
- description: A second, deliberately gated University of Waterloo API programme providing authenticated access to data from authoritative source systems including Quest (student information) and WatIAM (identity an
  name: University of Waterloo SourceAPI
  slug: university-of-waterloo-sourceapi
- description: The REST backend of UWSpace, the University of Waterloo institutional repository, running DSpace 8.4 on a University of Waterloo Libraries host. The root document at /server/api returns a HAL index of
  name: UWSpace DSpace REST API
  slug: uwspace-dspace-rest-api
- description: The OAI-PMH 2.0 metadata harvesting endpoint for UWSpace, the University of Waterloo institutional repository. A verb=Identify request returns protocolVersion 2.0, repositoryName UWSpace, an adminEmai
  name: UWSpace OAI-PMH Endpoint
  slug: uwspace-oai-pmh
- description: The University of Waterloo's own SAML 2.0 identity provider metadata, served as XML from idp.uwaterloo.ca. The EntityDescriptor carries entityID https://idp.uwaterloo.ca/idp/shibboleth, a shibboleth S
  name: University of Waterloo Shibboleth Identity Provider
  slug: university-of-waterloo-shibboleth-idp
- description: Waterloo's named research-data collection on Borealis, the Canadian consortial Dataverse repository operated by Scholars Portal for the Ontario Council of University Libraries. The collection is Water
  name: University of Waterloo Dataverse Collection (Borealis)
  slug: university-of-waterloo-borealis-collection
- description: The University of Waterloo is Crossref member 6095, holding DOI prefix 10.15353 with 3,104 DOIs registered as of 2026-09-01. This is an identifier-registry membership — a fact about Waterloo, shared w
  name: University of Waterloo Crossref Membership
  slug: university-of-waterloo-crossref-member
- description: The University of Waterloo's Research Organization Registry record, ROR ID https://ror.org/01aff2v68, carrying the uwaterloo.ca domain, an establishment year of 1956, and cross-references to Funder Re
  name: University of Waterloo ROR Record
  slug: university-of-waterloo-ror-record
- description: Waterloo's public service status page at status.uwaterloo.ca, with the full Statuspage v2 JSON API behind it — status.json, summary.json and an RSS incident history all return 200 unauthenticated. The
  name: University of Waterloo Status API
  slug: university-of-waterloo-status-api
artifact_total: 57
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations API
  slug: open-university-of-waterloo-academicorganizations-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Account API
  slug: open-university-of-waterloo-account-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations ClassSchedules API
  slug: open-university-of-waterloo-classschedules-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Courses API
  slug: open-university-of-waterloo-courses-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations ExamSchedules API
  slug: open-university-of-waterloo-examschedules-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations FoodServices API
  slug: open-university-of-waterloo-foodservices-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations HolidayDates API
  slug: open-university-of-waterloo-holidaydates-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations ImportantDates API
  slug: open-university-of-waterloo-importantdates-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Locations API
  slug: open-university-of-waterloo-locations-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Subjects API
  slug: open-university-of-waterloo-subjects-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Terms API
  slug: open-university-of-waterloo-terms-api
- collection_type: open
  name: Waterloo OpenData AcademicOrganizations Wcms API
  slug: open-university-of-waterloo-wcms-api
common:
- group: company
  title: ''
  type: Website
  url: https://uwaterloo.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uwaterloo.ca/api/
- group: docs
  title: ''
  type: Documentation
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/overview
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.data.uwaterloo.ca/swagger/v1/swagger.json
- group: docs
  title: ''
  type: Swagger
  url: https://openapi.data.uwaterloo.ca/api-docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34025641600/Getting+Started+-+OpenAPI
- group: start
  title: ''
  type: SignUp
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34025641600/Getting+Started+-+OpenAPI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34019780998/Terms+of+Service+SourceAPI
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34019781061/Acceptable+Use+Policy+SourceAPI
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uwaterloo.ca/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://uwaterloo.ca/secretariat-general-counsel/policies-procedures-guidelines/policy-46-information-management
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uwaterloo.ca/
- group: operate
  title: ''
  type: ChangeLog
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/blog/2026/01/23/44869681282/Open+Data+API+Functional+Changes
- group: operate
  title: ''
  type: Roadmap
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34019779689/Roadmap+-+OpenAPI
- group: operate
  title: ''
  type: Support
  url: https://uwaterloo.atlassian.net/servicedesk/customer/portal/115
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/uWaterloo/Datasets/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uWaterloo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uWaterloo/Datasets
- group: agent
  title: ''
  type: WellKnown
  url: https://uwaterloo.ca/.well-known/security.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-waterloo/
- group: company
  title: ''
  type: Blog
  url: https://uwaterloo.ca/news/
- group: other
  title: ''
  type: OpenData
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34019779691/Datasets+OpenAPI
- group: learn
  title: ''
  type: CourseCatalog
  url: https://uwaterloo.atlassian.net/wiki/spaces/UWAPI/pages/34006663321/Course+Schedule
- group: other
  title: ''
  type: ResearchRepository
  url: https://uwspace.uwaterloo.ca/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.uwaterloo.ca/idp/shibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://uwaterloo.ca/artificial-intelligence-institute/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-waterloo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-waterloo-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-waterloo-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/university-of-waterloo-scopes.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-waterloo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-waterloo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-waterloo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-waterloo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-waterloo-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-waterloo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-waterloo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-waterloo-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Waterloo is a public research university in Waterloo, Ontario, Canada, known for cooperative education and for strength in mathematics, engineering and computer science. Unusually for this cohort, Waterloo genuinely operates its own API programme rather than appearing programmable through a vendor''s contract: the Open Data API v3 at openapi.data.uwaterloo.ca is Waterloo-built and Waterloo-hosted, publishes a first-party OpenAPI at /swagger/v1/swagger.json, exposes 48 self-serve key-authenticated operations across courses, class and exam schedules, terms, subjects, academic organizations, locations, food services, important dates and web content, and carries a dated release-note stream, a published 120 requests-per-minute cap and a completed v2 retirement. Alongside it Waterloo runs a second, deliberately gated SourceAPI over authoritative Quest and WatIAM data, its own Shibboleth identity provider at idp.uwaterloo.ca, and the UWSpace institutional repository
  with DSpace REST and OAI-PMH endpoints on a Waterloo Libraries host. What it does not run is the research-data platform: Waterloo''s data collection is a tenancy on the consortial Borealis Dataverse, and its status page is a Statuspage tenancy — both recorded here as relationships, not as Waterloo engineering. There is no unified developer portal spanning the three programmes; documentation is split between a Confluence space, a GitHub wiki and a Swagger UI.'
examples:
- key_count: 5
  name: University Of Waterloo Academicorganization Detail Example
  slug: university-of-waterloo-academicorganization-detail-example
- key_count: 19
  name: University Of Waterloo Course Detail Example
  slug: university-of-waterloo-course-detail-example
- key_count: 7
  name: University Of Waterloo Location Detail Example
  slug: university-of-waterloo-location-detail-example
- key_count: 7
  name: University Of Waterloo Term Current Example
  slug: university-of-waterloo-term-current-example
finops:
- name: University Of Waterloo Finops
  service_category: Education
  slug: university-of-waterloo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-waterloo.png
json_schemas:
- name: AcademicOrganization
  property_count: 5
  slug: university-of-waterloo-academicorganization
- name: Course
  property_count: 19
  slug: university-of-waterloo-course
- name: Location
  property_count: 7
  slug: university-of-waterloo-location
- name: Subject
  property_count: 5
  slug: university-of-waterloo-subject
- name: Term
  property_count: 7
  slug: university-of-waterloo-term
json_structures:
- name: University Of Waterloo Course Structure
  property_count: 11
  slug: university-of-waterloo-course-structure
- name: University Of Waterloo Location Structure
  property_count: 6
  slug: university-of-waterloo-location-structure
- name: University Of Waterloo Subject Structure
  property_count: 5
  slug: university-of-waterloo-subject-structure
- name: University Of Waterloo Term Structure
  property_count: 7
  slug: university-of-waterloo-term-structure
jsonld:
- class_count: 28
  name: University Of Waterloo Context
  property_count: 0
  slug: university-of-waterloo-context
layout: provider
modified: '2026-09-01'
name: University of Waterloo
nav: Providers
network: true
overview: 'University of Waterloo publishes 12 APIs on the [APIs.io](https://apis.io/) network, including AcademicOrganizations API, Account API, ClassSchedules API, and 9 more. Tagged areas include Education, Higher Education, University, Open Data, and Canada.


  The University of Waterloo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Waterloo''s developer surface includes documentation, API reference, getting-started guide, signup flow, changelog, support, engineering blog, and 32 more developer resources.'
plans:
- name: University Of Waterloo Plans Pricing
  plan_count: 2
  slug: university-of-waterloo-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: University Of Waterloo Rate Limits
  slug: university-of-waterloo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Waterloo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-waterloo-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: University of Waterloo API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 2
  slug: university-of-waterloo-rules
scopes:
- name: University Of Waterloo Scopes
  scope_count: 0
  slug: university-of-waterloo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.3
    catalog_earned_first_party: 12.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 25.0
    contract_quality: 56.8
    developer_ergonomics: 57.1
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 73.7
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-waterloo/refs/heads/main/screenshots/university-of-waterloo-2026-06-20T200326.png
security:
- kind: authentication
  name: University Of Waterloo Authentication
  slug: university-of-waterloo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Waterloo Domain Security
  slug: university-of-waterloo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Waterloo Vulnerability Disclosure
  slug: university-of-waterloo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-waterloo
tags:
- Education
- Higher Education
- University
- Open Data
- Canada
- Ontario
- Research
- Research Data
- Course Catalog
- Identity Federation
- Research Repository
- Campus Life
website: https://uwaterloo.ca/
---
