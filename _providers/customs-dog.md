---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Customs Dog Agentic Access
  operation_count: 1
  slug: customs-dog-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: MCP JSON-RPC API for pet travel document management
  name: customs.dog API
  slug: customs-dog-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/customs-dog/agentic-access/customs-dog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/customs-dog-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/customs-dog/rules/customs-dog-rules.yml
  title: ''
  type: Spectral
  url: rules/customs-dog-rules.yml
- group: agent
  href: https://artifacts.apis.io/customs-dog/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/customs-dog/errors/customs-dog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/customs-dog-problem-types.yml
- group: design
  href: https://artifacts.apis.io/customs-dog/conformance/customs-dog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/customs-dog-conformance.yml
- group: agent
  href: https://artifacts.apis.io/customs-dog/llms/customs-dog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/customs-dog-llms.txt
- group: build
  href: https://artifacts.apis.io/customs-dog/mcp/customs-dog-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/customs-dog-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/customs-dog/mcp/customs-dog-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/customs-dog-mcp.yml
- group: other
  href: https://artifacts.apis.io/customs-dog/hosts/customs-dog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/customs-dog-hosts.yml
- group: other
  href: https://artifacts.apis.io/customs-dog/vendors/customs-dog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/customs-dog-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://customs.dog/login
- group: auth
  href: https://artifacts.apis.io/customs-dog/authentication/customs-dog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/customs-dog-authentication.yml
- group: auth
  href: https://artifacts.apis.io/customs-dog/security/customs-dog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/customs-dog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://customs.dog/
created: '2026-11-04'
description: customs.dog provides a web application that quickly tells pet owners whether their dog is cleared to cross a border and displays the required travel document on screen in seconds, even offline. The service offers a simple answer, an offline‑ready document wallet, and integrates with border checkpoints to streamline pet travel.
image: https://customs.dog/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at customs.dog requiring an API key.
  name: customs.dog MCP Server
  slug: customs-dog-mcp-yml
modified: '2026-11-04'
name: customs.dog
nav: Providers
network: true
overview: 'customs.dog is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pet travel, Border crossing, Customs, and Travel app.


  The customs.dog catalog on APIs.io includes 1 Spectral governance ruleset.


  customs.dog''s developer surface includes authentication and 13 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: customs.dog API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: customs-dog-rules
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Customs Dog Authentication
  slug: customs-dog-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Customs Dog Domain Security
  slug: customs-dog-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: customs-dog-mcp
  slug: customs-dog-mcp
slug: customs-dog
tags:
- Pet travel
- Border crossing
- Customs
- Travel app
website: https://customs.dog/
---
