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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Text and vision-language chat completions
  name: Wombo Chat API
  slug: wombo-chat-api
- description: Image generation and editing
  name: Wombo Images API
  slug: wombo-images-api
- description: Model discovery
  name: Wombo Models API
  slug: wombo-models-api
- description: Object detection and segmentation
  name: Wombo Predictions API
  slug: wombo-predictions-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: w.ai Inference Chat API
  slug: open-wombo-chat-api
- collection_type: open
  name: w.ai Inference Chat Images API
  slug: open-wombo-images-api
- collection_type: open
  name: w.ai Inference Chat Models API
  slug: open-wombo-models-api
- collection_type: open
  name: w.ai Inference Chat Predictions API
  slug: open-wombo-predictions-api
common:
- group: company
  title: ''
  type: Website
  url: https://w.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.w.ai/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.w.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.w.ai/w.ai-api/api-features
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.w.ai/get-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://app.w.ai/dashboard
- group: operate
  title: ''
  type: Support
  url: https://docs.w.ai/bugs-and-support/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://discord.gg/w-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/womboai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.w.ai/compute/terms
- group: other
  title: ''
  type: Download
  url: https://download.w.ai
- group: auth
  title: ''
  type: Authentication
  url: authentication/wombo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wombo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wombo-problem-types.yml
- group: build
  title: ''
  type: CLI
  url: cli/wombo-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/wombo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wombo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wombo-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wombo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wombo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wombo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wombo-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wombo-wai-overlay.yaml
created: '2026-07-17'
description: Wombo is the AI company behind Dream by WOMBO, a consumer AI art and video generator, and w.ai, a decentralized AI supercomputer that pools idle GPU compute worldwide to serve affordable on-demand inference. The w.ai developer platform exposes an OpenAI-compatible HTTP API at api.w.ai/v1 covering model discovery, text and vision-language chat completions with tool calling and streaming, text-to-image generation and editing (FLUX, SDXL), and object detection and segmentation (YOLO11n, SAM2) over images and video, plus a `wai` CLI and rentable Jupyter/SSH compute environments. Backed by 500 Global.
image: https://w.ai/wai-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Wombo MCP Server
  slug: wombo-mcp-server
modified: '2026-07-21'
name: Wombo
nav: Providers
network: true
overview: 'Wombo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Images API, Models API, and 1 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Inference, and LLM.


  Wombo''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, CLI, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Wombo Authentication
  slug: wombo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wombo Domain Security
  slug: wombo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wombo
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Inference
- LLM
- Image-Generation
- Generative AI
- Decentralized Compute
- GPU
- OpenAI-Compatible
website: https://w.ai/
---
