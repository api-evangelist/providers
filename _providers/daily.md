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
  score: 28.6
  scored_at: '2026-08-26'
api_count: 13
apis:
- description: The batch/rooms API from Daily — 1 operation(s) for batch/rooms.
  name: Daily batch/rooms API
  slug: daily-batch-rooms-api
- description: The dialin API from Daily — 1 operation(s) for dialin.
  name: Daily dialin API
  slug: daily-dialin-api
- description: The domain API from Daily — 1 operation(s) for domain.
  name: Daily domain API
  slug: daily-domain-api
- description: The domain-dialin-config API from Daily — 2 operation(s) for domain-dialin-config.
  name: Daily domain-dialin-config API
  slug: daily-domain-dialin-config-api
- description: The logs API from Daily — 2 operation(s) for logs.
  name: Daily logs API
  slug: daily-logs-api
- description: The meeting-tokens API from Daily — 2 operation(s) for meeting-tokens.
  name: Daily meeting-tokens API
  slug: daily-meeting-tokens-api
- description: The meetings API from Daily — 3 operation(s) for meetings.
  name: Daily meetings API
  slug: daily-meetings-api
- description: The phone-numbers API from Daily — 4 operation(s) for phone-numbers.
  name: Daily phone-numbers API
  slug: daily-phone-numbers-api
- description: The presence API from Daily — 1 operation(s) for presence.
  name: Daily presence API
  slug: daily-presence-api
- description: The recordings API from Daily — 3 operation(s) for recordings.
  name: Daily recordings API
  slug: daily-recordings-api
- description: The rooms API from Daily — 22 operation(s) for rooms.
  name: Daily rooms API
  slug: daily-rooms-api
- description: The transcript API from Daily — 3 operation(s) for transcript.
  name: Daily transcript API
  slug: daily-transcript-api
- description: The webhooks API from Daily — 2 operation(s) for webhooks.
  name: Daily webhooks API
  slug: daily-webhooks-api
artifact_total: 31
asyncapis:
- description: ''
  name: Daily Webhooks
  slug: daily-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Daily batch/rooms API
  slug: open-daily-batch-rooms-api
- collection_type: open
  name: Daily batch/rooms dialin API
  slug: open-daily-dialin-api
- collection_type: open
  name: Daily batch/rooms domain API
  slug: open-daily-domain-api
- collection_type: open
  name: Daily batch/rooms domain-dialin-config API
  slug: open-daily-domain-dialin-config-api
- collection_type: open
  name: Daily batch/rooms logs API
  slug: open-daily-logs-api
- collection_type: open
  name: Daily batch/rooms meeting-tokens API
  slug: open-daily-meeting-tokens-api
- collection_type: open
  name: Daily batch/rooms meetings API
  slug: open-daily-meetings-api
- collection_type: open
  name: Daily batch/rooms phone-numbers API
  slug: open-daily-phone-numbers-api
- collection_type: open
  name: Daily batch/rooms presence API
  slug: open-daily-presence-api
- collection_type: open
  name: Daily batch/rooms recordings API
  slug: open-daily-recordings-api
- collection_type: open
  name: Daily batch/ rooms API
  slug: open-daily-rooms-api
- collection_type: open
  name: Daily batch/rooms transcript API
  slug: open-daily-transcript-api
- collection_type: open
  name: Daily batch/rooms webhooks API
  slug: open-daily-webhooks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daily-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/daily-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.daily.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daily.co/docs/rest-api/index
- group: docs
  title: ''
  type: APIReference
  url: https://docs.daily.co/reference/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.daily.co/docs/daily-js/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.daily.co/contact/support
- group: company
  title: ''
  type: Blog
  url: https://www.daily.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daily-co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.daily.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.daily.co/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daily.co/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daily.co/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/daily-co
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daily.co/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.daily.co/docs/guides/privacy-and-security/hipaa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/daily-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/daily-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/daily-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/daily-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/daily-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/daily-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/daily-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/daily-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/daily-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/daily-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/daily-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/daily-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/daily-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/daily-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Daily is a Y Combinator-backed developer platform providing real-time audio and video APIs and client SDKs for embedding WebRTC video calls, live streaming, cloud recording, transcription, and SIP/PSTN telephony into web, mobile, and server applications. Its REST API manages rooms, meeting tokens, recordings, transcripts, webhooks, phone numbers, and domain configuration, complemented by the daily-js, daily-react, and native iOS/Android/Python/Flutter SDKs plus the embeddable Daily Prebuilt UI. Authentication uses a domain-scoped API key sent as an HTTP Bearer token.
image: https://www.daily.co/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Daily MCP Server
  slug: daily-mcp-server
modified: '2026-07-18'
name: Daily
nav: Providers
network: true
overview: 'Daily publishes 13 APIs on the [APIs.io](https://apis.io/) network, including batch/rooms API, dialin API, domain API, and 10 more. Tagged areas include Video, Audio, WebRTC, Real-Time Communication, and Video Conferencing.


  The Daily catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Daily''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 6
score:
  band: strong
  composite: 56.7
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 69.2
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 56.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daily/refs/heads/main/screenshots/daily-2026-07-25T211132.png
security:
- kind: authentication
  name: Daily Authentication
  slug: daily-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Daily Domain Security
  slug: daily-domain-security
  summary_line: TLSv1.2 · DMARC
slug: daily
tags:
- Video
- Audio
- WebRTC
- Real-Time Communication
- Video Conferencing
- Live Streaming
- Recording
- Transcription
- Telephony
- SIP
- PSTN
- Company
website: https://docs.daily.co/
---
