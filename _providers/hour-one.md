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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 71.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Hour One Agentic Access
  operation_count: 26
  slug: hour-one-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The general API from Hour One — 3 operation(s) for general.
  name: Hour One general API
  slug: hour-one-general-api
- description: The keys API from Hour One — 2 operation(s) for keys.
  name: Hour One keys API
  slug: hour-one-keys-api
- description: The playground API from Hour One — 4 operation(s) for playground.
  name: Hour One playground API
  slug: hour-one-playground-api
- description: The videos API from Hour One — 4 operation(s) for videos.
  name: Hour One videos API
  slug: hour-one-videos-api
- description: The voice-preview API from Hour One — 2 operation(s) for voice-preview.
  name: Hour One voice-preview API
  slug: hour-one-voice-preview-api
- description: The webhook API from Hour One — 5 operation(s) for webhook.
  name: Hour One webhook API
  slug: hour-one-webhook-api
artifact_total: 10
asyncapis:
- description: Outbound webhook notifications for video processing lifecycle. Hour One POSTs a signed JSON payload to your registered endpoint when a video finishes rendering or fails. Each request carries an x-hour
  name: Hour One (MakeReals) Webhooks
  slug: hour-one-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.hourone.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hourone.gitbook.io/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://hourone.gitbook.io/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://hourone.gitbook.io/api-docs/reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://hourone.gitbook.io/api-docs/blueprint-quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hourone-ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hour-one-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hour-one-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/hour-one-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hour-one-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hour-one-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hour-one-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hour-one-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hour-one-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hour-one-openapi-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hour-one-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hour-one-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hour-one-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hour-one-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Hour One is a generative-AI video company (an Insight Partners portfolio company, acquired by Wix in 2025) whose Studio / MakeReals API turns text and templates into AI presenter ("virtual human") videos programmatically. The REST API lets developers create videos two ways — Blueprint (render from an existing Hour One project template) and Dynamic (define scenes, transcripts, characters and voices directly) — then poll or receive HMAC-signed webhooks (video.ready / video.failed) on completion, generate voice previews, add translated subtitles in 18 languages, pull per-scene metadata, and query a video-creation analytics summary. Authentication is an api-key header for the video surface and an HTTP Bearer token for account/key/webhook management.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hour-one.png
layout: provider
mcp_servers:
- description: ''
  name: hour-one-mcp.yml
  slug: hour-one-mcpyml
modified: '2026-07-19'
name: Hour One
nav: Providers
network: true
overview: 'Hour One publishes 6 APIs on the [APIs.io](https://apis.io/) network, including general API, keys API, playground API, and 3 more. Tagged areas include Company, Video, Generative AI, AI Video, and Media.


  The Hour One catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hour One''s developer surface includes documentation, API reference, getting-started guide, authentication, and 16 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 66.4
    developer_ergonomics: 60.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 40.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Hour One Authentication
  slug: hour-one-authentication
  summary_line: apiKey/http · 2 schemes
slug: hour-one
tags:
- Company
- Video
- Generative AI
- AI Video
- Media
- Text to Video
- Avatars
- Content Creation
website: https://www.hourone.ai/
---
