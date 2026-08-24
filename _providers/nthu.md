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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Nthu Agentic Access
  operation_count: 23
  slug: nthu-agentic-access
  summary_line: 23 operations · 1 acting
api_count: 9
apis:
- description: The Announcements API from National Tsing Hua University — 3 operation(s) for announcements.
  name: National Tsing Hua University Announcements API
  slug: nthu-announcements-api
- description: The Buses API from National Tsing Hua University — 4 operation(s) for buses.
  name: National Tsing Hua University Buses API
  slug: nthu-buses-api
- description: The Courses API from National Tsing Hua University — 3 operation(s) for courses.
  name: National Tsing Hua University Courses API
  slug: nthu-courses-api
- description: The Departments API from National Tsing Hua University — 2 operation(s) for departments.
  name: National Tsing Hua University Departments API
  slug: nthu-departments-api
- description: The Dining API from National Tsing Hua University — 2 operation(s) for dining.
  name: National Tsing Hua University Dining API
  slug: nthu-dining-api
- description: The Energy API from National Tsing Hua University — 1 operation(s) for energy.
  name: National Tsing Hua University Energy API
  slug: nthu-energy-api
- description: The Libraries API from National Tsing Hua University — 3 operation(s) for libraries.
  name: National Tsing Hua University Libraries API
  slug: nthu-libraries-api
- description: The Locations API from National Tsing Hua University — 2 operation(s) for locations.
  name: National Tsing Hua University Locations API
  slug: nthu-locations-api
- description: The Newsletters API from National Tsing Hua University — 2 operation(s) for newsletters.
  name: National Tsing Hua University Newsletters API
  slug: nthu-newsletters-api
artifact_total: 42
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
- group: commercial
  title: ''
  type: License
  url: https://github.com/NTHU-SA/NTHU-Data-API/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nthu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nthu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nthu.edu.tw/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/NTHU-SA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-tsing-hua-university/
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
description: 'National Tsing Hua University (NTHU) is a national public research university in Hsinchu, Taiwan, originally founded in 1911 and re-established in Taiwan in 1956. It is ranked #210 in the QS World University Rankings 2025 and is one of Taiwan''s premier research institutions across science, engineering, humanities, and management. NTHU does not operate an official institution-wide developer portal, but its public developer footprint centers on the community-maintained NTHU Data API (NTHU-SA), a live FastAPI/OpenAPI service that aggregates public campus data such as courses, buses, dining, library spaces, announcements, and energy usage. Related open-source work lives across student and lab GitHub organizations.'
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
modified: '2026-06-03'
name: National Tsing Hua University
nav: Providers
network: true
overview: 'National Tsing Hua University publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Announcements API, Buses API, Courses API, and 6 more. Tagged areas include Education, Higher Education, University, Taiwan, and Open Data.


  The National Tsing Hua University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  National Tsing Hua University''s developer surface includes GitHub presence and 9 more developer resources.'
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
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 58.4
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 31.3
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
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nthu/refs/heads/main/screenshots/nthu-2026-06-20T190502.png
security:
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
- Open Data
- Campus
website: https://www.nthu.edu.tw/
---
