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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Lausanne Agentic Access
  operation_count: 6
  slug: university-of-lausanne-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: The Core API from University of Lausanne — 2 operation(s) for core.
  name: University of Lausanne Core API
  slug: university-of-lausanne-core-api
- description: The IRIS Repository (DSpace REST API) API from University of Lausanne — 1 operation(s) for iris repository (dspace rest api).
  name: University of Lausanne IRIS Repository (DSpace REST API) API
  slug: university-of-lausanne-iris-repository-dspace-rest-api-api
- description: The Projects API from University of Lausanne — 2 operation(s) for projects.
  name: University of Lausanne Projects API
  slug: university-of-lausanne-projects-api
- description: The Projects.json API from University of Lausanne — 1 operation(s) for projects.json.
  name: University of Lausanne Projects.json API
  slug: university-of-lausanne-projects-json-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-lausanne-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-lausanne-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unil.ch
- group: build
  title: ''
  type: GitHub
  url: https://github.com/openscienceunil
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-lausanne/
- group: auth
  title: ''
  type: Authentication
  url: https://my.unil.ch/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-lausanne-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-lausanne-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-lausanne-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Lausanne (UNIL) is a public research university in Lausanne, Switzerland, ranked #224 in the QS World University Rankings 2025. With roughly 17,000 students across seven faculties, UNIL maintains an Open Science strategy and a Kong-based internal API gateway underpinning its digital services. Its public developer footprint is modest and research-oriented: the SPICA single-cell spatial atlas exposes a documented JSON API, and the IRIS institutional repository is served by a public DSpace REST API. Most institutional and student-information APIs sit behind the my.unil.ch authentication gateway and are not publicly documented.'
examples:
- key_count: 2
  name: University Of Lausanne Listcommunities Example
  slug: university-of-lausanne-listCommunities-example
- key_count: 2
  name: University Of Lausanne Queryprojects Example
  slug: university-of-lausanne-queryProjects-example
finops:
- name: University Of Lausanne Finops
  service_category: Education
  slug: university-of-lausanne-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-lausanne.png
json_schemas:
- name: DSpace Community
  property_count: 9
  slug: university-of-lausanne-community
- name: SPICA Project
  property_count: 11
  slug: university-of-lausanne-project
json_structures:
- name: University Of Lausanne Community Structure
  property_count: 8
  slug: university-of-lausanne-community-structure
- name: University Of Lausanne Project Structure
  property_count: 11
  slug: university-of-lausanne-project-structure
jsonld:
- class_count: 14
  name: University Of Lausanne Context
  property_count: 6
  slug: university-of-lausanne-context
layout: provider
modified: '2026-06-03'
name: University of Lausanne
nav: Providers
network: true
overview: 'University of Lausanne publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Core API, IRIS Repository (DSpace REST API) API, Projects API, and 1 more. Tagged areas include Education, Higher Education, University, Switzerland, and Open Science.


  The University of Lausanne catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Lausanne''s developer surface includes GitHub presence, authentication, and 8 more developer resources.'
plans:
- name: University Of Lausanne Plans Pricing
  plan_count: 2
  slug: university-of-lausanne-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: University Of Lausanne Rate Limits
  slug: university-of-lausanne-rate-limits
rules:
- name: University of Lausanne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-lausanne-jsonschema-spectral-rules
- name: University of Lausanne API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: university-of-lausanne-rules
score:
  band: thin
  composite: 41.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-lausanne/refs/heads/main/screenshots/university-of-lausanne-2026-06-20T200157.png
security:
- kind: domain-security
  name: University Of Lausanne Domain Security
  slug: university-of-lausanne-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-lausanne
tags:
- Education
- Higher Education
- University
- Switzerland
- Open Science
- Research Data
- Institutional Repository
website: https://www.unil.ch
---
