---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Google Classroom Agentic Access
  operation_count: 23
  slug: google-classroom-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- baseURL: https://classroom.googleapis.com
  baseurl_source: declared
  description: The Courses API from Google Classroom — 9 operation(s) for courses.
  name: Google Classroom Courses API
  slug: google-classroom-courses-api
- baseURL: https://classroom.googleapis.com
  baseurl_source: declared
  description: The Invitations API from Google Classroom — 1 operation(s) for invitations.
  name: Google Classroom Invitations API
  slug: google-classroom-invitations-api
- baseURL: https://classroom.googleapis.com
  baseurl_source: declared
  description: The userProfiles API from Google Classroom — 1 operation(s) for userprofiles.
  name: Google Classroom userProfiles API
  slug: google-classroom-userprofiles-api
artifact_total: 19
collections:
- collection_type: postman
  name: Google Classroom Courses API
  slug: postman-google-classroom-courses-api
- collection_type: postman
  name: Google Classroom Courses Invitations API
  slug: postman-google-classroom-invitations-api
- collection_type: postman
  name: Google Classroom Courses userProfiles API
  slug: postman-google-classroom-userprofiles-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Classroom Courses API
  slug: open-google-classroom-courses-api
- collection_type: open
  name: Google Classroom Courses Invitations API
  slug: open-google-classroom-invitations-api
- collection_type: open
  name: Google Classroom Courses userProfiles API
  slug: open-google-classroom-userprofiles-api
- collection_type: open
  name: Google Classroom API
  slug: open-openapi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/google-classroom-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-classroom/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-classroom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-classroom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-classroom-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/classroom
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/classroom/guides/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: commercial
  title: ''
  type: Pricing
  url: https://edu.google.com/workspace-for-education/editions/overview/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/classroom/support
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Classroom API provides programmatic access to Google Classroom, enabling management of courses, coursework, student submissions, rosters, and invitations. It supports creating and organizing courses, distributing assignments and materials, managing student and teacher enrollments, tracking submissions and grades, and integrating with third-party educational tools through add-on attachments.
finops:
- name: Google Classroom Finops
  service_category: API
  slug: google-classroom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-classroom.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 7
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Classroom
nav: Providers
network: true
overview: 'Google Classroom publishes 3 APIs on the [APIs.io](https://apis.io/) network: Courses API, Invitations API, and userProfiles API. Tagged areas include Assignments, Classroom, Courses, Education, and Google.


  The Google Classroom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Classroom''s developer surface includes developer portal, getting-started guide, authentication, pricing, support, engineering blog, and 10 more developer resources.'
plans:
- name: Google Classroom Plans Pricing
  plan_count: 3
  slug: google-classroom-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Google Classroom Rate Limits
  slug: google-classroom-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Classroom API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-classroom-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 61.2
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-classroom/refs/heads/main/screenshots/google-classroom-2026-06-20T182040.png
security:
- kind: domain-security
  name: Google Classroom Domain Security
  slug: google-classroom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Classroom Vulnerability Disclosure
  slug: google-classroom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-classroom
tags:
- Assignments
- Classroom
- Courses
- Education
- Google
- Google Workspace
- Students
website: https://developers.google.com/workspace/classroom
---
