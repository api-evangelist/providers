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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National University Of Colombia Agentic Access
  operation_count: 7
  slug: national-university-of-colombia-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: OAI-PMH 2.0 metadata harvesting interface.
  name: National University of Colombia OAI-PMH API
  slug: national-university-of-colombia-oai-pmh-api
- description: DSpace HAL+JSON read endpoints for repository structure.
  name: National University of Colombia REST - Core API
  slug: national-university-of-colombia-rest-core-api
- description: Faceted search across archived objects.
  name: National University of Colombia REST - Discover API
  slug: national-university-of-colombia-rest-discover-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH API
  slug: open-national-university-of-colombia-oai-pmh-api
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH REST - Core API
  slug: open-national-university-of-colombia-rest-core-api
- collection_type: open
  name: National University of Colombia - Institutional Repository OAI-PMH REST - Discover API
  slug: open-national-university-of-colombia-rest-discover-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-university-of-colombia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-university-of-colombia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unal.edu.co/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/unal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universidad-nacional-de-colombia/
- group: commercial
  title: ''
  type: Plans
  url: plans/national-university-of-colombia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/national-university-of-colombia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/national-university-of-colombia-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: other
  title: ''
  type: ProductPage
  url: https://datosabiertos.unal.edu.co/
created: '2026-06-03'
description: 'The National University of Colombia (Universidad Nacional de Colombia, UNAL) is the country''s largest public research university, ranked #219 in the QS World University Rankings 2025. UNAL maintains an open-data portal and a DSpace-based institutional repository, but does not publish a formal, documented public developer portal or REST API program. The most accessible programmatic surface is the OAI-PMH interface exposed by its institutional repository, alongside an open-data portal and an official GitHub organization with limited public code.'
examples:
- key_count: 2
  name: National University Of Colombia Listcollections Example
  slug: national-university-of-colombia-listCollections-example
- key_count: 2
  name: National University Of Colombia Listcommunities Example
  slug: national-university-of-colombia-listCommunities-example
- key_count: 3
  name: National University Of Colombia Oairecord Example
  slug: national-university-of-colombia-oaiRecord-example
finops:
- name: National University Of Colombia Finops
  service_category: Education
  slug: national-university-of-colombia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-university-of-colombia.png
json_schemas:
- name: DSpace Collection
  property_count: 8
  slug: national-university-of-colombia-collection
- name: DSpace Community
  property_count: 8
  slug: national-university-of-colombia-community
json_structures:
- name: National University Of Colombia Collection Structure
  property_count: 6
  slug: national-university-of-colombia-collection-structure
- name: National University Of Colombia Community Structure
  property_count: 6
  slug: national-university-of-colombia-community-structure
jsonld:
- class_count: 18
  name: National University Of Colombia Context
  property_count: 3
  slug: national-university-of-colombia-context
layout: provider
modified: '2026-07-25'
name: National University of Colombia
nav: Providers
network: true
overview: 'National University of Colombia publishes 3 APIs on the [APIs.io](https://apis.io/) network: OAI-PMH API, REST - Core API, and REST - Discover API. Tagged areas include Education, Higher Education, University, Colombia, and Open Data.


  The National University of Colombia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  National University of Colombia''s developer surface includes GitHub presence and 9 more developer resources.'
plans:
- name: National University Of Colombia Plans Pricing
  plan_count: 2
  slug: national-university-of-colombia-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: National University Of Colombia Rate Limits
  slug: national-university-of-colombia-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: National University of Colombia API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: national-university-of-colombia-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: National University of Colombia API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 3
  slug: national-university-of-colombia-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 37.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 33.6
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
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: National University Of Colombia Domain Security
  slug: national-university-of-colombia-domain-security
  summary_line: TLSv1.2 · DMARC
slug: national-university-of-colombia
tags:
- Education
- Higher Education
- University
- Colombia
- Open Data
- Institutional Repository
- OAI-PMH
website: https://unal.edu.co/
---
