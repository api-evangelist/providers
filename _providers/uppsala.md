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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Uppsala Agentic Access
  operation_count: 7
  slug: uppsala-agentic-access
  summary_line: 7 operations
api_count: 9
apis:
- description: The Norse World REST-API, part of the Norse World research infrastructure at Uppsala University's Department of Scandinavian Languages, provides access to attestation and location records of foreign p
  name: Norse World REST-API
  slug: norseworld
- description: DiVA (Academic Archive On-line) is Uppsala University Library's institutional repository for publications and research data produced by the university's researchers and students. It exposes an OAI-PMH
  name: DiVA OAI-PMH
  slug: diva-oai
- description: The BattleDeaths API from Uppsala University — 1 operation(s) for battledeaths.
  name: Uppsala University BattleDeaths API
  slug: uppsala-battledeaths-api
- description: The Dyadic API from Uppsala University — 1 operation(s) for dyadic.
  name: Uppsala University Dyadic API
  slug: uppsala-dyadic-api
- description: The GEDEvents API from Uppsala University — 1 operation(s) for gedevents.
  name: Uppsala University GEDEvents API
  slug: uppsala-gedevents-api
- description: The NonState API from Uppsala University — 1 operation(s) for nonstate.
  name: Uppsala University NonState API
  slug: uppsala-nonstate-api
- description: The OneSided API from Uppsala University — 1 operation(s) for onesided.
  name: Uppsala University OneSided API
  slug: uppsala-onesided-api
- description: The OrganizedViolenceCY API from Uppsala University — 1 operation(s) for organizedviolencecy.
  name: Uppsala University OrganizedViolenceCY API
  slug: uppsala-organizedviolencecy-api
- description: The UcdpPrioConflict API from Uppsala University — 1 operation(s) for ucdpprioconflict.
  name: Uppsala University UcdpPrioConflict API
  slug: uppsala-ucdpprioconflict-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UCDP - The Public BattleDeaths API
  slug: open-uppsala-battledeaths-api
- collection_type: open
  name: UCDP - The Public BattleDeaths Dyadic API
  slug: open-uppsala-dyadic-api
- collection_type: open
  name: UCDP - The Public BattleDeaths GEDEvents API
  slug: open-uppsala-gedevents-api
- collection_type: open
  name: UCDP - The Public BattleDeaths NonState API
  slug: open-uppsala-nonstate-api
- collection_type: open
  name: UCDP - The Public BattleDeaths OneSided API
  slug: open-uppsala-onesided-api
- collection_type: open
  name: UCDP - The Public BattleDeaths OrganizedViolenceCY API
  slug: open-uppsala-organizedviolencecy-api
- collection_type: open
  name: UCDP - The Public BattleDeaths UcdpPrioConflict API
  slug: open-uppsala-ucdpprioconflict-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uppsala-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uppsala-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uppsala-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uppsala-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uu.se/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uppsala-university
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uppsala-university/
- group: commercial
  title: ''
  type: Plans
  url: plans/uppsala-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uppsala-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uppsala-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Uppsala University (Uppsala universitet) is Sweden''s oldest university, founded in 1477, and is ranked #103 in the QS World University Rankings 2025. Its public developer and API footprint is research-driven and decentralized across departments and infrastructures rather than a single developer portal. Confirmed public interfaces include the Uppsala Conflict Data Program (UCDP) RESTful API, the Norse World REST-API, and the DiVA institutional repository OAI-PMH endpoint. The university maintains an official GitHub organization hosting integration and research code.'
examples:
- key_count: 2
  name: Uppsala Gedevents Example
  slug: uppsala-gedevents-example
- key_count: 2
  name: Uppsala Ucdpprioconflict Example
  slug: uppsala-ucdpprioconflict-example
finops:
- name: Uppsala Finops
  service_category: Education
  slug: uppsala-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uppsala.png
json_schemas:
- name: UcdpApiResponse
  property_count: 5
  slug: uppsala-apiresponse
- name: GedDb
  property_count: 49
  slug: uppsala-gedevent
- name: OrganizedViolenceCYDb
  property_count: 74
  slug: uppsala-organizedviolencecy
- name: UcdpPrioConflictDb
  property_count: 28
  slug: uppsala-ucdpprioconflict
json_structures:
- name: Uppsala Gedevent Structure
  property_count: 49
  slug: uppsala-gedevent-structure
- name: Uppsala Ucdpprioconflict Structure
  property_count: 28
  slug: uppsala-ucdpprioconflict-structure
jsonld:
- class_count: 31
  name: Uppsala Context
  property_count: 3
  slug: uppsala-context
layout: provider
modified: '2026-06-03'
name: Uppsala University
nav: Providers
network: true
overview: 'Uppsala University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including BattleDeaths API, Dyadic API, GEDEvents API, and 4 more. Tagged areas include Education, Higher Education, University, Research, and Open Data.


  The Uppsala University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Uppsala University''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Uppsala Plans Pricing
  plan_count: 2
  slug: uppsala-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Uppsala Rate Limits
  slug: uppsala-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Uppsala University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uppsala-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Uppsala University API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: uppsala-rules
score:
  band: developing
  composite: 40.4
  delta: 4.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 55.1
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 42.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uppsala/refs/heads/main/screenshots/uppsala-2026-06-20T200453.png
security:
- kind: authentication
  name: Uppsala Authentication
  slug: uppsala-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uppsala Domain Security
  slug: uppsala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uppsala Vulnerability Disclosure
  slug: uppsala-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: uppsala
tags:
- Education
- Higher Education
- University
- Research
- Open Data
- Sweden
website: https://www.uu.se/
---
