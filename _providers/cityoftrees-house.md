---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cityoftrees House Agentic Access
  operation_count: 4
  slug: cityoftrees-house-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- baseURL: https://cityoftrees.house
  baseurl_source: declared
  description: The Agent API from City of Trees House — 4 operation(s) for agent.
  name: City of Trees House Agent API
  slug: cityoftrees-house-agent-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/cityoftrees-house/agentic-access/cityoftrees-house-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cityoftrees-house-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/rules/cityoftrees-house-rules.yml
  title: ''
  type: Spectral
  url: rules/cityoftrees-house-rules.yml
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/json-ld/cityoftrees-house-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cityoftrees-house-context.jsonld
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/vocabulary/cityoftrees-house-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cityoftrees-house-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cityoftrees-house/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/data-model/cityoftrees-house-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cityoftrees-house-data-model.yml
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/errors/cityoftrees-house-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cityoftrees-house-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cityoftrees-house/conformance/cityoftrees-house-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cityoftrees-house-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cityoftrees-house/llms/cityoftrees-house-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cityoftrees-house-llms.txt
- group: build
  href: https://artifacts.apis.io/cityoftrees-house/mcp/cityoftrees-house-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cityoftrees-house-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cityoftrees-house/mcp/cityoftrees-house-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cityoftrees-house-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cityoftrees-house/well-known/cityoftrees-house-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cityoftrees-house-well-known.yml
- group: other
  href: https://artifacts.apis.io/cityoftrees-house/hosts/cityoftrees-house-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cityoftrees-house-hosts.yml
- group: other
  href: https://artifacts.apis.io/cityoftrees-house/vendors/cityoftrees-house-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cityoftrees-house-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cityoftrees.house/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cityoftrees.house/privacy
- group: auth
  href: https://artifacts.apis.io/cityoftrees-house/security/cityoftrees-house-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cityoftrees-house-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cityoftrees.house/
- group: company
  title: ''
  type: Blog
  url: https://cityoftrees.house/blog
created: '2026-11-03'
description: City of Trees House is a West Sacramento family‑run vacation rental offering a house for groups of up to 10. Guests enjoy a full kitchen, hot tub, game room, and live availability booking directly through the site. The hosts, Ryan and Ashley, emphasize hospitality, local experiences, and a personal touch, providing a comfortable, tree‑filled retreat for travelers seeking a home‑like stay in the Sacramento area.
image: https://cityoftrees.house/city-of-trees-photos/living-room-tv-and-conversation-seating.webp
json_schemas:
- name: Availability
  property_count: 11
  slug: cityoftrees-house-availability
- name: Property
  property_count: 26
  slug: cityoftrees-house-property
- name: Quote
  property_count: 23
  slug: cityoftrees-house-quote
- name: Stay
  property_count: 4
  slug: cityoftrees-house-stay
jsonld:
- class_count: 9
  name: Cityoftrees House Context
  property_count: 73
  slug: cityoftrees-house-context
layout: provider
mcp_servers:
- description: Remote MCP server at cityoftrees.house.
  name: City of Trees House MCP Server
  slug: cityoftrees-house-mcp-yml
modified: '2026-11-03'
name: City of Trees House
nav: Providers
network: true
overview: 'City of Trees House publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include Vacation Rentals, West Sacramento, Family Run, Hospitality, and Vacation Home.


  The City of Trees House catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  City of Trees House''s developer surface includes engineering blog and 18 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: City of Trees House API Rules
  rule_count: 43
  severity_counts:
    error: 37
    hint: 0
    info: 4
    warn: 2
  slug: cityoftrees-house-rules
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 3.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cityoftrees House Domain Security
  slug: cityoftrees-house-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: cityoftrees-house-quote-stay
  slug: cityoftrees-house-quote-stay
slug: cityoftrees-house
tags:
- Vacation Rentals
- West Sacramento
- Family Run
- Hospitality
- Vacation Home
website: https://cityoftrees.house/
---
