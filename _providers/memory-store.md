---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Memory Store Model Context Protocol (MCP) server exposes shared team memory to AI clients (Claude, ChatGPT, Cursor, Raycast). It lets agents record and recall organizational context, search memory
  name: Memory Store MCP Server
  slug: memory-store-mcp-server
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memory-store-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://memory.store/guides
- group: docs
  title: ''
  type: Documentation
  url: https://memory.store/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://memory.store/guides
- group: start
  title: ''
  type: SignUp
  url: https://app.memory.store
- group: commercial
  title: ''
  type: Pricing
  url: https://memory.store/pricing
- group: company
  title: ''
  type: Blog
  url: https://memory.store/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/eREzXMqFpE
- group: operate
  title: ''
  type: StatusPage
  url: https://status.memory.store
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memory.store/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://memory.store/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/memorydotstore
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/memorystore
- group: agent
  title: ''
  type: MCPServer
  url: mcp/memory-store-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memory-store-lifecycle.yml
created: '2026-07-17'
description: Memory Store is a Y Combinator (Spring 2026) startup building a universal, shared memory layer for teams and AI agents. It automatically collects insights from communication and productivity tools — Gmail, Slack, Granola, Claude, ChatGPT and more — and synthesizes them into an organized, searchable "company brain." Memory Store is delivered primarily as a Model Context Protocol (MCP) server, letting AI clients such as Claude, ChatGPT, Cursor and Raycast record what matters and recall it anywhere without changing existing workflows. A signature feature, "Briefs," maintains self-updating living documents (decision logs, team status, customer requests) as new information arrives.
image: https://memory.store/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Memory Store MCP Server
  slug: memory-store-mcp-server
modified: '2026-07-20'
name: Memory Store
nav: Providers
network: true
overview: 'Memory Store publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Memory, AI Agents, MCP, and Knowledge-Management.


  Memory Store''s developer surface includes documentation, getting-started guide, signup flow, pricing, engineering blog, support, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.8
  provenance:
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memory-store/refs/heads/main/screenshots/memory-store-2026-08-07T172505.png
security:
- kind: domain-security
  name: Memory Store Domain Security
  slug: memory-store-domain-security
  summary_line: TLSv1.3 · DMARC
slug: memory-store
tags:
- Company
- Memory
- AI Agents
- MCP
- Knowledge-Management
- Context
- Productivity
- Y Combinator
website: https://memory.store/guides
---
