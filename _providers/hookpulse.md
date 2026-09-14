---
agentic_access:
- acting_count: 14
  human_in_the_loop: 2
  name: Hookpulse Agentic Access
  operation_count: 31
  slug: hookpulse-agentic-access
  summary_line: 31 operations · 14 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'Public REST/HTTP API for heartbeat monitors, ingest URLs, miss detection, alerts, status feeds, auth, billing, credit, and metrics. OpenAPI 3.1.0 with ~31 operations. Also exposes a hosted MCP server '
  name: HookPulse API
  slug: hookpulse-api
artifact_total: 10
asyncapis:
- description: ''
  name: Hookpulse Webhooks
  slug: hookpulse-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://hookpulse.net
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hookpulse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hookpulse.net/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hookpulse-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hookpulse-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hookpulse-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hookpulse-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hookpulse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hookpulse-security.txt
- group: other
  title: ''
  type: APIsJson
  url: https://hookpulse.net/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hookpulse-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/hookpulse-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hookpulse-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/hookpulse-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hookpulse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hookpulse-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hookpulse-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hookpulse-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hookpulse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hookpulse-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hookpulse-data-model.yml
- group: docs
  title: ''
  type: APIReference
  url: https://hookpulse.net/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://hookpulse.net/api/billing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hookpulse.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hookpulse.net/privacy
created: '2026-09-05'
description: A dead-man's-switch for cron jobs and webhooks. You create a monitor and your cron/Stripe/n8n pings its ingest URL on schedule; if pings stop past a tolerated interval, it records a miss and alerts. Explicitly not website uptime monitoring; its stated primary consumer is AI agents. Offers a public REST API, a hosted MCP server, and llms.txt/OKF agent-readable docs, with x402/USDC micropayments for paid actions.
image: https://hookpulse.net/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: HookPulse MCP Server
  slug: hookpulse-mcp-server
- description: ''
  name: HookPulse
  slug: hookpulse
modified: '2026-09-05'
name: HookPulse
nav: Providers
network: true
overview: 'HookPulse publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Monitoring, Observability, Cron, Webhooks, and Heartbeat.


  The HookPulse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HookPulse''s developer surface includes authentication, API reference, pricing, and 23 more developer resources.'
plans:
- name: Hookpulse Plans Pricing
  plan_count: 3
  slug: hookpulse-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Hookpulse Rate Limits
  slug: hookpulse-rate-limits
security:
- kind: authentication
  name: Hookpulse Authentication
  slug: hookpulse-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hookpulse Domain Security
  slug: hookpulse-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hookpulse Vulnerability Disclosure
  slug: hookpulse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hookpulse
tags:
- Monitoring
- Observability
- Cron
- Webhooks
- Heartbeat
- Dead-mans-switch
- Alerting
- Status pages
- Agent-native
- MCP
- x402
- Micropayments
website: https://hookpulse.net
---
