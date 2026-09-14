---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'Resource-oriented REST API to manage integrations, providers, sessions, portals, skills, identities and MCP access programmatically. Bearer API-key auth, cursor pagination, date-based versioning; 466 '
  name: Metorial API
  slug: metorial-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.metorial.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/metorial-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://metorial.com/security
- group: auth
  title: ''
  type: SecurityCenter
  url: https://metorial.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metorial-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.metorial.com
- group: docs
  title: ''
  type: Documentation
  url: https://metorial.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://metorial.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://metorial.com/docs/api-getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://metorial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.metorial.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metorial
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metorial.com
- group: company
  title: ''
  type: Blog
  url: https://metorial.com/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metorial-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/metorial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metorial-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/metorial-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/metorial-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metorial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metorial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metorial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metorial-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/metorial-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metorial-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metorial-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metorial-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/metorial-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metorial-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/metorial-api-catalog.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Metorial is agentic infrastructure for AI-native companies — "the Vercel for MCP." It hosts 1,200+ Model Context Protocol (MCP) servers serverlessly, giving AI agents and clients like Claude, ChatGPT, Cursor, Copilot and Codex one place to connect approved apps, tools and shared skills. Its hibernation technology makes every MCP server serverless (sub-second cold starts, pay-per-request), and it handles production OAuth, per-user isolation, tracing, access control (SSO/SAML) and ProtoGuard request safety. Developers integrate through a resource-oriented REST API (api.metorial.com) with official Node.js, Python and Go SDKs, a CLI, and standard MCP URLs. Founded 2025, San Francisco; backed by Y Combinator (F25).
image: https://metorial.com/logo/logo.svg
layout: provider
modified: '2026-07-20'
name: Metorial
nav: Providers
network: true
overview: 'Metorial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, AI Agents, Agentic Infrastructure, and Integration.


  Metorial''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, CLI, and 24 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 3
  name: Metorial Rate Limits
  slug: metorial-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/metorial/refs/heads/main/screenshots/metorial-2026-08-07T172725.png
security:
- kind: authentication
  name: Metorial Authentication
  slug: metorial-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Metorial Domain Security
  slug: metorial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Metorial Trust Center
  slug: metorial-trust-center
  summary_line: SOC 2, GDPR
slug: metorial
tags:
- Company
- MCP
- AI Agents
- Agentic Infrastructure
- Integration
- Developer Tools
- Serverless
website: https://www.metorial.com/
---
