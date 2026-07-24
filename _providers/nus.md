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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nus Agentic Access
  operation_count: 6
  slug: nus-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: ScholarBank@NUS is the digital institutional repository of the National University of Singapore, built on DSpace 7.6. Its HAL-style REST API exposes communities, collections, items, bitstreams, and me
  name: ScholarBank@NUS DSpace REST API
  slug: scholarbank-rest
- description: OAI-PMH metadata harvesting endpoint for ScholarBank@NUS, supporting standard verbs (Identify, ListRecords, ListMetadataFormats, GetRecord) for harvesting Dublin Core and other metadata formats from t
  name: ScholarBank@NUS OAI-PMH Interface
  slug: scholarbank-oai
- description: The Modules API from National University of Singapore — 4 operation(s) for modules.
  name: National University of Singapore Modules API
  slug: nus-modules-api
- description: The Venues API from National University of Singapore — 2 operation(s) for venues.
  name: National University of Singapore Venues API
  slug: nus-venues-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nus.edu.sg/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/national-university-of-singapore/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/NUSingapore
- group: auth
  title: ''
  type: Authentication
  url: https://vafs.nus.edu.sg/adfs/ls/
- group: commercial
  title: ''
  type: Plans
  url: plans/nus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nus-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The National University of Singapore (NUS) is Singapore''s flagship public research university, ranked #8 in the QS World University Rankings 2025. NUS does not operate a single unified, public developer portal; its documented, programmatically accessible footprint is concentrated in its open scholarly infrastructure. The institutional repository ScholarBank@NUS runs on DSpace 7.6 and exposes both a REST API and an OAI-PMH metadata harvesting interface. Module and timetable data is also available via the community-maintained NUSMods API (unofficial), which normalizes NUS course information. Most administrative and student-facing systems sit behind ADFS/SAML single sign-on and are not publicly documented.'
examples:
- key_count: 2
  name: Nus Module Example
  slug: nus-module-example
- key_count: 2
  name: Nus Modulelist Example
  slug: nus-modulelist-example
finops:
- name: Nus Finops
  service_category: Education
  slug: nus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nus.png
json_schemas:
- name: NUS Module
  property_count: 12
  slug: nus-module
- name: NUS ModuleCondensed
  property_count: 3
  slug: nus-modulecondensed
- name: NUS VenueInformation
  property_count: 3
  slug: nus-venueinformation
json_structures:
- name: Nus Module Structure
  property_count: 12
  slug: nus-module-structure
- name: Nus Modulecondensed Structure
  property_count: 3
  slug: nus-modulecondensed-structure
jsonld:
- class_count: 23
  name: Nus Context
  property_count: 4
  slug: nus-context
layout: provider
modified: '2026-06-03'
name: National University of Singapore
nav: Providers
network: true
overview: 'National University of Singapore publishes 2 APIs on the [APIs.io](https://apis.io/) network: Modules API and Venues API. Tagged areas include Education, Higher Education, University, Singapore, and Research.


  The National University of Singapore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  National University of Singapore''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Nus Plans Pricing
  plan_count: 2
  slug: nus-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Nus Rate Limits
  slug: nus-rate-limits
rules:
- name: National University of Singapore API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: nus-jsonschema-spectral-rules
- name: National University of Singapore API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: nus-rules
score:
  band: developing
  composite: 46.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.1
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 46.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nus/refs/heads/main/screenshots/nus-2026-06-20T190528.png
security:
- kind: domain-security
  name: Nus Domain Security
  slug: nus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nus
tags:
- Education
- Higher Education
- University
- Singapore
- Research
- Open Access
- Repository
website: https://nus.edu.sg/
---
