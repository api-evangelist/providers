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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Phonic Agentic Access
  operation_count: 50
  slug: phonic-agentic-access
  summary_line: 50 operations · 32 acting
api_count: 10
apis:
- description: The agents API from Phonic — 5 operation(s) for agents.
  name: Phonic agents API
  slug: phonic-agents-api
- description: The apiKeys API from Phonic — 3 operation(s) for apikeys.
  name: Phonic apiKeys API
  slug: phonic-apikeys-api
- description: The auth API from Phonic — 2 operation(s) for auth.
  name: Phonic auth API
  slug: phonic-auth-api
- description: The conversationItems API from Phonic — 1 operation(s) for conversationitems.
  name: Phonic conversationItems API
  slug: phonic-conversationitems-api
- description: The conversations API from Phonic — 9 operation(s) for conversations.
  name: Phonic conversations API
  slug: phonic-conversations-api
- description: The extractionSchemas API from Phonic — 2 operation(s) for extractionschemas.
  name: Phonic extractionSchemas API
  slug: phonic-extractionschemas-api
- description: The projects API from Phonic — 4 operation(s) for projects.
  name: Phonic projects API
  slug: phonic-projects-api
- description: The tools API from Phonic — 2 operation(s) for tools.
  name: Phonic tools API
  slug: phonic-tools-api
- description: The voices API from Phonic — 2 operation(s) for voices.
  name: Phonic voices API
  slug: phonic-voices-api
- description: The workspace API from Phonic — 1 operation(s) for workspace.
  name: Phonic workspace API
  slug: phonic-workspace-api
artifact_total: 16
asyncapis:
- description: ''
  name: API Reference
  slug: phonic-sts-asyncapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phonic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phonic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phonic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/phonic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/phonic-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/phonic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phonic-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/phonic-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/phonic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phonic-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.phonic.ai/
- group: design
  title: ''
  type: Conventions
  url: conventions/phonic-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phonic-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/phonic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.phonic.co/webhooks/overview
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.phonic.co/
- group: company
  title: ''
  type: Blog
  url: https://phonic.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Phonic-Co
- group: commercial
  title: ''
  type: Pricing
  url: https://phonic.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phonic.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phonic.co/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://phonic.ai/
created: '2026-07-17'
description: Phonic is a San Francisco voice AI company (founded 2024, seed-backed by Lux Capital) building the first end-to-end speech-to-speech platform for reliable conversational voice agents. The Phonic API lets developers create and configure voice agents, attach voices, place and receive inbound/outbound phone calls (including via SIP trunking and Amazon Connect), run real-time speech-to-speech conversations over a WebSocket, wire up webhook/WebSocket/context/transfer/MCP tools, and analyze, evaluate, and extract structured data from conversations. It ships an OpenAPI 3.1 REST spec, an AsyncAPI 2.6.0 WebSocket spec, official Node and Python SDKs, a hosted MCP server, and llms.txt docs for AI clients.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phonic.png
layout: provider
mcp_servers:
- description: ''
  name: phonic-mcp.yml
  slug: phonic-mcpyml
modified: '2026-07-20'
name: Phonic
nav: Providers
network: true
overview: 'Phonic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including agents API, apiKeys API, auth API, and 7 more. Tagged areas include Company, Artificial Intelligence, Voice AI, Conversational AI, and Speech.


  The Phonic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Phonic''s developer surface includes authentication, engineering blog, pricing, and 20 more developer resources.'
random_paper: 74
rate_limits:
- limit_count: 3
  name: Phonic Rate Limits
  slug: phonic-rate-limits
score:
  band: developing
  composite: 48.9
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 65.4
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 60.5
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Phonic Authentication
  slug: phonic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Phonic Domain Security
  slug: phonic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phonic
tags:
- Company
- Artificial Intelligence
- Voice AI
- Conversational AI
- Speech
- Voice Agents
- Telephony
- Speech To Speech
website: https://phonic.ai/
---
