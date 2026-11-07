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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cajusticewatch Com Agentic Access
  operation_count: 15
  slug: cajusticewatch-com-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- baseURL: https://cajusticewatch.com
  baseurl_source: declared
  description: California Justice Watch — public-data tools for AI agents researching California criminal-justice accountability.
  name: CA Justice Watch Cajusticewatch API
  slug: cajusticewatch-com-cajusticewatch-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/cajusticewatch-com/agentic-access/cajusticewatch-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cajusticewatch-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cajusticewatch-com/rules/cajusticewatch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cajusticewatch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cajusticewatch-com/vocabulary/cajusticewatch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cajusticewatch-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cajusticewatch-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cajusticewatch-com/errors/cajusticewatch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cajusticewatch-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cajusticewatch-com/conformance/cajusticewatch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cajusticewatch-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cajusticewatch-com/llms/cajusticewatch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cajusticewatch-com-llms.txt
- group: build
  href: https://artifacts.apis.io/cajusticewatch-com/mcp/cajusticewatch-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cajusticewatch-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cajusticewatch-com/mcp/cajusticewatch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cajusticewatch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cajusticewatch-com/well-known/cajusticewatch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cajusticewatch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cajusticewatch-com/hosts/cajusticewatch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cajusticewatch-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cajusticewatch-com/vendors/cajusticewatch-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cajusticewatch-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cajusticewatch
- group: auth
  href: https://artifacts.apis.io/cajusticewatch-com/security/cajusticewatch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cajusticewatch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cajusticewatch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cajusticewatch.com/about.html
- group: docs
  title: ''
  type: APIReference
  url: https://cajusticewatch.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://cajusticewatch.com/top100.html
created: '2026-11-03'
description: CA Justice Watch is a nonpartisan project that tracks prosecutorial injustice across all 58 California counties. It aggregates public‑record data on wrongful convictions, police misconduct, DA overcharging, and other systemic abuses, providing searchable databases and visualizations to promote accountability and reform.
image: https://cajusticewatch.com/owl-mascot.svg
layout: provider
mcp_servers:
- description: Remote MCP server at cajusticewatch.com.
  name: CA Justice Watch MCP Server
  slug: cajusticewatch-com-mcp-yml
modified: '2026-11-03'
name: CA Justice Watch
nav: Providers
network: true
overview: 'CA Justice Watch publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Cajusticewatch API. Tagged areas include Justice, Transparency, Data, California, and Public Records.


  The CA Justice Watch catalog on APIs.io includes 1 Spectral governance ruleset.


  CA Justice Watch''s developer surface includes documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: CA Justice Watch API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: cajusticewatch-com-rules
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 2.6
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cajusticewatch Com Domain Security
  slug: cajusticewatch-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cajusticewatch-com
tags:
- Justice
- Transparency
- Data
- California
- Public Records
website: https://cajusticewatch.com/
---
