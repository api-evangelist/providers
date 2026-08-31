---
access_model:
  confidence: high
  label: Paid API on a subscription plan
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.flora.ai/api
  - https://docs.flora.ai/plans-and-billing/pricing
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: FLORA's hosted remote Model Context Protocol server. Streamable HTTP at https://agents.flora.ai/mcp, authenticated with OAuth 2.1 + PKCE (RFC 8414 authorization-server metadata and RFC 9728 protected-
  name: FLORA MCP Server
  slug: flora-mcp
- description: Prebuilt action catalog endpoints.
  name: FLORA Actions API
  slug: flora-fauna-actions-api
- description: Asset upload and retrieval endpoints.
  name: FLORA Assets API
  slug: flora-fauna-assets-api
- description: Project canvas endpoints.
  name: FLORA Canvas API
  slug: flora-fauna-canvas-api
- description: Product feedback endpoints.
  name: FLORA Feedback API
  slug: flora-fauna-feedback-api
- description: Generation endpoints.
  name: FLORA Generations API
  slug: flora-fauna-generations-api
- description: Model catalog endpoints.
  name: FLORA Models API
  slug: flora-fauna-models-api
- description: Project management endpoints.
  name: FLORA Projects API
  slug: flora-fauna-projects-api
- description: Top-level run creation endpoints.
  name: FLORA Runs API
  slug: flora-fauna-runs-api
- description: Nested technique run endpoints.
  name: FLORA Technique Runs API
  slug: flora-fauna-technique-runs-api
- description: Technique catalog endpoints.
  name: FLORA Techniques API
  slug: flora-fauna-techniques-api
- description: Workspace discovery endpoints.
  name: FLORA Workspaces API
  slug: flora-fauna-workspaces-api
artifact_total: 21
asyncapis:
- description: ''
  name: Flora Fauna Webhooks
  slug: flora-fauna-webhooks
collections:
- collection_type: open
  name: Flora.ai API
  slug: open-flora-fauna-flora-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/flora-fauna-flora-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flora-fauna-flora-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flora-fauna-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flora-fauna-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flora-fauna-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/flora-fauna-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flora-fauna-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/flora-fauna-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flora-fauna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flora-fauna-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flora-fauna-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/flora-fauna-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flora-fauna-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flora-fauna-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flora-fauna-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flora-fauna-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flora-fauna-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flora-fauna-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flora.ai
- group: design
  title: ''
  type: Conformance
  url: conformance/flora-fauna-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/flora-fauna-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flora-fauna-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flora-fauna-plans-pricing.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flora-fauna-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flora-fauna-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.flora.ai
- group: docs
  title: ''
  type: APIReference
  url: https://developer.flora.ai/reference/resources/techniques
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.flora.ai/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/florafauna-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://flora.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.flora.ai
- group: company
  title: ''
  type: Website
  url: https://www.florafauna.ai
- group: other
  title: ''
  type: Application
  url: https://app.florafauna.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flora.ai
- group: company
  title: ''
  type: Blog
  url: https://flora.ai/blog
- group: operate
  title: ''
  type: Community
  url: https://app.florafauna.ai/community
- group: company
  title: ''
  type: Careers
  url: https://flora.ai/careers
- group: other
  title: ''
  type: JobBoard
  url: https://jobs.ashbyhq.com/FLORA
- group: other
  title: ''
  type: Brand
  url: https://flora.ai/brand
- group: operate
  title: ''
  type: Status
  url: https://status.flora.ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@florafauna.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.flora.ai/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flora.ai/legal/terms-of-service
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/florafaunaai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/floraai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@florafaunaai
- group: other
  title: ''
  type: FoundingAnnouncement
  url: https://flora.ai/blog/flora-raises-6-5m-to-build-the-world-s-most-powerful-creative-tool
created: '2026-05-25'
description: 'FLORA is a Brooklyn, New York-based applied AI / HCI company building a browser-based "infinite canvas" creative workspace for professional creators. Founded in 2024 by Weber Wong out of NYU''s Interactive Telecommunications Program (ITP), FLORA unifies 50+ third-party text, image, and video AI models inside a single node-based visual workspace where designers, filmmakers, photographers, and creative agencies wire prompts, references, characters, and outputs into reusable generative workflows called Techniques. The platform integrates leading image models (FLUX.2, FLUX Kontext, Stable Diffusion 3.5, Nano Banana, Recraft, Seedream, Minimax Hailuo) and video models (Veo 3, Sora 2, Runway Gen-4 Turbo / Gen-3 Alpha / Act-Two, Pika, Kling, Luma Ray 2, Seedance, Marey) alongside reasoning models such as Gemini 3 Pro and GPT-5.4, and ships a creative agent named FAUNA for ideation, iteration, and workflow scaffolding. FLORA is used at agencies and studios including Pentagram, Milk,
  and MSCHF; the company raised a $6.5M seed led by Mike Volpi at Hanabi Capital with Menlo Ventures, a16z Games Speedrun, Long Journey Ventures, Company Ventures, Alumni Ventures, Embedding VC, and angels including Justin Kan (Twitch) and Gabe Whaley (MSCHF), and operates in-person from the Domino Refinery in Williamsburg. Beyond the canvas FLORA now ships a public developer surface: the Flora.ai REST API (OpenAPI 3.1.1, base https://app.flora.ai/api/v1) for running Techniques, one-off generations, assets, projects, canvas patches and actions programmatically; a hosted remote MCP server at https://agents.flora.ai/mcp exposing two tools (search_docs, execute) over OAuth 2.1 + PKCE; first-party TypeScript and Go SDKs and a Go CLI; signed HMAC-SHA256 run webhooks; idempotency keys; and a Stainless-generated developer portal at developer.flora.ai. API and MCP access begin on the paid Starter plan.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flora-fauna.png
layout: provider
mcp_servers:
- description: ''
  name: FLORA MCP Server
  slug: flora-mcp-server
modified: '2026-08-12'
name: FLORA
nav: Providers
network: true
overview: 'FLORA publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Assets API, Canvas API, and 8 more. Tagged areas include Creative AI, Generative AI, Infinite Canvas, Node-Based Workflows, and Creative Workspace.


  The FLORA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FLORA''s developer surface includes CLI, authentication, changelog, API reference, getting-started guide, pricing, signup flow, and 41 more developer resources.'
plans:
- name: Flora Fauna Plans Pricing
  plan_count: 5
  slug: flora-fauna-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Flora Fauna Rate Limits
  slug: flora-fauna-rate-limits
scopes:
- name: Flora Fauna Scopes
  scope_count: 0
  slug: flora-fauna-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 63.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flora-fauna/refs/heads/main/screenshots/flora-fauna-2026-06-20T181332.png
security:
- kind: authentication
  name: Flora Fauna Authentication
  slug: flora-fauna-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Flora Fauna Domain Security
  slug: flora-fauna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flora Fauna Trust Center
  slug: flora-fauna-trust-center
  summary_line: SOC 2, GDPR
slug: flora-fauna
tags:
- Creative AI
- Generative AI
- Infinite Canvas
- Node-Based Workflows
- Creative Workspace
- Image-Generation
- Video Generation
- Text-to-Image
- Text-to-Video
- AI Agents
- Multimodal AI
- Design Tools
- Creative Professionals
- Advertising
- Film
- Fashion
- Branding
- VFX
- Photography
- Architecture
- Motion Design
- FAUNA
- MCP
- Agent Tools
- Workflow-Automation
website: https://www.florafauna.ai
---
