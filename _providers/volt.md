---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Authenticated remote MCP server that lets AI models and agents access a user's Volt (WhatsApp) data — contacts, chats, messages, groups, and lists.
  name: Volt MCP Server
  slug: volt-mcp-server
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://voltchat.com
- group: docs
  title: ''
  type: Documentation
  url: https://voltchat.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://voltchat.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://voltchat.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/volt-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/volt-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/volt-authentication.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volt-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/volt-llms.txt
created: '2026-07-17'
description: Volt is a desktop application (Mac, Windows, and Chrome) that supercharges WhatsApp for professionals and sales teams — turning long voice notes into readable transcripts and summaries, scheduling messages, adding keyboard-first navigation, organizing chats into focused workspaces, and sending personalized broadcasts. Message content stays under WhatsApp's end-to-end encryption and never passes through Volt's own servers. For agents and AI models, Volt runs an authenticated remote Model Context Protocol (MCP) server that exposes WhatsApp contacts, chats, messages, groups, and lists as tools. Volt is backed by 500 Global, EQT Ventures, and IVP.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volt.png
layout: provider
mcp_servers:
- description: ''
  name: volt-mcp.yml
  slug: volt-mcpyml
modified: '2026-07-21'
name: Volt
nav: Providers
network: true
overview: 'Volt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WhatsApp, Messaging, Productivity, and MCP.


  Volt''s developer surface includes documentation, pricing, engineering blog, changelog, authentication, and 5 more developer resources.'
random_paper: 73
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 17.9
  provenance:
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Volt Authentication
  slug: volt-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Volt Domain Security
  slug: volt-domain-security
  summary_line: TLSv1.3 · HSTS
slug: volt
tags:
- Company
- WhatsApp
- Messaging
- Productivity
- MCP
- AI Agents
- Sales
- Communication
website: https://voltchat.com
---
