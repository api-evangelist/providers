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
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-09-16'
api_count: 42
apis:
- description: Central campus API developer portal. Catalogs 37 campus APIs across six categories, renders each published contract with Swagger UI, and runs registration, App/consumer-key creation and the API Access
  name: UCSB API Developer Portal
  slug: developer-portal
- description: The single API front door for the campus, at api.ucsb.edu. Every campus API is published as a proxy on it and it enforces the ucsb-api-key application entitlement before a request reaches a backend we
  name: UCSB Campus API Gateway
  slug: campus-api-gateway
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
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The AdmitLevels API from University of California, Santa Barbara — 1 operation(s) for admitlevels.
  name: University of California, Santa Barbara Admit Levels API
  slug: ucsb-admitlevels-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Classes API from University of California, Santa Barbara — 2 operation(s) for classes.
  name: University of California, Santa Barbara Classes API
  slug: ucsb-classes-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Classifications API from University of California, Santa Barbara — 1 operation(s) for classifications.
  name: University of California, Santa Barbara Classifications API
  slug: ucsb-classifications-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The ClassLevels API from University of California, Santa Barbara — 1 operation(s) for classlevels.
  name: University of California, Santa Barbara Class Levels API
  slug: ucsb-classlevels-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The ClassList API from University of California, Santa Barbara — 1 operation(s) for classlist.
  name: University of California, Santa Barbara Class List API
  slug: ucsb-classlist-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The ClassSection API from University of California, Santa Barbara — 1 operation(s) for classsection.
  name: University of California, Santa Barbara Class Section API
  slug: ucsb-classsection-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The ClassSpaceAvailability API from University of California, Santa Barbara — 1 operation(s) for classspaceavailability.
  name: University of California, Santa Barbara Class Space Availability API
  slug: ucsb-classspaceavailability-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Colleges API from University of California, Santa Barbara — 1 operation(s) for colleges.
  name: University of California, Santa Barbara Colleges API
  slug: ucsb-colleges-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The CourseRepeats API from University of California, Santa Barbara — 1 operation(s) for courserepeats.
  name: University of California, Santa Barbara Course Repeats API
  slug: ucsb-courserepeats-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Courses API from University of California, Santa Barbara — 1 operation(s) for courses.
  name: University of California, Santa Barbara Courses API
  slug: ucsb-courses-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The CourseStatuses API from University of California, Santa Barbara — 1 operation(s) for coursestatuses.
  name: University of California, Santa Barbara Course Statuses API
  slug: ucsb-coursestatuses-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Days API from University of California, Santa Barbara — 1 operation(s) for days.
  name: University of California, Santa Barbara Days API
  slug: ucsb-days-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The DegreeStatus API from University of California, Santa Barbara — 1 operation(s) for degreestatus.
  name: University of California, Santa Barbara Degree Status API
  slug: ucsb-degreestatus-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Departments API from University of California, Santa Barbara — 3 operation(s) for departments.
  name: University of California, Santa Barbara Departments API
  slug: ucsb-departments-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Divisions API from University of California, Santa Barbara — 1 operation(s) for divisions.
  name: University of California, Santa Barbara Divisions API
  slug: ucsb-divisions-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Emphasis API from University of California, Santa Barbara — 2 operation(s) for emphasis.
  name: University of California, Santa Barbara Emphasis API
  slug: ucsb-emphasis-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Employees API from University of California, Santa Barbara — 7 operation(s) for employees.
  name: University of California, Santa Barbara Employees API
  slug: ucsb-employees-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Events API from University of California, Santa Barbara — 1 operation(s) for events.
  name: University of California, Santa Barbara Events API
  slug: ucsb-events-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The FeeStatus API from University of California, Santa Barbara — 1 operation(s) for feestatus.
  name: University of California, Santa Barbara Fee Status API
  slug: ucsb-feestatus-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Finals API from University of California, Santa Barbara — 1 operation(s) for finals.
  name: University of California, Santa Barbara Finals API
  slug: ucsb-finals-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The FWTMN001 API from University of California, Santa Barbara — 1 operation(s) for fwtmn001.
  name: University of California, Santa Barbara FWTMN001 API
  slug: ucsb-fwtmn001-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The FWTMN006 API from University of California, Santa Barbara — 1 operation(s) for fwtmn006.
  name: University of California, Santa Barbara FWTMN006 API
  slug: ucsb-fwtmn006-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The GenderIdentity API from University of California, Santa Barbara — 1 operation(s) for genderidentity.
  name: University of California, Santa Barbara Gender Identity API
  slug: ucsb-genderidentity-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Get Active or Specific ClassCode API from University of California, Santa Barbara — 1 operation(s) for get active or specific classcode.
  name: University of California, Santa Barbara Get Active or Specific ClassCode API
  slug: ucsb-get-active-or-specific-classcode-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Get all Active ClassCodes API from University of California, Santa Barbara — 1 operation(s) for get all active classcodes.
  name: University of California, Santa Barbara Get all Active ClassCodes API
  slug: ucsb-get-all-active-classcodes-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Grades API from University of California, Santa Barbara — 1 operation(s) for grades.
  name: University of California, Santa Barbara Grades API
  slug: ucsb-grades-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The GradingOptions API from University of California, Santa Barbara — 1 operation(s) for gradingoptions.
  name: University of California, Santa Barbara Grading Options API
  slug: ucsb-gradingoptions-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The InstructionTypes API from University of California, Santa Barbara — 1 operation(s) for instructiontypes.
  name: University of California, Santa Barbara Instruction Types API
  slug: ucsb-instructiontypes-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The InstructorFunctions API from University of California, Santa Barbara — 1 operation(s) for instructorfunctions.
  name: University of California, Santa Barbara Instructor Functions API
  slug: ucsb-instructorfunctions-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The InternationalStudents API from University of California, Santa Barbara — 1 operation(s) for internationalstudents.
  name: University of California, Santa Barbara International Students API
  slug: ucsb-internationalstudents-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Majors API from University of California, Santa Barbara — 4 operation(s) for majors.
  name: University of California, Santa Barbara Majors API
  slug: ucsb-majors-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Minors API from University of California, Santa Barbara — 3 operation(s) for minors.
  name: University of California, Santa Barbara Minors API
  slug: ucsb-minors-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The MultiEthnicity API from University of California, Santa Barbara — 1 operation(s) for multiethnicity.
  name: University of California, Santa Barbara Multi Ethnicity API
  slug: ucsb-multiethnicity-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Objectives API from University of California, Santa Barbara — 2 operation(s) for objectives.
  name: University of California, Santa Barbara Objectives API
  slug: ucsb-objectives-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The ObjMajEmps API from University of California, Santa Barbara — 1 operation(s) for objmajemps.
  name: University of California, Santa Barbara Obj Maj Emps API
  slug: ucsb-objmajemps-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Organizations API from University of California, Santa Barbara — 1 operation(s) for organizations.
  name: University of California, Santa Barbara Organizations API
  slug: ucsb-organizations-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Perms API from University of California, Santa Barbara — 1 operation(s) for perms.
  name: University of California, Santa Barbara Perms API
  slug: ucsb-perms-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Programs API from University of California, Santa Barbara — 2 operation(s) for programs.
  name: University of California, Santa Barbara Programs API
  slug: ucsb-programs-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Pronouns API from University of California, Santa Barbara — 2 operation(s) for pronouns.
  name: University of California, Santa Barbara Pronouns API
  slug: ucsb-pronouns-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Quarters API from University of California, Santa Barbara — 2 operation(s) for quarters.
  name: University of California, Santa Barbara Quarters API
  slug: ucsb-quarters-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Registration API from University of California, Santa Barbara — 2 operation(s) for registration.
  name: University of California, Santa Barbara Registration API
  slug: ucsb-registration-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The RegistrationBlocks API from University of California, Santa Barbara — 1 operation(s) for registrationblocks.
  name: University of California, Santa Barbara Registration Blocks API
  slug: ucsb-registrationblocks-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The RegStatus API from University of California, Santa Barbara — 1 operation(s) for regstatus.
  name: University of California, Santa Barbara Reg Status API
  slug: ucsb-regstatus-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The RepeatTypes API from University of California, Santa Barbara — 1 operation(s) for repeattypes.
  name: University of California, Santa Barbara Repeat Types API
  slug: ucsb-repeattypes-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The RequirementCourses API from University of California, Santa Barbara — 1 operation(s) for requirementcourses.
  name: University of California, Santa Barbara Requirement Courses API
  slug: ucsb-requirementcourses-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Requirements API from University of California, Santa Barbara — 1 operation(s) for requirements.
  name: University of California, Santa Barbara Requirements API
  slug: ucsb-requirements-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Rosters API from University of California, Santa Barbara — 1 operation(s) for rosters.
  name: University of California, Santa Barbara Rosters API
  slug: ucsb-rosters-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Schedules API from University of California, Santa Barbara — 7 operation(s) for schedules.
  name: University of California, Santa Barbara Schedules API
  slug: ucsb-schedules-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The SchoolTypes API from University of California, Santa Barbara — 1 operation(s) for schooltypes.
  name: University of California, Santa Barbara School Types API
  slug: ucsb-schooltypes-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Sessions API from University of California, Santa Barbara — 2 operation(s) for sessions.
  name: University of California, Santa Barbara Sessions API
  slug: ucsb-sessions-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Students API from University of California, Santa Barbara — 3 operation(s) for students.
  name: University of California, Santa Barbara Students API
  slug: ucsb-students-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The StudyLoadStatus API from University of California, Santa Barbara — 1 operation(s) for studyloadstatus.
  name: University of California, Santa Barbara Study Load Status API
  slug: ucsb-studyloadstatus-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Subjects API from University of California, Santa Barbara — 2 operation(s) for subjects.
  name: University of California, Santa Barbara Subjects API
  slug: ucsb-subjects-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Uc Fau Validation API from University of California, Santa Barbara — 1 operation(s) for uc fau validation.
  name: University of California, Santa Barbara Uc Fau Validation API
  slug: ucsb-uc-fau-validation-api
- baseURL: https://developer.ucsb.edu/
  baseurl_source: declared
  description: The Verifications API from University of California, Santa Barbara — 2 operation(s) for verifications.
  name: University of California, Santa Barbara Verifications API
  slug: ucsb-verifications-api
artifact_total: 87
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
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/security/ucsb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ucsb-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/plans/ucsb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ucsb-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/rate-limits/ucsb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ucsb-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/finops/ucsb-finops.yml
  title: ''
  type: FinOps
  url: finops/ucsb-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ucsb/refs/heads/main/json-ld/ucsb-context.jsonld
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
overview: 'University of California, Santa Barbara publishes 55 APIs on the [APIs.io](https://apis.io/) network, including Admit Levels API, Classes API, Classifications API, and 52 more. Tagged areas include Education, Higher Education, University, Public Research University, and UC System.


  The University of California, Santa Barbara catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of California, Santa Barbara''s developer surface includes documentation, API reference, getting-started guide, signup flow, GitHub presence, support, status page, and 21 more developer resources.'
plans:
- name: Ucsb Plans Pricing
  plan_count: 2
  slug: ucsb-plans-pricing
random_paper: 11
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
  composite: 53.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 56.1
    developer_ergonomics: 57.1
    discoverability: 59.3
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 53.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 55
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Developer Tools
website: https://www.ucsb.edu/
---
