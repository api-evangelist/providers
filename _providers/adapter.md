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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 61
  human_in_the_loop: 3
  name: Adapter Agentic Access
  operation_count: 110
  slug: adapter-agentic-access
  summary_line: 110 operations · 61 acting · 3 human-in-the-loop
api_count: 26
apis:
- description: The Adapter API API from Adapter — 1 operation(s) for adapter api.
  name: Adapter Adapter API API
  slug: adapter-adapter-api-api
- description: The assets API from Adapter — 8 operation(s) for assets.
  name: Adapter assets API
  slug: adapter-assets-api
- description: The auth API from Adapter — 23 operation(s) for auth.
  name: Adapter auth API
  slug: adapter-auth-api
- description: The conversations API from Adapter — 11 operation(s) for conversations.
  name: Adapter conversations API
  slug: adapter-conversations-api
- description: The Docs API from Adapter — 1 operation(s) for docs.
  name: Adapter Docs API
  slug: adapter-docs-api
- description: The Imessage API from Adapter — 1 operation(s) for imessage.
  name: Adapter Imessage API
  slug: adapter-imessage-api
- description: The knowledge API from Adapter — 11 operation(s) for knowledge.
  name: Adapter knowledge API
  slug: adapter-knowledge-api
- description: The life API from Adapter — 1 operation(s) for life.
  name: Adapter life API
  slug: adapter-life-api
- description: The Line API from Adapter — 1 operation(s) for line.
  name: Adapter Line API
  slug: adapter-line-api
- description: The location API from Adapter — 1 operation(s) for location.
  name: Adapter location API
  slug: adapter-location-api
- description: The management API from Adapter — 1 operation(s) for management.
  name: Adapter management API
  slug: adapter-management-api
- description: The Oauth API from Adapter — 1 operation(s) for oauth.
  name: Adapter Oauth API
  slug: adapter-oauth-api
- description: The oauth-connect API from Adapter — 3 operation(s) for oauth-connect.
  name: Adapter oauth-connect API
  slug: adapter-oauth-connect-api
- description: The oauth2 API from Adapter — 2 operation(s) for oauth2.
  name: Adapter oauth2 API
  slug: adapter-oauth2-api
- description: The Openapi.json API from Adapter — 1 operation(s) for openapi.json.
  name: Adapter Openapi.json API
  slug: adapter-openapi-json-api
- description: The proxy API from Adapter — 13 operation(s) for proxy.
  name: Adapter proxy API
  slug: adapter-proxy-api
- description: The radar API from Adapter — 2 operation(s) for radar.
  name: Adapter radar API
  slug: adapter-radar-api
- description: The Redoc API from Adapter — 1 operation(s) for redoc.
  name: Adapter Redoc API
  slug: adapter-redoc-api
- description: The reminders API from Adapter — 3 operation(s) for reminders.
  name: Adapter reminders API
  slug: adapter-reminders-api
- description: The reranking API from Adapter — 1 operation(s) for reranking.
  name: Adapter reranking API
  slug: adapter-reranking-api
- description: The Sendblue API from Adapter — 1 operation(s) for sendblue.
  name: Adapter Sendblue API
  slug: adapter-sendblue-api
- description: The Sms API from Adapter — 1 operation(s) for sms.
  name: Adapter Sms API
  slug: adapter-sms-api
- description: The support API from Adapter — 1 operation(s) for support.
  name: Adapter support API
  slug: adapter-support-api
- description: The Users API from Adapter — 1 operation(s) for users.
  name: Adapter Users API
  slug: adapter-users-api
- description: The Webhook API from Adapter — 3 operation(s) for webhook.
  name: Adapter Webhook API
  slug: adapter-webhook-api
- description: The Whatsapp API from Adapter — 2 operation(s) for whatsapp.
  name: Adapter Whatsapp API
  slug: adapter-whatsapp-api
artifact_total: 31
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/adapter-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adapter-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adapter-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adapter-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adapter-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adapter-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adapter-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adapter-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adapter-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adapter-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adapter-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adapter-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adapter-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adapter-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.adapter.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.adapter.com/get-access
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adapter.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adapter.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.adapter.com
- group: operate
  title: ''
  type: Support
  url: mailto:hello@adapter.com
created: '2026-07-17'
description: 'Adapter is a cognition API — a persistent memory and knowledge-graph layer that sits alongside AI models so understanding is already available when agents need answers. Founded by Adam Ghetti and David Bader, Adapter continuously reads and connects a user''s data (calendar, contacts, messages, email, conversations) into a living knowledge graph, grounding every response in cited sources and surfacing hidden connections across sources rather than starting each query from scratch. The Adapter API exposes multi-model conversation/completion endpoints, knowledge-graph and memory queries, life-radar events, reminders, multi-channel messaging, reranking, and an OAuth 2.0 + hosted MCP surface (mcp:read) for agent access. Tagline: "Give your model a mind."'
image: https://framerusercontent.com/images/jeqjDUjgYoFJr6KfWmg7Kvi2Rs.png
layout: provider
mcp_servers:
- description: ''
  name: adapter-mcp.yml
  slug: adapter-mcpyml
modified: '2026-07-17'
name: Adapter
nav: Providers
network: true
overview: 'Adapter publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Adapter API API, assets API, auth API, and 23 more. Tagged areas include Company, Ai, Cognition, Knowledge Graph, and Memory.


  Adapter''s developer surface includes authentication, engineering blog, signup flow, support, and 17 more developer resources.'
random_paper: 8
scopes:
- name: Adapter Scopes
  scope_count: 2
  slug: adapter-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 35.8
  delta: 0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 46.7
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Adapter Authentication
  slug: adapter-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Adapter Domain Security
  slug: adapter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: adapter
tags:
- Company
- Ai
- Cognition
- Knowledge Graph
- Memory
- Agents
- MCP
- LLM
website: https://www.adapter.com
---
