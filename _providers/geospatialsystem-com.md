---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Geospatialsystem Com Agentic Access
  operation_count: 16
  slug: geospatialsystem-com-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.geospatialsystem.com
  baseurl_source: declared
  description: The Catalogue API from geospatialsystem-com — 1 operation(s) for catalogue.
  name: geospatialsystem-com Catalogue API
  slug: geospatialsystem-com-catalogue-api
- baseURL: https://api.geospatialsystem.com
  baseurl_source: declared
  description: The Level 1 — Pixel API from geospatialsystem-com — 2 operation(s) for level 1 — pixel.
  name: geospatialsystem-com Level 1 — Pixel API
  slug: geospatialsystem-com-level-1-pixel-api
- baseURL: https://api.geospatialsystem.com
  baseurl_source: declared
  description: The Level 2 — Neighbourhood API from geospatialsystem-com — 4 operation(s) for level 2 — neighbourhood.
  name: geospatialsystem-com Level 2 — Neighbourhood API
  slug: geospatialsystem-com-level-2-neighbourhood-api
- baseURL: https://api.geospatialsystem.com
  baseurl_source: declared
  description: The Level 3 — Area Maps API from geospatialsystem-com — 2 operation(s) for level 3 — area maps.
  name: geospatialsystem-com Level 3 — Area Maps API
  slug: geospatialsystem-com-level-3-area-maps-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/geospatialsystem-com/agentic-access/geospatialsystem-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/geospatialsystem-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/rules/geospatialsystem-com-rules.yml
  title: ''
  type: Spectral
  url: rules/geospatialsystem-com-rules.yml
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/json-ld/geospatialsystem-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/geospatialsystem-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/vocabulary/geospatialsystem-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/geospatialsystem-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/geospatialsystem-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/data-model/geospatialsystem-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/geospatialsystem-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/errors/geospatialsystem-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/geospatialsystem-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/geospatialsystem-com/conformance/geospatialsystem-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/geospatialsystem-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/geospatialsystem-com/hosts/geospatialsystem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/geospatialsystem-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/geospatialsystem-com/authentication/geospatialsystem-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/geospatialsystem-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/geospatialsystem-com/security/geospatialsystem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/geospatialsystem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://geospatialsystem.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.geospatialsystem.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://geospatialsystem.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.bigdataearth.com/about-us/terms_and_conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.bigdataearth.com/about-us/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://geospatialsystem.com/#contact
created: '2026-10-30'
description: Geospatial System provides a high‑performance REST API and MCP server for terrain analysis, elevation data, slope statistics and 3‑D visualisation. Their platform offers AI‑native capabilities via integration with Claude, GPT and modern agents, targeting developers needing precise location profiling and terrain intelligence. The service includes free tier access, tiered pricing, and extensive documentation for quick integration.
json_schemas:
- name: LPBaseRequest
  property_count: 3
  slug: geospatialsystem-com-lpbase-request
- name: LPBatchRequest
  property_count: 1
  slug: geospatialsystem-com-lpbatch-request
- name: LPChartRequest
  property_count: 4
  slug: geospatialsystem-com-lpchart-request
- name: LPTerrainMapRequest
  property_count: 8
  slug: geospatialsystem-com-lpterrain-map-request
- name: LPTerrain3DRequest
  property_count: 7
  slug: geospatialsystem-com-lpterrain3-drequest
jsonld:
- class_count: 8
  name: Geospatialsystem Com Context
  property_count: 18
  slug: geospatialsystem-com-context
layout: provider
modified: '2026-10-30'
name: geospatialsystem-com
nav: Providers
network: true
overview: 'geospatialsystem-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalogue API, Level 1 — Pixel API, Level 2 — Neighbourhood API, and 1 more. Tagged areas include Company, Geospatial, Terrain, API, and AI.


  The geospatialsystem-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  geospatialsystem-com''s developer surface includes authentication, documentation, pricing, and 14 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: geospatialsystem-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: geospatialsystem-com-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 75.7
    catalog_earned_first_party: 0.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 54.3
    developer_ergonomics: 27.9
    discoverability: 62.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Geospatialsystem Com Authentication
  slug: geospatialsystem-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Geospatialsystem Com Domain Security
  slug: geospatialsystem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: geospatialsystem-com-create-and-retrieve-terrain-map
  slug: geospatialsystem-com-create-and-retrieve-terrain-map
- name: geospatialsystem-com-lp-elevation-analysis
  slug: geospatialsystem-com-lp-elevation-analysis
- name: geospatialsystem-com-lp-elevation-workflow
  slug: geospatialsystem-com-lp-elevation-workflow
slug: geospatialsystem-com
tags:
- Company
- Geospatial
- Terrain
- API
- AI
- Location
website: https://geospatialsystem.com/
---
