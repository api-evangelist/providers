---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 37
  human_in_the_loop: 5
  name: Livepeer Agentic Access
  operation_count: 64
  slug: livepeer-agentic-access
  summary_line: 64 operations · 37 acting · 5 human-in-the-loop
api_count: 28
apis:
- description: Primary REST API for the Livepeer Studio gateway. Resource-oriented JSON endpoints for live streams, on-demand assets, multistream targets, transcoding jobs, sessions, playback, signing keys, webhooks
  name: Livepeer Studio REST API
  slug: studio
- description: Endpoints for creating and managing live streams, ingest RTMP/WHIP URLs, profiles for adaptive bitrate transcoding, recording, and stream keys.
  name: Livepeer Streams API
  slug: streams
- description: Endpoints for uploading, importing, transcoding, and serving on-demand video assets, including direct upload, URL import, and IPFS storage.
  name: Livepeer Assets API
  slug: assets
- description: Endpoints for registering and managing multistream destinations that forward an active live stream to additional RTMP/RTMPS endpoints such as YouTube, Twitch, or X.
  name: Livepeer Multistream Targets API
  slug: multistream
- description: Webhook management endpoints plus outbound event notifications for stream lifecycle events (stream.started, stream.idle, recording.ready, asset.ready, playback.access_control). Signed payloads deliver
  name: Livepeer Webhooks API
  slug: webhooks
- description: Endpoints for one-off transcoding jobs against source files in object storage, returning a job handle and transcoded renditions.
  name: Livepeer Transcode API
  slug: transcode
- description: Endpoints for retrieving completed live session recordings and metadata for past live streams.
  name: Livepeer Sessions API
  slug: sessions
- description: Playback info endpoint returning HLS/WebRTC playback URLs and metadata for a stream or asset, plus access-control gating.
  name: Livepeer Playback API
  slug: playback
- description: Endpoints for managing JWT signing keys used for playback access control and webhook signature verification.
  name: Livepeer Signing Keys API
  slug: signing-keys
- description: AI video and image generation endpoints (text-to-image, image-to-image, image-to-video, upscale, audio-to-text) routed through the Livepeer AI subnet of GPU orchestrators.
  name: Livepeer AI Generate API
  slug: ai-generate
- description: Official TypeScript/JavaScript SDK (@livepeer/ai or livepeer) for the Livepeer Studio REST API and AI endpoints.
  name: Livepeer JavaScript/TypeScript SDK
  slug: js-sdk
- description: Official Python SDK for the Livepeer Studio REST API.
  name: Livepeer Python SDK
  slug: python-sdk
- description: Official Go SDK for the Livepeer Studio REST API.
  name: Livepeer Go SDK
  slug: go-sdk
- description: Official Ruby SDK for the Livepeer Studio REST API.
  name: Livepeer Ruby SDK
  slug: ruby-sdk
- description: React video player component for HLS/WebRTC playback of Livepeer streams and assets, with customisable controls and access-control integration.
  name: Livepeer React Player Component
  slug: react-player
- description: React component for in-browser WebRTC broadcasting to a Livepeer live stream, with device selection and settings controls.
  name: Livepeer React Broadcast Component
  slug: react-broadcast
- description: Operations related to access control/signing keys api
  name: Livepeer accessControl API
  slug: livepeer-accesscontrol-api
- description: Operations related to asset/vod api
  name: Livepeer asset API
  slug: livepeer-asset-api
- description: Operations related to AI generate api
  name: Livepeer generate API
  slug: livepeer-generate-api
- description: Operations related to metrics api
  name: Livepeer metrics API
  slug: livepeer-metrics-api
- description: Operations related to multistream api
  name: Livepeer multistream API
  slug: livepeer-multistream-api
- description: Operations related to playback api
  name: Livepeer playback API
  slug: livepeer-playback-api
- description: Operations related to rooms api
  name: Livepeer room API
  slug: livepeer-room-api
- description: Operations related to session api
  name: Livepeer session API
  slug: livepeer-session-api
- description: Operations related to livestream api
  name: Livepeer stream API
  slug: livepeer-stream-api
- description: Operations related to tasks api
  name: Livepeer task API
  slug: livepeer-task-api
- description: Operations related to transcode api
  name: Livepeer transcode API
  slug: livepeer-transcode-api
- description: Operations related to webhook api
  name: Livepeer webhook API
  slug: livepeer-webhook-api
arazzos:
- description: Create a clip from a live playback ID, poll the clip task, fetch the asset.
  name: Livepeer Clip a Livestream
  slug: livepeer-clip-livestream-workflow
- description: Create a stream, enable recording via update, and confirm the change.
  name: Livepeer Enable Recording on a Stream
  slug: livepeer-enable-stream-recording-workflow
- description: Upload an asset from an external URL, then poll the processing task.
  name: Livepeer Import an Asset from a URL
  slug: livepeer-import-asset-from-url-workflow
- description: Read a stream session and resolve its recording playback info.
  name: Livepeer Inspect a Session Recording
  slug: livepeer-inspect-session-recording-workflow
- description: Create a live stream, confirm it exists, and resolve its playback info.
  name: Livepeer Provision a Live Stream
  slug: livepeer-provision-live-stream-workflow
- description: Create a stream and attach an inline multistream target to restream it.
  name: Livepeer Provision Multistream Restreaming
  slug: livepeer-provision-multistream-restream-workflow
- description: Create a stream then register a webhook scoped to its lifecycle events.
  name: Livepeer Register a Stream Webhook
  slug: livepeer-register-stream-webhook-workflow
- description: Create a signing key, create a JWT-gated stream, and resolve playback.
  name: Livepeer Secure a Stream with a Signing Key
  slug: livepeer-secure-stream-signing-key-workflow
- description: Create a reusable multistream target, then bind it to a new stream by ID.
  name: Livepeer Reuse a Standalone Multistream Target
  slug: livepeer-standalone-multistream-target-workflow
- description: Submit a transcode job to S3/web3.storage and poll the task until done.
  name: Livepeer Run a Transcode Job
  slug: livepeer-transcode-video-job-workflow
- description: Request a direct upload URL, then poll the asset and task until ready.
  name: Livepeer Upload and Process an Asset
  slug: livepeer-upload-and-process-asset-workflow
artifact_total: 106
collections:
- collection_type: postman
  name: Livepeer AI Runner
  slug: postman-livepeer-ai-worker
- collection_type: postman
  name: Livepeer CLI Local HTTP API
  slug: postman-livepeer-cli-http
- collection_type: postman
  name: Livepeer AI Runner
  slug: postman-livepeer-gateway
- collection_type: postman
  name: Livepeer API Reference
  slug: postman-livepeer-studio
- collection_type: open
  name: Livepeer AI Runner
  slug: open-livepeer-ai-worker
- collection_type: open
  name: Livepeer CLI Local HTTP API
  slug: open-livepeer-cli-http
- collection_type: open
  name: Livepeer AI Runner
  slug: open-livepeer-gateway
- collection_type: open
  name: Livepeer API Reference
  slug: open-livepeer-studio
- collection_type: open
  name: Livepeer API Reference
  slug: open-livepeer
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/livepeer/livepeer-js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/livepeer/livepeer-js/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/livepeer/livepeer-js/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/livepeer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livepeer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livepeer-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/livepeer
- group: company
  title: ''
  type: Website
  url: https://livepeer.org/
- group: other
  title: ''
  type: Studio
  url: https://livepeer.studio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.livepeer.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/livepeer
- group: operate
  title: ''
  type: Status
  url: https://status.livepeer.studio/
- group: commercial
  title: ''
  type: Plans
  url: plans/livepeer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/livepeer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/livepeer-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.livepeer.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://livepeer.org/blog
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/livepeer/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-clip-livestream-workflow.yml
- group: start
  title: ''
  type: StudioPortal
  url: https://livepeer.studio
- group: docs
  title: ''
  type: APIReference
  url: https://docs.livepeer.org/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://livepeer.studio/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.livepeer.org/changelog
- group: other
  title: ''
  type: Explorer
  url: https://explorer.livepeer.org
- group: operate
  title: ''
  type: Forums
  url: https://forum.livepeer.org
- group: operate
  title: ''
  type: RoadMap
  url: https://roadmap.livepeer.org/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.livepeer.studio
- group: start
  title: ''
  type: Signup
  url: https://livepeer.studio/register
- group: start
  title: ''
  type: Login
  url: https://livepeer.studio/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livepeer.org/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livepeer.org/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/livepeer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/livepeer/go-livepeer
- group: build
  title: ''
  type: SDKs
  url: https://docs.livepeer.org/sdks
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/livepeer/livepeer-js
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/livepeer/livepeer-python
- group: build
  title: ''
  type: GoSDK
  url: https://github.com/livepeer/livepeer-go
- group: other
  title: ''
  type: UIKit
  url: https://github.com/livepeer/ui-kit
- group: docs
  title: ''
  type: ReferenceImplementation
  url: https://github.com/livepeer/go-livepeer
- group: other
  title: ''
  type: AIWorker
  url: https://github.com/livepeer/ai-worker
- group: build
  title: ''
  type: Plugin
  url: https://github.com/livepeer/naap
- group: other
  title: ''
  type: SmartContracts
  url: https://github.com/livepeer/protocol
- group: other
  title: ''
  type: NetworkExplorer
  url: https://explorer.livepeer.org
- group: auth
  title: ''
  type: TokenContractEthereum
  url: https://etherscan.io/token/0x58b6a8a3302369daec383334672404ee733ab239
- group: auth
  title: ''
  type: TokenContractArbitrum
  url: https://arbiscan.io/token/0x289ba1701c2f088cf0faf8b3705246331cb8a839
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/livepeer
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Livepeer
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LivepeerNetwork
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/livepeer-studio-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/livepeer-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/livepeer-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/livepeer-platform-structure.json
created: '2026-05-23'
description: Livepeer is a decentralized video infrastructure network. Independent orchestrators run GPU hardware to provide live and on-demand video transcoding services, paid for in ETH/LPT on the Livepeer protocol. Livepeer Studio is the managed gateway and developer platform sitting on top of the network, exposing a REST API at livepeer.studio/api for live streams, on- demand assets, multistream targets, transcoding jobs, sessions, playback, signing keys, AI generation (text-to-image, image-to-image, image-to-video, upscale, audio-to-text), and webhooks. Official SDKs are published for JavaScript/TypeScript, Python, Go, and Ruby, with React Player and React Broadcast components for client-side playback and ingest.
examples:
- key_count: 2
  name: Livepeer Ai Text To Image Example
  slug: livepeer-ai-text-to-image-example
- key_count: 2
  name: Livepeer Create Stream Example
  slug: livepeer-create-stream-example
- key_count: 2
  name: Livepeer Create Webhook Example
  slug: livepeer-create-webhook-example
- key_count: 2
  name: Livepeer Image To Video Example
  slug: livepeer-image-to-video-example
features:
- Decentralized GPU network for transcoding + AI inference
- LPT token live on Ethereum mainnet and Arbitrum One
- Probabilistic micropayment (PM) tickets for sub-cent settlement
- Livepeer Studio managed REST API with Bearer auth
- Live streaming via RTMP, SRT, and WHIP ingest
- Adaptive bitrate HLS + WebRTC playback
- Recording, clipping, and on-demand asset hosting
- Multistream simulcast to YouTube, Twitch, Facebook, etc.
- WebRTC rooms with optional RTMP egress
- Token-gated playback via signing keys, JWT, and webhook policies
- Webhooks for stream/asset/recording/task lifecycle
- AI pipelines (text-to-image, image-to-video, live video-to-video, LLM, etc.)
- Two AI gateways (community + Studio beta) interchangeable per request
- Official TypeScript, Python (Studio + AI + Gateway), and Go SDKs
- React UI Kit (Player, Broadcast) for client embedding
- go-livepeer reference node for operators
- NAAP plugin platform for the AI Compute Network
- Open governance via Livepeer Improvement Proposals (LIPs)
finops:
- name: Livepeer Finops
  service_category: API
  slug: livepeer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livepeer.png
integrations:
- YouTube, Twitch, Facebook Live (multistream targets)
- IPFS / Filecoin (asset storage)
- Ethereum Mainnet (LPT, governance)
- Arbitrum One (PM tickets, AI fee settlement)
- The Graph (subgraph for Livepeer protocol)
- OBS, Streamlabs, Larix, Restream (ingest tooling)
- OpenAI-compatible LLM clients (via /llm endpoint)
- Daydream, Embody, Frameworks, Stream.place, Storyboard (ecosystem apps)
json_schemas:
- name: Livepeer AI — Image-to-Video
  property_count: 10
  slug: livepeer-ai-image-to-video
- name: Livepeer AI — Text-to-Image
  property_count: 11
  slug: livepeer-ai-text-to-image
- name: Livepeer Asset
  property_count: 18
  slug: livepeer-asset
- name: Livepeer Stream
  property_count: 32
  slug: livepeer-stream
- name: Livepeer Task
  property_count: 12
  slug: livepeer-task
- name: Livepeer Webhook
  property_count: 10
  slug: livepeer-webhook
json_structures:
- name: Livepeer Platform Structure
  property_count: 0
  slug: livepeer-platform-structure
- name: Livepeer Stream Structure
  property_count: 0
  slug: livepeer-stream-structure
jsonld:
- class_count: 72
  name: Livepeer Context
  property_count: 0
  slug: livepeer-context
layout: provider
modified: '2026-08-08'
name: Livepeer
nav: Providers
network: true
overview: 'Livepeer publishes 12 APIs on the [APIs.io](https://apis.io/) network, including accessControl API, asset API, generate API, and 9 more. Tagged areas include Video, Streaming, Transcoding, Decentralized, and Web3.


  The Livepeer catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Livepeer''s developer surface includes authentication, documentation, GitHub presence, status page, engineering blog, API reference, pricing, and 45 more developer resources.'
plans:
- name: Livepeer Plans Pricing
  plan_count: 1
  slug: livepeer-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 2
  name: Livepeer Rate Limits
  slug: livepeer-rate-limits
rules:
- name: Livepeer API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: livepeer-ai-rules
- name: Livepeer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: livepeer-jsonschema-spectral-rules
- name: Livepeer API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 6
  slug: livepeer-studio-rules
score:
  band: strong
  composite: 59.9
  delta: 1.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 62.2
    developer_ergonomics: 43.5
    discoverability: 81.5
    governance: 37.5
    operational_transparency: 63.2
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livepeer/refs/heads/main/screenshots/livepeer-2026-06-20T184614.png
security:
- kind: authentication
  name: Livepeer Authentication
  slug: livepeer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Livepeer Domain Security
  slug: livepeer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livepeer
tags:
- Video
- Streaming
- Transcoding
- Decentralized
- Web3
- Live Video
- AI Video
use_cases:
- User-generated live streaming platforms (creator economy)
- On-demand video platforms with low transcoding cost
- Web3 / NFT video drops with on-chain provenance
- Multistream restreaming to incumbent social platforms
- Real-time video AI transformation (Daydream / live video-to-video)
- AI avatars and embodied agents (Embody)
- Open streaming infrastructure (Stream.place, Frameworks)
- Generative video for marketing, advertising, and entertainment
- Realtime sports / security / manufacturing video intelligence
- LLM inference on decentralized GPU capacity
website: https://livepeer.org/
---
