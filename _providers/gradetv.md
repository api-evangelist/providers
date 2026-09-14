---
agentic_access:
- acting_count: 41
  human_in_the_loop: 2
  name: Gradetv Agentic Access
  operation_count: 83
  slug: gradetv-agentic-access
  summary_line: 83 operations · 41 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: REST API for the Grade IPTV catalog and personal library, with a public OpenAPI 3.1 contract, hosted MCP server (46 tools), llms.txt agent documentation, and a well-known API catalog.
  name: Grade API
  slug: grade-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://gradetv.net
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/gradetv-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gradetv-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gradetv-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gradetv-security.txt
- group: auth
  title: ''
  type: Security
  url: security/gradetv-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gradetv-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gradetv-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gradetv-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gradetv-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gradetv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gradetv-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gradetv-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gradetv-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://gradetv.net/api/billing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gradetv.net/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gradetv.net/privacidade
- group: start
  title: ''
  type: GettingStarted
  url: https://gradetv.net/como-usar
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gradetv-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gradetv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradetv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gradetv-authentication.yml
created: '2026-09-05'
description: A searchable directory of public/free-to-air TV and radio broadcasts (sourced from iptv-org) plus a personal, URL-addressable media library with exportable feeds (M3U, M3U8, JSON, XSPF), EPG guide, per-channel health scores, and live chat. Exposes a REST API with OpenAPI 3.1, a hosted MCP server, and llms.txt agent docs.
image: https://gradetv.net/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Grade MCP Server
  slug: grade-mcp-server
- description: ''
  name: Grade
  slug: grade
modified: '2026-09-05'
name: Grade
nav: Providers
network: true
overview: 'Grade publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IPTV, Streaming, Live TV, Live Radio, and Media Catalog.


  Grade''s developer surface includes pricing, getting-started guide, authentication, and 20 more developer resources.'
plans:
- name: Gradetv Plans Pricing
  plan_count: 4
  slug: gradetv-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Gradetv Rate Limits
  slug: gradetv-rate-limits
security:
- kind: authentication
  name: Gradetv Authentication
  slug: gradetv-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradetv Domain Security
  slug: gradetv-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gradetv Vulnerability Disclosure
  slug: gradetv-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gradetv
tags:
- IPTV
- Streaming
- Live TV
- Live Radio
- Media Catalog
- Broadcast Metadata
- EPG
- TV Guide
- Content Aggregation
- Agent-native
- MCP
- x402
- Micropayments
- Brazil
website: https://gradetv.net
---
