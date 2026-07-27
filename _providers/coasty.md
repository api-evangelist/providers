---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 93.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 42
  human_in_the_loop: 5
  name: Coasty Agentic Access
  operation_count: 72
  slug: coasty-agentic-access
  summary_line: 72 operations · 42 acting · 5 human-in-the-loop
api_count: 8
apis:
- description: API key management and usage reporting.
  name: Coasty keys API
  slug: coasty-keys-api
- description: Provision and control managed VMs.
  name: Coasty machines API
  slug: coasty-machines-api
- description: Stateless CUA action prediction and grounding.
  name: Coasty predict API
  slug: coasty-predict-api
- description: Autonomous task runs — the agent drives a task to completion on a machine.
  name: Coasty runs API
  slug: coasty-runs-api
- description: Cron and one-shot scheduled CUA jobs.
  name: Coasty schedules API
  slug: coasty-schedules-api
- description: Stateful CUA sessions with persistent trajectory.
  name: Coasty sessions API
  slug: coasty-sessions-api
- description: Webhook and chain triggers for schedules.
  name: Coasty triggers API
  slug: coasty-triggers-api
- description: Versioned, branching multi-step automations (DSL) and their runs.
  name: Coasty workflows API
  slug: coasty-workflows-api
artifact_total: 16
asyncapis:
- description: ''
  name: Coasty Webhooks
  slug: coasty-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coasty-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://coasty.ai/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coasty-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coasty-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coasty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://coasty.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coasty.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://coasty.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://coasty.ai/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coasty.ai/guide?tab=api
- group: company
  title: ''
  type: Blog
  url: https://coasty.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coasty.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coasty.ai/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coasty.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coasty.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:founders@coasty.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coasty-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coasty.ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/coasty-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/coasty-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coasty-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coasty-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/coasty-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coasty-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/coasty-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coasty-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coasty-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coasty-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coasty-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coasty-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/coasty-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/coasty-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coasty-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coasty-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/coasty-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coasty-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Coasty is a computer-use AI agent platform (Y Combinator S26) that operates a full desktop, browser, and terminal like a human — reading the screen with vision, clicking, typing, filling forms, running commands, and verifying its own work across sandboxed virtual machines. It exposes a public REST API at coasty.ai/v1 with a published OpenAPI 3.1 spec (72 operations), a first-party MCP server (npx @coasty/mcp, 26 tools), free sandbox keys, HMAC-SHA256 webhook triggers, an Idempotency-Key contract, per-credit metered billing, and 1,000+ OAuth app integrations via Composio. Core API surfaces are Predict, Sessions, Ground, Parse, Machines, Schedules, Runs, and Workflows. Founded 2025-2026 by Prateek Jannu and Nitish Kovuru; #1 on the OSWorld benchmark among production computer-use agents.'
image: https://coasty.ai/icon-512.svg
layout: provider
mcp_servers:
- description: First-party MCP server (npx -y @coasty/mcp; remote https://api.coasty.ai/mcp) exposing 26 computer-use tools across predict, machines, schedules, account, and discovery groups.
  name: Coasty Computer-Use MCP Server
  slug: coasty-computer-use-mcp-server
modified: '2026-07-18'
name: Coasty
nav: Providers
network: true
overview: 'Coasty publishes 8 APIs on the [APIs.io](https://apis.io/) network, including keys API, machines API, predict API, and 5 more. Tagged areas include Company, Computer Use, AI Agents, Automation, and RPA.


  The Coasty catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coasty''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Coasty Plans
  plan_count: 4
  slug: coasty-plans
random_paper: 47
rate_limits:
- limit_count: 0
  name: Coasty Rate Limits
  slug: coasty-rate-limits
score:
  band: strong
  composite: 63.1
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 67.6
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 63.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coasty/refs/heads/main/screenshots/coasty-2026-07-25T205838.png
security:
- kind: authentication
  name: Coasty Authentication
  slug: coasty-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Coasty Domain Security
  slug: coasty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coasty Vulnerability Disclosure
  slug: coasty-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coasty
tags:
- Company
- Computer Use
- AI Agents
- Automation
- RPA
- Desktop Automation
- Browser Automation
- MCP
- Virtual Machines
- Developer Tools
website: https://coasty.ai
---
