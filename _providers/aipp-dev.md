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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/aipp-dev/llms/aipp-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aipp-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/aipp-dev/mcp/aipp-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aipp-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/aipp-dev/hosts/aipp-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aipp-dev-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aipp-dev/security/aipp-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aipp-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aipp.dev/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are served as HTML shells requiring JavaScript rendering, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://aipp.dev/docs.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AIPP provides infrastructure for digital actions, enabling developers to put a price on API calls, AI tasks, workflows, files, and digital services using Lightning and Base USDC payments. It offers pay-per-action mechanisms, smart tags, and a studio console for creating and managing paid digital experiences, supporting HTTP 402 challenges and L402 standards.
layout: provider
mcp_servers:
- description: Remote MCP server at aipp.dev.
  name: AIPP MCP Server
  slug: aipp-dev-mcp-yml
modified: '2026-11-01'
name: AIPP
nav: Providers
network: true
overview: AIPP is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Lightning, base-usdc, Digital Actions, Developer Tools, and AI Agents.
random_paper: 22
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 0.0
  previous_composite: 3.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aipp Dev Domain Security
  slug: aipp-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aipp-dev
tags:
- Lightning
- base-usdc
- Digital Actions
- Developer Tools
- AI Agents
website: https://aipp.dev/
---
