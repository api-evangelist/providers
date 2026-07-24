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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nas Academy Agentic Access
  operation_count: 36
  slug: nas-academy-agentic-access
  summary_line: 36 operations
api_count: 2
apis:
- description: Public machine-readable resources for AI assistants, crawlers, and agents.
  name: Nas.com (Nas Academy) AI discovery API
  slug: nas-academy-ai-discovery-api
- description: Public developer and integration guidance without private API contracts.
  name: Nas.com (Nas Academy) Developer discovery API
  slug: nas-academy-developer-discovery-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nas-academy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nas.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nas.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://nas.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nas.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://nas.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.nas.com/en
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nas-Company
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nas-academy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nas-academy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nas-academy-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/nas-academy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nas-academy-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nas-academy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nas-academy-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nas-academy-conventions.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nas-academy-discovery-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nas-academy-agentic-access.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nas-academy-data-model.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nas.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nas.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://nas.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://nas.com/signup
created: '2026-07-17'
description: 'Nas.com — formerly Nas.io and Nas Academy, launched by Nuseir Yassin of Nas Daily — is an AI-first business platform for sellers and creators. It turns a product photo or business idea into a storefront, marketing content, ad campaigns, leads, payments, sales, and owned community relationships. Nas.com exposes an unusually complete agent-native discovery surface: a public OpenAPI 3.1 discovery document, an official hosted MCP server (mcp.nas.com) behind OAuth 2.0, an A2A-style agent card, llms.txt / llms-full.txt, a RFC 9727 .well-known API catalog, schema.org entity JSON-LD, and published Agent Skills. The public discovery API is read-only and unauthenticated; authenticated business, member, product, and order context is available through the hosted MCP server.'
image: https://nas.com/images/nasLogo/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: nas-academy-mcp.yml
  slug: nas-academy-mcpyml
modified: '2026-07-20'
name: Nas.com (Nas Academy)
nav: Providers
network: true
overview: 'Nas.com (Nas Academy) publishes 2 APIs on the [APIs.io](https://apis.io/) network: AI discovery API and Developer discovery API. Tagged areas include Company, Creator Economy, Community, E-commerce, and AI.


  Nas.com (Nas Academy)''s developer surface includes documentation, API reference, pricing, support, authentication, getting-started guide, signup flow, and 17 more developer resources.'
random_paper: 20
scopes:
- name: Nas Academy Scopes
  scope_count: 6
  slug: nas-academy-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 46.9
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 43.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Nas Academy Authentication
  slug: nas-academy-authentication
  summary_line: none/oauth2 · 2 schemes
- kind: domain-security
  name: Nas Academy Domain Security
  slug: nas-academy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nas-academy
tags:
- Company
- Creator Economy
- Community
- E-commerce
- AI
- Agents
- MCP
- Online Courses
- Sellers
website: https://nas.com
---
