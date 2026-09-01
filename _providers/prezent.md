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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Prezent Agentic Access
  operation_count: 48
  slug: prezent-agentic-access
  summary_line: 48 operations · 34 acting
api_count: 1
apis:
- description: List and search the audience profiles configured for the caller's company.
  name: Prezent Audiences API
  slug: prezent-audiences-api
- description: Long-running and synchronous endpoints that generate and manipulate AI-authored presentations from prompts, files, and assets.
  name: Prezent AutoGenerator API
  slug: prezent-autogenerator-api
- description: Mint short-lived access tokens for the caller's stored files.
  name: Prezent File Access API
  slug: prezent-file-access-api
- description: Liveness and component health-check endpoints.
  name: Prezent Health API
  slug: prezent-health-api
- description: Open a Server-Sent Events stream to receive real-time progress events as Prezent generates a presentation. See the [Streaming guide](/docs/streaming) for a full walk-through plus reconnect semantics.
  name: Prezent Streaming API
  slug: prezent-streaming-api
- description: Apply a target brand template to an uploaded presentation, including review suggestions, work-area adjustment, layout change, and download.
  name: Prezent Template Converter API
  slug: prezent-template-converter-api
- description: List the presentation themes (brand templates) configured for the caller's company.
  name: Prezent Themes API
  slug: prezent-themes-api
- description: Validate, preprocess, and upload supporting files (PowerPoint, PDF, images, etc.).
  name: Prezent Upload API
  slug: prezent-upload-api
- description: Receive signed HTTPS callbacks when Prezent jobs complete or fail. Subscriptions are scoped per API key, retried over a 21h window, and auto-disabled after 50 consecutive failures. See the [Webhooks g
  name: Prezent Webhooks API
  slug: prezent-webhooks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Prezent Webhooks
  slug: prezent-webhooks
collections:
- collection_type: postman
  name: Prezent Platform Audiences API
  slug: postman-prezent-audiences-api
- collection_type: postman
  name: Prezent Platform Audiences AutoGenerator API
  slug: postman-prezent-autogenerator-api
- collection_type: postman
  name: Prezent Platform Audiences File Access API
  slug: postman-prezent-file-access-api
- collection_type: postman
  name: Prezent Platform Audiences Health API
  slug: postman-prezent-health-api
- collection_type: postman
  name: Prezent Platform Audiences Streaming API
  slug: postman-prezent-streaming-api
- collection_type: postman
  name: Prezent Platform Audiences Template Converter API
  slug: postman-prezent-template-converter-api
- collection_type: postman
  name: Prezent Platform Audiences Themes API
  slug: postman-prezent-themes-api
- collection_type: postman
  name: Prezent Platform Audiences Upload API
  slug: postman-prezent-upload-api
- collection_type: postman
  name: Prezent Platform Audiences Webhooks API
  slug: postman-prezent-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Prezent Platform Audiences API
  slug: open-prezent-audiences-api
- collection_type: open
  name: Prezent Platform Audiences AutoGenerator API
  slug: open-prezent-autogenerator-api
- collection_type: open
  name: Prezent Platform Audiences File Access API
  slug: open-prezent-file-access-api
- collection_type: open
  name: Prezent Platform Audiences Health API
  slug: open-prezent-health-api
- collection_type: open
  name: Prezent Platform Audiences Streaming API
  slug: open-prezent-streaming-api
- collection_type: open
  name: Prezent Platform Audiences Template Converter API
  slug: open-prezent-template-converter-api
- collection_type: open
  name: Prezent Platform Audiences Themes API
  slug: open-prezent-themes-api
- collection_type: open
  name: Prezent Platform Audiences Upload API
  slug: open-prezent-upload-api
- collection_type: open
  name: Prezent Platform Audiences Webhooks API
  slug: open-prezent-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/prezent/overview
- group: company
  title: ''
  type: Website
  url: https://prezent.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.prezent.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prezent.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.prezent.ai/api-reference
- group: operate
  title: ''
  type: Support
  url: https://prezent.ai/support
- group: company
  title: ''
  type: Blog
  url: https://prezent.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://prezent.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://prezent.ai/try-it-for-free
- group: start
  title: ''
  type: Login
  url: https://teams.prezent.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prezent.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prezent.ai/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://prezent.ai/security-compliance
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/prezent-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prezent-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/prezent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/prezent-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prezent-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prezent-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/prezent-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/prezent-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/prezent-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/prezent-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/prezent-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/prezent-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/prezent-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prezent-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/prezent-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/prezent-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prezent-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prezent-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prezent-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/prezent-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prezent-domain-security.yml
created: '2026-07-17'
description: Prezent is an AI-powered business communications and presentation platform, with Prezent Vivo purpose-built for life sciences teams. Its Prezent Platform API exposes the AutoGenerator (turn a prompt plus source files into an on-brand deck), Template Converter (reformat existing decks to a brand-compliant template), Audiences, Themes, and file-upload services as a uniform, agent-ready JSON HTTP API. The API uses a Bearer API key, a uniform success/error envelope with a stable error code catalog, Idempotency-Key support, cursor pagination, rate-limit headers, first-class webhooks, and ships an official Model Context Protocol (MCP) server plus typed Python and TypeScript SDKs. Backed by 500 Global.
image: https://teams.prezent.ai/prezent_favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: Prezent MCP Server
  slug: prezent-mcp-server
modified: '2026-07-20'
name: Prezent
nav: Providers
network: true
overview: 'Prezent publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, AutoGenerator API, File Access API, and 6 more. Tagged areas include Company, Presentations, Generative AI, AI Agents, and Life Sciences.


  The Prezent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Prezent''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, sandbox, and 28 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 5
  name: Prezent Rate Limits
  slug: prezent-rate-limits
score:
  band: strong
  composite: 61.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 67.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prezent/refs/heads/main/screenshots/prezent-2026-08-17T081335.png
security:
- kind: authentication
  name: Prezent Authentication
  slug: prezent-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Prezent Domain Security
  slug: prezent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Prezent Trust Center
  slug: prezent-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: prezent
tags:
- Company
- Presentations
- Generative AI
- AI Agents
- Life Sciences
- Content Generation
- Enterprise
- MCP
- Productivity
website: https://prezent.ai
---
