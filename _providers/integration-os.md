---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.withone.ai
  baseurl_source: declared
  description: One is the current successor brand to IntegrationOS and Pica. It provides agent infrastructure with a unified CLI for 250+ platforms and 50,000+ tools, managed OAuth (AuthKit), multi-step Flows, memor
  name: One (successor to IntegrationOS / Pica)
  slug: successor
artifact_total: 10
asyncapis:
- description: ''
  name: Integration Os Webhooks
  slug: integration-os-webhooks
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/integration-os-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/integration-os-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.withone.ai/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/withoneai/knowledge/issues
- group: other
  title: ''
  type: AgentCard
  url: a2a/integration-os-a2a.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integration-os-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integrationos
- group: start
  title: ''
  type: Portal
  url: https://withone.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.withone.ai/docs/welcome
- group: company
  title: ''
  type: Blog
  url: https://www.withone.ai/blog
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.withone.ai/knowledge
- group: start
  title: ''
  type: Signup
  url: https://app.withone.ai
- group: start
  title: ''
  type: Login
  url: https://app.withone.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/withoneai
- group: other
  title: ''
  type: HistoricalSite
  url: https://www.picaos.com/
- group: build
  title: ''
  type: HistoricalGitHub
  url: https://github.com/integration-os
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/integration-os-one-api-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/integration-os-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/integration-os-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/integration-os-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/integration-os-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/integration-os-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/integration-os-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/integration-os-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/integration-os-cli.yml
- group: design
  title: ''
  type: Components
  url: components/integration-os-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/integration-os-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/integration-os-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/integration-os-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/integration-os-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/integration-os-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/integration-os-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/integration-os-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withone.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/integration-os-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/integration-os-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/integration-os-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/integration-os-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/integration-os-rules.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/integration-os-one-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://www.withone.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.withone.ai/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.withone.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.withone.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.withone.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.withone.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withoneai
created: '2026-03-27'
description: 'IntegrationOS was a unified API platform that let developers add third-party integrations to their products with a single API call. The company rebranded as Pica (picaos.com) and then, on 2026-03-25, as One (withone.ai) — the provider''s own changelog records the step as "Pica is now One". One is an agent infrastructure platform: authenticated access to 789 platforms and 111,176 actions through a unified CLI, managed OAuth (AuthKit), multi-step Flows, inbound webhook Relay, and both a hosted and a local Model Context Protocol server. This record preserves the IntegrationOS history and profiles the active successor''s published surface, including its OpenAPI 3.1.0 contract (248 operations), its four-tool MCP server, its llms.txt and its agent.json.'
finops:
- name: Integration Os Finops
  service_category: API
  slug: integration-os-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: One ships BOTH a hosted remote MCP server and a local-stdio server, and the provider documents them as two ways to reach the same four tools. The remote endpoint is reachable and OAuth-gated; the loca
  name: IntegrationOS MCP Server
  slug: integrationos-mcp-server
modified: '2026-09-13'
name: IntegrationOS
nav: Providers
network: true
overview: 'IntegrationOS publishes 1 API on the [APIs.io](https://apis.io/) network: One (successor to IntegrationOS / Pica). Tagged areas include Agent Infrastructure, AI Agents, Connectors, Historical, and Integration.


  The IntegrationOS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  IntegrationOS''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, CLI, sandbox, and 41 more developer resources.'
plans:
- name: Integration Os Plans Pricing
  plan_count: 4
  slug: integration-os-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Integration Os Rate Limits
  slug: integration-os-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: IntegrationOS API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: integration-os-rules
scopes:
- name: Integration Os Scopes
  scope_count: 38
  slug: integration-os-scopes
  summary_line: 38 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/integration-os/refs/heads/main/screenshots/integration-os-2026-06-20T183438.png
security:
- kind: authentication
  name: Integration Os Authentication
  slug: integration-os-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Integration Os Domain Security
  slug: integration-os-domain-security
  summary_line: TLSv1.3 · HSTS
slug: integration-os
tags:
- Agent Infrastructure
- AI Agents
- Connectors
- Historical
- Integration
- iPaaS
- MCP
- Rebrand
- Unified-API
website: https://www.withone.ai/
---
