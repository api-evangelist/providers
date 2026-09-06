---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
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
  score: 22.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Paradox Agentic Access
  operation_count: 59
  slug: paradox-agentic-access
  summary_line: 59 operations · 34 acting
api_count: 1
apis:
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: OAuth 2.0 token and JWT verification endpoints
  name: Paradox Authentication API
  slug: paradox-authentication-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage custom candidate attribute data
  name: Paradox Candidate Attributes API
  slug: paradox-candidate-attributes-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage candidates including creating, retrieving, updating, deleting, messaging, and unsubscribing
  name: Paradox Candidates API
  slug: paradox-candidates-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Access company-level data including conversations, groups, schools, areas, and AI assistant
  name: Paradox Company API
  slug: paradox-company-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage location areas
  name: Paradox Location Areas API
  slug: paradox-location-areas-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage location rooms
  name: Paradox Location Rooms API
  slug: paradox-location-rooms-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage locations including creating, retrieving, updating, deleting, and lookup by job location code
  name: Paradox Locations API
  slug: paradox-locations-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Access and generate reports
  name: Paradox Reporting API
  slug: paradox-reporting-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage interview scheduling, interviewers, settings, rooms, alerts, and history
  name: Paradox Scheduling API
  slug: paradox-scheduling-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage user location permissions
  name: Paradox User Permissions API
  slug: paradox-user-permissions-api
- baseURL: https://api.paradox.ai
  baseurl_source: declared
  description: Manage users including creating, retrieving, updating, deleting, deactivating, and reactivating
  name: Paradox Users API
  slug: paradox-users-api
artifact_total: 69
collections:
- collection_type: postman
  name: Paradox Authentication API
  slug: postman-paradox-authentication-api
- collection_type: postman
  name: Paradox Authentication Candidate Attributes API
  slug: postman-paradox-candidate-attributes-api
- collection_type: postman
  name: Paradox Authentication Candidates API
  slug: postman-paradox-candidates-api
- collection_type: postman
  name: Paradox Authentication Company API
  slug: postman-paradox-company-api
- collection_type: postman
  name: Paradox Authentication Location Areas API
  slug: postman-paradox-location-areas-api
- collection_type: postman
  name: Paradox Authentication Location Rooms API
  slug: postman-paradox-location-rooms-api
- collection_type: postman
  name: Paradox Authentication Locations API
  slug: postman-paradox-locations-api
- collection_type: postman
  name: Paradox Authentication Reporting API
  slug: postman-paradox-reporting-api
- collection_type: postman
  name: Paradox Authentication Scheduling API
  slug: postman-paradox-scheduling-api
- collection_type: postman
  name: Paradox Authentication User Permissions API
  slug: postman-paradox-user-permissions-api
- collection_type: postman
  name: Paradox Authentication Users API
  slug: postman-paradox-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Paradox API
  slug: open-paradox-api
- collection_type: open
  name: Paradox Authentication API
  slug: open-paradox-authentication-api
- collection_type: open
  name: Paradox Authentication Candidate Attributes API
  slug: open-paradox-candidate-attributes-api
- collection_type: open
  name: Paradox Authentication Candidates API
  slug: open-paradox-candidates-api
- collection_type: open
  name: Paradox Authentication Company API
  slug: open-paradox-company-api
- collection_type: open
  name: Paradox Authentication Location Areas API
  slug: open-paradox-location-areas-api
- collection_type: open
  name: Paradox Authentication Location Rooms API
  slug: open-paradox-location-rooms-api
- collection_type: open
  name: Paradox Authentication Locations API
  slug: open-paradox-locations-api
- collection_type: open
  name: Paradox Authentication Reporting API
  slug: open-paradox-reporting-api
- collection_type: open
  name: Paradox Authentication Scheduling API
  slug: open-paradox-scheduling-api
- collection_type: open
  name: Paradox Authentication User Permissions API
  slug: open-paradox-user-permissions-api
- collection_type: open
  name: Paradox Authentication Users API
  slug: open-paradox-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/paradox-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/paradox/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/paradox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paradox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/paradox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paradox-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ParadoxAI
- group: start
  title: ''
  type: Portal
  url: https://readme.paradox.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://readme.paradox.ai/docs
- group: auth
  title: ''
  type: Authentication
  url: https://readme.paradox.ai/reference/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://readme.paradox.ai/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paradox.ai/
- group: start
  title: ''
  type: Login
  url: https://olivia.paradox.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paradox.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paradox.ai/legal/service-terms
- group: auth
  title: ''
  type: Security
  url: https://www.paradox.ai/legal/security
- group: operate
  title: ''
  type: FAQ
  url: https://www.paradox.ai/faqs
- group: operate
  title: ''
  type: Contact
  url: https://www.paradox.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.paradox.ai/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paradoxolivia
- group: company
  title: ''
  type: About
  url: https://www.paradox.ai/about
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/paradox-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/paradox-candidate-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/paradox-context.jsonld
created: '2025-01-01'
description: APIs and resources for Paradox, a conversational AI recruiting assistant platform powered by Olivia, an AI assistant that automates candidate screening, interview scheduling, and hiring workflows through chat, SMS, and mobile-driven experiences.
finops:
- name: Paradox Finops
  service_category: HR Technology
  slug: paradox-finops
image: https://www.paradox.ai/images/paradox-logo.png
json_schemas:
- name: AiAssistant
  property_count: 3
  slug: paradox-aiassistant
- name: Area
  property_count: 4
  slug: paradox-area
- name: AreaCreate
  property_count: 2
  slug: paradox-areacreate
- name: Paradox Candidate
  property_count: 45
  slug: paradox-candidate
- name: CandidateCreate
  property_count: 43
  slug: paradox-candidatecreate
- name: CandidateUpdate
  property_count: 28
  slug: paradox-candidateupdate
- name: Conversation
  property_count: 6
  slug: paradox-conversation
- name: Group
  property_count: 2
  slug: paradox-group
- name: Interview
  property_count: 11
  slug: paradox-interview
- name: Interviewer
  property_count: 4
  slug: paradox-interviewer
- name: InterviewSettings
  property_count: 5
  slug: paradox-interviewsettings
- name: Location
  property_count: 12
  slug: paradox-location
- name: LocationCreate
  property_count: 8
  slug: paradox-locationcreate
- name: LocationPermission
  property_count: 3
  slug: paradox-locationpermission
- name: LocationUpdate
  property_count: 9
  slug: paradox-locationupdate
- name: Report
  property_count: 6
  slug: paradox-report
- name: Role
  property_count: 3
  slug: paradox-role
- name: Room
  property_count: 5
  slug: paradox-room
- name: RoomCreate
  property_count: 2
  slug: paradox-roomcreate
- name: SchoolArea
  property_count: 3
  slug: paradox-schoolarea
- name: SuccessResponse
  property_count: 1
  slug: paradox-successresponse
- name: User
  property_count: 14
  slug: paradox-user
- name: UserCreate
  property_count: 8
  slug: paradox-usercreate
- name: UserUpdate
  property_count: 8
  slug: paradox-userupdate
json_structures:
- name: Paradox Structure
  property_count: 0
  slug: paradox-structure
jsonld:
- class_count: 0
  name: Paradox Context
  property_count: 9
  slug: paradox-context
layout: provider
modified: '2026-05-19'
name: Paradox
nav: Providers
network: true
overview: 'Paradox publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Candidate Attributes API, Candidates API, and 8 more. Tagged areas include Artificial Intelligence, Candidate Screening, Chatbots, Conversational AI, and Hiring Automation.


  The Paradox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Paradox''s developer surface includes authentication, developer portal, documentation, changelog, FAQ, engineering blog, and 18 more developer resources.'
plans:
- name: Paradox Plans Pricing
  plan_count: 1
  slug: paradox-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Paradox Rate Limits
  slug: paradox-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Paradox API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: paradox-jsonschema-spectral-rules
scopes:
- name: Paradox Scopes
  scope_count: 0
  slug: paradox-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.3
    catalog_earned_first_party: 0.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 9.8
    contract_quality: 65.1
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paradox/refs/heads/main/screenshots/paradox-2026-06-20T191353.png
security:
- kind: authentication
  name: Paradox Authentication
  slug: paradox-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Paradox Domain Security
  slug: paradox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paradox
tags:
- Artificial Intelligence
- Candidate Screening
- Chatbots
- Conversational AI
- Hiring Automation
- HR Technology
- Interview Scheduling
- Recruiting
- SMS
- Talent Acquisition
website: https://readme.paradox.ai/
---
