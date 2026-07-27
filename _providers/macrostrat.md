---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Macrostrat Agentic Access
  operation_count: 16
  slug: macrostrat-agentic-access
  summary_line: 16 operations
api_count: 14
apis:
- description: The Age Model API from Macrostrat — 1 operation(s) for age model.
  name: Macrostrat Age Model API
  slug: macrostrat-age-model-api
- description: The Cartography API from Macrostrat — 1 operation(s) for cartography.
  name: Macrostrat Cartography API
  slug: macrostrat-cartography-api
- description: The Columns API from Macrostrat — 1 operation(s) for columns.
  name: Macrostrat Columns API
  slug: macrostrat-columns-api
- description: The Definitions API from Macrostrat — 1 operation(s) for definitions.
  name: Macrostrat Definitions API
  slug: macrostrat-definitions-api
- description: The Fossils API from Macrostrat — 1 operation(s) for fossils.
  name: Macrostrat Fossils API
  slug: macrostrat-fossils-api
- description: The Geologic Maps API from Macrostrat — 3 operation(s) for geologic maps.
  name: Macrostrat Geologic Maps API
  slug: macrostrat-geologic-maps-api
- description: The Grids API from Macrostrat — 1 operation(s) for grids.
  name: Macrostrat Grids API
  slug: macrostrat-grids-api
- description: The Measurements API from Macrostrat — 1 operation(s) for measurements.
  name: Macrostrat Measurements API
  slug: macrostrat-measurements-api
- description: The Meta API from Macrostrat — 1 operation(s) for meta.
  name: Macrostrat Meta API
  slug: macrostrat-meta-api
- description: The Mobile API from Macrostrat — 1 operation(s) for mobile.
  name: Macrostrat Mobile API
  slug: macrostrat-mobile-api
- description: The Paleogeography API from Macrostrat — 1 operation(s) for paleogeography.
  name: Macrostrat Paleogeography API
  slug: macrostrat-paleogeography-api
- description: The Sections API from Macrostrat — 1 operation(s) for sections.
  name: Macrostrat Sections API
  slug: macrostrat-sections-api
- description: The Stats API from Macrostrat — 1 operation(s) for stats.
  name: Macrostrat Stats API
  slug: macrostrat-stats-api
- description: The Units API from Macrostrat — 1 operation(s) for units.
  name: Macrostrat Units API
  slug: macrostrat-units-api
artifact_total: 20
collections:
- collection_type: open
  name: Macrostrat API
  slug: open-macrostrat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/macrostrat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macrostrat-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uw-macrostrat
created: '2024-11-14'
description: Macrostrat is a platform for the aggregation and distribution of geological data relevant to the spatial and temporal distribution of sedimentary, igneous, and metamorphic rocks as well as data extracted from them.
finops:
- name: Macrostrat Finops
  service_category: API
  slug: macrostrat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/macrostrat.png
layout: provider
modified: '2026-05-19'
name: Macrostrat
nav: Providers
network: true
overview: Macrostrat publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Age Model API, Cartography API, Columns API, and 11 more. Tagged areas include Geological Data, Geology, Rocks, Paleontology, and Earth Science.
plans:
- name: Macrostrat Plans Pricing
  plan_count: 3
  slug: macrostrat-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Macrostrat Rate Limits
  slug: macrostrat-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.7
    developer_ergonomics: 0.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macrostrat/refs/heads/main/screenshots/macrostrat-2026-06-20T184834.png
security:
- kind: domain-security
  name: Macrostrat Domain Security
  slug: macrostrat-domain-security
  summary_line: TLSv1.3
slug: macrostrat
tags:
- Geological Data
- Geology
- Rocks
- Paleontology
- Earth Science
---
