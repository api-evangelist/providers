---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-01'
api_count: 21
apis:
- description: Central campus API developer portal. Catalogs 37 campus APIs across six categories, renders each published contract with Swagger UI, and runs registration, App/consumer-key creation and the API Access
  name: UCSB API Developer Portal
  slug: developer-portal
- description: The single API front door for the campus, at api.ucsb.edu. Every campus API is published as a proxy on it and it enforces the ucsb-api-key application entitlement before a request reaches a backend we
  name: UCSB Campus API Gateway
  slug: campus-api-gateway
- description: Search and retrieve the UCSB schedule of classes for a quarter — classes, sections, final exams, space availability and general-education codes. The most substantial public academic contract UCSB publ
  name: UCSB Academic Curriculums
  slug: academic-curriculums
- description: List UCSB graduate degree programs and retrieve one by id, with department, degree types and application detail, from the Graduate Division. Published as Swagger 2.0, 2 paths, base https://api.ucsb.ed
  name: UCSB Academic Graduate Programs
  slug: academic-graduate-programs
- description: 'The Office of the Registrar''s quarter calendar — first/last day of classes and finals, the three registration passes, fee deadline and add/drop deadlines. The keystone contract of the estate: everythi'
  name: UCSB Academic Quarter Calendar
  slug: academic-quarter-calendar
- description: Quarter and term calendar as the BARC student billing system sees it, which is deliberately distinct from the Registrar calendar. Private tier. Published as Swagger 2.0, 2 paths, base https://api.ucsb
  name: UCSB BARC Quarter Calendar
  slug: barc-quarter-calendar
- description: Student records as held by BARC, the campus Billing, Accounts Receivable and Collections system. Private tier; the contract is public, the data is not. Published as Swagger 2.0, 1 path, base https://a
  name: UCSB BARC Students API
  slug: barc-students-api
- description: Subjects and skills workshops offered by Campus Learning Assistance Services. One of only two UCSB contracts published as OpenAPI 3.0.1, and the only one that requires the ucsb-api-version header on e
  name: UCSB CLAS Schedules
  slug: clas-schedules
- description: Lookup of BARC class codes, which determine a student billing category. Access Approval Required. Published as Swagger 2.0, 2 paths, base https://api.ucsb.edu/administration/financial/barc/classcode/v
  name: UCSB ClassCode Lookup Service
  slug: classcode-lookup-service
- description: Department, cost centre, cost type and project-code chartfields from the campus financial system. Published as OpenAPI 3.0.1 and the only contract that declares test and dev environments alongside pro
  name: UCSB Department Chartfield
  slug: department-chartfield
- description: Registrar extract of a department course list with sections, time/locations, instructors and concurrent courses. Private tier. Published as Swagger 2.0, 1 path, base https://api.ucsb.edu/students/priv
  name: UCSB Department Course Extract
  slug: department-course-extract
- description: Employment and job data drawn from UCPath — employee records, job codes, job class codes and employment status. Private tier; the most sensitive contract UCSB publishes a spec for. Published as Swagge
  name: UCSB Employee Job
  slug: employee-job
- description: Campus academic events list. The smallest contract in the estate — one GET, no declared schema. Published as Swagger 2.0, 1 path, base https://api.ucsb.edu/academics/.
  name: UCSB Events
  slug: events
- description: Graduate Division application verification service. The one published contract that does NOT run on the Campus API Gateway — it is served directly from gradpoint.ucsb.edu, which sits behind campus ADF
  name: UCSB Grad Application Verifications
  slug: grad-application-verifications
- description: Registrar service backing student access to Santa Barbara Metropolitan Transit District bus service. Private tier; the campus-life corner of the estate. Published as Swagger 2.0, 1 path, base https://
  name: UCSB MTD Access
  slug: mtd-access
- description: 'Validation of PeopleSoft Functional Accounting Unit chartstring combinations. A POST-based validation service and one of only three write-bearing contracts UCSB publishes. Published as Swagger 2.0, 1 '
  name: UCSB PeopleSoft FAU (Functional Accounting Unit) Combination Service
  slug: peoplesoft-fau-functional-accounting-unit-combination-service
- description: A student’s declared majors and minors. Access Approval Required; FERPA-governed. Published as Swagger 2.0, 3 paths, base https://api.ucsb.edu/students.
  name: UCSB Student Academic Programs (Majors / Minors)
  slug: student-academic-programs-majors-minors
- description: Basic and extended student demographic and enrollment records. Access Approval Required; FERPA-governed. Published as Swagger 2.0, 2 paths, base https://api.ucsb.edu/students.
  name: UCSB Student Basic Student Info
  slug: student-basic-student-info
- description: The courses a student is enrolled in for a quarter. Access Approval Required; FERPA-governed. Its base path /students/courses is the exact nesting UCSB’s own published design standard tells campus tea
  name: UCSB Student Courses
  slug: student-courses
- description: Thirty-nine reference tables from the Student Information System — majors, minors, colleges, departments, divisions, grades, grading options, classifications, pronouns, gender identity, instruction ty
  name: UCSB Student Record Code Lookups
  slug: student-record-code-lookups
- description: Student registration records and registration blocks for a quarter. Access Approval Required; one of three write-bearing contracts. Published as Swagger 2.0, 3 paths, base https://api.ucsb.edu/student
  name: UCSB Student Registrations
  slug: student-registrations
- description: The roster of students enrolled in a course section. Access Approval Required; FERPA-governed. Published as Swagger 2.0, 1 path, base https://api.ucsb.edu/students.
  name: UCSB Student Rosters
  slug: student-rosters
- description: A student’s class schedule with meeting times, locations and instructors. Access Approval Required; FERPA-governed. Published as Swagger 2.0, 1 path, base https://api.ucsb.edu/students/schedules.
  name: UCSB Student Schedules
  slug: student-schedules
- description: 'UCSB operates its own Shibboleth identity provider, "Passport", at passport.identity.ucsb.edu, registered in InCommon as entityID urn:mace:incommon:ucsb.edu. Its SAML 2.0 metadata is machine-readable '
  name: UCSB Identity Federation (Passport / InCommon)
  slug: identity-federation
- description: UCSB Library's institutional research repository, moved from alexandria.ucsb.edu to digital.library.ucsb.edu and served through CloudFront. The host is UCSB's and the front end is UCSB Library's own c
  name: Alexandria Digital Research Library (ADRL)
  slug: alexandria-digital-research-library
- description: UCSB Library’s catalog and discovery layer. The host search.library.ucsb.edu is a UCSB CNAME onto ucsb.primo.exlibrisgroup.com, and the service resolves to Ex Libris tenancy 01UCSB_INST. The collectio
  name: UCSB Library Discovery (Ex Libris Primo VE)
  slug: library-discovery
- description: UCSB’s open-access scholarship collection inside eScholarship, the University of California’s systemwide repository operated by the California Digital Library. It IS OAI-PMH harvestable (https://escho
  name: UCSB on eScholarship
  slug: escholarship
artifact_total: 53
common:
- group: company
  title: ''
  type: Website
  url: https://www.ucsb.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ucsb.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ucsb.edu/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ucsb.edu/apis/all
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ucsb.edu/docs/getting-started
- group: start
  title: ''
  type: Signup
  url: https://developer.ucsb.edu/user/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ucsb
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsb
- group: operate
  title: ''
  type: Support
  url: mailto:support@developer.ucsb.edu
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ucsb.edu/terms-of-use
- group: other
  title: ''
  type: Accessibility
  url: https://www.ucsb.edu/accessibility
- group: operate
  title: ''
  type: Status
  url: https://status.sa.ucsb.edu/
- group: operate
  title: ''
  type: Status
  url: https://status.library.ucsb.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.ucsb.edu/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.news.ucsb.edu/all/feed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-santa-barbara/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://developer.ucsb.edu/content/academic-curriculums
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucsb.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://digital.library.ucsb.edu/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://search.library.ucsb.edu/
- group: other
  title: ''
  type: Registrar
  url: https://registrar.sa.ucsb.edu/
- group: other
  title: ''
  type: InformationTechnology
  url: https://it.ucsb.edu/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsb-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucsb-context.jsonld
coverage:
  detail: 'UCSB is one of the genuinely programmable institutions in this cohort, but nothing it publishes is callable without a manually approved account. The CONTRACTS are open: 21 first-party OpenAPI documents download anonymously from developer.ucsb.edu and every one declares a ucsb.edu host, so the estate is fully readable and fully attributable. The ENDPOINTS are not: api.ucsb.edu returns 401 to any request without a ucsb-api-key, portal registration is approved by hand, 25 of 37 catalogued APIs sit above the Auto-Approved tier, and 16 of the 37 do not expose a contract publicly at all — their portal pages return an Access-denied body under HTTP 200. No response bodies, rate-limit headers or live schemas could therefore be captured. The gap is authorization, not absence.'
  evidence:
  - note: 37 APIs listed with access classification
    status: 200
    url: https://developer.ucsb.edu/apis/all
  - note: first-party OpenAPI, downloads anonymously
    status: 200
    url: https://developer.ucsb.edu/sites/default/files/openapi/quartercalendar-v1-api.ucsb_.edu_.yaml
  - note: live gateway; Invalid ApiKey fault, no key issuable without approval
    status: 401
    url: https://api.ucsb.edu/academics/quartercalendar/v1/quarters/current
  - note: HTTP 200 but body is "Access denied" — one of 16 APIs with no public contract
    status: 200
    url: https://developer.ucsb.edu/content/dining-commons
  - note: '"an administrator will review your account and will grant new accounts manually"'
    status: 200
    url: https://developer.ucsb.edu/docs/getting-started
  - note: SAML metadata for UCSB IdP, retrievable without credentials
    status: 200
    url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucsb.edu
  - note: no OAI-PMH on a UCSB host
    status: 403
    url: https://digital.library.ucsb.edu/oai-pmh?verb=Identify
  - note: superseded v1 contract deleted, still referenced by UCSB own client repo
    status: 404
    url: https://developer.ucsb.edu/sites/default/files/openapi/curriculums-v1.out_.api_.yml
  - status: 404
    url: https://www.ucsb.edu/llms.txt
  - status: 404
    url: https://developer.ucsb.edu/.well-known/security.txt
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'University of California, Santa Barbara is a public land-grant research university in the University of California system and an Association of American Universities member. Unusually for this cohort, UCSB runs a real, institution-operated API programme rather than a shelf of vendor contracts: a Campus API Gateway at api.ucsb.edu, a developer portal at developer.ucsb.edu cataloging 37 campus APIs across Academics, Administration, Dining, Employees, Housing and Students, a written and binding API design standard for campus publishers, and 21 downloadable first-party OpenAPI documents — every one of which declares a ucsb.edu host, so none of it is misattributed vendor engineering. The programme is real but it is closed: portal accounts are approved by hand, 25 of the 37 APIs sit above the Auto-Approved tier, and no endpoint is callable without an approved consumer key (an unauthenticated probe returns 401). UCSB also operates its own Shibboleth identity provider registered in
  InCommon, whose SAML metadata is openly machine-readable, and the Alexandria Digital Research Library, which is institution-run but has no API. Its library discovery layer and its open-access scholarship are vendor and UC-system tenancies and are recorded as such. There is no open-data portal, no OAuth authorization server, no llms.txt and no changelog.'
examples:
- key_count: 6
  name: Ucsb Clas Schedules Subjects Example
  slug: ucsb-clas-schedules-subjects-example
- key_count: 6
  name: Ucsb Curriculum Class Search Example
  slug: ucsb-curriculum-class-search-example
- key_count: 5
  name: Ucsb Gateway Error Example
  slug: ucsb-gateway-error-example
- key_count: 6
  name: Ucsb Lookups Departments Example
  slug: ucsb-lookups-departments-example
- key_count: 6
  name: Ucsb Quarter Calendar Current Example
  slug: ucsb-quarter-calendar-current-example
finops:
- name: Ucsb Finops
  service_category: Education
  slug: ucsb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsb.png
json_schemas:
- name: Schedule
  property_count: 14
  slug: ucsb-clas-schedule
- name: Class
  property_count: 20
  slug: ucsb-class
- name: ClassSection
  property_count: 19
  slug: ucsb-class-section
- name: ClassCodeItem
  property_count: 13
  slug: ucsb-classcode
- name: Roster
  property_count: 2
  slug: ucsb-course-roster
- name: DepartmentModel
  property_count: 8
  slug: ucsb-department-chartfield
- name: EmployeeJobModel
  property_count: 7
  slug: ucsb-employee-job
- name: GraduateProgramDetail
  property_count: 14
  slug: ucsb-graduate-program
- name: QuarterCalendar
  property_count: 18
  slug: ucsb-quarter-calendar
- name: Course
  property_count: 9
  slug: ucsb-student-course
- name: Registration
  property_count: 14
  slug: ucsb-student-registration
- name: StudentScheduleCourse
  property_count: 9
  slug: ucsb-student-schedule-course
- name: StudentExtended
  property_count: 19
  slug: ucsb-student
jsonld:
- class_count: 17
  name: Ucsb Context
  property_count: 6
  slug: ucsb-context
layout: provider
modified: '2026-08-30'
name: University of California, Santa Barbara
nav: Providers
network: true
overview: 'University of California, Santa Barbara publishes 21 APIs on the [APIs.io](https://apis.io/) network, including UCSB Academic Curriculums, UCSB Academic Graduate Programs, UCSB Academic Quarter Calendar, and 18 more. Tagged areas include Education, Higher Education, University, Public Research University, and UC System.


  The University of California, Santa Barbara catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of California, Santa Barbara''s developer surface includes documentation, API reference, getting-started guide, signup flow, GitHub presence, support, status page, and 21 more developer resources.'
plans:
- name: Ucsb Plans Pricing
  plan_count: 2
  slug: ucsb-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Ucsb Rate Limits
  slug: ucsb-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: University of California, Santa Barbara API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ucsb-rules
scopes:
- name: Ucsb Scopes
  scope_count: 3
  slug: ucsb-scopes
  summary_line: 3 scopes
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.4
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 53.1
    developer_ergonomics: 57.1
    discoverability: 64.8
    governance: 22.0
    operational_transparency: 23.7
  previous_composite: 54.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/screenshots/ucsb-2026-06-20T195943.png
security:
- kind: authentication
  name: Ucsb Authentication
  slug: ucsb-authentication
  summary_line: apiKey/basic/oauth2 · 3 schemes
- kind: domain-security
  name: Ucsb Domain Security
  slug: ucsb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucsb
tags:
- Education
- Higher Education
- University
- Public Research University
- UC System
- United States
- California
- Campus
- Student Information System
- Course Catalog
- Academics
- Identity Federation
- Research Repository
- Library
- API Gateway
- Developer Portal
website: https://www.ucsb.edu/
---
