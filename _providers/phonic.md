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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Phonic Agentic Access
  operation_count: 50
  slug: phonic-agentic-access
  summary_line: 50 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The agents API from Phonic — 5 operation(s) for agents.
  name: Phonic agents API
  slug: phonic-agents-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The apiKeys API from Phonic — 3 operation(s) for apikeys.
  name: Phonic apiKeys API
  slug: phonic-apikeys-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The auth API from Phonic — 2 operation(s) for auth.
  name: Phonic auth API
  slug: phonic-auth-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The conversationItems API from Phonic — 1 operation(s) for conversationitems.
  name: Phonic conversationItems API
  slug: phonic-conversationitems-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The conversations API from Phonic — 9 operation(s) for conversations.
  name: Phonic conversations API
  slug: phonic-conversations-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The extractionSchemas API from Phonic — 2 operation(s) for extractionschemas.
  name: Phonic extractionSchemas API
  slug: phonic-extractionschemas-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The projects API from Phonic — 4 operation(s) for projects.
  name: Phonic projects API
  slug: phonic-projects-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The tools API from Phonic — 2 operation(s) for tools.
  name: Phonic tools API
  slug: phonic-tools-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The voices API from Phonic — 2 operation(s) for voices.
  name: Phonic voices API
  slug: phonic-voices-api
- baseURL: https://api.phonic.ai/v1
  baseurl_source: declared
  description: The workspace API from Phonic — 1 operation(s) for workspace.
  name: Phonic workspace API
  slug: phonic-workspace-api
artifact_total: 27
asyncapis:
- description: ''
  name: API Reference
  slug: phonic-sts-asyncapi-original
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference agents API
  slug: open-phonic-agents-api
- collection_type: open
  name: API Reference agents apiKeys API
  slug: open-phonic-apikeys-api
- collection_type: open
  name: API Reference agents auth API
  slug: open-phonic-auth-api
- collection_type: open
  name: API Reference agents conversationItems API
  slug: open-phonic-conversationitems-api
- collection_type: open
  name: API Reference agents conversations API
  slug: open-phonic-conversations-api
- collection_type: open
  name: API Reference agents extractionSchemas API
  slug: open-phonic-extractionschemas-api
- collection_type: open
  name: API Reference agents projects API
  slug: open-phonic-projects-api
- collection_type: open
  name: API Reference agents tools API
  slug: open-phonic-tools-api
- collection_type: open
  name: API Reference agents voices API
  slug: open-phonic-voices-api
- collection_type: open
  name: API Reference agents workspace API
  slug: open-phonic-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/phonic-openapi-overlay.yaml
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
- description: Phonic's inbound MCP server exposes the Phonic API as MCP tools so a client such as Claude Code, Codex, or Cursor can manage agents, conversations, voices, and projects. It stays up to date with the P
  name: Phonic MCP Server
  slug: phonic-mcp-server
modified: '2026-07-20'
name: Phonic
nav: Providers
network: true
overview: 'Phonic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including agents API, apiKeys API, auth API, and 7 more. Tagged areas include Company, Artificial Intelligence, Voice AI, Conversational AI, and Speech.


  The Phonic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Phonic''s developer surface includes authentication, engineering blog, pricing, and 21 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 3
  name: Phonic Rate Limits
  slug: phonic-rate-limits
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 65.1
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 48.5
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phonic/refs/heads/main/screenshots/phonic-2026-08-17T081212.png
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
- Speech to Speech
website: https://phonic.ai/
---
