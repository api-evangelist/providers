---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Space Comman Agentic Access
  operation_count: 8
  slug: us-space-comman-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Session-based authentication
  name: US Space Command Authentication API
  slug: us-space-comman-authentication-api
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Conjunction data messages (collision warnings)
  name: US Space Command Conjunction Data API
  slug: us-space-comman-conjunction-data-api
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Satellite decay data and tracking impact predictions
  name: US Space Command Decay and Reentry API
  slug: us-space-comman-decay-and-reentry-api
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Current orbital element sets for tracked space objects
  name: US Space Command General Perturbations API
  slug: us-space-comman-general-perturbations-api
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Satellite catalog metadata
  name: US Space Command Satellite Catalog API
  slug: us-space-comman-satellite-catalog-api
- baseURL: https://www.space-track.org
  baseurl_source: spec
  description: Historical orbital ephemerides
  name: US Space Command Space Object History API
  slug: us-space-comman-space-object-history-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Space-Track.org REST Authentication API
  slug: open-us-space-comman-authentication-api
- collection_type: open
  name: Space-Track.org REST Authentication Conjunction Data API
  slug: open-us-space-comman-conjunction-data-api
- collection_type: open
  name: Space-Track.org REST Authentication Decay and Reentry API
  slug: open-us-space-comman-decay-and-reentry-api
- collection_type: open
  name: Space-Track.org REST Authentication General Perturbations API
  slug: open-us-space-comman-general-perturbations-api
- collection_type: open
  name: Space-Track.org REST Authentication Satellite Catalog API
  slug: open-us-space-comman-satellite-catalog-api
- collection_type: open
  name: Space-Track.org REST Authentication Space Object History API
  slug: open-us-space-comman-space-object-history-api
- collection_type: open
  name: Space-Track.org REST API
  slug: open-us-space-command-space-track
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-space-comman-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-space-comman-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-space-comman-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usspacecom
created: '2024-12-03'
description: US Space Command (USSPACECOM) is a unified combatant command in the United States Department of Defense responsible for conducting operations in, from, and through space to deter conflict and, if necessary, defeat aggressors. The command provides space situational awareness (SSA) data through Space-Track.org, including the official satellite catalog with orbital element sets, conjunction warnings, and reentry predictions for all tracked objects.
examples:
- key_count: 2
  name: Space Track Conjunction Data Example
  slug: space-track-conjunction-data-example
- key_count: 2
  name: Space Track Query Iss Gp Example
  slug: space-track-query-iss-gp-example
finops:
- name: Us Space Comman Finops
  service_category: API
  slug: us-space-comman-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-space-comman.png
json_schemas:
- name: USSPACECOM General Perturbations (GP) Orbital Element Set
  property_count: 19
  slug: us-space-command-gp
json_structures:
- name: Us Space Command Gp Structure
  property_count: 0
  slug: us-space-command-gp-structure
jsonld:
- class_count: 3
  name: Us Space Comman Context
  property_count: 20
  slug: us-space-comman-context
layout: provider
modified: '2026-05-19'
name: US Space Command
nav: Providers
network: true
overview: 'US Space Command publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Conjunction Data API, Decay and Reentry API, and 3 more. Tagged areas include Federal-Government, Space, Space Situational Awareness, Satellite Tracking, and Open Data.


  The US Space Command catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Space Command''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Us Space Comman Plans Pricing
  plan_count: 3
  slug: us-space-comman-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Us Space Comman Rate Limits
  slug: us-space-comman-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Space Command API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-space-comman-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: US Space Command API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: us-space-comman-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 61.2
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-space-comman/refs/heads/main/screenshots/us-space-comman-2026-06-20T200629.png
security:
- kind: authentication
  name: Us Space Comman Authentication
  slug: us-space-comman-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Us Space Comman Domain Security
  slug: us-space-comman-domain-security
  summary_line: TLSv1.3
slug: us-space-comman
tags:
- Federal-Government
- Space
- Space Situational Awareness
- Satellite Tracking
- Open Data
---
