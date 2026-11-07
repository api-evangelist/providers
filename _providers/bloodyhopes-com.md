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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bloodyhopes Com Agentic Access
  operation_count: 10
  slug: bloodyhopes-com-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 1
apis:
- baseURL: https://bloodyhopes.com
  baseurl_source: declared
  description: The Campfire API from Bloody Hopes — 7 operation(s) for campfire.
  name: Bloody Hopes Campfire API
  slug: bloodyhopes-com-campfire-api
- baseURL: https://bloodyhopes.com
  baseurl_source: declared
  description: The Growth API from Bloody Hopes — 1 operation(s) for growth.
  name: Bloody Hopes Growth API
  slug: bloodyhopes-com-growth-api
- baseURL: https://bloodyhopes.com
  baseurl_source: declared
  description: The Harness API from Bloody Hopes — 2 operation(s) for harness.
  name: Bloody Hopes Harness API
  slug: bloodyhopes-com-harness-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/bloodyhopes-com/agentic-access/bloodyhopes-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bloodyhopes-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/rules/bloodyhopes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bloodyhopes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/json-ld/bloodyhopes-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bloodyhopes-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/vocabulary/bloodyhopes-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bloodyhopes-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bloodyhopes-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/data-model/bloodyhopes-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bloodyhopes-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/errors/bloodyhopes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bloodyhopes-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bloodyhopes-com/conformance/bloodyhopes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bloodyhopes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bloodyhopes-com/llms/bloodyhopes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloodyhopes-com-llms.txt
- group: build
  href: https://artifacts.apis.io/bloodyhopes-com/mcp/bloodyhopes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bloodyhopes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bloodyhopes-com/mcp/bloodyhopes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bloodyhopes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bloodyhopes-com/well-known/bloodyhopes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bloodyhopes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bloodyhopes-com/hosts/bloodyhopes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bloodyhopes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bloodyhopes-com/vendors/bloodyhopes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bloodyhopes-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloodyhopes.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bloodyhopes.com/press
- group: auth
  href: https://artifacts.apis.io/bloodyhopes-com/security/bloodyhopes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloodyhopes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloodyhopes.com/
- group: company
  title: ''
  type: About
  url: https://bloodyhopes.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://bloodyhopes.com/campfire
- group: company
  title: ''
  type: Blog
  url: https://bloodyhopes.com/feed.xml
created: '2026-11-02'
description: Bloody Hopes is a cinematic historical music project delivering war ballads and folk songs about forgotten soldiers and lost battles. The site offers AI‑assisted, historically grounded tracks, sourced articles, and a catalog of songs spanning the American Civil War, Napoleonic Wars, Seven Years' War, Crimean War, and more, preserving the human cost of conflict through music and storytelling.
image: https://bloodyhopes.com/assets/seo/bloody-hopes-remembrance-1200x630.jpg
json_schemas:
- name: CriticalVoiceRequest
  property_count: 15
  slug: bloodyhopes-com-critical-voice-request
- name: QuickVoiceRequest
  property_count: 5
  slug: bloodyhopes-com-quick-voice-request
jsonld:
- class_count: 2
  name: Bloodyhopes Com Context
  property_count: 15
  slug: bloodyhopes-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at bloodyhopes.com.
  name: Bloody Hopes MCP Server
  slug: bloodyhopes-com-mcp-yml
modified: '2026-11-02'
name: Bloody Hopes
nav: Providers
network: true
overview: 'Bloody Hopes publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Campfire API, Growth API, and Harness API. Tagged areas include Music, Historical, War, Ballads, and AI-assisted.


  The Bloody Hopes catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bloody Hopes'' developer surface includes getting-started guide, engineering blog, and 19 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Bloody Hopes API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: bloodyhopes-com-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 8.9
    discoverability: 65.8
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bloodyhopes Com Domain Security
  slug: bloodyhopes-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: bloodyhopes-com-submit-voice
  slug: bloodyhopes-com-submit-voice
slug: bloodyhopes-com
tags:
- Music
- Historical
- War
- Ballads
- AI-assisted
website: https://bloodyhopes.com/
---
