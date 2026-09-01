---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
  score: 24.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 31
  human_in_the_loop: 2
  name: Talentlms Agentic Access
  operation_count: 63
  slug: talentlms-agentic-access
  summary_line: 63 operations · 31 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'REST API for TalentLMS providing programmatic access to users, courses, categories, branches, groups, enrollments, and reporting data including test and survey results. Over 50 endpoints support full '
  name: TalentLMS API
  slug: talentlms-api
- description: This section introduces endpoints that perform bulk actions. After invoking any of the below endpoints, their response includes a background task ID.. You can use the `GET api/v2/tasks/:id` endpoint t
  name: TalentLMS Batch Actions API
  slug: talentlms-batch-actions-api
- description: The Branch API from TalentLMS — 5 operation(s) for branch.
  name: TalentLMS Branch API
  slug: talentlms-branch-api
- description: The Category API from TalentLMS — 3 operation(s) for category.
  name: TalentLMS Category API
  slug: talentlms-category-api
- description: The Course API from TalentLMS — 6 operation(s) for course.
  name: TalentLMS Course API
  slug: talentlms-course-api
- description: The Group API from TalentLMS — 5 operation(s) for group.
  name: TalentLMS Group API
  slug: talentlms-group-api
- description: The Learning Paths API from TalentLMS — 3 operation(s) for learning paths.
  name: TalentLMS Learning Paths API
  slug: talentlms-learning-paths-api
- description: The Portal API from TalentLMS — 2 operation(s) for portal.
  name: TalentLMS Portal API
  slug: talentlms-portal-api
- description: The Task API from TalentLMS — 1 operation(s) for task.
  name: TalentLMS Task API
  slug: talentlms-task-api
- description: The Timeline API from TalentLMS — 1 operation(s) for timeline.
  name: TalentLMS Timeline API
  slug: talentlms-timeline-api
- description: The Unit API from TalentLMS — 2 operation(s) for unit.
  name: TalentLMS Unit API
  slug: talentlms-unit-api
- description: The User API from TalentLMS — 16 operation(s) for user.
  name: TalentLMS User API
  slug: talentlms-user-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TalentLMS Public Batch Actions API
  slug: open-talentlms-batch-actions-api
- collection_type: open
  name: TalentLMS Public Batch Actions Branch API
  slug: open-talentlms-branch-api
- collection_type: open
  name: TalentLMS Public Batch Actions Category API
  slug: open-talentlms-category-api
- collection_type: open
  name: TalentLMS Public Batch Actions Course API
  slug: open-talentlms-course-api
- collection_type: open
  name: TalentLMS Public Batch Actions Group API
  slug: open-talentlms-group-api
- collection_type: open
  name: TalentLMS Public Batch Actions Learning Paths API
  slug: open-talentlms-learning-paths-api
- collection_type: open
  name: TalentLMS Public Batch Actions Portal API
  slug: open-talentlms-portal-api
- collection_type: open
  name: TalentLMS Public Batch Actions Task API
  slug: open-talentlms-task-api
- collection_type: open
  name: TalentLMS Public Batch Actions Timeline API
  slug: open-talentlms-timeline-api
- collection_type: open
  name: TalentLMS Public Batch Actions Unit API
  slug: open-talentlms-unit-api
- collection_type: open
  name: TalentLMS Public Batch Actions User API
  slug: open-talentlms-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/talentlms-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Trifoia/talentlms-sdk/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Trifoia/talentlms-sdk/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talentlms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talentlms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talentlms-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developers.talentlms.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.talentlms.com/hc/en-us/articles/24874457011356-TalentLMS-API-V2
- group: build
  title: ''
  type: PostmanCollection
  url: https://documenter.getpostman.com/view/31867199/2sAY548Kou
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talentlms.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.talentlms.com/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.talentlms.com/hc/en-us/sections/9593869767452-Product-News
- group: operate
  title: ''
  type: Support
  url: https://help.talentlms.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://www.talentlms.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.talentlms.com/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/talentlms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talentlms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talentlms-finops.yml
created: '2026-06-13'
description: TalentLMS is a cloud-based learning management system (LMS) with a REST API for managing users, courses, categories, branches, groups, and enrollments, as well as accessing completion and assessment report data. The API supports over 50 endpoints covering user and course lifecycle management, group and branch administration, and retrieval of test and survey results. Authentication uses API key-based HTTP Basic Auth on V1 and header-based API keys on V2. TalentLMS V2 introduces versioned requests, clear rate-limit response headers, and a dedicated developer hub.
finops:
- name: Talentlms Finops
  service_category: ''
  slug: talentlms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talentlms.png
json_schemas:
- name: getuserbranches-response-200
  property_count: 1
  slug: getuserbranches-response-200
- name: getuserbyid-response-200
  property_count: 1
  slug: getuserbyid-response-200
- name: getusercertificates-response-200
  property_count: 1
  slug: getusercertificates-response-200
- name: getusercourses-response-200
  property_count: 1
  slug: getusercourses-response-200
- name: getusergroups-response-200
  property_count: 1
  slug: getusergroups-response-200
- name: getuserresources-response-200
  property_count: 1
  slug: getuserresources-response-200
- name: GroupCourseItem
  property_count: 3
  slug: groupcourseitem
- name: PaginationLinks
  property_count: 5
  slug: paginationlinks
- name: PaginationMeta
  property_count: 1
  slug: paginationmeta
- name: UserGamification
  property_count: 3
  slug: usergamification
- name: UserGamificationBadge
  property_count: 6
  slug: usergamificationbadge
- name: UserListItem
  property_count: 14
  slug: userlistitem
jsonld:
- class_count: 0
  name: Talentlms Context
  property_count: 0
  slug: talentlms
layout: provider
modified: '2026-06-13'
name: TalentLMS
nav: Providers
network: true
overview: 'TalentLMS publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Batch Actions API, Branch API, and 10 more. Tagged areas include Learning Management System, LMS, E-Learning, Training, and Courses.


  The TalentLMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TalentLMS''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, release notes, support, and 11 more developer resources.'
plans:
- name: Talentlms Plans Pricing
  plan_count: 5
  slug: talentlms-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Talentlms Rate Limits
  slug: talentlms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TalentLMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: talentlms-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 9.8
    contract_quality: 50.6
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 0.0
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/talentlms/refs/heads/main/screenshots/talentlms-2026-06-20T194902.png
security:
- kind: authentication
  name: Talentlms Authentication
  slug: talentlms-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Talentlms Domain Security
  slug: talentlms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talentlms
tags:
- Learning Management System
- LMS
- E-Learning
- Training
- Courses
- User
- Enrollments
- Education
- HR Tech
- Cloud
website: https://developers.talentlms.io/
---
