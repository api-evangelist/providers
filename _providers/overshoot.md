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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-03'
api_count: 8
apis:
- description: Pricing, prepaid balance, and checkout.
  name: Overshoot Billing API
  slug: overshoot-billing-api
- description: The Chat API from Overshoot — 1 operation(s) for chat.
  name: Overshoot Chat API
  slug: overshoot-chat-api
- description: The Healthz API from Overshoot — 1 operation(s) for healthz.
  name: Overshoot Healthz API
  slug: overshoot-healthz-api
- description: The Metrics API from Overshoot — 1 operation(s) for metrics.
  name: Overshoot Metrics API
  slug: overshoot-metrics-api
- description: The Models API from Overshoot — 2 operation(s) for models.
  name: Overshoot Models API
  slug: overshoot-models-api
- description: The Readyz API from Overshoot — 1 operation(s) for readyz.
  name: Overshoot Readyz API
  slug: overshoot-readyz-api
- description: Create, inspect, keep alive, and delete live video streams.
  name: Overshoot Streams API
  slug: overshoot-streams-api
- description: The V1beta API from Overshoot — 1 operation(s) for v1beta.
  name: Overshoot V1beta API
  slug: overshoot-v1beta-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overshoot-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.overshoot.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overshoot.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overshoot.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.overshoot.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://overshoot.ai/blogs
- group: operate
  title: ''
  type: Support
  url: https://overshoot.ai/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Overshoot-ai
- group: start
  title: ''
  type: SignUp
  url: https://platform.overshoot.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://platform.overshoot.ai/privacy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overshoot-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/overshoot-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/overshoot-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overshoot-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overshoot-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/overshoot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/overshoot-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/overshoot-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/overshoot-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/overshoot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/overshoot-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/overshoot-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Overshoot is a real-time video understanding API. Developers create a live video stream, publish frames over WebRTC (LiveKit), then query what the camera sees with vision-language models through an OpenAI-compatible chat completions endpoint — sub-200ms inference against a large catalog of VLMs. Overshoot (YC W2026) targets physical security, safety, gaming, robotics, and consumer products, exposing stream lifecycle management, model listing, prepaid-credit billing, and per-model pricing over a single REST host at api.overshoot.ai.
image: https://platform.overshoot.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: overshoot-mcp.yml
  slug: overshoot-mcpyml
modified: '2026-07-20'
name: Overshoot
nav: Providers
network: true
overview: 'Overshoot publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Chat API, Healthz API, and 5 more. Tagged areas include Company, Artificial Intelligence, Computer Vision, Video, and Video Understanding.


  Overshoot''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 51
rate_limits:
- limit_count: 2
  name: Overshoot Rate Limits
  slug: overshoot-rate-limits
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 48.4
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 43.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Overshoot Authentication
  slug: overshoot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Overshoot Domain Security
  slug: overshoot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overshoot
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Video
- Video Understanding
- Vision Language Models
- Real Time
- Streaming
- WebRTC
- Inference
- Multimodal
- Machine Learning
website: https://platform.overshoot.ai
---
