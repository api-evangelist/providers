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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 2
  name: University Of Pennsylvania Agentic Access
  operation_count: 68
  slug: university-of-pennsylvania-agentic-access
  summary_line: 68 operations · 30 acting · 2 human-in-the-loop
api_count: 32
apis:
- description: Penn's institutional OpenData platform (an ISC enterprise service bus) providing access to Registrar/course, Dining, Directory, Transit, News, Events, Maps, Calendar, and Laundry data. Most services r
  name: Penn OpenData API
  slug: opendata
- description: Open-source Python module maintained by Penn Labs that wraps the Penn OpenData services (Registrar, Dining, Directory and more). A validated OpenData API token is required for most calls.
  name: Penn SDK (Python)
  slug: penn-sdk-python
- description: Open-source JavaScript/Node SDK from Penn Labs for the Penn OpenData API.
  name: Penn OpenData Node SDK
  slug: penn-sdk-js
- description: These routes allow interaction with the User object of a Penn Labs Accounts user. We do not document `/accounts/...` authentication routes here, as they are described by the [Authentication](#section/
  name: University of Pennsylvania [Accounts] User API
  slug: university-of-pennsylvania-accounts-user-api
- description: As the main API endpoints for PCA, these routes allow interaction with the user's PCA registrations. An important concept which is referenced throughout the documentation for these routes is that of t
  name: University of Pennsylvania [PCA] Registration API
  slug: university-of-pennsylvania-pca-registration-api
- description: These routes expose a user's registration history (including inactive and obsolete registrations) for the current semester. Inactive registrations are registrations which would not trigger a notificat
  name: University of Pennsylvania [PCA] Registration History API
  slug: university-of-pennsylvania-pca-registration-history-api
- description: The [PCP] Break API from University of Pennsylvania — 2 operation(s) for [pcp] break.
  name: University of Pennsylvania [PCP] Break API
  slug: university-of-pennsylvania-pcp-break-api
- description: The [PCP] Calendar API from University of Pennsylvania — 1 operation(s) for [pcp] calendar.
  name: University of Pennsylvania [PCP] Calendar API
  slug: university-of-pennsylvania-pcp-calendar-api
- description: The [PCP] Course Recommendations API from University of Pennsylvania — 1 operation(s) for [pcp] course recommendations.
  name: University of Pennsylvania [PCP] Course Recommendations API
  slug: university-of-pennsylvania-pcp-course-recommendations-api
- description: The [PCP] Primary Schedule API from University of Pennsylvania — 2 operation(s) for [pcp] primary schedule.
  name: University of Pennsylvania [PCP] Primary Schedule API
  slug: university-of-pennsylvania-pcp-primary-schedule-api
- description: These routes allow interfacing with the user's PCP Schedules for the current semester, stored on the backend. Ever since we integrated Penn Labs Accounts into PCP so that users can store their schedul
  name: University of Pennsylvania [PCP] Schedule API
  slug: university-of-pennsylvania-pcp-schedule-api
- description: The [PCR] Autocomplete Dump API from University of Pennsylvania — 1 operation(s) for [pcr] autocomplete dump.
  name: University of Pennsylvania [PCR] Autocomplete Dump API
  slug: university-of-pennsylvania-pcr-autocomplete-dump-api
- description: The [PCR] Course Reviews API from University of Pennsylvania — 1 operation(s) for [pcr] course reviews.
  name: University of Pennsylvania [PCR] Course Reviews API
  slug: university-of-pennsylvania-pcr-course-reviews-api
- description: The [PCR] Department Reviews API from University of Pennsylvania — 1 operation(s) for [pcr] department reviews.
  name: University of Pennsylvania [PCR] Department Reviews API
  slug: university-of-pennsylvania-pcr-department-reviews-api
- description: The [PCR] Instructor Reviews API from University of Pennsylvania — 1 operation(s) for [pcr] instructor reviews.
  name: University of Pennsylvania [PCR] Instructor Reviews API
  slug: university-of-pennsylvania-pcr-instructor-reviews-api
- description: The [PCR] Plots API from University of Pennsylvania — 1 operation(s) for [pcr] plots.
  name: University of Pennsylvania [PCR] Plots API
  slug: university-of-pennsylvania-pcr-plots-api
- description: The [PCR] Section-Specific Reviews API from University of Pennsylvania — 1 operation(s) for [pcr] section-specific reviews.
  name: University of Pennsylvania [PCR] Section-Specific Reviews API
  slug: university-of-pennsylvania-pcr-section-specific-reviews-api
- description: The [PCx] Attributes API from University of Pennsylvania — 1 operation(s) for [pcx] attributes.
  name: University of Pennsylvania [PCx] Attributes API
  slug: university-of-pennsylvania-pcx-attributes-api
- description: The [PCx] Course API from University of Pennsylvania — 3 operation(s) for [pcx] course.
  name: University of Pennsylvania [PCx] Course API
  slug: university-of-pennsylvania-pcx-course-api
- description: The [PCx] Friendship API from University of Pennsylvania — 1 operation(s) for [pcx] friendship.
  name: University of Pennsylvania [PCx] Friendship API
  slug: university-of-pennsylvania-pcx-friendship-api
- description: The [PCx] Healths API from University of Pennsylvania — 1 operation(s) for [pcx] healths.
  name: University of Pennsylvania [PCx] Healths API
  slug: university-of-pennsylvania-pcx-healths-api
- description: The [PCx] NGSS Restrictions API from University of Pennsylvania — 1 operation(s) for [pcx] ngss restrictions.
  name: University of Pennsylvania [PCx] NGSS Restrictions API
  slug: university-of-pennsylvania-pcx-ngss-restrictions-api
- description: The [PCx] Pre-NGSS Requirements API from University of Pennsylvania — 1 operation(s) for [pcx] pre-ngss requirements.
  name: University of Pennsylvania [PCx] Pre-NGSS Requirements API
  slug: university-of-pennsylvania-pcx-pre-ngss-requirements-api
- description: The [PCx] Section API from University of Pennsylvania — 2 operation(s) for [pcx] section.
  name: University of Pennsylvania [PCx] Section API
  slug: university-of-pennsylvania-pcx-section-api
- description: The [PCx] Status Updates API from University of Pennsylvania — 1 operation(s) for [pcx] status updates.
  name: University of Pennsylvania [PCx] Status Updates API
  slug: university-of-pennsylvania-pcx-status-updates-api
- description: The [PDP] Degree API from University of Pennsylvania — 2 operation(s) for [pdp] degree.
  name: University of Pennsylvania [PDP] Degree API
  slug: university-of-pennsylvania-pdp-degree-api
- description: The [PDP] Degree Plan Detail API from University of Pennsylvania — 4 operation(s) for [pdp] degree plan detail.
  name: University of Pennsylvania [PDP] Degree Plan Detail API
  slug: university-of-pennsylvania-pdp-degree-plan-detail-api
- description: The [PDP] Degree Plan Lists API from University of Pennsylvania — 1 operation(s) for [pdp] degree plan lists.
  name: University of Pennsylvania [PDP] Degree Plan Lists API
  slug: university-of-pennsylvania-pdp-degree-plan-lists-api
- description: The [PDP] Docked Course API from University of Pennsylvania — 2 operation(s) for [pdp] docked course.
  name: University of Pennsylvania [PDP] Docked Course API
  slug: university-of-pennsylvania-pdp-docked-course-api
- description: The [PDP] Fulfillment API from University of Pennsylvania — 5 operation(s) for [pdp] fulfillment.
  name: University of Pennsylvania [PDP] Fulfillment API
  slug: university-of-pennsylvania-pdp-fulfillment-api
- description: The [PDP] Onboard From Transcript API from University of Pennsylvania — 1 operation(s) for [pdp] onboard from transcript.
  name: University of Pennsylvania [PDP] Onboard From Transcript API
  slug: university-of-pennsylvania-pdp-onboard-from-transcript-api
- description: The [PDP] Satisfied Rule Lists API from University of Pennsylvania — 1 operation(s) for [pdp] satisfied rule lists.
  name: University of Pennsylvania [PDP] Satisfied Rule Lists API
  slug: university-of-pennsylvania-pdp-satisfied-rule-lists-api
artifact_total: 47
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-pennsylvania-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-pennsylvania-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.upenn.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/upenn
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pennlabs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pennlabs.org/resources/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-pennsylvania/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-pennsylvania-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-pennsylvania-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-pennsylvania-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://penntoday.upenn.edu/rss.xml
- group: company
  title: ''
  type: About
  url: https://www.library.upenn.edu/about/policies/open-metadata
created: '2026-06-03'
description: 'The University of Pennsylvania (Penn) is a private Ivy League research university in Philadelphia, ranked #11 in the QS World University Rankings 2025. Penn''s public developer footprint centers on the Penn OpenData API, an institutional ESB service exposing Registrar, Dining, Directory, Transit, News and Events, Maps, Calendar, and Laundry data; access generally requires a validated API token issued by the university. A large share of the community-facing surface is built and documented by Penn Labs, a student-run software organization that publishes open-source SDKs (Python and JavaScript) and JSON REST APIs for Penn Courses, Penn Course Review, and Penn Mobile on top of the OpenData platform. Penn Libraries additionally exposes bibliographic metadata through OAI-PMH and Z39.50 under an open-metadata policy.'
examples:
- key_count: 2
  name: University Of Pennsylvania Course Detail Example
  slug: university-of-pennsylvania-course-detail-example
- key_count: 2
  name: University Of Pennsylvania Section Detail Example
  slug: university-of-pennsylvania-section-detail-example
finops:
- name: University Of Pennsylvania Finops
  service_category: Education
  slug: university-of-pennsylvania-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-pennsylvania.png
json_schemas:
- name: CourseDetail
  property_count: 16
  slug: university-of-pennsylvania-course
- name: Schedule
  property_count: 7
  slug: university-of-pennsylvania-schedule
- name: SectionDetail
  property_count: 14
  slug: university-of-pennsylvania-section
json_structures:
- name: University Of Pennsylvania Course Structure
  property_count: 11
  slug: university-of-pennsylvania-course-structure
- name: University Of Pennsylvania Section Structure
  property_count: 8
  slug: university-of-pennsylvania-section-structure
jsonld:
- class_count: 18
  name: University Of Pennsylvania Context
  property_count: 5
  slug: university-of-pennsylvania-context
layout: provider
modified: '2026-07-25'
name: University of Pennsylvania
nav: Providers
network: true
overview: 'University of Pennsylvania publishes 29 APIs on the [APIs.io](https://apis.io/) network, including [Accounts] User API, [PCA] Registration API, [PCA] Registration History API, and 26 more. Tagged areas include Education, Higher Education, University, Open Data, and Courses.


  The University of Pennsylvania catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Pennsylvania''s developer surface includes GitHub presence, engineering blog, and 11 more developer resources.'
plans:
- name: University Of Pennsylvania Plans Pricing
  plan_count: 2
  slug: university-of-pennsylvania-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 1
  name: University Of Pennsylvania Rate Limits
  slug: university-of-pennsylvania-rate-limits
rules:
- name: University of Pennsylvania API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-pennsylvania-jsonschema-spectral-rules
- name: University of Pennsylvania API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 3
  slug: university-of-pennsylvania-rules
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.9
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-pennsylvania/refs/heads/main/screenshots/university-of-pennsylvania-2026-06-20T200220.png
security:
- kind: domain-security
  name: University Of Pennsylvania Domain Security
  slug: university-of-pennsylvania-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-pennsylvania
tags:
- Education
- Higher Education
- University
- Open Data
- Courses
- Library
- United States
- Ivy League
website: https://www.upenn.edu/
---
