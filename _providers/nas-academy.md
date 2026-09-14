---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nas Academy Agentic Access
  operation_count: 36
  slug: nas-academy-agentic-access
  summary_line: 36 operations
api_count: 1
apis:
- baseURL: https://nas.com
  baseurl_source: spec
  description: Public machine-readable resources for AI assistants, crawlers, and agents.
  name: Nas Academy AI discovery API
  slug: nas-academy-ai-discovery-api
- baseURL: https://nas.com
  baseurl_source: spec
  description: Public developer and integration guidance without private API contracts.
  name: Nas Academy Developer discovery API
  slug: nas-academy-developer-discovery-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nas.com Public Discovery AI discovery API
  slug: open-nas-academy-ai-discovery-api
- collection_type: open
  name: Nas.com Public Discovery AI discovery Developer discovery API
  slug: open-nas-academy-developer-discovery-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/nas-academy-discovery-skill.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nas-academy-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nas-academy-discovery-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://nasdaily.com
created: '2026-07-17'
description: Nas Academy is a company surfaced as a portfolio company of 500-global and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: Official authenticated hosted MCP server for Nas.com business, member, product, and order context.
  name: Nas Academy MCP Server
  slug: nas-academy-mcp-server
modified: '2026-07-17'
name: Nas Academy
nav: Providers
network: true
overview: 'Nas Academy publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI discovery API and Developer discovery API. Tagged areas include Company.'
random_paper: 20
scopes:
- name: Nas Academy Scopes
  scope_count: 6
  slug: nas-academy-scopes
  summary_line: 6 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/nas-academy/refs/heads/main/screenshots/nas-academy-2026-08-07T184637.png
security:
- kind: authentication
  name: Nas Academy Authentication
  slug: nas-academy-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Nas Academy Domain Security
  slug: nas-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nas-academy
tags:
- Company
website: https://nasdaily.com
---
