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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Macrostrat Agentic Access
  operation_count: 16
  slug: macrostrat-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Age Model API from Macrostrat — 1 operation(s) for age model.
  name: Macrostrat Age Model API
  slug: macrostrat-age-model-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Cartography API from Macrostrat — 1 operation(s) for cartography.
  name: Macrostrat Cartography API
  slug: macrostrat-cartography-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Columns API from Macrostrat — 1 operation(s) for columns.
  name: Macrostrat Columns API
  slug: macrostrat-columns-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Definitions API from Macrostrat — 1 operation(s) for definitions.
  name: Macrostrat Definitions API
  slug: macrostrat-definitions-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Fossils API from Macrostrat — 1 operation(s) for fossils.
  name: Macrostrat Fossils API
  slug: macrostrat-fossils-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Geologic Maps API from Macrostrat — 3 operation(s) for geologic maps.
  name: Macrostrat Geologic Maps API
  slug: macrostrat-geologic-maps-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Grids API from Macrostrat — 1 operation(s) for grids.
  name: Macrostrat Grids API
  slug: macrostrat-grids-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Measurements API from Macrostrat — 1 operation(s) for measurements.
  name: Macrostrat Measurements API
  slug: macrostrat-measurements-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Meta API from Macrostrat — 1 operation(s) for meta.
  name: Macrostrat Meta API
  slug: macrostrat-meta-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Mobile API from Macrostrat — 1 operation(s) for mobile.
  name: Macrostrat Mobile API
  slug: macrostrat-mobile-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Paleogeography API from Macrostrat — 1 operation(s) for paleogeography.
  name: Macrostrat Paleogeography API
  slug: macrostrat-paleogeography-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Sections API from Macrostrat — 1 operation(s) for sections.
  name: Macrostrat Sections API
  slug: macrostrat-sections-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Stats API from Macrostrat — 1 operation(s) for stats.
  name: Macrostrat Stats API
  slug: macrostrat-stats-api
- baseURL: https://macrostrat.org/api/v2
  baseurl_source: declared
  description: The Units API from Macrostrat — 1 operation(s) for units.
  name: Macrostrat Units API
  slug: macrostrat-units-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Macrostrat Age Model API
  slug: open-macrostrat-age-model-api
- collection_type: open
  name: Macrostrat Age Model Cartography API
  slug: open-macrostrat-cartography-api
- collection_type: open
  name: Macrostrat Age Model Columns API
  slug: open-macrostrat-columns-api
- collection_type: open
  name: Macrostrat Age Model Definitions API
  slug: open-macrostrat-definitions-api
- collection_type: open
  name: Macrostrat Age Model Fossils API
  slug: open-macrostrat-fossils-api
- collection_type: open
  name: Macrostrat Age Model Geologic Maps API
  slug: open-macrostrat-geologic-maps-api
- collection_type: open
  name: Macrostrat Age Model Grids API
  slug: open-macrostrat-grids-api
- collection_type: open
  name: Macrostrat Age Model Measurements API
  slug: open-macrostrat-measurements-api
- collection_type: open
  name: Macrostrat Age Model Meta API
  slug: open-macrostrat-meta-api
- collection_type: open
  name: Macrostrat Age Model Mobile API
  slug: open-macrostrat-mobile-api
- collection_type: open
  name: Macrostrat Age Model Paleogeography API
  slug: open-macrostrat-paleogeography-api
- collection_type: open
  name: Macrostrat Age Model Sections API
  slug: open-macrostrat-sections-api
- collection_type: open
  name: Macrostrat Age Model Stats API
  slug: open-macrostrat-stats-api
- collection_type: open
  name: Macrostrat Age Model Units API
  slug: open-macrostrat-units-api
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
random_paper: 17
rate_limits:
- limit_count: 5
  name: Macrostrat Rate Limits
  slug: macrostrat-rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
