---
api_count: 2
apis:
- description: 'REST API to list models and launch/track image and video generations. Endpoints: GET /api/models (unauthenticated catalog & pricing), POST /api/generate, GET /api/generate/status. Uses imk_ bearer-key'
  name: Imaginode REST API
  slug: imaginode-rest-api
- description: 'Hosted MCP server (Streamable HTTP transport) exposing four tools: list_models, generate_image, generate_video, get_generation_status. Authenticated via Authorization: Bearer imk_ header.'
  name: Imaginode MCP Server
  slug: imaginode-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://imaginode.ai
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imaginode-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imaginode-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/imaginode-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imaginode-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imaginode-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/imaginode-problem-types.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/imaginode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imaginode-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://imaginode.ai/en/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://imaginode.ai/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://imaginode.ai/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imaginode.ai/en/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imaginode.ai/en/legal/terms
- group: start
  title: ''
  type: Login
  url: https://imaginode.ai/en/login
created: '2026-09-03'
description: Browser-based AI creation studio with a node canvas for generating images, videos, voice-overs and LLM outputs. Provides a REST API, a hosted MCP server, and an llms.txt for programmatic and agent-based generation using a shared credit balance.
image: https://imaginode.ai/icons-512.png
layout: provider
mcp_servers:
- description: ''
  name: Imaginode MCP Server
  slug: imaginode-mcp-server
- description: Official hosted MCP server exposing Imaginode's generation pipeline (images, video, model catalog, job status) to any MCP client over Streamable HTTP. Stateless; billed against the connected account's
  name: Imaginode MCP Server
  slug: imaginode-mcp-server-2
modified: '2026-09-03'
name: Imaginode
nav: Providers
network: true
overview: 'Imaginode publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ai, image generation, video generation, text to speech, and mcp.


  Imaginode''s developer surface includes authentication, documentation, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Imaginode Plans Pricing
  plan_count: 3
  slug: imaginode-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Imaginode Rate Limits
  slug: imaginode-rate-limits
security:
- kind: authentication
  name: Imaginode Authentication
  slug: imaginode-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Imaginode Domain Security
  slug: imaginode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imaginode
tags:
- ai
- image generation
- video generation
- text to speech
- mcp
- generative ai
- llm
- creative tools
website: https://imaginode.ai
---
