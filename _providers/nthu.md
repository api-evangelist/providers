---
access_model:
  confidence: high
  label: Free · public and keyless on the tenant data API, application-gated on the institution's own OAuth service
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - https://oauth.ccxp.nthu.edu.tw/v1.1/doc/
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nthu Agentic Access
  operation_count: 23
  slug: nthu-agentic-access
  summary_line: 23 operations · 1 acting
api_count: 1
apis:
- description: The one API National Tsing Hua University operates itself. An OAuth 2.0 authorization-code service run by the Computer and Communication Center on NTHU's own host, letting a reviewed external applicat
  name: NTHU Academic Information System OAuth 2.0 Service
  slug: nthu-oauth-api
- description: A live, keyless, MIT-licensed FastAPI service publishing 22 paths over NTHU campus data — announcements by unit, campus bus routes and schedules, the course catalog and course search, department direc
  name: NTHU Data API
  slug: nthu-data-api
- description: NTHU's institutional research repository and researcher-profile portal, running on Ex Libris Esploro. The former institutional repository host nthur.lib.nthu.edu.tw now redirects here. An OAI-PMH serv
  name: NTHU Research Portal (Esploro tenant)
  slug: nthu-research-portal
- description: 'NTHU Library''s discovery service on Ex Libris Primo VE. Notable for what it reveals rather than what it offers: its sign-in link declares authenticationProfile=NTHU_SAML and auth=SAML, which is the on'
  name: NTHU Library Discovery (Primo VE tenant)
  slug: nthu-library-discovery
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NTHU Data Announcements API
  slug: open-nthu-announcements-api
- collection_type: open
  name: NTHU Data Announcements Buses API
  slug: open-nthu-buses-api
- collection_type: open
  name: NTHU Data Announcements Courses API
  slug: open-nthu-courses-api
- collection_type: open
  name: NTHU Data Announcements Departments API
  slug: open-nthu-departments-api
- collection_type: open
  name: NTHU Data Announcements Dining API
  slug: open-nthu-dining-api
- collection_type: open
  name: NTHU Data Announcements Energy API
  slug: open-nthu-energy-api
- collection_type: open
  name: NTHU Data Announcements Libraries API
  slug: open-nthu-libraries-api
- collection_type: open
  name: NTHU Data Announcements Locations API
  slug: open-nthu-locations-api
- collection_type: open
  name: NTHU Data Announcements Newsletters API
  slug: open-nthu-newsletters-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.nthu.edu.tw/
- group: company
  title: ''
  type: Website
  url: https://nthu-en.site.nthu.edu.tw/
- group: docs
  title: ''
  type: Documentation
  url: https://oauth.ccxp.nthu.edu.tw/v1.1/doc/
- group: docs
  title: ''
  type: APIReference
  url: https://api.nthusa.tw/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://law.site.nthu.edu.tw/p/406-1326-197509,r6923.php
- group: other
  title: ''
  type: IdentityFederation
  url: https://oauth.ccxp.nthu.edu.tw/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholars.nthu.edu.tw/esploro/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://nthu.primo.exlibrisgroup.com/discovery/search?vid=886UST_NTHU
- group: learn
  title: ''
  type: CourseCatalog
  url: https://curricul.site.nthu.edu.tw/
- group: other
  title: ''
  type: AIPolicy
  url: https://curricul.site.nthu.edu.tw/p/404-1208-248357.php?Lang=zh-tw
- group: other
  title: ''
  type: AIPolicy
  url: https://ctld.site.nthu.edu.tw/p/450-1217-253458,c0.php?Lang=zh-tw
- group: operate
  title: ''
  type: Support
  url: https://ccc.site.nthu.edu.tw/
- group: operate
  title: ''
  type: Support
  url: https://net.nthu.edu.tw/netsys/service:portal:login_from_ccxp
- group: build
  title: ''
  type: GitHub
  url: https://github.com/NTHU-SA
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nthumodifications
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-tsing-hua-university/
- group: commercial
  title: ''
  type: License
  url: https://github.com/NTHU-SA/NTHU-Data-API/blob/main/LICENSE
- group: auth
  title: ''
  type: Authentication
  url: authentication/nthu-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/nthu-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/nthu-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nthu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nthu-conformance.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nthu-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nthu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nthu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nthu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nthu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nthu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'National Tsing Hua University (NTHU) is a national public research university in Hsinchu, Taiwan, founded in Beijing in 1911 and re-established in Taiwan in 1956. It has no central developer portal, no API catalog and no institution-wide API program, and this profile is deliberately small because the honest footprint is small. It does, however, hold something most of this cohort does not: one genuinely institution-operated, institution-governed API. NTHU''s Computer and Communication Center runs an OAuth 2.0 authorization and identity service at oauth.ccxp.nthu.edu.tw, fronting the Academic Information System (CCXP), documented by the university in its own interface manual, governed by a regulation passed by the Computer and Communication Committee in December 2020, and carrying a published scheduled repeal date of 2027-07-31. It is not self-service — a request needs a unit head''s signature, Computer and Communication Center review, and sign-off from every unit that owns a
  requested data field — but it is NTHU''s own engineering on NTHU''s own host. Everything else programmable that carries NTHU''s name is operated by someone else. The widely cited NTHU Data API, a live FastAPI service with an OpenAPI 3.1.0 description and 22 keyless public paths over campus announcements, buses, courses, departments, dining, energy, library spaces, locations and newsletters, is built and hosted by the NTHU Student Association on nthusa.tw, not by the university on nthu.edu.tw. The research portal at scholars.nthu.edu.tw is an Ex Libris Esploro tenant, and the library discovery service is an Ex Libris Primo VE tenant shared through the University System of Taiwan consortium. Those are real institutional facts and they are recorded as tenant relationships, but they are not NTHU''s contracts and are not scored as such.'
examples:
- key_count: 4
  name: Nthu Getbusroutedata Example
  slug: nthu-getBusRouteData-example
- key_count: 4
  name: Nthu Searchcoursesbycondition_Request Example
  slug: nthu-searchCoursesByCondition_request-example
finops:
- name: Nthu Finops
  service_category: Education
  slug: nthu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nthu.png
json_schemas:
- name: AnnouncementDetail
  property_count: 5
  slug: nthu-announcement
- name: BusInfo
  property_count: 4
  slug: nthu-bus
- name: CourseData
  property_count: 19
  slug: nthu-course
- name: Department
  property_count: 4
  slug: nthu-department
- name: DiningRestaurant
  property_count: 6
  slug: nthu-dining-restaurant
- name: EnergyElectricityInfo
  property_count: 5
  slug: nthu-energy
- name: LibrarySpace
  property_count: 5
  slug: nthu-library-space
- name: LocationDetail
  property_count: 3
  slug: nthu-location
json_structures:
- name: Nthu Bus Structure
  property_count: 4
  slug: nthu-bus-structure
- name: Nthu Course Structure
  property_count: 7
  slug: nthu-course-structure
- name: Nthu Energy Structure
  property_count: 5
  slug: nthu-energy-structure
- name: Nthu Library Space Structure
  property_count: 5
  slug: nthu-library-space-structure
- name: Nthu Location Structure
  property_count: 3
  slug: nthu-location-structure
jsonld:
- class_count: 20
  name: Nthu Context
  property_count: 12
  slug: nthu-context
layout: provider
modified: '2026-08-30'
name: National Tsing Hua University
nav: Providers
network: true
overview: 'National Tsing Hua University publishes 2 APIs on the [APIs.io](https://apis.io/) network: NTHU Academic Information System OAuth 2.0 Service and NTHU Data API. Tagged areas include Education, Higher Education, University, Taiwan, and Public Research University.


  The National Tsing Hua University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  National Tsing Hua University''s developer surface includes documentation, API reference, support, GitHub presence, authentication, and 24 more developer resources.'
plans:
- name: Nthu Plans Pricing
  plan_count: 2
  slug: nthu-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Nthu Rate Limits
  slug: nthu-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: National Tsing Hua University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nthu-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: National Tsing Hua University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 2
    info: 0
    warn: 2
  slug: nthu-rules
scopes:
- name: Nthu Scopes
  scope_count: 6
  slug: nthu-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 39.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 43.2
    contract_quality: 59.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 43.2
    operational_transparency: 26.3
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nthu/refs/heads/main/screenshots/nthu-2026-06-20T190502.png
security:
- kind: authentication
  name: Nthu Authentication
  slug: nthu-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Nthu Domain Security
  slug: nthu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nthu
tags:
- Education
- Higher Education
- University
- Taiwan
- Public Research University
- Identity
- Authentication
- Open Data
- Campus
- Course Catalog
- Research Repository
- Library
website: https://www.nthu.edu.tw/
---
