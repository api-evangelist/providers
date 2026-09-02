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
    agent_skills: true
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Memories Agentic Access
  operation_count: 34
  slug: memories-agentic-access
  summary_line: 34 operations · 27 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Serve API from Memories — 30 operation(s) for serve.
  name: Memories Serve API
  slug: memories-serve-api
- description: The Stream Understanding API from Memories — 2 operation(s) for stream understanding.
  name: Memories Stream Understanding API
  slug: memories-stream-understanding-api
- description: The Understand API from Memories — 2 operation(s) for understand.
  name: Memories Understand API
  slug: memories-understand-api
artifact_total: 14
asyncapis:
- description: ''
  name: Memories Webhooks
  slug: memories-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve API
  slug: open-memories-serve-api
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve Stream Understanding API
  slug: open-memories-stream-understanding-api
- collection_type: open
  name: Memories Platform API (Docs Mapping) Serve Understand API
  slug: open-memories-understand-api
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/memories-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-platform.memories.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api-tools.memories.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-tools.memories.ai/visual-intelligence/getting-started/introduction
- group: start
  title: ''
  type: SignUp
  url: https://api-platform.memories.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://api-tools.memories.ai/visual-search/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Memories-ai-labs
- group: auth
  title: ''
  type: Compliance
  url: https://memories.ai/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/memories-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/memories-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/memories-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/memories-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/memories-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/memories-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/memories-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/memories-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/memories-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/memories-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/memories-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/memories-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/memories-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memories-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/memories-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/memories-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://memories.ai
created: '2026-07-17'
description: 'Memories.ai (MAVI) is a video-intelligence platform that turns raw video into searchable, agent-ready understanding. It ships three products on a shared video-understanding stack: Visual Intelligence (stateless REST APIs for transcription, captioning, frame description, embeddings, social-media scraping, and real-time audio/video stream moderation via VLMs such as Gemini, Nova, and Qwen), Visual Search (an auto-indexed private and public video/image library searchable by text, image, or transcript), and Visual Agents (pre-built workflows for video search, AI video editing, and screenplay extraction). The platform authenticates with sk-mavi- API keys, bills on a unified per-endpoint credit model, and is HIPAA, SOC 2 Type 2, and GDPR compliant. It is a Seedcamp portfolio company.'
image: https://mintcdn.com/memories/xyhRN3OJaXxxzcxh/logo/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Memories MCP Server
  slug: memories-mcp-server
modified: '2026-07-20'
name: Memories
nav: Providers
network: true
overview: 'Memories publishes 3 APIs on the [APIs.io](https://apis.io/) network: Serve API, Stream Understanding API, and Understand API. Tagged areas include Company, Video Intelligence, Video Understanding, Video Search, and Transcription.


  The Memories catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Memories'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, authentication, CLI, and 20 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: Memories Rate Limits
  slug: memories-rate-limits
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 60.2
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memories/refs/heads/main/screenshots/memories-2026-08-07T172506.png
security:
- kind: authentication
  name: Memories Authentication
  slug: memories-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Memories Domain Security
  slug: memories-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Memories Trust Center
  slug: memories-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: memories
tags:
- Company
- Video Intelligence
- Video Understanding
- Video Search
- Transcription
- Embeddings
- Multimodal AI
- Content Moderation
- AI Agents
- Machine-Learning
website: http://memories.ai
---
