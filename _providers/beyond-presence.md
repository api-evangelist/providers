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
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: The Agents API from Beyond Presence — 2 operation(s) for agents.
  name: Beyond Presence Agents API
  slug: beyond-presence-agents-api
- description: The Authentication API from Beyond Presence — 1 operation(s) for authentication.
  name: Beyond Presence Authentication API
  slug: beyond-presence-authentication-api
- description: The Avatars API from Beyond Presence — 2 operation(s) for avatars.
  name: Beyond Presence Avatars API
  slug: beyond-presence-avatars-api
- description: The Calls API from Beyond Presence — 3 operation(s) for calls.
  name: Beyond Presence Calls API
  slug: beyond-presence-calls-api
- description: The External APIs API from Beyond Presence — 2 operation(s) for external apis.
  name: Beyond Presence External APIs API
  slug: beyond-presence-external-apis-api
- description: The Knowledge Files API from Beyond Presence — 4 operation(s) for knowledge files.
  name: Beyond Presence Knowledge Files API
  slug: beyond-presence-knowledge-files-api
- description: The Sessions API from Beyond Presence — 2 operation(s) for sessions.
  name: Beyond Presence Sessions API
  slug: beyond-presence-sessions-api
artifact_total: 19
asyncapis:
- description: ''
  name: Beyond Presence Webhooks
  slug: beyond-presence-webhooks
collections:
- collection_type: postman
  name: Fast Agents API
  slug: postman-beyond-presence-agents-api
- collection_type: postman
  name: Fast Agents Authentication API
  slug: postman-beyond-presence-authentication-api
- collection_type: postman
  name: Fast Agents Avatars API
  slug: postman-beyond-presence-avatars-api
- collection_type: postman
  name: Fast Agents Calls API
  slug: postman-beyond-presence-calls-api
- collection_type: postman
  name: Fast Agents External APIs API
  slug: postman-beyond-presence-external-apis-api
- collection_type: postman
  name: Fast Agents Knowledge Files API
  slug: postman-beyond-presence-knowledge-files-api
- collection_type: postman
  name: Fast Agents Sessions API
  slug: postman-beyond-presence-sessions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/beyond-presence/overview
- group: other
  title: ''
  type: AgentCard
  url: a2a/beyond-presence-a2a.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bey.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bey.dev/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bey.dev/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bey.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://beyondpresence.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://beyondpresence.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.bey.chat/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyondpresence.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyondpresence.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/A3JTzk5aWa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bey-dev
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.bey.dev/learn/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bey.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beyond-presence-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bey.dev/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bey.dev/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beyond-presence-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/beyond-presence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/beyond-presence-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beyond-presence-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beyond-presence-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beyond-presence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beyond-presence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beyond-presence-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beyond-presence-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beyond-presence-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/beyond-presence-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beyond-presence-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/beyond-presence-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beyond-presence-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Beyond Presence (brand "bey") is a Europe-based AI company building real-time conversational AI video agents and speech-to-video (S2V) technology. Its platform lets developers deploy hyper-realistic AI video avatars that respond in real time (sub-1.2s latency at up to 1080p) across HR, sales, support, and coaching use cases. Two products are exposed through one REST API at api.bey.dev: a Speech-to-Video API that turns audio streams into lifelike avatars over LiveKit, and a Managed Agents API that runs end-to-end conversational agents with knowledge files, external LLM/API configuration, and webhook events. Official Python and TypeScript SDKs, an OpenAPI spec, and GDPR / SOC 2 Type II compliance are published. Surfaced as an HV Capital portfolio company and enriched from its public developer surface.'
image: https://beyondpresence.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: beyond-presence-mcp.yml
  slug: beyond-presence-mcpyml
modified: '2026-07-18'
name: Beyond Presence
nav: Providers
network: true
overview: 'Beyond Presence publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Authentication API, Avatars API, and 4 more. Tagged areas include Company, Ai Enterprise Software, Artificial Intelligence, Avatars, and Video.


  The Beyond Presence catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beyond Presence''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 26 more developer resources.'
random_paper: 19
score:
  band: strong
  composite: 60.4
  delta: 0.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.3
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 59.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beyond-presence/refs/heads/main/screenshots/beyond-presence-2026-07-25T202842.png
security:
- kind: authentication
  name: Beyond Presence Authentication
  slug: beyond-presence-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Beyond Presence Domain Security
  slug: beyond-presence-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Beyond Presence Trust Center
  slug: beyond-presence-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: beyond-presence
tags:
- Company
- Ai Enterprise Software
- Artificial Intelligence
- Avatars
- Video
- Conversational AI
- Agents
- Speech To Video
- Real Time Communication
website: https://docs.bey.dev
---
