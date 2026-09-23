---
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: templated
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.8
  scored_at: '2026-09-23'
api_count: 2
apis:
- baseURL: https://api.airia.ai
  baseurl_source: declared
  description: 'The platform REST API behind the Airia console: agents (pipelines) and pipeline execution, projects, data sources and knowledge retrieval, deployments, MCP deployments/gateways, governance use cases a'
  name: Airia Web APIs
  slug: airia-web-apis
- description: Remote, OAuth-protected MCP Gateway (Streamable HTTP) that aggregates the MCP servers, SpecLink-converted OpenAPI tools, Agent Skills repositories and Airia-deployed agents an administrator has approv
  name: Airia MCP Gateway
  slug: airia-mcp-gateway
artifact_total: 10
asyncapis:
- description: ''
  name: Airia Webhooks
  slug: airia-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://airia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://airia.ai/docs/developers-hub/capabilities/intro
- group: docs
  title: ''
  type: Documentation
  url: https://airia.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.airia.ai/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://airia.ai/docs/home/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://airia.ai/docs/contact-us/support
- group: company
  title: ''
  type: Blog
  url: https://airia.com/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://airia.com/category/airia-news/
- group: other
  title: ''
  type: Leadership
  url: https://airia.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://airia.ai/docs/build/interface-options/usage_limits
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airia.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airia.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.airia.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airia-enterprise-ai/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Airia_AI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AiriaLLC
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/llms/airia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airia-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://airia.ai/docs/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://airia.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/well-known/airia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airia-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/packages/airia-packages.yml
  title: ''
  type: Packages
  url: packages/airia-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/packages/airia-packages.yml
  title: ''
  type: SDKs
  url: packages/airia-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/lifecycle/airia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airia-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/lifecycle/airia-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/airia-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/conformance/airia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airia-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/rate-limits/airia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airia-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/plans/airia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airia-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/security/airia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airia-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/asyncapi/airia-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/airia-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/errors/airia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airia-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/authentication/airia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airia-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/conventions/airia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airia-conventions.yml
- group: other
  title: ''
  type: DataResidency
  url: https://airia.ai/docs/developers-hub/capabilities/data-residency
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/regulatory/airia-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/airia-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airia/refs/heads/main/scopes/airia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/airia-scopes.yml
- group: start
  title: ''
  type: SignUp
  url: https://airia.com/creator-signup/
created: '2026-09-19'
description: 'Airia (Airia LLC, Atlanta) is an enterprise AI orchestration, security and governance platform: a no-code/low-code/pro-code agent builder, a model routing and cost gateway, an MCP Gateway that fronts 1,000+ app connectors and turns hosted OpenAPI specs and Agent Skills repositories into governed MCP tools, plus AI discovery (shadow-AI inventory), red teaming, guardrails, risk registry and use-case governance. The platform is driven by the Airia Web APIs at api.airia.ai (OpenAPI 3.0, 1,299 operations, X-API-Key auth), a Python SDK on PyPI, and a remote OAuth-protected MCP Gateway at mcp-gateway.airia.ai.'
image: https://airia.com/images/wp-content/uploads/2026/02/home-header-bg.jpg
layout: provider
mcp_servers:
- description: Airia operates a remote MCP Gateway as a first-class product surface, not a single fixed server. An administrator composes a Gateway from approved MCP servers (a catalogue of app connectors), SpecLink
  name: Airia MCP Gateway
  slug: airia-mcp-gateway
modified: '2026-09-19'
name: Airia
nav: Providers
network: true
overview: 'Airia publishes 1 API on the [APIs.io](https://apis.io/) network: Web APIs. Tagged areas include Company, Enterprise AI, AI Agents, AI Governance, and AI Security.


  The Airia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, YouTube channel, and 30 more developer resources.'
plans:
- name: Airia Plans Pricing
  plan_count: 3
  slug: airia-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Airia Rate Limits
  slug: airia-rate-limits
scopes:
- name: Airia Scopes
  scope_count: 0
  slug: airia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 54.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 65.8
  previous_composite: 59.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Airia Authentication
  slug: airia-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Airia Domain Security
  slug: airia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Airia Trust Center
  slug: airia-trust-center
  summary_line: trust center published
slug: airia
tags:
- Company
- Enterprise AI
- AI Agents
- AI Governance
- AI Security
- MCP
- MCP Gateway
- Agent Orchestration
- LLM Gateway
- AI Discovery
- Red Teaming
- Guardrails
- Knowledge Retrieval
- RAG
- Agent-Native
website: https://airia.com/
---
