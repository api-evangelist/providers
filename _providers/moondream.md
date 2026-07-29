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
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 5
  name: Moondream Agentic Access
  operation_count: 6
  slug: moondream-agentic-access
  summary_line: 6 operations · 6 acting · 5 human-in-the-loop
api_count: 2
apis:
- description: OpenAI-compatible chat completions endpoint.
  name: Moondream OpenAI Compatibility API
  slug: moondream-openai-compatibility-api
- description: Moondream vision Skills — query, caption, detect, point, segment.
  name: Moondream Skills API
  slug: moondream-skills-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/moondream-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moondream-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moondream-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moondream-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moondream-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moondream.ai/pricing
- group: design
  title: ''
  type: DataModel
  url: data-model/moondream-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moondream-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/moondream-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moondream-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moondream-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moondream-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moondream-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moondream-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moondream-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moondream-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://moondream.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moondream.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moondream.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moondream.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moondream.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://moondream.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://moondream.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://moondream.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moondream.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moondream.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/m87-labs
- group: start
  title: ''
  type: Sandbox
  url: https://moondream.ai/c/playground
- group: operate
  title: ''
  type: Support
  url: mailto:sales@moondream.ai
created: '2026-07-17'
description: Moondream is a fast, efficient open vision language model (VLM) from M87 Labs. The Moondream Cloud API turns images into structured output through five Skills — Query (visual question answering), Caption, Detect (bounding boxes), Point (center coordinates), and Segment (SVG path masks) — plus an OpenAI-compatible chat endpoint, an asynchronous Batch API, and cloud finetuning (Lens). Model weights are open and downloadable from Hugging Face; hosted inference is pay-per-token with HIPAA and SOC 2 available. Official Python and Node.js SDKs are published.
image: https://moondream.ai/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: moondream-mcp.yml
  slug: moondream-mcpyml
modified: '2026-07-20'
name: Moondream
nav: Providers
network: true
overview: 'Moondream publishes 2 APIs on the [APIs.io](https://apis.io/) network: OpenAI Compatibility API and Skills API. Tagged areas include Company, Artificial Intelligence, Machine Learning, Computer Vision, and Vision Language Model.


  Moondream''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 53.7
  delta: -0.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.9
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moondream Authentication
  slug: moondream-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Moondream Domain Security
  slug: moondream-domain-security
  summary_line: TLSv1.3 · DMARC
slug: moondream
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Computer Vision
- Vision Language Model
- Object Detection
- Image Captioning
- OCR
- Developer Tools
website: https://moondream.ai
---
