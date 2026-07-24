---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 66
  human_in_the_loop: 5
  name: Livepeer Com Agentic Access
  operation_count: 99
  slug: livepeer-com-agentic-access
  summary_line: 99 operations · 66 acting · 5 human-in-the-loop
api_count: 19
apis:
- description: Operations related to access control/signing keys api
  name: Livepeer accessControl API
  slug: livepeer-com-accesscontrol-api
- description: Operations related to asset/vod api
  name: Livepeer asset API
  slug: livepeer-com-asset-api
- description: Ethereum operations and token transfers
  name: Livepeer Ethereum API
  slug: livepeer-com-ethereum-api
- description: Gateway/broadcaster configuration
  name: Livepeer Gateway API
  slug: livepeer-com-gateway-api
- description: The generate API from Livepeer — 17 operation(s) for generate.
  name: Livepeer generate API
  slug: livepeer-com-generate-api
- description: The Hardware API from Livepeer — 2 operation(s) for hardware.
  name: Livepeer Hardware API
  slug: livepeer-com-hardware-api
- description: The Health API from Livepeer — 1 operation(s) for health.
  name: Livepeer Health API
  slug: livepeer-com-health-api
- description: Operations related to metrics api
  name: Livepeer metrics API
  slug: livepeer-com-metrics-api
- description: Operations related to multistream api
  name: Livepeer multistream API
  slug: livepeer-com-multistream-api
- description: Orchestrator configuration and management
  name: Livepeer Orchestrator API
  slug: livepeer-com-orchestrator-api
- description: Operations related to playback api
  name: Livepeer playback API
  slug: livepeer-com-playback-api
- description: Operations related to rooms api
  name: Livepeer room API
  slug: livepeer-com-room-api
- description: Operations related to session api
  name: Livepeer session API
  slug: livepeer-com-session-api
- description: Token bonding and delegation operations
  name: Livepeer Staking API
  slug: livepeer-com-staking-api
- description: Node status and information
  name: Livepeer Status API
  slug: livepeer-com-status-api
- description: Operations related to livestream api
  name: Livepeer stream API
  slug: livepeer-com-stream-api
- description: Operations related to tasks api
  name: Livepeer task API
  slug: livepeer-com-task-api
- description: Operations related to transcode api
  name: Livepeer transcode API
  slug: livepeer-com-transcode-api
- description: Operations related to webhook api
  name: Livepeer webhook API
  slug: livepeer-com-webhook-api
arazzos:
- description: Create a clip from a live playback ID, poll the clip task, fetch the asset.
  name: Livepeer Clip a Livestream
  slug: livepeer-com-clip-livestream-workflow
- description: Create a stream, enable recording via update, and confirm the change.
  name: Livepeer Enable Recording on a Stream
  slug: livepeer-com-enable-stream-recording-workflow
- description: Upload an asset from an external URL, then poll the processing task.
  name: Livepeer Import an Asset from a URL
  slug: livepeer-com-import-asset-from-url-workflow
- description: Read a stream session and resolve its recording playback info.
  name: Livepeer Inspect a Session Recording
  slug: livepeer-com-inspect-session-recording-workflow
- description: Create a live stream, confirm it exists, and resolve its playback info.
  name: Livepeer Provision a Live Stream
  slug: livepeer-com-provision-live-stream-workflow
- description: Create a stream and attach an inline multistream target to restream it.
  name: Livepeer Provision Multistream Restreaming
  slug: livepeer-com-provision-multistream-restream-workflow
- description: Create a stream then register a webhook scoped to its lifecycle events.
  name: Livepeer Register a Stream Webhook
  slug: livepeer-com-register-stream-webhook-workflow
- description: Create a signing key, create a JWT-gated stream, and resolve playback.
  name: Livepeer Secure a Stream with a Signing Key
  slug: livepeer-com-secure-stream-signing-key-workflow
- description: Create a reusable multistream target, then bind it to a new stream by ID.
  name: Livepeer Reuse a Standalone Multistream Target
  slug: livepeer-com-standalone-multistream-target-workflow
- description: Submit a transcode job to S3/web3.storage and poll the task until done.
  name: Livepeer Run a Transcode Job
  slug: livepeer-com-transcode-video-job-workflow
- description: Request a direct upload URL, then poll the asset and task until ready.
  name: Livepeer Upload and Process an Asset
  slug: livepeer-com-upload-and-process-asset-workflow
artifact_total: 96
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
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/livepeer-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livepeer-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livepeer-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/livepeer/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-clip-livestream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-enable-stream-recording-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-import-asset-from-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-inspect-session-recording-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-provision-live-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-provision-multistream-restream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-register-stream-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-secure-stream-signing-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-standalone-multistream-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-transcode-video-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/livepeer-com-upload-and-process-asset-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://livepeer.org
- group: start
  title: ''
  type: StudioPortal
  url: https://livepeer.studio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.livepeer.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.livepeer.org/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://livepeer.studio/pricing
- group: company
  title: ''
  type: Blog
  url: https://livepeer.org/blog
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
  type: GitHubRepository
  url: https://github.com/livepeer/studio
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/livepeer/docs
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
  type: PythonSDK
  url: https://github.com/livepeer/livepeer-ai-python
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/livepeer/livepeer-python-gateway
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
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/livepeer
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.livepeer.org/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.livepeer.org/llms-full.txt
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/livepeer-studio-rules.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/livepeer-ai-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/livepeer-com-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/livepeer-com-context.jsonld
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/livepeer-platform-structure.json
- group: commercial
  title: ''
  type: Plans
  url: plans/livepeer-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/livepeer-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/livepeer-com-finops.yml
created: '2026-05-25'
description: Livepeer is the open, permissionless protocol for video transcoding, streaming, and AI video inference, coordinated on Ethereum mainnet and Arbitrum One via the Livepeer Token (LPT). The company commercializes the network through Livepeer Studio (a managed REST API for live streaming, VOD, multistream, recording, rooms, access control, and AI generate) and the Livepeer AI Network, where any GPU operator can serve text-to-image, image-to-video, live video-to-video, LLM, audio-to-text, text-to-speech, upscale, and segmentation pipelines for fees settled in ETH via probabilistic micropayments. The reference Go implementation (go-livepeer), official SDKs in TypeScript, Python, and Go, the React UI Kit, the AI worker, and the Gateway are all open source under the Livepeer GitHub organization.
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
- name: Livepeer Com Finops
  service_category: Media & Streaming, AI Inference
  slug: livepeer-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livepeer-com.png
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
  name: Livepeer Com Context
  property_count: 0
  slug: livepeer-com-context
layout: provider
modified: '2026-05-25'
name: Livepeer
nav: Providers
network: true
overview: 'Livepeer publishes 19 APIs on the [APIs.io](https://apis.io/) network, including accessControl API, asset API, Ethereum API, and 16 more. Tagged areas include Video, Live Streaming, Video On Demand, AI Video, and Decentralized Compute.


  The Livepeer catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Livepeer''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, changelog, signup flow, and 55 more developer resources.'
plans:
- name: Livepeer Com Plans Pricing
  plan_count: 4
  slug: livepeer-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 8
  name: Livepeer Com Rate Limits
  slug: livepeer-com-rate-limits
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
  slug: livepeer-com-jsonschema-spectral-rules
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
  composite: 61.0
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 57.1
    developer_ergonomics: 39.1
    discoverability: 67.5
    governance: 47.4
    operational_transparency: 73.7
  previous_composite: 61.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livepeer-com/refs/heads/main/screenshots/livepeer-com-2026-06-20T184614.png
security:
- kind: authentication
  name: Livepeer Com Authentication
  slug: livepeer-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Livepeer Com Domain Security
  slug: livepeer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: livepeer-com
tags:
- Video
- Live Streaming
- Video On Demand
- AI Video
- Decentralized Compute
- GPU Network
- Ethereum
- Arbitrum
- Web3
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
website: https://livepeer.org
---
