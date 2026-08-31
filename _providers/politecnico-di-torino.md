---
access_model:
  confidence: high
  label: No public onboarding · bearer token issued against a PoliTO institutional account
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - openapi
  - probe
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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Politecnico Di Torino Agentic Access
  operation_count: 132
  slug: politecnico-di-torino-agentic-access
  summary_line: 132 operations · 44 acting
api_count: 3
apis:
- description: Politecnico di Torino's official React Native mobile applications for students and faculty, open-sourced under EUPL-1.2 in the verified @polito GitHub organisation. They are the reference consumers of
  name: PoliTO Students App (mobile backend client)
  slug: students-app
- description: Institutional open-data portal publishing freely reusable academic datasets — study programmes and courses, student enrolment, international students, graduates, mobility and doctoral programmes — und
  name: PoliTO Open Data
  slug: open-data
- description: Machine-readable SAML 2.0 identity-provider metadata for Politecnico di Torino, served from the university's own address space at idp.polito.it (130.192.55.75) and mirrored at idem.polito.it. Verified
  name: Politecnico di Torino Shibboleth Identity Provider (IDEM GARR / eduGAIN)
  slug: identity-federation
- description: OAI-PMH 2.0 harvesting service over IRIS, Politecnico di Torino's institutional research repository, reachable at https://iris.polito.it/oai/request. Verified live on 2026-08-30 across Identify, ListM
  name: IRIS PoliTO OAI-PMH Metadata Service (CINECA deployment)
  slug: iris-oai
- description: Announcements resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in Ty
  name: Politecnico di Torino Announcements API
  slug: politecnico-di-torino-announcements-api
- description: Auth resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec an
  name: Politecnico di Torino Auth API
  slug: politecnico-di-torino-auth-api
- description: Bookings resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpe
  name: Politecnico di Torino Bookings API
  slug: politecnico-di-torino-bookings-api
- description: Courses resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec
  name: Politecnico di Torino Courses API
  slug: politecnico-di-torino-courses-api
- description: Esc resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec an
  name: Politecnico di Torino Esc API
  slug: politecnico-di-torino-esc-api
- description: 'Exams resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec '
  name: Politecnico di Torino Exams API
  slug: politecnico-di-torino-exams-api
- description: Job Offers resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in Type
  name: Politecnico di Torino Job offers API
  slug: politecnico-di-torino-job-offers-api
- description: Lectures resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpe
  name: Politecnico di Torino Lectures API
  slug: politecnico-di-torino-lectures-api
- description: News resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec an
  name: Politecnico di Torino News API
  slug: politecnico-di-torino-news-api
- description: Offering resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSp
  name: Politecnico di Torino Offering API
  slug: politecnico-di-torino-offering-api
- description: 'People resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec '
  name: Politecnico di Torino People API
  slug: politecnico-di-torino-people-api
- description: 'Places resources of the Polito Faculty API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpec '
  name: Politecnico di Torino Places API
  slug: politecnico-di-torino-places-api
- description: Student resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpe
  name: Politecnico di Torino Student API
  slug: politecnico-di-torino-student-api
- description: Surveys resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpe
  name: Politecnico di Torino Surveys API
  slug: politecnico-di-torino-surveys-api
- description: Tickets resources of the Polito Students API, split per tag from openapi/_original/. Operated by Politecnico di Torino on app.didattica.polito.it; the contract is authored by the university in TypeSpe
  name: Politecnico di Torino Tickets API
  slug: politecnico-di-torino-tickets-api
- description: Four keyless JSON web services operated by Politecnico di Torino on its own hosts, found on 2026-08-30 in the client JavaScript behind https://www.polito.it/en/search and probed live. search_people.as
  name: PoliTO Public Search Web Services (people, departments, teachings, rooms)
  slug: public-search-services
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polito Faculty API — Announcements
  slug: open-politecnico-di-torino-announcements-api
- collection_type: open
  name: Polito Faculty API — Auth
  slug: open-politecnico-di-torino-auth-api
- collection_type: open
  name: Polito Faculty API — Bookings
  slug: open-politecnico-di-torino-bookings-api
- collection_type: open
  name: Polito Faculty API — Courses
  slug: open-politecnico-di-torino-courses-api
- collection_type: open
  name: Polito Students API — Esc
  slug: open-politecnico-di-torino-esc-api
- collection_type: open
  name: Polito Students API — Exams
  slug: open-politecnico-di-torino-exams-api
- collection_type: open
  name: Polito Students API — Job offers
  slug: open-politecnico-di-torino-job-offers-api
- collection_type: open
  name: Polito Faculty API — Lectures
  slug: open-politecnico-di-torino-lectures-api
- collection_type: open
  name: Polito Faculty API — News
  slug: open-politecnico-di-torino-news-api
- collection_type: open
  name: Polito Students API — Offering
  slug: open-politecnico-di-torino-offering-api
- collection_type: open
  name: Polito Faculty API — People
  slug: open-politecnico-di-torino-people-api
- collection_type: open
  name: Polito Faculty API — Places
  slug: open-politecnico-di-torino-places-api
- collection_type: open
  name: Polito Students API — Student
  slug: open-politecnico-di-torino-student-api
- collection_type: open
  name: Polito Students API — Surveys
  slug: open-politecnico-di-torino-surveys-api
- collection_type: open
  name: Polito Students API — Tickets
  slug: open-politecnico-di-torino-tickets-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/politecnico-di-torino-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/polito/rn-apps/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/polito/rn-apps/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/polito/rn-apps/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/polito/rn-apps/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/polito/rn-apps/blob/main/LICENSE.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/politecnico-di-torino-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/politecnico-di-torino-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/politecnico-di-torino-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.polito.it/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/polito
- group: company
  title: ''
  type: LinkedIn
  url: https://it.linkedin.com/school/politecnico-di-torino/
- group: other
  title: ''
  type: OpenData
  url: https://www.polito.it/open-data
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/polito/api-spec
- group: commercial
  title: ''
  type: Plans
  url: plans/politecnico-di-torino-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/politecnico-di-torino-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/politecnico-di-torino-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/polito/api-spec
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/polito/api-spec/master/dist/clients/student/openapi.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/polito/api-spec/master/dist/clients/faculty/openapi.yaml
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.polito.it/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://iris.polito.it/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.polito.it/en/education
- group: operate
  title: ''
  type: Status
  url: https://status.polito.it/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polito.it/en/privacy
- group: design
  title: ''
  type: x-conformance
  url: conformance/politecnico-di-torino-conformance.yml
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.polito.it/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://mypoli.polito.it/dotnet/ws_anagrafe/search_teachings.ashx?_lang=en&q=ingegneria
created: '2026-06-03'
description: 'Politecnico di Torino (PoliTO) is Italy''s oldest technical university, founded in Turin in 1859, with roughly 38,000 students across engineering, architecture and design. Unusually for this cohort, its programmable footprint is genuinely its own rather than a vendor''s: the university publishes the OpenAPI definition of the REST API behind its official student and faculty mobile applications in the verified @polito GitHub organisation (polito/api-spec, authored in TypeSpec and emitted as two client contracts, Polito Faculty API and Polito Students API), and the React Native apps that consume it are open-sourced under EUPL-1.2 in polito/rn-apps and polito/students-app. That API runs on the university''s own host, app.didattica.polito.it, and covers announcements, authentication with MFA, room and slot bookings, courses, lectures, news, people, places, exams, grades, degree offering, job offers, surveys, support tickets and the European Student Card. It is not a self-service
  developer programme: the production base path returns 403 to an anonymous caller, every operation is bearer authenticated against a PoliTO account, and no key can be requested by an outsider. Two further institution-operated machine-readable surfaces exist and are recorded here for the first time — a Shibboleth SAML 2.0 identity provider registered in IDEM GARR and eduGAIN since 2020, and an OAI-PMH 2.0 harvesting service over the IRIS research repository, the latter a CINECA tenant deployment rather than PoliTO engineering. A fourth institution-operated surface was found on 2026-08-30 and is the only one an outsider can actually call: four keyless JSON web services behind the polito.it site search — staff, departments and teachings at mypoli.polito.it/dotnet/ws_anagrafe and a campus room locator at legacyprod.polito.it — all returning HTTP 200 and real data with no credential, on hosts inside the university''s own GARR address space. They are undocumented and unversioned, PoliTO does
  not present them as a developer product, and the OpenAPI held here is derived from probing rather than published. The university also runs HPC@PoliTO, an academic computing service managed in-house, whose allocation process is entirely by email with no programmatic surface. The institutional open-data portal publishes downloadable datasets only, with no API behind it, and there is no data.polito.it or api.polito.it host in service.'
examples:
- key_count: 5
  name: Politecnico Di Torino Getannouncements Example
  slug: politecnico-di-torino-getAnnouncements-example
- key_count: 5
  name: Politecnico Di Torino Getexams Example
  slug: politecnico-di-torino-getExams-example
- key_count: 5
  name: Politecnico Di Torino Getstudent Example
  slug: politecnico-di-torino-getStudent-example
finops:
- name: Politecnico Di Torino Finops
  service_category: Education
  slug: politecnico-di-torino-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/politecnico-di-torino.png
json_schemas:
- name: Announcement
  property_count: 8
  slug: politecnico-di-torino-announcement
- name: Booking
  property_count: 9
  slug: politecnico-di-torino-booking
- name: Exam
  property_count: 17
  slug: politecnico-di-torino-exam
- name: Student
  property_count: 20
  slug: politecnico-di-torino-student
json_structures:
- name: Politecnico Di Torino Exam Structure
  property_count: 17
  slug: politecnico-di-torino-exam-structure
- name: Politecnico Di Torino Student Structure
  property_count: 20
  slug: politecnico-di-torino-student-structure
jsonld:
- class_count: 33
  name: Politecnico Di Torino Context
  property_count: 5
  slug: politecnico-di-torino-context
layout: provider
modified: '2026-08-30'
name: Politecnico di Torino
nav: Providers
network: true
overview: 'Politecnico di Torino publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Announcements API, Auth API, Bookings API, and 13 more. Tagged areas include Education, Higher Education, University, Technical University, and Italy.


  The Politecnico di Torino catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Politecnico di Torino''s developer surface includes authentication, GitHub presence, documentation, status page, and 25 more developer resources.'
plans:
- name: Politecnico Di Torino Plans Pricing
  plan_count: 2
  slug: politecnico-di-torino-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Politecnico Di Torino Rate Limits
  slug: politecnico-di-torino-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Politecnico di Torino API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: politecnico-di-torino-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Politecnico di Torino API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: politecnico-di-torino-rules
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 61.0
    developer_ergonomics: 21.4
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 85.0
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/politecnico-di-torino/refs/heads/main/screenshots/politecnico-di-torino-2026-06-20T191855.png
security:
- kind: authentication
  name: Politecnico Di Torino Authentication
  slug: politecnico-di-torino-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Politecnico Di Torino Domain Security
  slug: politecnico-di-torino-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: politecnico-di-torino
tags:
- Education
- Higher Education
- University
- Technical University
- Italy
- Course Catalog
- Research Data
- Identity Federation
- Open Data
- Mobile
- OpenAPI
website: https://www.polito.it/en
---
