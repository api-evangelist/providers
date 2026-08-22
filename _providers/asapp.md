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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 93
  human_in_the_loop: 2
  name: Asapp Agentic Access
  operation_count: 137
  slug: asapp-agentic-access
  summary_line: 137 operations · 93 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: Improve agent productivity with AutoCompose API
  name: ASAPP AutoCompose API
  slug: asapp-autocompose-api
- description: Endpoints for summarizing conversations and retrieving structured data
  name: ASAPP AutoSummary API
  slug: asapp-autosummary-api
- description: Get streaming URL to transcribe audio
  name: ASAPP AutoTranscribe API
  slug: asapp-autotranscribe-api
- description: Operations for controlling AutoTranscribe Media Gateway transcription and streaming
  name: ASAPP AutoTranscribe Media Gateway API
  slug: asapp-autotranscribe-media-gateway-api
- description: Operations to manage ASAPP configurations
  name: ASAPP Configuration API
  slug: asapp-configuration-api
- description: Operations to send conversational inputs to ASAPP AI services
  name: ASAPP Conversations API
  slug: asapp-conversations-api
- description: end the connection of a call with GenAgent
  name: ASAPP Disengage API
  slug: asapp-disengage-api
- description: establish the connection of a call with GenAgent
  name: ASAPP Engage API
  slug: asapp-engage-api
- description: API to get client exports
  name: ASAPP File Exporter API
  slug: asapp-file-exporter-api
- description: Operations to send messages and trigger GenerativeAgent to respond or query the current state
  name: ASAPP GenerativeAgent API
  slug: asapp-generativeagent-api
- description: Operations to ensure that ASAPP APIs are up and running.
  name: ASAPP Health Check API
  slug: asapp-health-check-api
- description: The Knowledge Base API from ASAPP — 3 operation(s) for knowledge base.
  name: ASAPP Knowledge Base API
  slug: asapp-knowledge-base-api
- description: API to submit entity's attributes to ASAPP
  name: ASAPP Metadata API
  slug: asapp-metadata-api
- description: The Twilio Media Stream API from ASAPP — 1 operation(s) for twilio media stream.
  name: ASAPP Twilio Media Stream API
  slug: asapp-twilio-media-stream-api
artifact_total: 36
asyncapis:
- description: ''
  name: Asapp Realtime Events Webhooks
  slug: asapp-realtime-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AutoCompose API
  slug: open-asapp-autocompose-api
- collection_type: open
  name: AutoCompose AutoSummary API
  slug: open-asapp-autosummary-api
- collection_type: open
  name: AutoCompose AutoTranscribe API
  slug: open-asapp-autotranscribe-api
- collection_type: open
  name: AutoCompose AutoTranscribe Media Gateway API
  slug: open-asapp-autotranscribe-media-gateway-api
- collection_type: open
  name: AutoCompose Configuration API
  slug: open-asapp-configuration-api
- collection_type: open
  name: AutoCompose Conversations API
  slug: open-asapp-conversations-api
- collection_type: open
  name: AutoCompose Disengage API
  slug: open-asapp-disengage-api
- collection_type: open
  name: AutoCompose Engage API
  slug: open-asapp-engage-api
- collection_type: open
  name: AutoCompose File Exporter API
  slug: open-asapp-file-exporter-api
- collection_type: open
  name: AutoCompose GenerativeAgent API
  slug: open-asapp-generativeagent-api
- collection_type: open
  name: AutoCompose Health Check API
  slug: open-asapp-health-check-api
- collection_type: open
  name: AutoCompose Knowledge Base API
  slug: open-asapp-knowledge-base-api
- collection_type: open
  name: AutoCompose Metadata API
  slug: open-asapp-metadata-api
- collection_type: open
  name: AutoCompose Twilio Media Stream API
  slug: open-asapp-twilio-media-stream-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/asapp-autosummary-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.asapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asapp.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asapp.com/apis/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asapp.com/getting-started/developers
- group: auth
  title: ''
  type: Authentication
  url: authentication/asapp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/asapp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/asapp-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/asapp-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/asapp-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asapp.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/asapp-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/asapp-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/asapp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/asapp-packages.yml
- group: design
  title: ''
  type: Components
  url: components/asapp-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/asapp-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/asapp-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/asapp-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.asapp.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/asapp-realtime-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/asapp-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/asapp-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/asapp-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asapp-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.asapp.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asapp.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://www.asapp.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://docs.asapp.com/support
- group: company
  title: ''
  type: Website
  url: https://www.asapp.com
created: '2026-07-17'
description: ASAPP is an AI-native customer experience (CX) company whose platform, ASAPP CXP, automates and augments contact-center interactions across voice and chat. Its flagship GenerativeAgent resolves customer issues autonomously while keeping a human in the loop (HILA), backed by AI productivity tools (AutoCompose agent suggestions, AI Summary, AI Transcribe), a Knowledge Base, Digital Agent Desk, and Insights. ASAPP exposes a REST API platform (api.asapp.com) covering Conversations, Messages, GenerativeAgent, AutoSummary, AutoCompose, AutoTranscribe, Knowledge Base, Metadata Ingestion, File Exporter, Partner Configuration, and a webhook-based Real-Time Event API, secured with API Id + API Secret credentials. Backed by Emergence Capital. Enriched from the provider's public developer docs.
image: https://www.asapp.com/favicon.ico
json_schemas:
- name: Asapp Messaging Feeds
  property_count: 0
  slug: asapp-messaging-feeds
layout: provider
mcp_servers:
- description: ''
  name: asapp-mcp.yml
  slug: asapp-mcpyml
modified: '2026-07-18'
name: ASAPP
nav: Providers
network: true
overview: 'ASAPP publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AutoCompose API, AutoSummary API, AutoTranscribe API, and 11 more. Tagged areas include Company, AI, Conversational AI, Contact Center, and Customer Experience.


  The ASAPP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ASAPP''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 24 more developer resources.'
random_paper: 8
score:
  band: strong
  composite: 56.0
  delta: 1.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 66.1
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 39.5
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asapp/refs/heads/main/screenshots/asapp-2026-07-25T201402.png
security:
- kind: authentication
  name: Asapp Authentication
  slug: asapp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Asapp Domain Security
  slug: asapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Asapp Trust Center
  slug: asapp-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: asapp
tags:
- Company
- AI
- Conversational AI
- Contact Center
- Customer Experience
- Customer Service
- Generative AI
- Agent Assist
- Speech Recognition
- Knowledge Base
website: https://www.asapp.com
---
