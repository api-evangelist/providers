---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Public GraphQL API for the Glue workspace — send messages (sendMessage), read workspaces, threads, and groups, with Relay cursor-connection pagination and OAuth2 bearer auth.
  name: Glue GraphQL API
  slug: glue-graphql-api
artifact_total: 6
asyncapis:
- description: Faithful AsyncAPI rendering of Glue's documented outbound webhook catalog. Webhooks are configured per OAuth Application; when a workspace authorizes the app, Glue creates a webhook posting to the app
  name: Glue Outbound Webhooks
  slug: glue-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glue.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.glue.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.glue.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.glue.ai/developers/graphql-api/getting_started.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.glue.ai/developers/graphql-api/getting_started.md
- group: company
  title: ''
  type: Blog
  url: https://glue.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://glue.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.glue.ai/auth?intent=signup
- group: start
  title: ''
  type: Login
  url: https://app.glue.ai/auth?intent=signin
- group: operate
  title: ''
  type: Support
  url: https://docs.glue.ai/get-started/help-and-support.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glue.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glue.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.glue.ai
- group: auth
  title: ''
  type: Compliance
  url: https://glue.ai/company/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/glue-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/glue-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glue-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/glue-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/glue-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/glue-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glue-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/glue-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glue-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/glue-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glue-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Glue is a team communication platform that replaces channel-based chat with structured, named threads so decisions stay organized and don't get lost, with AI agents (@Glue, @Cursor) that can be mentioned inside threads to summarize, add context, and generate work. For developers, Glue exposes a public GraphQL API at api.gluegroups.com for sending messages and reading workspaces, threads, and groups; OAuth 2.0 authentication (client-credentials for the GraphQL API, plus an authorization-code flow with dynamic client registration and PKCE for a hosted remote MCP server at mcp.glue.ai); outbound webhooks (message.created, thread.created) signed with HMAC-SHA256; and idempotent upsert keys on message and thread creation. Glue is SOC 2 compliant, supports SSO (Google, Okta), and is backed by Craft Ventures and Y Combinator.
image: https://glue.ai/images/opengraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: glue-mcp.yml
  slug: glue-mcpyml
modified: '2026-07-19'
name: Glue
nav: Providers
network: true
overview: 'Glue publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Team Communication, Messaging, and Collaboration.


  The Glue catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Glue''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 44
scopes:
- name: Glue Scopes
  scope_count: 6
  slug: glue-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 51.6
  delta: 9.6
  facets:
    commercial_clarity: 52.6
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 42.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/glue/refs/heads/main/screenshots/glue-2026-07-25T215936.png
security:
- kind: authentication
  name: Glue Authentication
  slug: glue-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Glue Domain Security
  slug: glue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glue
tags:
- Company
- SaaS
- Team Communication
- Messaging
- Collaboration
- GraphQL
- Webhooks
- MCP
- Productivity
- AI Agents
website: https://glue.ai
---
