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
api_count: 1
apis:
- description: AgentRouter MCP API documented at https://www.agent-router.org/docs
  name: AgentRouter API
  slug: agentrouter-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/agent-router-org/llms/agent-router-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-router-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-router-org/mcp/agent-router-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agent-router-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/agent-router-org/hosts/agent-router-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-router-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-router-org/vendors/agent-router-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-router-org-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agent-router.org/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.agent-router.org/docs
- group: auth
  href: https://artifacts.apis.io/agent-router-org/security/agent-router-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-router-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-router.org/
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec is available.
  evidence:
  - status: 200
    url: https://www.agent-router.org/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: AgentRouter provides a Model Context Protocol (MCP) platform that connects AI agents to a network of specialized tools and services. Users can configure their agents to discover and delegate tasks to hundreds of specialist agents without writing custom integrations. The platform offers a dashboard, documentation, and pricing details, enabling rapid setup in minutes with no API keys or credit cards required. It supports building custom agents, automation workflows, and integration with tools like n8n, Make, and custom Python agents.
image: https://agent-router.org/opengraph-image.png?opengraph-image.679ea0cd.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.agent-router.org.
  name: AgentRouter MCP Server
  slug: agent-router-org-mcp-yml
modified: '2026-10-31'
name: AgentRouter
nav: Providers
network: true
overview: 'AgentRouter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Integration, and Platform.


  AgentRouter''s developer surface includes pricing, documentation, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 8.2
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
  name: Agent Router Org Domain Security
  slug: agent-router-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agent-router-org
tags:
- Company
- Artificial Intelligence
- MCP
- Integration
- Platform
website: https://agent-router.org/
---
