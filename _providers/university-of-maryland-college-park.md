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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Maryland College Park Agentic Access
  operation_count: 20
  slug: university-of-maryland-college-park-agentic-access
  summary_line: 20 operations
api_count: 7
apis:
- description: The University of Maryland Office of the Registrar's Testudo Schedule of Classes (SOC) is a public web application for browsing course offerings by semester and department. It is a web interface rathe
  name: Testudo Schedule of Classes
  slug: testudo-soc
- description: DRUM (Digital Repository at the University of Maryland) is the UMD Libraries' DSpace-based institutional repository of scholarship and research outputs. It is publicly browsable; programmatic access v
  name: DRUM Institutional Repository
  slug: drum
- description: This endpoint lets you get data about bus routes, schedules, stops, locations, and predicted arrival times. The data is provided by NextBus, which monitors buses and gives the data to us via their API
  name: University of Maryland College Park bus API
  slug: university-of-maryland-college-park-bus-api
- description: This set of endpoints lets you get data about university courses and their sections. You can get one course or section at a time, several courses or sections at a time, or a list of all the courses. A
  name: University of Maryland College Park courses API
  slug: university-of-maryland-college-park-courses-api
- description: Data about the various majors offered on campus.
  name: University of Maryland College Park majors API
  slug: university-of-maryland-college-park-majors-api
- description: Data about things on campus, such as buildings, dining halls, and other facilities.
  name: University of Maryland College Park map API
  slug: university-of-maryland-college-park-map-api
- description: This endpoint contains information about university professors and the courses they have taught.
  name: University of Maryland College Park professors API
  slug: university-of-maryland-college-park-professors-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-maryland-college-park-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-maryland-college-park-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.umd.edu
- group: build
  title: ''
  type: GitHub
  url: https://github.com/umdio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-maryland/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-maryland-college-park-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-maryland-college-park-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-maryland-college-park-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://today.umd.edu/rss
created: '2026-06-03'
description: 'The University of Maryland, College Park (UMD) is the flagship public research university of the University System of Maryland, located in College Park, Maryland, United States. It is ranked #218 in the QS World University Rankings 2025. UMD does not operate a central, officially branded public developer portal. The most prominent public, documented programmatic access to UMD data is umd.io, a student-run open-source REST API (api.umd.io) covering courses, course sections, professors, campus bus routes, building/map data, and majors. The Office of the Registrar''s Testudo Schedule of Classes provides course data via a public web interface, and the libraries'' DRUM (DSpace) institutional repository is publicly accessible.'
examples:
- key_count: 2
  name: University Of Maryland College Park Getbuildingbyid Example
  slug: university-of-maryland-college-park-getBuildingById-example
- key_count: 2
  name: University Of Maryland College Park Getcoursesbyid Example
  slug: university-of-maryland-college-park-getCoursesById-example
- key_count: 2
  name: University Of Maryland College Park Getmajors Example
  slug: university-of-maryland-college-park-getMajors-example
- key_count: 2
  name: University Of Maryland College Park Getprofessors Example
  slug: university-of-maryland-college-park-getProfessors-example
- key_count: 2
  name: University Of Maryland College Park Getroutesbyid Example
  slug: university-of-maryland-college-park-getRoutesById-example
- key_count: 2
  name: University Of Maryland College Park Getsections Example
  slug: university-of-maryland-college-park-getSections-example
finops:
- name: University Of Maryland College Park Finops
  service_category: Education
  slug: university-of-maryland-college-park-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-maryland-college-park.png
json_schemas:
- name: Building
  property_count: 5
  slug: university-of-maryland-college-park-building
- name: Course
  property_count: 12
  slug: university-of-maryland-college-park-course
- name: Major
  property_count: 4
  slug: university-of-maryland-college-park-major
- name: Professor
  property_count: 2
  slug: university-of-maryland-college-park-professor
- name: Route
  property_count: 9
  slug: university-of-maryland-college-park-route
- name: Section
  property_count: 9
  slug: university-of-maryland-college-park-section
json_structures:
- name: University Of Maryland College Park Course Structure
  property_count: 12
  slug: university-of-maryland-college-park-course-structure
- name: University Of Maryland College Park Section Structure
  property_count: 9
  slug: university-of-maryland-college-park-section-structure
jsonld:
- class_count: 40
  name: University Of Maryland College Park Context
  property_count: 3
  slug: university-of-maryland-college-park-context
layout: provider
modified: '2026-06-03'
name: University of Maryland College Park
nav: Providers
network: true
overview: 'University of Maryland College Park publishes 5 APIs on the [APIs.io](https://apis.io/) network, including bus API, courses API, majors API, and 2 more. Tagged areas include Education, Higher Education, University, United States, and Open Data.


  The University of Maryland College Park catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Maryland College Park''s developer surface includes GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: University Of Maryland College Park Plans Pricing
  plan_count: 2
  slug: university-of-maryland-college-park-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Maryland College Park Rate Limits
  slug: university-of-maryland-college-park-rate-limits
rules:
- name: University of Maryland College Park API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-maryland-college-park-jsonschema-spectral-rules
- name: University of Maryland College Park API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: university-of-maryland-college-park-rules
score:
  band: thin
  composite: 39.8
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.4
    developer_ergonomics: 2.2
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 42.6
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-maryland-college-park/refs/heads/main/screenshots/university-of-maryland-college-park-2026-06-20T200223.png
security:
- kind: domain-security
  name: University Of Maryland College Park Domain Security
  slug: university-of-maryland-college-park-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-maryland-college-park
tags:
- Education
- Higher Education
- University
- United States
- Open Data
- Courses
- Student Run
website: https://www.umd.edu
---
