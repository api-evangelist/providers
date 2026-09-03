---
api_count: 1
apis:
- description: REST/HTTP API to discover, inspect, run and poll third-party agent tools, with smart-run capabilities, leaderboards, wallet balance and agent self-registration. Exposes OpenAPI 3.1, two hosted MCP ser
  name: Cracked API
  slug: cracked-api
artifact_total: 12
asyncapis:
- description: ''
  name: Cracked Webhooks
  slug: cracked-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cracked-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cracked-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cracked-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cracked-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/cracked-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cracked-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cracked-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cracked-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cracked-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/cracked-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cracked-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cracked-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cracked-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cracked-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cracked-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://cracked.ai/status
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cracked-scopes.yml
- group: auth
  title: ''
  type: Security
  url: https://cracked.ai/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cracked-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cracked-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cracked-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cracked-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://cracked.ai/changelog
- group: build
  title: ''
  type: CLI
  url: cli/cracked-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cracked-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cracked-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cracked-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cracked-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cracked.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cracked.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://cracked.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://cracked.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cracked.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cracked.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cracked.ai/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://cracked.ai/postman/cracked.postman_collection.json
created: '2026-09-03'
description: 'Cracked is a tool router for AI agents: one API key and one prepaid balance to discover, inspect, run and poll thousands of third-party tools. It exposes 9,521 endpoints from 1,183 providers plus 50,000+ Apify actors, publishing measured success rate, median latency and per-call price per tool.'
image: https://cracked.ai/brand/icon.png
layout: provider
mcp_servers:
- description: ''
  name: Cracked API MCP Server
  slug: cracked-api-mcp-server
- description: ''
  name: Cracked API MCP Server
  slug: cracked-api-mcp-server-2
- description: ''
  name: Cracked API MCP Server
  slug: cracked-api-mcp-server-3
modified: '2026-09-03'
name: Cracked API
nav: Providers
network: true
overview: 'Cracked API publishes 1 API on the [APIs.io](https://apis.io/) network: Cracked API. Tagged areas include ai agents, agent tools, mcp, tool router, and API aggregator.


  The Cracked API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cracked API''s developer surface includes authentication, sandbox, changelog, CLI, API reference, getting-started guide, pricing, and 30 more developer resources.'
plans:
- name: Cracked Plans Pricing
  plan_count: 3
  slug: cracked-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Cracked Rate Limits
  slug: cracked-rate-limits
scopes:
- name: Cracked Scopes
  scope_count: 4
  slug: cracked-scopes
  summary_line: 4 scopes · authorizationCode
security:
- kind: authentication
  name: Cracked Authentication
  slug: cracked-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cracked Domain Security
  slug: cracked-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cracked Vulnerability Disclosure
  slug: cracked-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cracked Trust Center
  slug: cracked-trust-center
  summary_line: trust center published
slug: cracked
tags:
- ai agents
- agent tools
- mcp
- tool router
- API aggregator
- web search
- web scraping
- data enrichment
- llms.txt
- agent skills
- pay-per-call
- ai-agents
- agent-tools
- tool-router
- aggregator
- web-search
- web-scraping
- data-enrichment
- lead-generation
- ai-models
- developer-tools
- AI agents
- MCP
- lead gen
- SEO
- social media data
- ecommerce
- finance
- weather
- AI models
website: https://cracked.ai/docs
---
