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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 11
  human_in_the_loop: 5
  name: Mirage Agentic Access
  operation_count: 23
  slug: mirage-agentic-access
  summary_line: 23 operations · 11 acting · 5 human-in-the-loop
api_count: 7
apis:
- description: The Audio API from Mirage — 1 operation(s) for audio.
  name: Mirage Audio API
  slug: mirage-audio-api
- description: The health API from Mirage — 1 operation(s) for health.
  name: Mirage health API
  slug: mirage-health-api
- description: The internal API from Mirage — 8 operation(s) for internal.
  name: Mirage internal API
  slug: mirage-internal-api
- description: The Meta Text Overlays API from Mirage — 2 operation(s) for meta text overlays.
  name: Mirage Meta Text Overlays API
  slug: mirage-meta-text-overlays-api
- description: The root API from Mirage — 1 operation(s) for root.
  name: Mirage root API
  slug: mirage-root-api
- description: The Video Captions API from Mirage — 3 operation(s) for video captions.
  name: Mirage Video Captions API
  slug: mirage-video-captions-api
- description: The Videos API from Mirage — 3 operation(s) for videos.
  name: Mirage Videos API
  slug: mirage-videos-api
artifact_total: 20
asyncapis:
- description: ''
  name: Mirage Webhooks
  slug: mirage-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mirage Video Audio API
  slug: open-mirage-audio-api
- collection_type: open
  name: Mirage Video Audio health API
  slug: open-mirage-health-api
- collection_type: open
  name: Mirage Video Audio internal API
  slug: open-mirage-internal-api
- collection_type: open
  name: Mirage Video Audio Meta Text Overlays API
  slug: open-mirage-meta-text-overlays-api
- collection_type: open
  name: Mirage Video Audio root API
  slug: open-mirage-root-api
- collection_type: open
  name: Mirage Video Audio Video Captions API
  slug: open-mirage-video-captions-api
- collection_type: open
  name: Mirage Video Audio Videos API
  slug: open-mirage-videos-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mirage-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mirage-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mirage-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://captions.ai/help/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://captions.ai/help/docs/api/overview
- group: docs
  title: ''
  type: APIReference
  url: https://captions.ai/help/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://captions.ai/help/docs/api/overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/mirage-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://captions.ai/help/docs/api/pricing
- group: start
  title: ''
  type: SignUp
  url: https://captions.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mirage.app/legal/captions-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mirage.app/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://captions.ai/help
- group: company
  title: ''
  type: Blog
  url: https://captions.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://captions.ai/help/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mirage-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://captions.ai/solutions/enterprise
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mirage-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mirage-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mirage-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mirage-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mirage-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mirage-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mirage-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mirage-webhooks.yml
created: '2026-07-17'
description: 'Mirage is an AI research company headquartered in New York City that builds Captions, an AI video editor and generator used by more than 20 million creators, small businesses, and enterprises worldwide. The Mirage Video API exposes the company''s state-of-the-art video models over a simple HTTP interface: generate expressive human video from an image and audio (Mirage Video 1), apply styled captions to an existing video, synthesize speech with text-to-speech voices, and render meta text overlays. It is an asynchronous submit-and-poll REST API authenticated with an x-api-key header and priced by usage (per minute of captioning, per second of generated video).'
image: https://captions.ai/mrkt-static/captions-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Mirage MCP Server
  slug: mirage-mcp-server
modified: '2026-07-20'
name: Mirage
nav: Providers
network: true
overview: 'Mirage publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Audio API, health API, internal API, and 4 more. Tagged areas include Company, Artificial Intelligence, Video, Video Generation, and Captions.


  The Mirage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mirage''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 19 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 49.8
  delta: 1.4
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 57.0
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mirage/refs/heads/main/screenshots/mirage-2026-08-07T183717.png
security:
- kind: authentication
  name: Mirage Authentication
  slug: mirage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mirage Domain Security
  slug: mirage-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: mirage
tags:
- Company
- Artificial Intelligence
- Video
- Video Generation
- Captions
- Media
- Content Creation
- Text-to-Speech
- Machine-Learning
website: https://captions.ai/help/api-reference
---
