---
api_count: 1
apis:
- description: Synchronous REST API for scraping public social media data across ~23 platforms, returning structured JSON. 206 operations under /v1. API-key auth via x-api-key header. Supports x402 USDC-on-Base pay-
  name: Social Fetch REST API
  slug: social-fetch-rest-api
artifact_total: 11
asyncapis:
- description: ''
  name: Social Fetch Webhooks
  slug: social-fetch-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.socialfetch.dev
- group: build
  title: ''
  type: x-ToolCrosswalk
  url: mcp/social-fetch-tool-crosswalk.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/social-fetch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/social-fetch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/social-fetch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/social-fetch-authentication.yml
- group: auth
  title: ''
  type: Security
  url: security/social-fetch-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/social-fetch-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/social-fetch-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/social-fetch-llms.yml
- group: build
  title: ''
  type: Packages
  url: packages/social-fetch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/social-fetch-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/social-fetch-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/social-fetch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/social-fetch-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/social-fetch-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/social-fetch-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/social-fetch-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/social-fetch-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/social-fetch-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/social-fetch-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/social-fetch-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.socialfetch.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.socialfetch.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.socialfetch.dev/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.socialfetch.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.socialfetch.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.socialfetch.dev/blog
- group: operate
  title: ''
  type: Support
  url: https://www.socialfetch.dev/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/social-freak-ltd
created: '2026-09-10'
description: Hosted social-media scraper API returning structured JSON for public profiles, posts, comments, engagement metrics, transcripts, and search across ~23 platforms. Offers a REST API with public OpenAPI contract, a hosted MCP server, an llms.txt file set, published agent skills, and x402 pay-per-call payments.
layout: provider
mcp_servers:
- description: ''
  name: Social Fetch MCP Server
  slug: social-fetch-mcp-server
- description: Typed social-data tools (TikTok, Instagram, YouTube, X, Reddit, and 20+ more platforms) plus live docs search, exposed over a hosted remote MCP server. The tool surface is a near 1:1 typed mirror of t
  name: Social Fetch MCP
  slug: social-fetch-mcp
modified: '2026-09-11'
name: Social Fetch
nav: Providers
network: true
overview: 'Social Fetch publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include social media, web scraping, data extraction, social listening, and monitoring.


  The Social Fetch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Social Fetch''s developer surface includes authentication, pricing, signup flow, engineering blog, support, and 26 more developer resources.'
plans:
- name: Social Fetch Plans Pricing
  plan_count: 3
  slug: social-fetch-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Social Fetch Rate Limits
  slug: social-fetch-rate-limits
scopes:
- name: Social Fetch Scopes
  scope_count: 0
  slug: social-fetch-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Social Fetch Authentication
  slug: social-fetch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Social Fetch Domain Security
  slug: social-fetch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Social Fetch Vulnerability Disclosure
  slug: social-fetch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Social Fetch Trust Center
  slug: social-fetch-trust-center
  summary_line: trust center published
slug: social-fetch
tags:
- social media
- web scraping
- data extraction
- social listening
- monitoring
- structured data
- JSON API
- REST
- MCP
- agent-native
- TypeScript SDK
- transcripts
- ads intelligence
website: https://www.socialfetch.dev
---
