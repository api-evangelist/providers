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
    agent_skills: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cadenalaser Com Agentic Access
  operation_count: 3
  slug: cadenalaser-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://cadenalaser.com/api/v1
  baseurl_source: declared
  description: The Noticias API from Cadena Láser — 2 operation(s) for noticias.
  name: Cadena Láser Noticias API
  slug: cadenalaser-com-noticias-api
- baseURL: https://cadenalaser.com/api/v1
  baseurl_source: declared
  description: The Radios API from Cadena Láser — 1 operation(s) for radios.
  name: Cadena Láser Radios API
  slug: cadenalaser-com-radios-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/cadenalaser-com/agentic-access/cadenalaser-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cadenalaser-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cadenalaser-com/rules/cadenalaser-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cadenalaser-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/cadenalaser-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cadenalaser-com/errors/cadenalaser-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cadenalaser-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cadenalaser-com/conformance/cadenalaser-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cadenalaser-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cadenalaser-com/llms/cadenalaser-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cadenalaser-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cadenalaser-com/mcp/cadenalaser-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cadenalaser-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cadenalaser-com/well-known/cadenalaser-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cadenalaser-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cadenalaser-com/hosts/cadenalaser-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cadenalaser-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/cadenalaser-com/security/cadenalaser-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadenalaser-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cadenalaser.com/
created: '2026-11-03'
description: Cadena Láser is a regional news and live radio platform serving Río Tercero, Córdoba, offering up-to-date weather, currency rates, and live streaming of local radio stations. The site provides a wide range of news categories including local, regional, national, sports, politics, economy, technology, culture, and tourism, along with live radio broadcasts and community updates.
image: https://cadenalaser.com/opengraph-image?94ced753971c1c1e
layout: provider
mcp_servers:
- description: Remote MCP server at cadenalaser.com.
  name: Cadena Láser MCP Server
  slug: cadenalaser-com-mcp-yml
modified: '2026-11-03'
name: Cadena Láser
nav: Providers
network: true
overview: 'Cadena Láser publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Noticias API and Radios API. Tagged areas include Media, News, Radio, Córdoba, and Argentina.


  The Cadena Láser catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Cadena Láser API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: cadenalaser-com-rules
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 42.2
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cadenalaser Com Domain Security
  slug: cadenalaser-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: news
  slug: cadenalaser-com-news
slug: cadenalaser-com
tags:
- Media
- News
- Radio
- Córdoba
- Argentina
website: https://cadenalaser.com/
---
