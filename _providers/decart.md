---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Decart Agentic Access
  operation_count: 75
  slug: decart-agentic-access
  summary_line: 75 operations · 67 acting
api_count: 4
apis:
- description: The Decart REST API at api.decart.ai. Covers the Queue API (submit an asynchronous video job against a Lucy model, poll its status, download the rendered content), the Process API (synchronous image e
  name: Decart API
  slug: decart-api
- description: The realtime video transformation surface. A client opens a WebRTC session (LiveKit-managed transport) against a Lucy realtime model and streams camera or video frames in; the model returns transforme
  name: Decart Realtime API
  slug: decart-realtime-api
- description: A gRPC session protocol for Oasis 3 Preview, Decart's promptable real-time world model. A client initializes a session, sets a scene with a text prompt, then loops Infer calls that submit four driving
  name: Decart Oasis Action-to-Video (gRPC)
  slug: decart-oasis-a2v
- description: 'A hosted, unauthenticated Model Context Protocol server at docs.platform.decart.ai/mcp that exposes the Decart API Platform documentation to agents. Three tools: full-text search across the knowledge '
  name: Decart Documentation MCP Server
  slug: decart-docs-mcp
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/decart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decart-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decart.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.decart.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.platform.decart.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.platform.decart.ai/api-reference/lucy-25
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.platform.decart.ai/getting-started/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.platform.decart.ai/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://decart.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DecartAI
- group: operate
  title: ''
  type: Support
  url: mailto:contact@decart.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.platform.decart.ai/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.decart.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.platform.decart.ai/resources/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.platform.decart.ai/resources/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.platform.decart.ai/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.decart.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/decart-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/decart-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/decart-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/decart-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/decart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/decart-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/decart-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/decart-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/decart-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/decart-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/decart-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/decart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decart-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/decart-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://oasis3-preview.decart.ai/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://docs.platform.decart.ai/resources/aup
- group: other
  title: ''
  type: DPA
  url: https://docs.platform.decart.ai/resources/dpa
- group: operate
  title: ''
  type: FAQ
  url: https://docs.platform.decart.ai/resources/faq
- group: build
  title: ''
  type: Examples
  url: examples/decart-examples.yml
- group: build
  title: ''
  type: Examples
  url: https://docs.platform.decart.ai/examples/overview
- group: design
  title: ''
  type: Conformance
  url: conformance/decart-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/decart-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/decart-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/decart-api-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/decart-a2v.proto
created: '2026-08-01'
description: 'Decart is an AI research lab and API platform building real-time world models — foundation models that generate and transform video frame-by-frame as they are watched. Its Decart API Platform (platform.decart.ai) exposes the Lucy family of realtime and batch video/image models plus the Oasis promptable world model through three surfaces: a Realtime API that edits a live WebRTC camera or video stream with text prompts and reference images, a Queue API that submits asynchronous video jobs and polls them to completion, and a Process API for synchronous image editing. The platform ships first-party JavaScript, Python, Swift and Android SDKs, ephemeral client tokens for browser and mobile apps, a Files API for reusable reference images, and a gRPC action-to-video session protocol for Oasis 3 Preview. Pricing is pay-as-you-go and metered per generated second (video and realtime) or per generation (images).'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: decart-mcp.yml
  slug: decart-mcpyml
modified: '2026-08-01'
name: Decart
nav: Providers
network: true
overview: 'Decart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine Learning, Video, Video Generation, and Video Editing.


  Decart''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, pricing, and 36 more developer resources.'
plans:
- name: Decart Plans Pricing
  plan_count: 5
  slug: decart-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Decart Rate Limits
  slug: decart-rate-limits
score:
  band: strong
  composite: 62.7
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 47.3
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 68.4
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Decart Authentication
  slug: decart-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Decart Domain Security
  slug: decart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: decart
tags:
- Artificial Intelligence
- Machine Learning
- Video
- Video Generation
- Video Editing
- Image Editing
- Real Time
- Generative AI
- World Models
- Streaming
- WebRTC
- Media
- Developer Tools
- Company
website: https://decart.ai/
---
