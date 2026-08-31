---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The 3d API from LocalAI — 2 operation(s) for 3d.
  name: LocalAI 3d API
  slug: localai-3d-api
- description: The agent-jobs API from LocalAI — 7 operation(s) for agent-jobs.
  name: LocalAI Agent Jobs API
  slug: localai-agent-jobs-api
- description: The audio API from LocalAI — 14 operation(s) for audio.
  name: LocalAI Audio API
  slug: localai-audio-api
- description: The backends API from LocalAI — 11 operation(s) for backends.
  name: LocalAI Backends API
  slug: localai-backends-api
- description: The branding API from LocalAI — 3 operation(s) for branding.
  name: LocalAI Branding API
  slug: localai-branding-api
- description: The config API from LocalAI — 6 operation(s) for config.
  name: LocalAI Config API
  slug: localai-config-api
- description: The depth API from LocalAI — 1 operation(s) for depth.
  name: LocalAI Depth API
  slug: localai-depth-api
- description: The detection API from LocalAI — 1 operation(s) for detection.
  name: LocalAI Detection API
  slug: localai-detection-api
- description: The embeddings API from LocalAI — 1 operation(s) for embeddings.
  name: LocalAI Embeddings API
  slug: localai-embeddings-api
- description: The face-recognition API from LocalAI — 6 operation(s) for face-recognition.
  name: LocalAI Face Recognition API
  slug: localai-face-recognition-api
- description: The images API from LocalAI — 3 operation(s) for images.
  name: LocalAI Images API
  slug: localai-images-api
- description: The inference API from LocalAI — 7 operation(s) for inference.
  name: LocalAI Inference API
  slug: localai-inference-api
- description: The instructions API from LocalAI — 2 operation(s) for instructions.
  name: LocalAI Instructions API
  slug: localai-instructions-api
- description: The mcp API from LocalAI — 1 operation(s) for mcp.
  name: LocalAI MCP API
  slug: localai-mcp-api
- description: The models API from LocalAI — 10 operation(s) for models.
  name: LocalAI Models API
  slug: localai-models-api
- description: The moderation API from LocalAI — 1 operation(s) for moderation.
  name: LocalAI Moderation API
  slug: localai-moderation-api
- description: The monitoring API from LocalAI — 16 operation(s) for monitoring.
  name: LocalAI Monitoring API
  slug: localai-monitoring-api
- description: The Nodes API from LocalAI — 3 operation(s) for nodes.
  name: LocalAI Nodes API
  slug: localai-nodes-api
- description: The p2p API from LocalAI — 2 operation(s) for p2p.
  name: LocalAI P2p API
  slug: localai-p2p-api
- description: The pii API from LocalAI — 2 operation(s) for pii.
  name: LocalAI Pii API
  slug: localai-pii-api
- description: The rerank API from LocalAI — 1 operation(s) for rerank.
  name: LocalAI Rerank API
  slug: localai-rerank-api
- description: The router API from LocalAI — 3 operation(s) for router.
  name: LocalAI Router API
  slug: localai-router-api
- description: The tokenize API from LocalAI — 4 operation(s) for tokenize.
  name: LocalAI Tokenize API
  slug: localai-tokenize-api
- description: The video API from LocalAI — 1 operation(s) for video.
  name: LocalAI Video API
  slug: localai-video-api
- description: The voice-profiles API from LocalAI — 3 operation(s) for voice-profiles.
  name: LocalAI Voice Profiles API
  slug: localai-voice-profiles-api
- description: The voice-recognition API from LocalAI — 6 operation(s) for voice-recognition.
  name: LocalAI Voice Recognition API
  slug: localai-voice-recognition-api
artifact_total: 33
asyncapis:
- description: The LocalAI Realtime API — an OpenAI Realtime-compatible, low-latency, multi-modal (voice and text) conversation surface carried over WebSocket, with an alternative WebRTC transport negotiated through
  name: LocalAI Realtime API
  slug: localai-realtime-asyncapi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/localai-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://localai.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://localai.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://localai.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://localai.io/docs/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://localai.io/basics/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://github.com/mudler/LocalAI/discussions
- group: company
  title: ''
  type: Blog
  url: https://localai.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mudler/LocalAI
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mudler/LocalAI
- group: commercial
  title: ''
  type: License
  url: https://github.com/mudler/LocalAI/blob/master/LICENSE
- group: auth
  title: ''
  type: Security
  url: https://github.com/mudler/LocalAI/blob/master/SECURITY.md
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/localai-changelog.yml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mudler/LocalAI/releases
- group: build
  title: ''
  type: Packages
  url: packages/localai-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/localai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/localai-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/localai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/localai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/localai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/localai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/localai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/localai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/localai-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/localai-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/localai-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/localai-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/localai-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/localai-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/localai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/localai-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/localai-realtime-asyncapi.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/localai-backend.proto
- group: other
  title: ''
  type: gRPC
  url: grpc/localai-backend-proto.yml
created: '2026-08-27'
description: 'LocalAI is the open-source, self-hosted AI inference engine that acts as a drop-in replacement for the OpenAI and Anthropic REST APIs. A single Go binary (or container) exposes 123 HTTP operations across chat completions, completions, embeddings, image and video generation, 3D generation, text-to-speech, speech-to-text, audio classification and diarization, object detection, depth estimation, reranking, moderation, tokenization, face and voice recognition, and the OpenAI Realtime API over WebSocket and WebRTC — all running locally on CPU or GPU with no external API calls and no data leaving the host. Beyond OpenAI parity, LocalAI ships its own management surface: a model and backend gallery, P2P and federated distributed inference, an agent/job runtime with a Skills system and Agent Hub, request middleware for NER-based PII redaction and policy-based intelligent model routing, tracing, per-user usage accounting, and a first-party stdio MCP server (`local-ai mcp-server`) that
  exposes the admin surface as agent tools. Authentication spans legacy shared API keys through a full user system with roles, sessions, GitHub OAuth and OIDC single sign-on. Distributed under the MIT licence by Ettore Di Giacinto (mudler) and community contributors.'
image: https://raw.githubusercontent.com/mudler/LocalAI/master/core/http/static/logo_horizontal.png
layout: provider
mcp_servers:
- description: ''
  name: LocalAI Assistant MCP server
  slug: localai-assistant-mcp-server
modified: '2026-08-27'
name: LocalAI
nav: Providers
network: true
overview: 'LocalAI publishes 26 APIs on the [APIs.io](https://apis.io/) network, including 3d API, Agent Jobs API, Audio API, and 23 more. Tagged areas include Artificial Intelligence, Machine-Learning, Large Language Models, Inference, and Self-Hosted.


  The LocalAI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LocalAI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 28 more developer resources.'
plans:
- name: Localai Plans Pricing
  plan_count: 0
  slug: localai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Localai Rate Limits
  slug: localai-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 46.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 42.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Localai Authentication
  slug: localai-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Localai Domain Security
  slug: localai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Localai Vulnerability Disclosure
  slug: localai-vulnerability-disclosure
  summary_line: contact published
slug: localai
tags:
- Artificial Intelligence
- Machine-Learning
- Large Language Models
- Inference
- Self-Hosted
- Open-Source
- Agents
- MCP
- Speech
- Computer-Vision
- Embeddings
- Edge Computing
website: https://localai.io/
---
