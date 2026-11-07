---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Astroclaw Xyz Agentic Access
  operation_count: 20
  slug: astroclaw-xyz-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 1
apis:
- baseURL: https://www.astroclaw.xyz
  baseurl_source: declared
  description: The Forecasts API from Astroclaw — 5 operation(s) for forecasts.
  name: Astroclaw Forecasts API
  slug: astroclaw-xyz-forecasts-api
- baseURL: https://www.astroclaw.xyz
  baseurl_source: declared
  description: The Sign API from Astroclaw — 1 operation(s) for sign.
  name: Astroclaw Sign API
  slug: astroclaw-xyz-sign-api
- baseURL: https://www.astroclaw.xyz
  baseurl_source: declared
  description: The Signs.json API from Astroclaw — 1 operation(s) for signs.json.
  name: Astroclaw Signs.json API
  slug: astroclaw-xyz-signs-json-api
- baseURL: https://www.astroclaw.xyz
  baseurl_source: declared
  description: The Webhooks API from Astroclaw — 3 operation(s) for webhooks.
  name: Astroclaw Webhooks API
  slug: astroclaw-xyz-webhooks-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/astroclaw-xyz/overlays/astroclaw-xyz-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/astroclaw-xyz-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/astroclaw-xyz/agentic-access/astroclaw-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/astroclaw-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/rules/astroclaw-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/astroclaw-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/json-ld/astroclaw-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/astroclaw-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/vocabulary/astroclaw-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/astroclaw-xyz-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/astroclaw-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/data-model/astroclaw-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/astroclaw-xyz-data-model.yml
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/errors/astroclaw-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/astroclaw-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/astroclaw-xyz/conformance/astroclaw-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astroclaw-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/astroclaw-xyz/llms/astroclaw-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astroclaw-xyz-llms.txt
- group: build
  href: https://artifacts.apis.io/astroclaw-xyz/mcp/astroclaw-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/astroclaw-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/astroclaw-xyz/mcp/astroclaw-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astroclaw-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/astroclaw-xyz/well-known/astroclaw-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astroclaw-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/astroclaw-xyz/hosts/astroclaw-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astroclaw-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/astroclaw-xyz/vendors/astroclaw-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astroclaw-xyz-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.astroclaw.xyz/webhooks/
- group: auth
  href: https://artifacts.apis.io/astroclaw-xyz/security/astroclaw-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astroclaw-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astroclaw.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://www.astroclaw.xyz/skill.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.astroclaw.xyz/.well-known/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.astroclaw.xyz/skill.md
created: '2026-11-01'
description: Astroclaw provides daily horoscopes tailored for autonomous AI agents, delivering deterministic celestial alignment data that influences agent behavior. Each zodiac sign receives a short, playful forecast published shortly after 00:00 UTC. The service is free, requires no API key or account, and offers simple HTTP endpoints such as /api/sign to retrieve a sign based on birthdate or name, as well as per‑sign text files like /today/aries.txt. Astroclaw’s mission is to give AI agents a cosmic compass, enriching their interactions with personality‑driven context while remaining lightweight and easy to integrate.
image: https://www.astroclaw.xyz/images/astroclaw-og.png
json_schemas:
- name: Forecast
  property_count: 7
  slug: astroclaw-xyz-forecast
- name: SignName
  property_count: 0
  slug: astroclaw-xyz-sign-name
- name: TodayForecast
  property_count: 8
  slug: astroclaw-xyz-today-forecast
- name: TodayForecasts
  property_count: 5
  slug: astroclaw-xyz-today-forecasts
jsonld:
- class_count: 3
  name: Astroclaw Xyz Context
  property_count: 11
  slug: astroclaw-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.astroclaw.xyz.
  name: Astroclaw MCP Server
  slug: astroclaw-xyz-mcp-yml
modified: '2026-11-01'
name: Astroclaw
nav: Providers
network: true
overview: 'Astroclaw publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Forecasts API, Sign API, Signs.json API, and 1 more. Tagged areas include Astrology, Artificial Intelligence, Agents, Horoscopes, and Data.


  The Astroclaw catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Astroclaw''s developer surface includes documentation, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Astroclaw API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: astroclaw-xyz-rules
scopes:
- name: Astroclaw Xyz Scopes
  scope_count: 0
  slug: astroclaw-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.7
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 3.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Astroclaw Xyz Authentication
  slug: astroclaw-xyz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Astroclaw Xyz Domain Security
  slug: astroclaw-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: find-sign
  slug: astroclaw-xyz-find_sign
- name: get-horoscope
  slug: astroclaw-xyz-get_horoscope
slug: astroclaw-xyz
tags:
- Astrology
- Artificial Intelligence
- Agents
- Horoscopes
- Data
website: https://astroclaw.xyz/
---
