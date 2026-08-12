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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Samora Ai Agentic Access
  operation_count: 17
  slug: samora-ai-agentic-access
  summary_line: 17 operations · 10 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Trigger and retrieve individual outbound calls.
  name: Samora AI Calls API
  slug: samora-ai-calls-api
- description: Create and manage outbound calling campaigns and their scheduled recipients.
  name: Samora AI Campaigns API
  slug: samora-ai-campaigns-api
- description: Subscribe to real-time call events.
  name: Samora AI Webhooks API
  slug: samora-ai-webhooks-api
artifact_total: 8
asyncapis:
- description: Real-time call events delivered by Samora AI to a subscriber-provided HTTPS endpoint. Subscriptions are managed via the REST /v2/webhooks operations; each subscription returns a signing secret used to
  name: Samora AI Webhooks
  slug: samora-ai-webhooks-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.samora.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.samora.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.samora.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.samora.ai
- group: company
  title: ''
  type: Website
  url: https://samora.ai
- group: start
  title: ''
  type: SignUp
  url: https://app.samora.ai/login
- group: start
  title: ''
  type: Login
  url: https://app.samora.ai/login
- group: operate
  title: ''
  type: Support
  url: https://cal.com/team/samora/quick-chat
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/samora-ai-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samora-ai-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/samora-ai-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/samora-ai-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/samora-ai-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/samora-ai-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/samora-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/samora-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/samora-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/samora-ai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/samora-ai-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/samora-ai-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/samora-ai-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/samora-ai-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samora-ai-domain-security.yml
created: '2026-07-17'
description: Samora AI is a Y Combinator (W2026) company building multilingual voice agents that automate high-volume inbound and outbound calling for financial services, recruitment, healthcare, and government. Its agents handle natural conversation across 20+ languages with interruption handling, code-switching, and escalation to human operators, plus omnichannel support (voice, WhatsApp, SMS, email) and CRM integration. Samora exposes a server-to-server REST API to trigger outbound calls, manage outbound calling campaigns and their scheduled recipients, and subscribe to real-time call events through signed webhooks. Authentication is an organization API key sent in the X-API-Key header; the base URL is https://api.samora.ai and the developer documentation is at https://docs.samora.ai.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samora-ai.png
layout: provider
mcp_servers:
- description: ''
  name: samora-ai-mcp.yml
  slug: samora-ai-mcpyml
modified: '2026-07-21'
name: Samora AI
nav: Providers
network: true
overview: 'Samora AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Calls API, Campaigns API, and Webhooks API. Tagged areas include Company, Voice Agents, Conversational AI, Voice AI, and Telephony.


  The Samora AI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Samora AI''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 30.1
  delta: -1.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 24.6
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Samora Ai Authentication
  slug: samora-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Samora Ai Domain Security
  slug: samora-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: samora-ai
tags:
- Company
- Voice Agents
- Conversational AI
- Voice AI
- Telephony
- Customer Communications
- Contact Center
- Campaigns
- Webhooks
website: https://samora.ai
---
