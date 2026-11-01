---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Alert configuration and monitoring
  name: Agnost AI Alerts API
  slug: agnost-ai-alerts-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: API key management
  name: Agnost AI API Keys API
  slug: agnost-ai-api-keys-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: OAuth authentication callbacks
  name: Agnost AI Auth API
  slug: agnost-ai-auth-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Stripe billing management
  name: Agnost AI Billing API
  slug: agnost-ai-billing-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: LLM-based classification operations
  name: Agnost AI Classification API
  slug: agnost-ai-classification-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: External integrations (Slack)
  name: Agnost AI Connections API
  slug: agnost-ai-connections-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Conversation message and span retrieval
  name: Agnost AI Conversations API
  slug: agnost-ai-conversations-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Analytics and metrics for the dashboard
  name: Agnost AI Dashboard API
  slug: agnost-ai-dashboard-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: First-run helpers used during organization setup
  name: Agnost AI Onboarding API
  slug: agnost-ai-onboarding-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Organization management
  name: Agnost AI Organizations API
  slug: agnost-ai-organizations-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Event ingestion endpoints used by SDKs
  name: Agnost AI SDK API
  slug: agnost-ai-sdk-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Sentiment and intent analysis
  name: Agnost AI Sentiments API
  slug: agnost-ai-sentiments-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Standard Operating Procedures
  name: Agnost AI SOPs API
  slug: agnost-ai-sops-api
- baseURL: https://api.agnost.ai
  baseurl_source: declared
  description: Health checks, webhooks, internal endpoints
  name: Agnost AI System API
  slug: agnost-ai-system-api
artifact_total: 39
collections:
- collection_type: open
  name: Agnost AI Alerts API
  slug: open-agnost-ai-alerts-api
- collection_type: open
  name: Agnost AI Alerts API Keys API
  slug: open-agnost-ai-api-keys-api
- collection_type: open
  name: Agnost AI Alerts Auth API
  slug: open-agnost-ai-auth-api
- collection_type: open
  name: Agnost AI Alerts Billing API
  slug: open-agnost-ai-billing-api
- collection_type: open
  name: Agnost AI Alerts Classification API
  slug: open-agnost-ai-classification-api
- collection_type: open
  name: Agnost AI Alerts Connections API
  slug: open-agnost-ai-connections-api
- collection_type: open
  name: Agnost AI Alerts Conversations API
  slug: open-agnost-ai-conversations-api
- collection_type: open
  name: Agnost AI Alerts Dashboard API
  slug: open-agnost-ai-dashboard-api
- collection_type: open
  name: Agnost AI Alerts Onboarding API
  slug: open-agnost-ai-onboarding-api
- collection_type: open
  name: Agnost AI Alerts Organizations API
  slug: open-agnost-ai-organizations-api
- collection_type: open
  name: Agnost AI Alerts SDK API
  slug: open-agnost-ai-sdk-api
- collection_type: open
  name: Agnost AI Alerts Sentiments API
  slug: open-agnost-ai-sentiments-api
- collection_type: open
  name: Agnost AI Alerts SOPs API
  slug: open-agnost-ai-sops-api
- collection_type: open
  name: Agnost AI Alerts System API
  slug: open-agnost-ai-system-api
common:
- group: commercial
  href: https://artifacts.apis.io/agnost-ai/plans/agnost-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agnost-ai-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://agnost.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://agnost.ai/rss.xml
- group: other
  href: https://artifacts.apis.io/agnost-ai/capabilities/agnost-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agnost-ai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.agnost.ai/
- group: other
  href: https://artifacts.apis.io/agnost-ai/overlays/agnost-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agnost-ai-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agnost.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agnost.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agnost.ai/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agnost.ai/quickstart
- group: build
  title: ''
  type: SDKs
  url: https://docs.agnost.ai/sdks
- group: company
  title: ''
  type: Blog
  url: https://agnost.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.agnost.ai/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agnostai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agnost.ai
- group: operate
  title: ''
  type: Support
  url: https://call.agnost.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://agnost.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.agnost.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agnost.ai/terms
- group: auth
  title: ''
  type: Compliance
  url: https://trust.agnost.ai
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.agnost.ai/mcp
- group: build
  href: https://artifacts.apis.io/agnost-ai/packages/agnost-ai-packages.yml
  title: ''
  type: Packages
  url: packages/agnost-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/agnost-ai/packages/agnost-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/agnost-ai-packages.yml
- group: agent
  href: https://artifacts.apis.io/agnost-ai/mcp/agnost-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agnost-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agnost-ai/well-known/agnost-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agnost-ai-well-known.yml
- group: agent
  href: https://artifacts.apis.io/agnost-ai/llms/agnost-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agnost-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/agnost-ai/authentication/agnost-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agnost-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agnost-ai/scopes/agnost-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agnost-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/agnost-ai/conformance/agnost-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agnost-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/agnost-ai/errors/agnost-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agnost-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agnost-ai/lifecycle/agnost-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agnost-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agnost-ai/conventions/agnost-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agnost-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/agnost-ai/data-model/agnost-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agnost-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agnost-ai/security/agnost-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agnost-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/agnost-ai/security/agnost-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agnost-ai-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/agnost-ai/skills/agnost-ai-published.md
  title: ''
  type: AgentSkill
  url: skills/agnost-ai-published.md
- group: agent
  href: https://artifacts.apis.io/agnost-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Agnost AI is a production monitoring and product-analytics platform for teams building chat and voice AI agents. It continuously reads production agent conversations, MCP tool calls, and OpenTelemetry traces, clusters recurring intents, feature requests, frustration, and failure patterns, and catches agent failures that offline evals miss. It then turns the highest-impact patterns into reviewed fixes, including pull requests against prompts, tools, and agent harnesses. Agnost is OpenTelemetry-native, works with any LLM and framework, and ships SDKs for Python and TypeScript conversation tracking, MCP-server analytics (Python, TypeScript, Go), plus a hosted OAuth-protected MCP server for querying your dashboard from Claude Desktop, Cursor, and any MCP client. Founded in 2025 and part of Y Combinator's Summer 2026 (S26) batch.
finops:
- has_sources: true
  method: derived
  name: Agnost Ai Finops
  primary_unit: events
  service_category: ''
  slug: agnost-ai-finops
  template: false
image: https://agnost.ai/logo.png
layout: provider
mcp_servers:
- description: Hosted, OAuth 2.1-protected MCP server (streamable-HTTP) for querying your Agnost dashboard from Claude Desktop, Cursor, and any MCP client.
  name: Agnost MCP Server
  slug: agnost-mcp-server
modified: '2026-10-06'
name: Agnost AI
nav: Providers
network: true
overview: 'Agnost AI publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, API Keys API, Auth API, and 11 more. Tagged areas include Company, AI Agents, Agent Analytics, Observability, and OpenTelemetry.


  Agnost AI''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Agnost Ai Plans Pricing
  plan_count: 4
  slug: agnost-ai-plans-pricing
- name: Agnost Ai Price Estimates
  plan_count: 0
  slug: agnost-ai-price-estimates
random_paper: 11
scopes:
- name: Agnost Ai Scopes
  scope_count: 1
  slug: agnost-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 26.3
  previous_composite: 49.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agnost-ai/agnost-ai-2026-07-25T195316.png
security:
- kind: authentication
  name: Agnost Ai Authentication
  slug: agnost-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Agnost Ai Domain Security
  slug: agnost-ai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Agnost Ai Trust Center
  slug: agnost-ai-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: Capture an agent conversation into Agnost
  slug: agnost-ai-capture-conversation
- name: agnost-ai
  slug: agnost-ai-published
- name: Triage agent failures in Agnost
  slug: agnost-ai-triage-failures
slug: agnost-ai
tags:
- Company
- AI Agents
- Agent Analytics
- Observability
- OpenTelemetry
- MCP
- Conversational AI
- Monitoring
- Developer Tools
- Analytics
website: https://www.agnost.ai/
---
