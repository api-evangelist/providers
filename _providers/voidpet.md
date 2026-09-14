---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://voidpet.com
  baseurl_source: declared
  description: The Discovery API from Voidpet — 1 operation(s) for discovery.
  name: Voidpet Discovery API
  slug: voidpet-discovery-api
- baseURL: https://voidpet.com
  baseurl_source: declared
  description: The Health API from Voidpet — 1 operation(s) for health.
  name: Voidpet Health API
  slug: voidpet-health-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voidpet Public Discovery API
  slug: open-voidpet-discovery-api
- collection_type: open
  name: Voidpet Public Discovery Health API
  slug: open-voidpet-health-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.voidpet.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/voidpet-discovery-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voidpet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voidpet-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voidpet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voidpet-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voidpet-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/voidpet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voidpet-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://voidpet.com/.well-known/api-docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://voidpet.com/.well-known/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://voidpet.com/o/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voidpet.com/o/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voidpet.com/o/privacy
created: '2026-07-17'
description: Voidpet is a creative games studio behind emotion-inspired games, stories, characters, and community — including Voidpet Dungeon, a turn-based roguelite RPG about befriending and battling emotion-inspired creatures, and Voidpet Garden, a mental-health companion game for collecting emotions and practicing self care. Beyond the games, Voidpet publishes a small, public, read-only Discovery API (OpenAPI 3.1) plus a hosted Model Context Protocol server and a packaged Agent Skill so agents can discover its public products, pages, and legal documents. The discovery surface exposes no accounts, game state, or authenticated actions — it is agent-facing metadata only.
image: https://voidpet.com/ogimage.png
layout: provider
mcp_servers:
- description: Read-only, public MCP server exposing Voidpet's public products, pages, and legal-document discovery metadata. No authentication; no account or game-state access.
  name: Voidpet MCP Server
  slug: voidpet-mcp-server
modified: '2026-07-21'
name: Voidpet
nav: Providers
network: true
overview: 'Voidpet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and Health API. Tagged areas include Company, Games, Gaming, Mental Health, and Wellness.


  Voidpet''s developer surface includes authentication, documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/voidpet/refs/heads/main/screenshots/voidpet-2026-09-02T170212.png
security:
- kind: authentication
  name: Voidpet Authentication
  slug: voidpet-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Voidpet Domain Security
  slug: voidpet-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: voidpet
tags:
- Company
- Games
- Gaming
- Mental Health
- Wellness
- Discovery
- Agents
- MCP
- Read Only
website: https://www.voidpet.com/
---
