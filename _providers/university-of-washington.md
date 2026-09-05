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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: University Of Washington Agentic Access
  operation_count: 56
  slug: university-of-washington-agentic-access
  summary_line: 56 operations · 5 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://mango.u.washington.edu:646/registry/v3
  baseurl_source: declared
  description: The UW-IT Identity Registry REST API. V3 (28 paths) and V2 (13 paths) OpenAPI descriptions are published openly by UW at iam-tools.u.washington.edu and are saved here; the runtime listens on a non-sta
  name: Identity Registration Web Service (IRWS)
  slug: identity-registry-web-service
- description: Enterprise Web Services (EWS) is UW-IT's secure collection of REST/SOAP web services that let enterprise business applications access commonly shared source data in a scalable, real-time, highly avail
  name: UW-IT Enterprise Web Services Registry
  slug: enterprise-web-services
- baseURL: https://groups.uw.edu/group_sws/v3
  baseurl_source: declared
  description: The University of Washington Group Service API — UW-IT's institution-operated group registry and membership service. UW publishes the OpenAPI itself, with an explicit termsOfService (washington.edu/on
  name: UW Groups Web Service (GWS)
  slug: groups-web-service
- baseURL: https://taws.s.uw.edu:716/token/v2
  baseurl_source: declared
  description: UW-IT's Token Authentication Web Service V2 — the institution-operated issuer for the AccessToken credential that the Student and IdCard Web Services accept. Three paths; the OpenAPI is published by U
  name: UW Token Authentication Web Service (TAWS)
  slug: token-authentication-web-service
- description: UW's Shibboleth identity provider publishes signed SAML 2.0 metadata at a stable URL — entityID urn:mace:incommon:washington.edu, scope washington.edu, InCommon registration ID INC20180221T195121. Mac
  name: UW Shibboleth Identity Provider (InCommon)
  slug: identity-federation
- description: ResearchWorks is UW Libraries' institutional repository, running DSpace 9.2 on UW's own host. The DSpace REST root document is public (HTTP 200) and item retrieval is gated (HTTP 401), but the OAI-PMH
  name: ResearchWorks Repository (DSpace REST + OAI-PMH)
  slug: researchworks-dspace
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Campus API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificatio
  name: Student Web Service (SWS) Campus API
  slug: university-of-washington-campus-api
- baseURL: https://ws.admin.washington.edu/idcard
  baseurl_source: declared
  description: IdCard Web Service (IdCardWS) Card API — a resource of the UW-IT IdCard Web Service, split out per resource by the API Evangelist refine step from the institution-published IdCardWS v1 OpenAPI. Specif
  name: IdCard Web Service (IdCardWS) Card API
  slug: university-of-washington-card-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) College API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificati
  name: Student Web Service (SWS) College API
  slug: university-of-washington-college-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Course API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificatio
  name: Student Web Service (SWS) Course API
  slug: university-of-washington-course-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Curriculum API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specific
  name: Student Web Service (SWS) Curriculum API
  slug: university-of-washington-curriculum-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Degree API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificatio
  name: Student Web Service (SWS) Degree API
  slug: university-of-washington-degree-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Degree Audit API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specif
  name: Student Web Service (SWS) Degree Audit API
  slug: university-of-washington-degreeaudit-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Degree Audit Exception API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenA
  name: Student Web Service (SWS) Degree Audit Exception API
  slug: university-of-washington-degreeauditexception-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Degree Audit Program API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI
  name: Student Web Service (SWS) Degree Audit Program API
  slug: university-of-washington-degreeauditprogram-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Degree Audit Status API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI.
  name: Student Web Service (SWS) Degree Audit Status API
  slug: university-of-washington-degreeauditstatus-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Department API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specific
  name: Student Web Service (SWS) Department API
  slug: university-of-washington-department-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Enrollment API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specific
  name: Student Web Service (SWS) Enrollment API
  slug: university-of-washington-enrollment-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Enrollment Major API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Sp
  name: Student Web Service (SWS) Enrollment Major API
  slug: university-of-washington-enrollmentmajor-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Major Students API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Spec
  name: Student Web Service (SWS) Major Students API
  slug: university-of-washington-majorstudents-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Notice API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificatio
  name: Student Web Service (SWS) Notice API
  slug: university-of-washington-notice-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Person API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificatio
  name: Student Web Service (SWS) Person API
  slug: university-of-washington-person-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: 'Student Web Service (SWS) Personal Financial API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. '
  name: Student Web Service (SWS) Personal Financial API
  slug: university-of-washington-personalfinancial-api
- baseURL: https://ws.admin.washington.edu/idcard
  baseurl_source: declared
  description: IdCard Web Service (IdCardWS) Photo API — a resource of the UW-IT IdCard Web Service, split out per resource by the API Evangelist refine step from the institution-published IdCardWS v1 OpenAPI. Speci
  name: IdCard Web Service (IdCardWS) Photo API
  slug: university-of-washington-photo-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Program API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificati
  name: Student Web Service (SWS) Program API
  slug: university-of-washington-program-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Registration API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specif
  name: Student Web Service (SWS) Registration API
  slug: university-of-washington-registration-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: UW Enterprise Web Services Resource List API — a discovery resource published at the root of both the Student Web Service and the IdCard Web Service. Per-path servers[] in the specification record whi
  name: UW Enterprise Web Services Resource List API
  slug: university-of-washington-resourcelist-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Schedule API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificat
  name: Student Web Service (SWS) Schedule API
  slug: university-of-washington-schedule-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Section API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specificati
  name: Student Web Service (SWS) Section API
  slug: university-of-washington-section-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: 'Student Web Service (SWS) Term API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specification '
  name: Student Web Service (SWS) Term API
  slug: university-of-washington-term-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: Student Web Service (SWS) Test Score API — a resource of the UW-IT Student Web Service, split out per resource by the API Evangelist refine step from the institution-published SWS v5 OpenAPI. Specific
  name: Student Web Service (SWS) Test Score API
  slug: university-of-washington-testscore-api
- baseURL: https://ws.admin.washington.edu/student
  baseurl_source: declared
  description: UW Enterprise Web Services Version API — a discovery resource published at the root of both the Student Web Service and the IdCard Web Service. Per-path servers[] in the specification record which hos
  name: UW Enterprise Web Services Version API
  slug: university-of-washington-version-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus API
  slug: open-university-of-washington-campus-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Card API
  slug: open-university-of-washington-card-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus College API
  slug: open-university-of-washington-college-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Course API
  slug: open-university-of-washington-course-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Curriculum API
  slug: open-university-of-washington-curriculum-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Degree API
  slug: open-university-of-washington-degree-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus DegreeAudit API
  slug: open-university-of-washington-degreeaudit-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus DegreeAuditException API
  slug: open-university-of-washington-degreeauditexception-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus DegreeAuditProgram API
  slug: open-university-of-washington-degreeauditprogram-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus DegreeAuditStatus API
  slug: open-university-of-washington-degreeauditstatus-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Department API
  slug: open-university-of-washington-department-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Enrollment API
  slug: open-university-of-washington-enrollment-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus EnrollmentMajor API
  slug: open-university-of-washington-enrollmentmajor-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus MajorStudents API
  slug: open-university-of-washington-majorstudents-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Notice API
  slug: open-university-of-washington-notice-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Person API
  slug: open-university-of-washington-person-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus PersonalFinancial API
  slug: open-university-of-washington-personalfinancial-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Photo API
  slug: open-university-of-washington-photo-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Program API
  slug: open-university-of-washington-program-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Registration API
  slug: open-university-of-washington-registration-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus ResourceList API
  slug: open-university-of-washington-resourcelist-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Schedule API
  slug: open-university-of-washington-schedule-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Section API
  slug: open-university-of-washington-section-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Term API
  slug: open-university-of-washington-term-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus TestScore API
  slug: open-university-of-washington-testscore-api
- collection_type: open
  name: IdCard Web Service (IdCardWS) Campus Version API
  slug: open-university-of-washington-version-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-washington-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-washington-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-washington-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.washington.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uw-it-aca
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uwwebservices
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-washington/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-washington-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-washington-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-washington-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://www.washington.edu/news/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://webservices.washington.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://webservices.washington.edu/service/browse/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://it.uw.edu/summary/enterprise-web-services/
- group: docs
  title: ''
  type: Documentation
  url: https://webservices.washington.edu/learn/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.washington.edu/online/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.washington.edu/online/privacy/
- group: operate
  title: ''
  type: Support
  url: https://it.uw.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.u.washington.edu/metadata/idp-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://digital.lib.washington.edu/researchworks/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.lib.washington.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.washington.edu/students/crscat/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.washington.edu/students/timeschd/
- group: other
  title: ''
  type: ResearchComputing
  url: https://hyak.uw.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://it.uw.edu/topics/artificial-intelligence/
- group: build
  title: ''
  type: AITooling
  url: https://it.uw.edu/guides/ai/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-washington-domain-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-washington-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-washington-astra-roles.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-washington-api-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-washington-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-washington-rules.yml
coverage:
  detail: 'The University of Washington genuinely operates its own API estate — six UW-IT Enterprise Web Services with institution-authored OpenAPI descriptions on University of Washington registrable domains. What is NOT open is the data. Specifications and Swagger UIs return 200 unauthenticated, but every SWS/IdCardWS data resource 302s to UW NetID sign-in through Microsoft Entra ID, DSpace REST item retrieval returns 401, and the IRWS and TAWS runtimes do not answer from the public internet at all. Two surfaces ARE open and were verified live: the ResearchWorks OAI-PMH 2.0 endpoint and the signed Shibboleth / InCommon SAML metadata document. No open-data portal exists (data.uw.edu and data.washington.edu do not resolve) and no self-service developer programme was found — access is institutional, requested through UW-IT, and authorised by named ASTRA roles. The 26 per-resource SWS/IdCardWS entries in apis[] are OUR refine step''s split of TWO institution contracts, not 26 independent APIs;
    x-service groups them. Removed 22 pointers to wiki.cac.washington.edu: the whole host times out on connect (curl 28), so the SWS Confluence space UW''s own registry links to is dead.'
  evidence:
  - status: 200
    url: https://webservices.washington.edu/service/browse/index.html
  - status: 200
    url: https://ws.admin.washington.edu/student/swagger/v5/swagger.json
  - status: 302
    url: https://ws.admin.washington.edu/student/v5/campus.json
  - status: 200
    url: https://iam-tools.u.washington.edu/apis/gws/api.yaml
  - status: 200
    url: https://iam-tools.u.washington.edu/apis/irwsv3/irwsv3.yaml
  - status: 200
    url: https://iam-tools.u.washington.edu/apis/tawsv2/tawsv2.yaml
  - status: 0
    url: https://mango.u.washington.edu:646/registry/v2/person
  - status: 200
    url: https://digital.lib.washington.edu/server/oai/request?verb=Identify
  - status: 200
    url: https://digital.lib.washington.edu/server/api
  - status: 401
    url: https://digital.lib.washington.edu/server/api/core/items
  - status: 200
    url: https://idp.u.washington.edu/metadata/idp-metadata.xml
  - status: 0
    url: https://data.uw.edu/
  - status: 0
    url: https://data.washington.edu/
  - status: 0
    url: https://wiki.cac.washington.edu/display/SWS
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'The University of Washington (UW) is a public research university in Seattle, Washington, United States, and one of the few higher-education institutions in this catalog that genuinely engineers and operates its own API estate rather than only buying one. UW-IT''s Enterprise Web Services (EWS) programme publishes a browsable service registry and institution-authored OpenAPI descriptions for the Student Web Service (SWS v5), the IdCard Web Service (IdCardWS v1), the Groups Web Service (GWS 2.3.x at groups.uw.edu), the Identity Registration Web Service (IRWS v2 and v3) and the Token Authentication Web Service (TAWS v2) — every one of them hosted on a University of Washington registrable domain, so the operator is the institution and not a platform vendor. The honest limit matters as much as the footprint: the specifications and Swagger UIs are public, but essentially every data resource behind them is gated by UW NetID (Microsoft Entra ID OIDC), an X.509 InCommon client certificate
  and named ASTRA authorisation roles, and the IRWS and TAWS runtimes are not reachable from the public internet at all. UW additionally operates two open, unauthenticated machine-readable surfaces of real value — an OAI-PMH 2.0 endpoint over the ResearchWorks DSpace 9.2 repository, and a signed SAML 2.0 / Shibboleth identity-provider metadata document registered in InCommon as urn:mace:incommon:washington.edu. No central open-data portal (data.uw.edu / data.washington.edu do not resolve) and no free public developer programme were found.'
examples:
- key_count: 2
  name: University Of Washington Get Course Example
  slug: university-of-washington-get-course-example
- key_count: 2
  name: University Of Washington Get Photo Example
  slug: university-of-washington-get-photo-example
finops:
- name: University Of Washington Finops
  service_category: Education
  slug: university-of-washington-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-washington.png
json_schemas:
- name: Course
  property_count: 16
  slug: university-of-washington-course
- name: Photo
  property_count: 11
  slug: university-of-washington-photo
json_structures:
- name: University Of Washington Course Structure
  property_count: 16
  slug: university-of-washington-course-structure
- name: University Of Washington Photo Structure
  property_count: 11
  slug: university-of-washington-photo-structure
jsonld:
- class_count: 6
  name: University Of Washington Context
  property_count: 3
  slug: university-of-washington-context
layout: provider
modified: '2026-08-30'
name: University of Washington
nav: Providers
network: true
overview: 'University of Washington publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Identity Registration Web Service (IRWS), UW Groups Web Service (GWS), UW Token Authentication Web Service (TAWS), and 26 more. Tagged areas include University, Higher Education, Education, United States, and Washington.


  The University of Washington catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Washington''s developer surface includes GitHub presence, engineering blog, API reference, documentation, support, authentication, and 27 more developer resources.'
plans:
- name: University Of Washington Plans Pricing
  plan_count: 2
  slug: university-of-washington-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: University Of Washington Rate Limits
  slug: university-of-washington-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Washington API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-washington-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of Washington API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: university-of-washington-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.3
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 21.3
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.0
      derived: 26
      marker_coverage: 100.0
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-washington/refs/heads/main/screenshots/university-of-washington-2026-06-20T200317.png
security:
- kind: authentication
  name: University Of Washington Authentication
  slug: university-of-washington-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Washington Domain Security
  slug: university-of-washington-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-washington
tags:
- University
- Higher Education
- Education
- United States
- Washington
- Association of American Universities
- Public Research University
- Research
- Student Information
- Identity
- Identity Federation
- Course Catalog
- Research Repository
- Library
- Enterprise Web Services
website: https://www.washington.edu/
---
