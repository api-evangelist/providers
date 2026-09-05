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
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Decart Agentic Access
  operation_count: 75
  slug: decart-agentic-access
  summary_line: 75 operations · 67 acting
api_count: 2
apis:
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The realtime video transformation surface. A client opens a WebRTC session (LiveKit-managed transport) against a Lucy realtime model and streams camera or video frames in; the model returns transforme
  name: Decart Realtime API
  slug: decart-realtime-api
- description: A gRPC session protocol for Oasis 3 Preview, Decart's promptable real-time world model. A client initializes a session, sets a scene with a text prompt, then loops Infer calls that submit four driving
  name: Decart Oasis Action-to-Video (gRPC)
  slug: decart-oasis-a2v
- description: 'A hosted, unauthenticated Model Context Protocol server at docs.platform.decart.ai/mcp that exposes the Decart API Platform documentation to agents. Three tools: full-text search across the knowledge '
  name: Decart Documentation MCP Server
  slug: decart-docs-mcp
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Client API from Decart — 1 operation(s) for client.
  name: Decart Client API
  slug: decart-client-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Files API from Decart — 2 operation(s) for files.
  name: Decart Files API
  slug: decart-files-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Generate API from Decart — 4 operation(s) for generate.
  name: Decart Generate API
  slug: decart-generate-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Jobs API from Decart — 43 operation(s) for jobs.
  name: Decart Jobs API
  slug: decart-jobs-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Models API from Decart — 1 operation(s) for models.
  name: Decart Models API
  slug: decart-models-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Realtime API from Decart — 1 operation(s) for realtime.
  name: Decart Realtime API
  slug: decart-realtime-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Verify API from Decart — 1 operation(s) for verify.
  name: Decart Verify API
  slug: decart-verify-api
- baseURL: https://api.decart.ai
  baseurl_source: declared
  description: The Watch Stream API from Decart — 1 operation(s) for watch stream.
  name: Decart Watch Stream API
  slug: decart-watch-stream-api
artifact_total: 19
collections:
- collection_type: open
  name: Decart API
  slug: open-decart-api-openapi-original
- collection_type: open
  name: Decart API
  slug: open-decart-platform-openapi-original
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
- description: 'Decart publishes a hosted, remote MCP server on its documentation host. It is a documentation-knowledge server, not a wrapper over the Decart REST API: its three tools search and query the Decart API '
  name: Decart MCP Server
  slug: decart-mcp-server
modified: '2026-08-01'
name: Decart
nav: Providers
network: true
overview: 'Decart publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Realtime API, Client API, Files API, and 6 more. Tagged areas include Artificial Intelligence, Machine-Learning, Video, Video Generation, and Video Editing.


  Decart''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, support, pricing, and 36 more developer resources.'
plans:
- name: Decart Plans Pricing
  plan_count: 5
  slug: decart-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Decart Rate Limits
  slug: decart-rate-limits
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 48.6
    developer_ergonomics: 75.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/decart/refs/heads/main/screenshots/decart-2026-08-07T164225.png
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
- Machine-Learning
- Video
- Video Generation
- Video Editing
- Image Editing
- Real-Time
- Generative AI
- World Models
- Streaming
- WebRTC
- Media
- Developer Tools
- Company
website: https://decart.ai/
---
