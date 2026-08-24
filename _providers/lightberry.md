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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.1
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lightberry-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://lightberry.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lightberry.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lightberry.com
- group: operate
  title: ''
  type: Support
  url: mailto:hello@lightberry.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/lightberry
- group: learn
  title: ''
  type: Youtube
  url: https://youtube.com/@lightberryinc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightberry-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightberry-domain-security.yml
created: '2026-07-17'
description: Lightberry is a San Francisco robotics software company (Y Combinator Fall 2025) that builds conversational AI "personality" software for humanoid and quadruped robots. Its platform lets a robot listen, speak, see its surroundings, and act on natural-language instruction without the owner writing any code, emphasizing emotional intelligence, contextual awareness, and autonomy rather than a simple speech-to-text voice pipeline. Lightberry ships pre-installed on robots sold through its partnership with Unitree, and the company runs a manufacturer-compatibility program with robot makers including Fourier, Booster Robotics, and High Torque. Its published documentation today covers device setup (power-on, WiFi provisioning, starting a conversation) plus an MCP architecture note describing a Model Context Protocol server that routes tool calls to individual Lightberry devices, which each expose a REST endpoint. There is no public developer portal, API reference, SDK, or OpenAPI definition
  at this time.
image: https://lightberry.com/assets/images/share.jpg
layout: provider
mcp_servers:
- description: ''
  name: Lightberry MCP Server
  slug: lightberry-mcp-server
modified: '2026-07-19'
name: Lightberry
nav: Providers
network: true
overview: 'Lightberry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Conversational AI, and Voice.


  Lightberry''s developer surface includes documentation, getting-started guide, support, YouTube channel, and 5 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 11.0
  provenance:
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightberry/refs/heads/main/screenshots/lightberry-2026-07-25T225107.png
security:
- kind: domain-security
  name: Lightberry Domain Security
  slug: lightberry-domain-security
  summary_line: TLSv1.3
slug: lightberry
tags:
- Company
- Robotics
- Artificial Intelligence
- Conversational AI
- Voice
- Hardware
- MCP
- Agents
- Y Combinator
website: https://lightberry.com
---
