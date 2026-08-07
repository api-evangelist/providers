---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 113
  human_in_the_loop: 0
  name: Seekr Agentic Access
  operation_count: 212
  slug: seekr-agentic-access
  summary_line: 212 operations · 113 acting
api_count: 5
apis:
- description: The core SeekrFlow control plane — agents (v1 and v2), custom tools, the AI-ready data engine (file ingestion, data jobs, alignment / instruction-pair generation), vector databases and chunk metadata,
  name: SeekrFlow Platform API
  slug: seekrflow-platform-api
- description: 'The runtime half of SeekrFlow agents — threads, messages, runs (including SSE streaming and a Vercel AI SDK stream shape), run cancel and attach, uploaded custom Python functions used as agent tools, '
  name: SeekrFlow Agent Runtime API
  slug: seekrflow-agent-runtime-api
- description: Seekr's differentiating surface — context attribution (which retrieved sources influenced an answer, from a stored run or an arbitrary response/context pair), training-data attribution via a per-model
  name: SeekrFlow Explainability API
  slug: seekrflow-explainability-api
- description: OpenAI-compatible inference — chat completions, completions, embeddings, rerank, score and audio transcription — plus batch jobs, file handling for batches, model listing, engine health/metrics and sl
  name: SeekrFlow Inference & Serving API
  slug: seekrflow-inference-serving-api
- description: A hosted, anonymous, read-only MCP server that gives an AI assistant direct access to the SeekrFlow documentation and the four SeekrFlow OpenAPI specs, so the assistant can generate working authentica
  name: Seekr Documentation MCP Server
  slug: seekr-documentation-mcp-server
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/seekr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/seekr-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.seekr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.seekr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seekr.com/flow
- group: docs
  title: ''
  type: APIReference
  url: https://docs.seekr.com/flow/reference/getting-started-with-your-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seekr.com/flow/sdk/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.seekr.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.seekr.com/resource-center/?type=blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.seekr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://apps.seekr.com/signup
- group: start
  title: ''
  type: Login
  url: https://apps.seekr.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seekr.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seekr.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.seekr.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.seekr.com/flow/changelog/seekr-managed/2026
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/seekr-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.seekr.com/flow/reference/getting-started-with-your-api#versioning
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seekr-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.seekr.com/security-compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/seekr-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seekr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seekr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/seekr-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/seekr-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/seekr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seekr-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seekr-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/seekr-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/seekr-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seekr-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/seekr-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seekr-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/seekr-llm-training-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/seekr-agents-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/seekr-explainability-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/seekr-serving-overlay.yaml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seekrtechnologies/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@seekrtechnologies
- group: company
  title: ''
  type: Twitter
  url: https://x.com/seekrtechnology
created: '2026-08-05'
description: Seekr Technologies builds explainable, auditable, sovereign AI for regulated industries and high-stakes government missions. Its platform, SeekrFlow, is an end-to-end AI operating system that covers document ingestion and AI-ready data preparation, vector databases and retrieval, instruction / LoRA / DPO / GRPO / vision-language fine-tuning, model deployment, OpenAI-compatible inference, and agent orchestration with tools — all wrapped in an explainability layer that traces every response back to the retrieved chunks, tool calls, spans and training examples that produced it. Companion products are SeekrGuard (third-party and open-weight model evaluation and certification), SeekrGeo (multimodal geospatial intelligence) and SeekrIntel (investigative entity mapping). SeekrFlow is reachable through a no-code web app, the seekrai Python SDK, and a REST API at flow.seekr.com, and deploys to Seekr's cloud, a customer cloud, on-premises, the edge or fully air-gapped environments.
image: https://s48368.pcdn.co/wp-content/uploads/2025/10/Seekr-Thumbnail-OG-Image-1.png
layout: provider
mcp_servers:
- description: ''
  name: seekr-mcp.yml
  slug: seekr-mcpyml
modified: '2026-08-05'
name: Seekr
nav: Providers
network: true
overview: 'Seekr publishes 4 APIs on the [APIs.io](https://apis.io/) network, including SeekrFlow Platform API, SeekrFlow Agent Runtime API, SeekrFlow Explainability API, and 1 more. Tagged areas include artificial-intelligence, generative-ai, agents, llm, and fine-tuning.


  Seekr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
random_paper: 86
score:
  band: strong
  composite: 57.0
  delta: 0.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.1
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 25.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Seekr Authentication
  slug: seekr-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Seekr Domain Security
  slug: seekr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Seekr Trust Center
  slug: seekr-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO/IEC 27001:2022, CMMC Certified
slug: seekr
tags:
- artificial-intelligence
- generative-ai
- agents
- llm
- fine-tuning
- inference
- rag
- vector-database
- explainability
- ai-governance
- model-evaluation
- observability
- geospatial-intelligence
- defense
- government
- regulated-industries
- mcp
- agent-native
website: https://www.seekr.com/
---
