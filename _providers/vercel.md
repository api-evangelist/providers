---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Vercel Agentic Access
  operation_count: 6
  slug: vercel-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 2
apis:
- description: Vercel is a developer cloud to build and deploy web applications.
  name: Vercel
  slug: vercel
- description: Vercel Webhooks deliver platform events to a subscriber-configured HTTPS endpoint via HTTP POST with a JSON body. Subscriptions are created as Account Webhooks (Team Settings) or through Vercel Integr
  name: Vercel Webhooks
  slug: vercel-webhooks
- description: Chat completions (OpenAI-compatible)
  name: Vercel Chat API
  slug: vercel-chat-api
- description: AI-powered app generation via chat sessions
  name: Vercel Chats API
  slug: vercel-chats-api
- description: Text embeddings
  name: Vercel Embeddings API
  slug: vercel-embeddings-api
- description: List available AI models
  name: Vercel Models API
  slug: vercel-models-api
arazzos:
- description: Attempt a chat completion with a provider fallback chain, retrying on rate limit.
  name: Vercel AI Gateway Chat Completion With Provider Fallback
  slug: vercel-chat-completion-with-fallback-workflow
- description: Run a cost-sorted chat completion, then send a follow-up turn carrying the prior reply.
  name: Vercel AI Gateway Cost-Routed Two-Turn Conversation
  slug: vercel-cost-routed-conversation-workflow
- description: List available models, confirm the requested one is present, then run a chat completion.
  name: Vercel AI Gateway Discover Model Then Complete
  slug: vercel-discover-model-then-complete-workflow
- description: List available models, confirm the embedding model is present, then create an embedding.
  name: Vercel AI Gateway Discover Model Then Embed
  slug: vercel-discover-model-then-embed-workflow
- description: Create an embedding for a document, then run a chat completion that summarizes it.
  name: Vercel AI Gateway Embed Then Summarize
  slug: vercel-embed-then-summarize-workflow
- description: Generate an app with v0, fetch its files, then explain the code via the AI Gateway.
  name: Vercel Generate App Then Explain Code
  slug: vercel-generate-app-then-explain-code-workflow
- description: Generate a web app from a prompt, then poll the chat until generated files are present.
  name: Vercel v0 Generate App Then Poll For Files
  slug: vercel-generate-app-then-poll-workflow
- description: Generate an app from a prompt, then send a follow-up refinement in the same chat.
  name: Vercel v0 Generate Then Refine App
  slug: vercel-generate-then-refine-app-workflow
- description: Generate an app, apply two sequential refinements, then read back the final chat.
  name: Vercel v0 Iterative App Build
  slug: vercel-iterative-app-build-workflow
- description: Draft an app spec via the AI Gateway, then feed that spec into v0 to generate the app.
  name: Vercel Draft Spec With Gateway Then Build App
  slug: vercel-prompt-with-gateway-then-build-app-workflow
- description: Fetch an existing chat to confirm it exists, then continue it with a refinement.
  name: Vercel v0 Resume And Refine Chat
  slug: vercel-resume-and-refine-chat-workflow
artifact_total: 64
asyncapis:
- description: AsyncAPI definition for Vercel's webhook surface. Vercel webhooks are HTTP POST deliveries from Vercel to a subscriber-configured endpoint URL registered either as an Account Webhook (Team Settings ->
  name: Vercel Webhooks
  slug: vercel-webhooks-asyncapi
collections:
- collection_type: postman
  name: Vercel AI Gateway Chat API
  slug: postman-vercel-chat-api
- collection_type: postman
  name: Vercel AI Gateway Chat Chats API
  slug: postman-vercel-chats-api
- collection_type: postman
  name: Vercel AI Gateway Chat Embeddings API
  slug: postman-vercel-embeddings-api
- collection_type: postman
  name: Vercel AI Gateway Chat Models API
  slug: postman-vercel-models-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vercel AI Gateway API
  slug: open-vercel-ai-gateway
- collection_type: open
  name: Vercel AI Gateway Chat API
  slug: open-vercel-chat-api
- collection_type: open
  name: Vercel AI Gateway Chat Chats API
  slug: open-vercel-chats-api
- collection_type: open
  name: Vercel AI Gateway Chat Embeddings API
  slug: open-vercel-embeddings-api
- collection_type: open
  name: Vercel AI Gateway Chat Models API
  slug: open-vercel-models-api
- collection_type: open
  name: Vercel v0 Platform API
  slug: open-vercel-v0-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vercel/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vercel-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vercel-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vercel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vercel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vercel-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-chat-completion-with-fallback-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-cost-routed-conversation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-discover-model-then-complete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-discover-model-then-embed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-embed-then-summarize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-generate-app-then-explain-code-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-generate-app-then-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-generate-then-refine-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-iterative-app-build-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-prompt-with-gateway-then-build-app-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/vercel-resume-and-refine-chat-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vercel
- group: docs
  title: ''
  type: Guide
  url: https://vercel.com/guides
- group: company
  title: ''
  type: Blog
  url: https://vercel.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://vercel.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://vercel.com/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://vercel.com/docs
- group: operate
  title: ''
  type: RateLimits
  url: https://vercel.com/docs/rest-api/reference#rate-limits
- group: design
  title: ''
  type: Versioning
  url: https://vercel.com/docs/rest-api/reference#versioning
- group: design
  title: ''
  type: Pagination
  url: https://vercel.com/docs/rest-api/reference#pagination
- group: operate
  title: ''
  type: Support
  url: https://vercel.com/help
- group: commercial
  title: ''
  type: Pricing
  url: https://vercel.com/pricing
- group: other
  title: ''
  type: Templates
  url: https://vercel.com/templates
- group: start
  title: ''
  type: Login
  url: https://vercel.com/login
- group: start
  title: ''
  type: Signup
  url: https://vercel.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vercel/vercel
- group: operate
  title: ''
  type: Forums
  url: https://community.vercel.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.vercel-status.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vercel.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vercel.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://security.vercel.com
- group: build
  title: ''
  type: CLI
  url: https://vercel.com/docs/cli
- group: build
  title: ''
  type: SDKs
  url: https://vercel.com/docs/ai-sdk
- group: auth
  title: ''
  type: Security
  url: https://vercel.com/docs/vercel-firewall
- group: docs
  title: ''
  type: Documentation
  url: https://vercel.com/docs/vercel-firewall/firewall-api
- group: docs
  title: ''
  type: OpenAPI
  url: https://openapi.vercel.sh/
- group: auth
  title: ''
  type: Security
  url: https://vercel.com/security
- group: docs
  title: ''
  type: APIReference
  url: https://vercel.com/docs/rest-api/reference
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/vercel/next-devtools-mcp
created: '2025-02-08'
description: Vercel is a cloud platform that helps developers build, deploy, and scale modern web applications quickly and efficiently. It provides an optimized hosting environment for frontend frameworks like Next.js (which it created), as well as other React, Vue, Angular, and static site projects. Vercel automates workflows for continuous deployment, edge caching, and serverless functions, so developers can push code changes and see them live almost instantly.
examples:
- key_count: 2
  name: Vercel Ai Gateway Chat Completion Example
  slug: vercel-ai-gateway-chat-completion-example
- key_count: 2
  name: Vercel Ai Gateway List Models Example
  slug: vercel-ai-gateway-list-models-example
- key_count: 2
  name: Vercel V0 Create Chat Example
  slug: vercel-v0-create-chat-example
features:
- 'Hobby plan (free, non-commercial): 100GB bandwidth, 1M edge req/mo'
- Pro plan at $20/dev/mo with $20 usage credits and 1TB bandwidth
- Enterprise with custom limits, SAML SSO, SOC 2/HIPAA
- Bandwidth overage at $0.15/GB above 1TB
- Edge requests overage at $2/1M above 10M included
- Function invocations at $0.60/1M
- Active CPU at $0.128/hour, Provisioned Memory at $0.0106/GB-hour
- Image Optimization with on-demand transformations
- Blob Storage, KV, Postgres, Edge Config
- REST API for projects, deployments, domains, env vars
- 'Deployment limits: 100/day Hobby, 6000/day Pro'
- 'Build concurrency: 1 Hobby, 12 Pro'
- GitHub/GitLab/Bitbucket auto-deploy
- Edge Functions and Edge Middleware
- Speed Insights and Web Analytics
- AI Gateway for LLM routing and observability
finops:
- name: Vercel Finops
  service_category: Edge Hosting
  slug: vercel-finops
graphqls:
- description: ''
  name: Vercel GraphQL API
  slug: vercel-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vercel.png
json_schemas:
- name: Vercel AI Gateway Chat Completion Request
  property_count: 7
  slug: vercel-chat-completion
json_structures:
- name: Vercel Chat Completion Structure
  property_count: 0
  slug: vercel-chat-completion-structure
jsonld:
- class_count: 30
  name: Vercel Context
  property_count: 2
  slug: vercel-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Vercel
nav: Providers
network: true
overview: 'Vercel publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Chat API, Chats API, and 2 more. Tagged areas include AI Gateways, Gateways, Observability, and Webhook.


  The Vercel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Vercel''s developer surface includes authentication, engineering blog, changelog, documentation, support, pricing, signup flow, and 38 more developer resources.'
plans:
- name: Vercel Plans Pricing
  plan_count: 3
  slug: vercel-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Vercel Rate Limits
  slug: vercel-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Vercel API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: vercel-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Vercel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vercel-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Vercel API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 6
  slug: vercel-rules
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 13.6
    contract_quality: 69.0
    developer_ergonomics: 66.7
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 52.6
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vercel/refs/heads/main/screenshots/vercel-2026-06-20T200923.png
security:
- kind: authentication
  name: Vercel Authentication
  slug: vercel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vercel Domain Security
  slug: vercel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vercel Vulnerability Disclosure
  slug: vercel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Vercel Trust Center
  slug: vercel-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: vercel
tags:
- AI Gateways
- Gateways
- Observability
- Webhook
---
