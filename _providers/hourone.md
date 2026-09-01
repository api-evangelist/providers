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
  band: agent-aware
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Hourone Agentic Access
  operation_count: 26
  slug: hourone-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The general API from Hourone — 3 operation(s) for general.
  name: Hourone general API
  slug: hourone-general-api
- description: The keys API from Hourone — 2 operation(s) for keys.
  name: Hourone keys API
  slug: hourone-keys-api
- description: The playground API from Hourone — 4 operation(s) for playground.
  name: Hourone playground API
  slug: hourone-playground-api
- description: The videos API from Hourone — 4 operation(s) for videos.
  name: Hourone videos API
  slug: hourone-videos-api
- description: The voice-preview API from Hourone — 2 operation(s) for voice-preview.
  name: Hourone voice-preview API
  slug: hourone-voice-preview-api
- description: The webhook API from Hourone — 5 operation(s) for webhook.
  name: Hourone webhook API
  slug: hourone-webhook-api
artifact_total: 17
asyncapis:
- description: Outbound webhook notifications for video processing lifecycle. Hour One POSTs a signed JSON payload to your registered endpoint when a video finishes rendering or fails. Each request carries an x-hour
  name: Hour One (MakeReals) Webhooks
  slug: hourone-webhooks-asyncapi
- description: ''
  name: Hourone Webhooks
  slug: hourone-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: sizzle-server general API
  slug: open-hourone-general-api
- collection_type: open
  name: sizzle-server general keys API
  slug: open-hourone-keys-api
- collection_type: open
  name: sizzle-server general playground API
  slug: open-hourone-playground-api
- collection_type: open
  name: sizzle-server general videos API
  slug: open-hourone-videos-api
- collection_type: open
  name: sizzle-server general webhook API
  slug: open-hourone-webhook-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hourone-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://hourone.ai/
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
- group: operate
  title: ''
  type: Support
  url: https://help.hourone.ai/hc/en-us/categories/8918170914449-Hour-One
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hourone-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.hourone.ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hourone-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/hourone-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hourone-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hourone-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hourone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hourone-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hourone-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hourone-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hourone-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hourone-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hourone-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hourone-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hourone-webhooks-asyncapi.yml
created: '2026-07-17'
description: Hour One (developer surface "MakeReals") is an AI video-generation platform that turns text, scripts and data into studio-quality videos fronted by lifelike AI presenters (characters) and text-to-speech voices. Its REST API lets developers create videos programmatically two ways — from a Blueprint (an existing HourOne studio project/template) or Dynamically (scenes built from scratch with media, text, palette, character and voice) — preview voices, generate multi-language subtitles, pull usage analytics, manage API keys, and subscribe to video.ready / video.failed webhooks. The API is asynchronous (create, then poll by id or receive a signed webhook) and authenticates with a single api-key header. Common uses include personalized video at scale, L&D and training content, CRM/LMS automation, and localized marketing video. Hour One is a portfolio company of Kindred Ventures.
image: https://hourone.ai/
layout: provider
mcp_servers:
- description: ''
  name: Hourone MCP Server
  slug: hourone-mcp-server
modified: '2026-08-08'
name: Hourone
nav: Providers
network: true
overview: 'Hourone publishes 6 APIs on the [APIs.io](https://apis.io/) network, including general API, keys API, playground API, and 3 more. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Generative AI.


  The Hourone catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Hourone''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 61.9
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hourone/refs/heads/main/screenshots/hourone-2026-07-25T221530.png
security:
- kind: authentication
  name: Hourone Authentication
  slug: hourone-authentication
  summary_line: apiKey/http · 2 schemes
slug: hourone
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Generative AI
- AI Avatars
- Text-to-Speech
- Media
- Content Creation
- Webhook
website: https://hourone.ai/
---
