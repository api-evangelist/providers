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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Arcalune Music provides a Machine-Callable Protocol (MCP) for searching tracks, retrieving track details, and listing tags.
  name: Arcalune Music MCP
  slug: arcalune-music-mcp
- description: 'Arcalune Music API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Arcalune Music API
  slug: arcalune-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/arcalune-com/rules/arcalune-com-rules.yml
  title: ''
  type: Spectral
  url: rules/arcalune-com-rules.yml
- group: design
  href: https://artifacts.apis.io/arcalune-com/vocabulary/arcalune-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcalune-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arcalune-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arcalune-com/conformance/arcalune-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcalune-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcalune-com/llms/arcalune-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcalune-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arcalune-com/mcp/arcalune-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcalune-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/arcalune-com/hosts/arcalune-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcalune-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcalune-com/vendors/arcalune-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcalune-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcalune.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://arcalune.com/se/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcalune.com/developers
- group: auth
  href: https://artifacts.apis.io/arcalune-com/security/arcalune-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcalune-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcalune.com/
created: '2026-11-01'
description: Arcalune Music is a Japanese‑origin online music library offering original compositions, fan‑arranged game tracks, and royalty‑free background music and sound effects. All tracks are available for free streaming and download, suitable for use in videos, live streams, and game projects. The site provides high‑quality MP3 files under Creative Commons licensing, with multilingual navigation (Japanese, English, Spanish, Portuguese, Hindi, Indonesian, French).
image: https://arcalune.com/og-card-v1.png
layout: provider
mcp_servers:
- description: Remote MCP server at arcalune.com.
  name: Arcalune Music MCP Server
  slug: arcalune-com-mcp-yml
modified: '2026-11-01'
name: Arcalune Music
nav: Providers
network: true
overview: 'Arcalune Music is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Free BGM, Sound Effects, Japanese, and Creative Commons.


  The Arcalune Music catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Arcalune Music API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: arcalune-com-rules
scopes:
- name: Arcalune Com Scopes
  scope_count: 0
  slug: arcalune-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 11.2
    discoverability: 57.5
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcalune Com Authentication
  slug: arcalune-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arcalune Com Domain Security
  slug: arcalune-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arcalune-com
tags:
- Music
- Free BGM
- Sound Effects
- Japanese
- Creative Commons
website: https://arcalune.com/
---
