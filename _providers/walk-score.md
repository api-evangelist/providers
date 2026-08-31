---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Walk Score Agentic Access
  operation_count: 7
  slug: walk-score-agentic-access
  summary_line: 7 operations
api_count: 2
apis:
- description: Supported cities list
  name: Walk Score Cities API
  slug: walk-score-cities-api
- description: Transit route details
  name: Walk Score Routes API
  slug: walk-score-routes-api
- description: Walk Score, Transit Score, and Bike Score for locations
  name: Walk Score Scores API
  slug: walk-score-scores-api
- description: Transit stop search and details
  name: Walk Score Stops API
  slug: walk-score-stops-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Walk Score Cities API
  slug: open-walk-score-cities-api
- collection_type: open
  name: Walk Score Cities Routes API
  slug: open-walk-score-routes-api
- collection_type: open
  name: Walk Score Cities Scores API
  slug: open-walk-score-scores-api
- collection_type: open
  name: Walk Score Cities Stops API
  slug: open-walk-score-stops-api
- collection_type: open
  name: Walk Score Transit API
  slug: open-walk-score-transit
- collection_type: open
  name: Walk Score API
  slug: open-walk-score
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/walk-score-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walk-score-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/walk-score-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/walk-score
- group: company
  title: ''
  type: Website
  url: https://www.walkscore.com
- group: start
  title: ''
  type: Portal
  url: https://www.walkscore.com/professional/api.php
- group: docs
  title: ''
  type: Documentation
  url: https://walkscore-api.readthedocs.io/en/latest/
- group: start
  title: ''
  type: Signup
  url: https://www.walkscore.com/professional/api-sign-up.php
created: '2025-03-01'
description: Walk Score measures the walkability, transit accessibility, and bikeability of any address in the United States and Canada. The Walk Score API returns Walk Score, Transit Score, and Bike Score for any geographic location, supporting real estate platforms, commute calculators, urban planning tools, and location intelligence applications. The Public Transit API provides detailed transit data including nearby stops, route networks, and supported cities, enabling comprehensive transportation accessibility analysis.
examples:
- key_count: 2
  name: Walk Score Get Transit Score Example
  slug: walk-score-get-transit-score-example
- key_count: 2
  name: Walk Score Get Walk Score Example
  slug: walk-score-get-walk-score-example
- key_count: 2
  name: Walk Score Search Transit Stops Example
  slug: walk-score-search-transit-stops-example
finops:
- name: Walk Score Finops
  service_category: API
  slug: walk-score-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/walk-score.png
json_schemas:
- name: Walk Score Response
  property_count: 13
  slug: walk-score-score
- name: Walk Score Transit Stop
  property_count: 9
  slug: walk-score-transit-stop
json_structures:
- name: Walk Score Score Structure
  property_count: 0
  slug: walk-score-score-structure
jsonld:
- class_count: 28
  name: Walk Score Context
  property_count: 7
  slug: walk-score-context
layout: provider
modified: '2026-05-19'
name: Walk Score
nav: Providers
network: true
overview: 'Walk Score publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cities API, Routes API, Scores API, and 1 more. Tagged areas include Walkability, Transit, Bikeability, Location, and Real-Estate.


  The Walk Score catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Walk Score''s developer surface includes authentication, developer portal, documentation, signup flow, and 4 more developer resources.'
plans:
- name: Walk Score Plans Pricing
  plan_count: 3
  slug: walk-score-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Walk Score Rate Limits
  slug: walk-score-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Walk Score API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: walk-score-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Walk Score API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: walk-score-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 13.6
    contract_quality: 65.1
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walk-score/refs/heads/main/screenshots/walk-score-2026-06-20T201208.png
security:
- kind: authentication
  name: Walk Score Authentication
  slug: walk-score-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Walk Score Domain Security
  slug: walk-score-domain-security
  summary_line: TLSv1.2 · DMARC
slug: walk-score
tags:
- Walkability
- Transit
- Bikeability
- Location
- Real-Estate
- Urban Planning
- Transportation
website: https://www.walkscore.com
---
