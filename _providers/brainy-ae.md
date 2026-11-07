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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/brainy-ae/llms/brainy-ae-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brainy-ae-llms.txt
- group: agent
  href: https://artifacts.apis.io/brainy-ae/mcp/brainy-ae-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brainy-ae-mcp.yml
- group: other
  href: https://artifacts.apis.io/brainy-ae/hosts/brainy-ae-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brainy-ae-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brainy.ae/privacy
- group: auth
  href: https://artifacts.apis.io/brainy-ae/security/brainy-ae-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brainy-ae-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brainy.ae/
- group: other
  title: ''
  type: Image
  url: https://brainy.ae/static/img/og.png
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known hosts.
  evidence:
  - status: 406
    url: https://pos.brainy.ae/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Brainy is a small product studio that builds and runs live AI‑native products, including luxury market trackers, fan platforms, ad‑tech solutions, and AI tools. They operate with a fleet of AI agents to deliver innovative services for clients, focusing on cutting‑edge technology and rapid product development. The company emphasizes a boutique approach, combining design, engineering, and AI expertise to create market‑ready solutions.
image: https://brainy.ae/static/img/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at pos.brainy.ae.
  name: Brainy MCP Server
  slug: brainy-ae-mcp-yml
modified: '2026-11-02'
name: Brainy
nav: Providers
network: true
overview: Brainy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Product Studio, Innovation, and Technology.
random_paper: 0
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brainy Ae Domain Security
  slug: brainy-ae-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brainy-ae
tags:
- Company
- Artificial Intelligence
- Product Studio
- Innovation
- Technology
website: https://brainy.ae/
---
