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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Space Comman Agentic Access
  operation_count: 8
  slug: us-space-comman-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 6
apis:
- description: Session-based authentication
  name: US Space Command Authentication API
  slug: us-space-comman-authentication-api
- description: Conjunction data messages (collision warnings)
  name: US Space Command Conjunction Data API
  slug: us-space-comman-conjunction-data-api
- description: Satellite decay data and tracking impact predictions
  name: US Space Command Decay and Reentry API
  slug: us-space-comman-decay-and-reentry-api
- description: Current orbital element sets for tracked space objects
  name: US Space Command General Perturbations API
  slug: us-space-comman-general-perturbations-api
- description: Satellite catalog metadata
  name: US Space Command Satellite Catalog API
  slug: us-space-comman-satellite-catalog-api
- description: Historical orbital ephemerides
  name: US Space Command Space Object History API
  slug: us-space-comman-space-object-history-api
artifact_total: 20
collections:
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
overview: 'US Space Command publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Conjunction Data API, Decay and Reentry API, and 3 more. Tagged areas include Federal Government, Space, Space Situational Awareness, Satellite Tracking, and Open Data.


  The US Space Command catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Space Command''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Us Space Comman Plans Pricing
  plan_count: 3
  slug: us-space-comman-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Us Space Comman Rate Limits
  slug: us-space-comman-rate-limits
rules:
- name: US Space Command API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: us-space-comman-jsonschema-spectral-rules
- name: US Space Command API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: us-space-comman-rules
score:
  band: developing
  composite: 42.5
  delta: -4.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 46.5
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Federal Government
- Space
- Space Situational Awareness
- Satellite Tracking
- Open Data
---
