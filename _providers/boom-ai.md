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
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 71.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Boom Ai Agentic Access
  operation_count: 80
  slug: boom-ai-agentic-access
  summary_line: 80 operations · 41 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The CDP Custom Objects API from Boom Ai — 5 operation(s) for cdp custom objects.
  name: Boom Ai CDP Custom Objects API
  slug: boom-ai-cdp-custom-objects-api
- description: The CDP Events API from Boom Ai — 3 operation(s) for cdp events.
  name: Boom Ai CDP Events API
  slug: boom-ai-cdp-events-api
- description: The CDP People API from Boom Ai — 4 operation(s) for cdp people.
  name: Boom Ai CDP People API
  slug: boom-ai-cdp-people-api
- description: The CDP Relationships API from Boom Ai — 4 operation(s) for cdp relationships.
  name: Boom Ai CDP Relationships API
  slug: boom-ai-cdp-relationships-api
- description: The CDP Sources API from Boom Ai — 1 operation(s) for cdp sources.
  name: Boom Ai CDP Sources API
  slug: boom-ai-cdp-sources-api
- description: The HTTP credentials API from Boom Ai — 1 operation(s) for http credentials.
  name: Boom Ai HTTP credentials API
  slug: boom-ai-http-credentials-api
- description: The Initiatives API from Boom Ai — 14 operation(s) for initiatives.
  name: Boom Ai Initiatives API
  slug: boom-ai-initiatives-api
- description: The Journeys API from Boom Ai — 16 operation(s) for journeys.
  name: Boom Ai Journeys API
  slug: boom-ai-journeys-api
- description: The Segments API from Boom Ai — 7 operation(s) for segments.
  name: Boom Ai Segments API
  slug: boom-ai-segments-api
- description: The WhatsApp templates API from Boom Ai — 3 operation(s) for whatsapp templates.
  name: Boom Ai WhatsApp templates API
  slug: boom-ai-whatsapp-templates-api
artifact_total: 30
asyncapis:
- description: ''
  name: Boom Ai Webhooks
  slug: boom-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boom CDP Custom Objects API
  slug: open-boom-ai-cdp-custom-objects-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Events API
  slug: open-boom-ai-cdp-events-api
- collection_type: open
  name: Boom CDP Custom Objects CDP People API
  slug: open-boom-ai-cdp-people-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Relationships API
  slug: open-boom-ai-cdp-relationships-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Sources API
  slug: open-boom-ai-cdp-sources-api
- collection_type: open
  name: Boom CDP Custom Objects HTTP credentials API
  slug: open-boom-ai-http-credentials-api
- collection_type: open
  name: Boom CDP Custom Objects Initiatives API
  slug: open-boom-ai-initiatives-api
- collection_type: open
  name: Boom CDP Custom Objects Journeys API
  slug: open-boom-ai-journeys-api
- collection_type: open
  name: Boom CDP Custom Objects Segments API
  slug: open-boom-ai-segments-api
- collection_type: open
  name: Boom CDP Custom Objects WhatsApp templates API
  slug: open-boom-ai-whatsapp-templates-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boom-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boom-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boom-ai-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.useboom.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useboom.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useboom.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useboom.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://useboom.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://useboom.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://useboom.ai/demo
- group: start
  title: ''
  type: Login
  url: https://app.useboom.ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@useboom.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drive.google.com/file/d/1SlTp1_QWhVASpbxncSj1NpmFqiiGBcF1/view
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drive.google.com/file/d/1ITWbsA8ZmyhinJYYr4ezRdhNe-MWQBC_/view
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/boom-ai-openapi-original.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boom-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boom-ai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/boom-ai-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/boom-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boom-ai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boom-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useboom.ai/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/boom-ai-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boom-ai-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/boom-ai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boom-ai-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/boom-ai-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boom-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/boom-ai-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/boom-ai-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boom-ai-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/boom-ai-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/boom-ai-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/boom-ai-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/boom-ai-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/boom-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.useboom.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BOOM-TML
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/BOOM-TML/skills
created: '2026-07-17'
description: Boom AI (useboom.ai) is a Y Combinator-backed (Fall 2025) San Francisco company building "an AI workforce for your customers" — autonomous agents that hold real, multi-turn conversations over SMS, email, WhatsApp, and phone in 50+ languages to run collections and payment recovery, churn recovery, retention monitoring, customer onboarding, sales qualification, and market research for e-commerce and B2B brands. Boom exposes one uniform public REST API — and a hosted MCP server over the same capabilities — covering a customer data platform (people, custom objects, behavioral events, relationships, sources), segments, initiatives and participants, and journey authoring. Authentication is a Bearer organization API key (boom_org_...); the API uses cursor pagination, 1,000 requests/minute rate limits with X-RateLimit-*/Retry-After signaling, and idempotent upsert plus up-to-1000-record batch endpoints.
image: https://useboom.ai/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: boom-ai-mcp.yml
  slug: boom-ai-mcpyml
modified: '2026-08-13'
name: Boom Ai
nav: Providers
network: true
overview: 'Boom Ai publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CDP Custom Objects API, CDP Events API, CDP People API, and 7 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Customer Engagement, and Customer Data Platform.


  The Boom Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Boom Ai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Boom Ai Plans Pricing
  plan_count: 4
  slug: boom-ai-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 2
  name: Boom Ai Rate Limits
  slug: boom-ai-rate-limits
scopes:
- name: Boom Ai Scopes
  scope_count: 7
  slug: boom-ai-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.4
  delta: 5.3
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 65.0
    developer_ergonomics: 71.4
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 47.4
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/screenshots/boom-ai-2026-07-25T203612.png
security:
- kind: authentication
  name: Boom Ai Authentication
  slug: boom-ai-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Boom Ai Domain Security
  slug: boom-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Boom Ai Trust Center
  slug: boom-ai-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: boom-ai
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Customer Engagement
- Customer Data Platform
- Messaging
- WhatsApp
- SMS
- Marketing Automation
- E-commerce
- Agents
- MCP
website: https://docs.useboom.ai
---
