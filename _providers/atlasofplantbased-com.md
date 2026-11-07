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
    error_semantics: false
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
  score: 25.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Atlasofplantbased Com Agentic Access
  operation_count: 3
  slug: atlasofplantbased-com-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://atlasofplantbased.com
  baseurl_source: declared
  description: The Pct API from Atlas of Plant Based — 3 operation(s) for pct.
  name: Atlas of Plant Based Pct API
  slug: atlasofplantbased-com-pct-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/atlasofplantbased-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/atlasofplantbased-com/agentic-access/atlasofplantbased-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atlasofplantbased-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/atlasofplantbased-com/rules/atlasofplantbased-com-rules.yml
  title: ''
  type: Spectral
  url: rules/atlasofplantbased-com-rules.yml
- group: design
  href: https://artifacts.apis.io/atlasofplantbased-com/conformance/atlasofplantbased-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlasofplantbased-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlasofplantbased-com/llms/atlasofplantbased-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlasofplantbased-com-llms.txt
- group: build
  href: https://artifacts.apis.io/atlasofplantbased-com/mcp/atlasofplantbased-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atlasofplantbased-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/atlasofplantbased-com/mcp/atlasofplantbased-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlasofplantbased-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atlasofplantbased-com/well-known/atlasofplantbased-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlasofplantbased-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlasofplantbased-com/hosts/atlasofplantbased-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasofplantbased-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlasofplantbased-com/vendors/atlasofplantbased-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasofplantbased-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/atlasofplantbased-com/security/atlasofplantbased-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasofplantbased-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasofplantbased.com/
- group: docs
  title: ''
  type: Documentation
  url: https://atlasofplantbased.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://atlasofplantbased.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://atlasofplantbased.com/about/
- group: company
  title: ''
  type: Blog
  url: https://atlasofplantbased.com/rss.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasofplantbased.com/privacy/
created: '2026-11-01'
description: Atlas of Plant Based is a travel and trail‑food website founded in 2026 by Jeffrey Combs. It documents a vegan thru‑hike of the Pacific Crest Trail, offering guides, maps, gear lists, water sources, and plant‑based food recommendations for hikers.
image: https://atlasofplantbased.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at atlasofplantbased.com.
  name: Atlas of Plant Based MCP Server
  slug: atlasofplantbased-com-mcp-yml
modified: '2026-11-01'
name: Atlas of Plant Based
nav: Providers
network: true
overview: 'Atlas of Plant Based publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Pct API. Tagged areas include Travel, Vegan, Hiking, Plant-Based, and Outdoor.


  The Atlas of Plant Based catalog on APIs.io includes 1 Spectral governance ruleset.


  Atlas of Plant Based''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Atlas of Plant Based API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: atlasofplantbased-com-rules
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 41.0
    developer_ergonomics: 21.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlasofplantbased Com Domain Security
  slug: atlasofplantbased-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-pct-leg
  slug: atlasofplantbased-com-get-pct-leg
slug: atlasofplantbased-com
tags:
- Travel
- Vegan
- Hiking
- Plant-Based
- Outdoor
website: https://atlasofplantbased.com/
---
