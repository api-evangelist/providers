---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryglen.com/
- group: company
  title: ''
  type: Blog
  url: https://tryglen.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://tryglen.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryglen.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryglen.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glen-mcp.yml
created: '2026-07-17'
description: Glen is a Y Combinator (Summer 2026) startup building a shared organizational learning and memory system for fleets of AI agents. The platform acts as a centralized store that every AI agent in a company can read from and write to, so that when one agent learns something the whole organization gains access to it. Glen preserves decisions, customer insights and operational procedures with full audit trails, applies role-based access control per observation at recall time, and connects to coding agents, PR assistants, bug bots and sales agents over the Model Context Protocol (MCP). It integrates with the tools where work already lives (code repositories, pull requests, issues, documentation and meetings) to give both agents and humans unified organizational context, aiming to eliminate knowledge silos, reduce new-hire ramp time and retain institutional knowledge through employee turnover. The company is pre-launch and operating a waitlist; its primary integration surface is an
  MCP server rather than a traditional REST API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glen.png
layout: provider
mcp_servers:
- description: ''
  name: Glen MCP Server
  slug: glen-mcp-server
modified: '2026-07-19'
name: Glen
nav: Providers
network: true
overview: 'Glen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, MCP, and Organizational Memory.


  Glen''s developer surface includes engineering blog, signup flow, and 5 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Glen Domain Security
  slug: glen-domain-security
  summary_line: TLSv1.3 · HSTS
slug: glen
tags:
- Company
- Artificial Intelligence
- AI Agents
- MCP
- Organizational Memory
- Knowledge-Management
- Developer Tools
- Y Combinator
website: https://tryglen.com/
---
