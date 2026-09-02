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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Exactly Ai Agentic Access
  operation_count: 20
  slug: exactly-ai-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 1
apis:
- description: The Images v1 API from Exactly Ai — 6 operation(s) for images v1.
  name: Exactly Ai Images v1 API
  slug: exactly-ai-images-v1-api
- description: The Models v1 API from Exactly Ai — 9 operation(s) for models v1.
  name: Exactly Ai Models v1 API
  slug: exactly-ai-models-v1-api
arazzos:
- description: Generate an image from an existing style model, then upscale, vectorize, and remove its background.
  name: Exactly.ai — generate and post-process an image
  slug: exactly-ai-generate-and-postprocess
- description: Create a custom style model, train it on brand images, then generate on-brand images once ready.
  name: Exactly.ai — train a style model and generate images
  slug: exactly-ai-train-and-generate
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Exactly Public Images v1 API
  slug: open-exactly-ai-images-v1-api
- collection_type: open
  name: Exactly Public Images v1 Models v1 API
  slug: open-exactly-ai-models-v1-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/exactly-ai-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exactly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exactly-ai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.exactly.ai/public/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.exactly.ai/public/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.exactly.ai/public/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://exactly.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://exactly.ai/help-center
- group: start
  title: ''
  type: SignUp
  url: https://exactly.ai/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exactly.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exactly.ai/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://exactly.ai/help-center/collections/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/exactly-ai
- group: auth
  title: ''
  type: Compliance
  url: https://exactly.ai/help-center/data-protection-privacy-ico-registered-private-by-default
- group: auth
  title: ''
  type: Authentication
  url: authentication/exactly-ai-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/exactly-ai-public-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exactly-ai-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exactly-ai-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exactly-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/exactly-ai-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exactly-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exactly-ai-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exactly-ai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/exactly-ai-public-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/exactly-ai-train-style-model.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/exactly-ai-generate-images.md
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exactly-ai-train-and-generate.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exactly-ai-generate-and-postprocess.yml
created: '2026-07-17'
description: Exactly.ai is a private, brand-safe AI image generation platform for brands, agencies, and creative teams. It trains custom AI "style" models from as few as ten brand images, then generates hundreds of on-brand image variations with consistent look and feel. Beyond generation the platform edits and animates images, pins characters, upscales to 8K, vectorizes to SVG, and removes backgrounds, with outputs fully licensed for commercial use and original artists compensated when their styles are used. Exactly.ai exposes an enterprise Public API (bearer-token authenticated) for programmatic model creation and training, image generation, upscaling, vectorization, and background removal, alongside the e.studio web product. The company is a portfolio company of Speedinvest and is tracked in the API Evangelist network.
image: https://framerusercontent.com/images/WlAkvz0GvPEt7p9O61w5Zp9WtY.png
layout: provider
mcp_servers:
- description: ''
  name: Exactly Ai MCP Server
  slug: exactly-ai-mcp-server
modified: '2026-07-19'
name: Exactly Ai
nav: Providers
network: true
overview: 'Exactly Ai publishes 2 APIs on the [APIs.io](https://apis.io/) network: Images v1 API and Models v1 API. Tagged areas include Company, Artificial Intelligence, Image-Generation, Generative AI, and Creative Tools.


  Exactly Ai''s developer surface includes documentation, API reference, pricing, support, signup flow, getting-started guide, authentication, and 21 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exactly-ai/refs/heads/main/screenshots/exactly-ai-2026-07-25T213837.png
security:
- kind: authentication
  name: Exactly Ai Authentication
  slug: exactly-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Exactly Ai Domain Security
  slug: exactly-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: exactly-ai
tags:
- Company
- Artificial Intelligence
- Image-Generation
- Generative AI
- Creative Tools
- Brand
- Machine-Learning
- Media
website: https://api.exactly.ai/public/docs/
---
