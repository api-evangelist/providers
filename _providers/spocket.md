---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Hosted MCP server (Streamable HTTP) with ~20 tools for deploying and managing always-on apps. Uses OAuth 2.1 with PKCE and dynamic client registration; usable by any account holder from Claude Code, C
  name: Spocket MCP Server
  slug: spocket-mcp-server
- description: White-label reseller/provisioning REST API for hosting apps from a customer backend. OAuth2 client-credentials auth; endpoints for apps, power control, logs, sub-accounts and account. Gated behind the
  name: Spocket Platform REST API
  slug: spocket-platform-rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spocket-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spocket.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.spocket.dev/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://www.spocket.dev/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.spocket.dev/documentation/platform-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.spocket.dev/documentation/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@spocket.dev
- group: company
  title: ''
  type: Blog
  url: https://www.spocket.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spocket.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.spocket.dev/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spocket.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spocket.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.spocket.dev/status
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spocket-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spocket-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spocket-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spocket-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/spocket-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spocket-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spocket-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spocket-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spocket-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/spocket-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spocket-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-07'
description: Agent-native deployment/hosting platform. An AI coding agent ships a folder over MCP and it runs 24/7 with HTTPS URLs and custom domains. Supports Discord/Slack/Telegram/Twitch bots, web apps/APIs, static sites, scrapers, queue consumers and cron jobs on Node 22 and Python 3.11. No CLI, Dockerfile, or YAML.
image: https://www.spocket.dev/brand/spocket-wordmark.png
layout: provider
mcp_servers:
- description: ''
  name: Spocket MCP Server
  slug: spocket-mcp-server
modified: '2026-08-09'
name: Spocket
nav: Providers
network: true
overview: 'Spocket publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Platform-as-a-Service, Application Hosting, bot-hosting, Developer Tools, and Agent Infrastructure.


  Spocket''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Spocket Plans Pricing
  plan_count: 4
  slug: spocket-plans-pricing
random_paper: 5
scopes:
- name: Spocket Scopes
  scope_count: 5
  slug: spocket-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 38.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Spocket Authentication
  slug: spocket-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Spocket Domain Security
  slug: spocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spocket
tags:
- Platform-as-a-Service
- Application Hosting
- bot-hosting
- Developer Tools
- Agent Infrastructure
- MCP
- Deployment
- Serverless
- always-on
website: https://www.spocket.dev
---
