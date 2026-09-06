---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 93
  human_in_the_loop: 2
  name: Asapp Agentic Access
  operation_count: 137
  slug: asapp-agentic-access
  summary_line: 137 operations · 93 acting · 2 human-in-the-loop
api_count: 13
apis:
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Improve agent productivity with AutoCompose API
  name: ASAPP AutoCompose API
  slug: asapp-autocompose-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Endpoints for summarizing conversations and retrieving structured data
  name: ASAPP AutoSummary API
  slug: asapp-autosummary-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Get streaming URL to transcribe audio
  name: ASAPP AutoTranscribe API
  slug: asapp-autotranscribe-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Operations for controlling AutoTranscribe Media Gateway transcription and streaming
  name: ASAPP AutoTranscribe Media Gateway API
  slug: asapp-autotranscribe-media-gateway-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Operations to manage ASAPP configurations
  name: ASAPP Configuration API
  slug: asapp-configuration-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Operations to send conversational inputs to ASAPP AI services
  name: ASAPP Conversations API
  slug: asapp-conversations-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: end the connection of a call with GenAgent
  name: ASAPP Disengage API
  slug: asapp-disengage-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: establish the connection of a call with GenAgent
  name: ASAPP Engage API
  slug: asapp-engage-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: API to get client exports
  name: ASAPP File Exporter API
  slug: asapp-file-exporter-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Operations to send messages and trigger GenerativeAgent to respond or query the current state
  name: ASAPP GenerativeAgent API
  slug: asapp-generativeagent-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: Operations to ensure that ASAPP APIs are up and running.
  name: ASAPP Health Check API
  slug: asapp-health-check-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: The Knowledge Base API from ASAPP — 3 operation(s) for knowledge base.
  name: ASAPP Knowledge Base API
  slug: asapp-knowledge-base-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: API to submit entity's attributes to ASAPP
  name: ASAPP Metadata API
  slug: asapp-metadata-api
- baseURL: https://api.asapp.com
  baseurl_source: declared
  description: The Twilio Media Stream API from ASAPP — 1 operation(s) for twilio media stream.
  name: ASAPP Twilio Media Stream API
  slug: asapp-twilio-media-stream-api
artifact_total: 35
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
  type: CapabilityMap
  url: capabilities/asapp-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: ASAPP
nav: Providers
network: true
overview: 'ASAPP publishes 14 APIs on the [APIs.io](https://apis.io/) network, including AutoCompose API, AutoSummary API, AutoTranscribe API, and 11 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Contact Center, and Customer Experience.


  The ASAPP catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ASAPP''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 25 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 64.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 54.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Artificial Intelligence
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
