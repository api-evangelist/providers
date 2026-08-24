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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: Fetch generated assets and projects
  name: Kaedim Assets API
  slug: kaedim-assets-api
- description: Token refresh
  name: Kaedim Auth API
  slug: kaedim-auth-api
- description: Submit images for 3D asset generation
  name: Kaedim Generation API
  slug: kaedim-generation-api
- description: Register a webhook endpoint and obtain a JWT
  name: Kaedim Webhooks API
  slug: kaedim-webhooks-api
artifact_total: 13
asyncapis:
- description: Event surface for Kaedim 3D asset generation. After registering an HTTPS endpoint via the Web API (/registerHook), Kaedim POSTs a signed webhook to that endpoint whenever a generation stage changes st
  name: Kaedim Webhooks
  slug: kaedim-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kaedim Web Assets API
  slug: open-kaedim-assets-api
- collection_type: open
  name: Kaedim Web Assets Auth API
  slug: open-kaedim-auth-api
- collection_type: open
  name: Kaedim Web Assets Generation API
  slug: open-kaedim-generation-api
- collection_type: open
  name: Kaedim Web Assets Webhooks API
  slug: open-kaedim-webhooks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaedim-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kaedim-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kaedim-conventions.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/kaedim-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kaedim-webhooks-asyncapi.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kaedim-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kaedim-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/Kaedim/kaedim_status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kaedim-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kaedim-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kaedim-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/kaedim-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kaedim-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kaedim-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kaedim-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kaedim-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kaedim3d.com/privacy
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kaedim-web-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kaedim3d.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kaedim3d.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kaedim3d.com/enterprise-features/custom-integrations/apis/web-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kaedim3d.com/welcome/get-started/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kaedim
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kaedim3d.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://docs.kaedim3d.com/welcome/get-started/sign-up
- group: company
  title: ''
  type: Website
  url: https://www.kaedim3d.com
created: '2026-07-17'
description: 'Kaedim is an AI 3D asset generation company (backed by a16z) that turns 2D images — photos, sketches and concept art — into production-ready 3D models for games, e-commerce and simulation. The Enterprise Web API lets developers integrate Kaedim''s 2D-to-3D pipeline into internal modelling workflows and user-generated-content products: submit up to six images at a chosen level of quality, track generation by requestID, receive results via signed webhooks, and download models in obj, fbx, glb, gltf, mtl and usd formats. Kaedim also ships first-party plugins for Unity, Unreal, Blender, Cinema 4D and NVIDIA Omniverse. Authentication uses an X-API-Key header plus a 12-hour JWT bearer token; generation is asynchronous and completes in roughly 10-15 minutes.'
image: https://www.kaedim3d.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Kaedim MCP Server
  slug: kaedim-mcp-server
modified: '2026-07-19'
name: Kaedim
nav: Providers
network: true
overview: 'Kaedim publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Auth API, Generation API, and 1 more. Tagged areas include Company, 3D, Artificial Intelligence, Generative AI, and Gaming.


  The Kaedim catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kaedim''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, signup flow, and 20 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 30.3
    contract_quality: 66.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 42.1
  previous_composite: 53.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaedim/refs/heads/main/screenshots/kaedim-2026-07-25T223407.png
security:
- kind: authentication
  name: Kaedim Authentication
  slug: kaedim-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Kaedim Domain Security
  slug: kaedim-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kaedim
tags:
- Company
- 3D
- Artificial Intelligence
- Generative AI
- Gaming
- 3D Models
- Asset Generation
- Content Generation
- Machine-Learning
website: https://www.kaedim3d.com
---
