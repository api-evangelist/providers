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
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 5
  name: Moondream Agentic Access
  operation_count: 6
  slug: moondream-agentic-access
  summary_line: 6 operations · 6 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.moondream.ai/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completions endpoint.
  name: Moondream OpenAI Compatibility API
  slug: moondream-openai-compatibility-api
- baseURL: https://api.moondream.ai/v1
  baseurl_source: declared
  description: Moondream vision Skills — query, caption, detect, point, segment.
  name: Moondream Skills API
  slug: moondream-skills-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moondream Cloud OpenAI Compatibility API
  slug: open-moondream-openai-compatibility-api
- collection_type: open
  name: Moondream Cloud OpenAI Compatibility Skills API
  slug: open-moondream-skills-api
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
- description: Candidate MCP server derived from the documented Moondream Cloud Skill operations. No official Moondream-hosted MCP server was found as of the probe date; this is a proposed tool surface, not a publis
  name: Moondream MCP Server
  slug: moondream-mcp-server
modified: '2026-07-20'
name: Moondream
nav: Providers
network: true
overview: 'Moondream publishes 2 APIs on the [APIs.io](https://apis.io/) network: OpenAI Compatibility API and Skills API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Computer-Vision, and Vision Language Model.


  Moondream''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 14.5
    developer_ergonomics: 69.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moondream/refs/heads/main/screenshots/moondream-2026-08-07T184237.png
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
- Machine-Learning
- Computer-Vision
- Vision Language Model
- Object Detection
- Image Captioning
- OCR
- Developer Tools
website: https://moondream.ai
---
