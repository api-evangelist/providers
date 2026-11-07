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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Asternym Com Agentic Access
  operation_count: 12
  slug: asternym-com-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://asternym.com
  baseurl_source: declared
  description: The Bazi API from AsterNym — 2 operation(s) for bazi.
  name: AsterNym Bazi API
  slug: asternym-com-bazi-api
- baseURL: https://asternym.com
  baseurl_source: declared
  description: The Natal API from AsterNym — 1 operation(s) for natal.
  name: AsterNym Natal API
  slug: asternym-com-natal-api
- baseURL: https://asternym.com
  baseurl_source: declared
  description: The Numerology API from AsterNym — 1 operation(s) for numerology.
  name: AsterNym Numerology API
  slug: asternym-com-numerology-api
- baseURL: https://asternym.com
  baseurl_source: declared
  description: The Reading API from AsterNym — 1 operation(s) for reading.
  name: AsterNym Reading API
  slug: asternym-com-reading-api
- baseURL: https://asternym.com
  baseurl_source: declared
  description: The Zodiac API from AsterNym — 1 operation(s) for zodiac.
  name: AsterNym Zodiac API
  slug: asternym-com-zodiac-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/asternym-com/agentic-access/asternym-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asternym-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/asternym-com/rules/asternym-com-rules.yml
  title: ''
  type: Spectral
  url: rules/asternym-com-rules.yml
- group: design
  href: https://artifacts.apis.io/asternym-com/json-ld/asternym-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asternym-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/asternym-com/vocabulary/asternym-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asternym-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/asternym-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/asternym-com/data-model/asternym-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asternym-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/asternym-com/errors/asternym-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asternym-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asternym-com/conformance/asternym-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asternym-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asternym-com/llms/asternym-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asternym-com-llms.txt
- group: build
  href: https://artifacts.apis.io/asternym-com/mcp/asternym-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/asternym-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/asternym-com/mcp/asternym-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asternym-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/asternym-com/hosts/asternym-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asternym-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asternym-com/vendors/asternym-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asternym-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asternym.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asternym.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://asternym.com/blog
- group: auth
  href: https://artifacts.apis.io/asternym-com/security/asternym-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asternym-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asternym.com/
created: '2026-11-01'
description: AsterNym reads your birth through eight symbolic systems and one real astronomical sky, calculates each by its own rules, keeps them apart, and shows which parts are measured and which parts are believed.
image: https://asternym.com/og/home-og.png
json_schemas:
- name: EngineResult
  property_count: 6
  slug: asternym-com-engine-result
- name: Reading
  property_count: 10
  slug: asternym-com-reading
jsonld:
- class_count: 2
  name: Asternym Com Context
  property_count: 11
  slug: asternym-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at asternym.com.
  name: AsterNym MCP Server
  slug: asternym-com-mcp-yml
modified: '2026-11-01'
name: AsterNym
nav: Providers
network: true
overview: 'AsterNym publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bazi API, Natal API, Numerology API, and 2 more. Tagged areas include Astrology, BaZi, Numerology, Compatibility, and BirthChart.


  The AsterNym catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AsterNym''s developer surface includes engineering blog and 17 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: AsterNym API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: asternym-com-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 58.7
    developer_ergonomics: 7.6
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 30.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asternym Com Domain Security
  slug: asternym-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: reading
  slug: asternym-com-reading-skill
slug: asternym-com
tags:
- Astrology
- BaZi
- Numerology
- Compatibility
- BirthChart
website: https://asternym.com/
---
