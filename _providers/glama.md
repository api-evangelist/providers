---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Glama Agentic Access
  operation_count: 6
  slug: glama-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- description: Glama's MCP platform indexes open-source MCP servers and hosted connectors, offers an ephemeral MCP Inspector, hosts MCP servers on managed infrastructure, and proxies MCP traffic through the Glama Ga
  name: Glama MCP Marketplace & Gateway
  slug: mcp-platform
- description: The Auth API from Glama AI — 1 operation(s) for auth.
  name: Glama AI Auth API
  slug: glama-auth-api
- description: The Chat Completions API from Glama AI — 1 operation(s) for chat completions.
  name: Glama AI Chat Completions API
  slug: glama-chat-completions-api
- description: The Models API from Glama AI — 2 operation(s) for models.
  name: Glama AI Models API
  slug: glama-models-api
- description: The Observability API from Glama AI — 1 operation(s) for observability.
  name: Glama AI Observability API
  slug: glama-observability-api
- description: The Responses API from Glama AI — 1 operation(s) for responses.
  name: Glama AI Responses API
  slug: glama-responses-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Glama Gateway Auth API
  slug: open-glama-auth-api
- collection_type: open
  name: Glama Gateway Auth Chat Completions API
  slug: open-glama-chat-completions-api
- collection_type: open
  name: Glama Gateway Auth Models API
  slug: open-glama-models-api
- collection_type: open
  name: Glama Gateway Auth Observability API
  slug: open-glama-observability-api
- collection_type: open
  name: Glama Gateway Auth Responses API
  slug: open-glama-responses-api
- collection_type: open
  name: Glama Gateway API
  slug: open-glama
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glama-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glama-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glama-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://glama.ai
- group: agent
  title: ''
  type: MCPHub
  url: https://glama.ai/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://glama.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://glama.ai/blog
- group: start
  title: ''
  type: Signup
  url: https://glama.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glama.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glama.ai/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/glamaai
created: '2026-05-23'
description: Glama AI operates an MCP (Model Context Protocol) marketplace and gateway that aggregates more than 23,000 open-source MCP servers and 4,000 hosted connectors, each maintainer-verified, continuously rebuilt, and scored for quality and safety. Customers use Glama to discover MCP tools, test them in an ephemeral MCP Inspector sandbox, host servers on managed infrastructure, and route AI client traffic through the Glama Gateway with JSON-RPC logging, per-tool access control, managed OAuth, and usage analytics. The platform also exposes an AI Gateway that unifies access to OpenAI, Anthropic, Google, DeepSeek, Mistral, and xAI models. Pricing is a freemium SaaS with paid tiers at $9, $26, and $80/month that bundle AI credits and hosted MCP server slots; open-source MCP maintainers can host for free.
finops:
- name: Glama Finops
  service_category: API
  slug: glama-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glama.png
layout: provider
modified: '2026-05-23'
name: Glama AI
nav: Providers
network: true
overview: 'Glama AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Chat Completions API, Models API, and 2 more. Tagged areas include MCP, MCP Marketplace, MCP Gateway, MCP Hosting, and MCP Inspector.


  Glama AI''s developer surface includes authentication, pricing, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Glama Plans Pricing
  plan_count: 1
  slug: glama-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Glama Rate Limits
  slug: glama-rate-limits
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 46.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glama/refs/heads/main/screenshots/glama-2026-06-20T181857.png
security:
- kind: authentication
  name: Glama Authentication
  slug: glama-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glama Domain Security
  slug: glama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: glama
tags:
- MCP
- MCP Marketplace
- MCP Gateway
- MCP Hosting
- MCP Inspector
- AI Gateway
- LLM Gateway
- Connectors
- Authentication
- Observability
- Multi-Provider
website: https://glama.ai
---
