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
    agent_card: conformant
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agentbuilt-dev/llms/agentbuilt-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbuilt-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentbuilt-dev/a2a/agentbuilt-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentbuilt-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentbuilt-dev/mcp/agentbuilt-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbuilt-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentbuilt-dev/hosts/agentbuilt-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbuilt-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentbuilt-dev/vendors/agentbuilt-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentbuilt-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentbuilt-dev/security/agentbuilt-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbuilt-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbuilt.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://agentbuilt.dev/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://agentbuilt.dev/api/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://agentbuilt.dev/visibility
- group: commercial
  title: ''
  type: Pricing
  url: https://agentbuilt.dev/free-ai-visibility-check
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are HTML rendered with JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://agentbuilt.dev/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: Agentbuilt provides data tools for AI pipelines, offering extraction services such as YouTube transcript extraction, Substack scraping, and Shopify product feeds. Operated by an AI agent with human oversight by Matt Edward in Calgary, the studio bills per result and emphasizes transparent limits and pricing. Tools are callable via the Apify API or as MCP tools, supporting integration with agents, n8n, Make, and Zapier.
layout: provider
mcp_servers:
- description: Remote MCP server at agentbuilt.dev.
  name: agentbuilt MCP Server
  slug: agentbuilt-dev-mcp-yml
modified: '2026-10-31'
name: agentbuilt
nav: Providers
network: true
overview: 'agentbuilt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Tools, Extraction, MCP, and Agent-Operated.


  agentbuilt''s developer surface includes documentation, API reference, getting-started guide, pricing, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 45.0
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentbuilt Dev Domain Security
  slug: agentbuilt-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentbuilt-dev
tags:
- Artificial Intelligence
- Data Tools
- Extraction
- MCP
- Agent-Operated
website: https://agentbuilt.dev/
---
