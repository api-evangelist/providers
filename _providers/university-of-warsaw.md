---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Warsaw Agentic Access
  operation_count: 8
  slug: university-of-warsaw-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: 'The University of Warsaw Research Data Repository (Dane Badawcze UW) is a Dataverse-based institutional repository for long-term storage and open sharing of research data across all disciplines, with '
  name: Dane Badawcze UW Research Data Repository REST API
  slug: rdr-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the University of Warsaw Research Data Repository (Dataverse). The repository identifies itself as the "Dane Badawcze UW Dataverse OAI Archive" and support
  name: Dane Badawcze UW OAI-PMH Endpoint
  slug: rdr-oai-pmh
- description: Machine-readable method reference
  name: University of Warsaw apiref API
  slug: university-of-warsaw-apiref-api
- description: USOS API server information and time
  name: University of Warsaw apisrv API
  slug: university-of-warsaw-apisrv-api
- description: Academic calendar events
  name: University of Warsaw calendar API
  slug: university-of-warsaw-calendar-api
- description: Courses and course editions
  name: University of Warsaw courses API
  slug: university-of-warsaw-courses-api
- description: Faculties and organizational units
  name: University of Warsaw fac API
  slug: university-of-warsaw-fac-api
artifact_total: 24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-warsaw-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-warsaw-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-warsaw-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://en.uw.edu.pl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/icm-uw
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uniwersytet-warszawski
- group: start
  title: ''
  type: DeveloperPortal
  url: https://usosapps.uw.edu.pl/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://usosapps.uw.edu.pl/developers/api/authorization/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-warsaw-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-warsaw-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-warsaw-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: Blog
  url: https://en.uw.edu.pl/category/news/feed/
created: '2026-06-03'
description: 'The University of Warsaw (Uniwersytet Warszawski) is Poland''s largest and highest-ranked university, placed #258 in the QS World University Rankings 2025. Its public developer footprint centers on the USOS API, a documented OAuth-secured REST-like protocol exposing the institution''s academic database (courses, grades, exams, users, payments and more), and on the Dane Badawcze UW research data repository, a Dataverse instance that offers a native REST API and an OAI-PMH endpoint for metadata harvesting. Developer access to USOS requires registration for an API key (Consumer Key/Secret) via the USOS developers portal.'
examples:
- key_count: 2
  name: University Of Warsaw Course Error Example
  slug: university-of-warsaw-course-error-example
- key_count: 6
  name: University Of Warsaw Installation Example
  slug: university-of-warsaw-installation-example
- key_count: 2
  name: University Of Warsaw Now Example
  slug: university-of-warsaw-now-example
finops:
- name: University Of Warsaw Finops
  service_category: Education
  slug: university-of-warsaw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-warsaw.png
json_schemas:
- name: USOS Course
  property_count: 14
  slug: university-of-warsaw-course
- name: USOS Faculty
  property_count: 9
  slug: university-of-warsaw-faculty
- name: USOS Installation
  property_count: 9
  slug: university-of-warsaw-installation
json_structures:
- name: University Of Warsaw Course Structure
  property_count: 9
  slug: university-of-warsaw-course-structure
- name: University Of Warsaw Installation Structure
  property_count: 9
  slug: university-of-warsaw-installation-structure
jsonld:
- class_count: 23
  name: University Of Warsaw Context
  property_count: 8
  slug: university-of-warsaw-context
layout: provider
modified: '2026-06-03'
name: University of Warsaw
nav: Providers
network: true
overview: 'University of Warsaw publishes 5 APIs on the [APIs.io](https://apis.io/) network, including apiref API, apisrv API, calendar API, and 2 more. Tagged areas include Education, Higher Education, University, Poland, and Academic Data.


  The University of Warsaw catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Warsaw''s developer surface includes authentication, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: University Of Warsaw Plans Pricing
  plan_count: 2
  slug: university-of-warsaw-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 1
  name: University Of Warsaw Rate Limits
  slug: university-of-warsaw-rate-limits
rules:
- name: University of Warsaw API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-warsaw-jsonschema-spectral-rules
- name: University of Warsaw API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: university-of-warsaw-rules
score:
  band: developing
  composite: 44.0
  delta: -5.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 73.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-warsaw/refs/heads/main/screenshots/university-of-warsaw-2026-06-20T200305.png
security:
- kind: authentication
  name: University Of Warsaw Authentication
  slug: university-of-warsaw-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Warsaw Domain Security
  slug: university-of-warsaw-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: university-of-warsaw
tags:
- Education
- Higher Education
- University
- Poland
- Academic Data
- Research Data
- Open Data
website: https://en.uw.edu.pl/
---
