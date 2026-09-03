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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Higgsfield Agentic Access
  operation_count: 50
  slug: higgsfield-agentic-access
  summary_line: 50 operations · 49 acting
api_count: 1
apis:
- baseURL: https://platform.higgsfield.ai
  baseurl_source: declared
  description: 'Asynchronous generative-media API. Submit a generation request to any of the 100+ model endpoints (POST /{model_id}), then retrieve status (GET /requests/{request_id}/status), cancel a queued request '
  name: Higgsfield API
  slug: higgsfield-api
artifact_total: 8
asyncapis:
- description: ''
  name: Higgsfield Webhooks
  slug: higgsfield-webhooks
collections:
- collection_type: open
  name: API Reference
  slug: open-higgsfield-openapi-original
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/higgsfield-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/higgsfield-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/higgsfield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://higgsfield.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.higgsfield.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.higgsfield.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.higgsfield.ai/docs/how-to/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.higgsfield.ai/docs/how-to/introduction
- group: company
  title: ''
  type: Blog
  url: https://higgsfield.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://higgsfield.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/higgsfield-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://higgsfield.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.higgsfield.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://higgsfield.ai/terms-of-use-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://higgsfield.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/higgsfield-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/higgsfield-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/higgsfield-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/higgsfield-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/higgsfield-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/higgsfield-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/higgsfield-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/higgsfield-well-known.yml
- group: auth
  title: ''
  type: Security
  url: https://higgsfield.ai/security-policy.pdf
- group: design
  title: ''
  type: Conventions
  url: conventions/higgsfield-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/higgsfield-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/higgsfield-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/higgsfield-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.higgsfield.ai/
- group: design
  title: ''
  type: DataModel
  url: data-model/higgsfield-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/higgsfield-webhooks.yml
created: '2026-07-17'
description: 'Higgsfield is a multi-model generative AI platform for video, image, editing, storyboarding, and commercial content creation. Its public developer API (platform.higgsfield.ai) exposes 100+ generative models — Sora 2, Veo 3.1, Kling, Seedance, Hailuo, FLUX, Nano Banana, Reve, and Higgsfield''s own Soul / DoP / Popcorn models — behind a single asynchronous request/response contract: POST a model endpoint to enqueue a generation, then poll the request status or receive a webhook when it completes. The platform ships an official Python SDK (higgsfield-client), a Node.js/TypeScript SDK (@higgsfield/client), a cross-platform CLI (@higgsfield/cli), a remote MCP server (mcp.higgsfield.ai) for agent access, and a public set of Agent Skills for Claude, Cursor, and Codex. Backed by Accel and Menlo Ventures.'
image: https://higgsfield.ai/favicon.ico
layout: provider
mcp_servers:
- description: Official hosted (remote) Higgsfield MCP server. Exposes the full Higgsfield generation platform (30+ video and image models — Veo 3.1, Sora 2, Kling 3.0, Seedance 2.0, and more) to MCP-capable agents.
  name: Higgsfield MCP Server
  slug: higgsfield-mcp-server
modified: '2026-07-19'
name: Higgsfield
nav: Providers
network: true
overview: 'Higgsfield publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Video Generation, and Image-Generation.


  The Higgsfield catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Higgsfield''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, pricing, signup flow, and 25 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/higgsfield/refs/heads/main/screenshots/higgsfield-2026-07-25T221304.png
security:
- kind: authentication
  name: Higgsfield Authentication
  slug: higgsfield-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Higgsfield Domain Security
  slug: higgsfield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Higgsfield Vulnerability Disclosure
  slug: higgsfield-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: higgsfield
tags:
- Company
- Artificial Intelligence
- Generative AI
- Video Generation
- Image-Generation
- Machine-Learning
- Media
- Content Creation
- Developer API
website: https://higgsfield.ai/
---
