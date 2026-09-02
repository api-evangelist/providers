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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Hosted remote MCP server at https://mcp.samaya.ai/mcp that connects ChatGPT, Claude and other AI applications to Samaya''s expert financial research capabilities. Live and reachable: an anonymous tools'
  name: Samaya MCP Server
  slug: samaya-mcp-server
- description: Application GraphQL endpoint at https://api.samaya.ai/graphql/ serving the Samaya web app at app.samaya.ai. The API host root 302s to /graphql/, and an anonymous introspection POST returns HTTP 401 "U
  name: Samaya GraphQL API
  slug: samaya-graphql-api
- description: The Organizations API from Samaya AI — 1 operation(s) for organizations.
  name: Samaya AI Organizations API
  slug: samaya-ai-organizations-api
- description: The Teams API from Samaya AI — 2 operation(s) for teams.
  name: Samaya AI Teams API
  slug: samaya-ai-teams-api
- description: The Users API from Samaya AI — 1 operation(s) for users.
  name: Samaya AI Users API
  slug: samaya-ai-users-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://samaya.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api.samaya.ai/v1/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://samaya.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/samaya-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.samaya.ai/sign-in
- group: start
  title: ''
  type: Login
  url: https://app.samaya.ai/sign-in
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samaya.ai/privacy/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@samaya.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.samaya.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.samaya.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/samaya-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.samaya.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/samaya-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/samaya-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/samaya-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samaya-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/samaya-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/samaya-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/samaya-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/samaya-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/samaya-ai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/samaya-ai-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samaya-ai-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/samaya-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/samaya-ai-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/samaya-ai-public-api-overlay.yaml
- group: other
  title: ''
  type: Research
  url: https://samaya.ai/research
created: '2026-08-26'
description: 'Samaya AI builds domain-trained "Expert AI Agents" for financial services — investment research, client advisory and deal diligence — deployed across 10,000+ seats at bulge-bracket banks including Morgan Stanley. The platform ingests filings, broker research and a firm''s own proprietary documents, reconciles figures across them, and cites every number it returns. Founded in 2022 by Maithra Raghu (formerly Google Brain) and Fabio Petroni, it raised a $43.5M Series A led by NEA with NVentures (NVIDIA), Databricks Ventures, Eric Schmidt and Yann LeCun participating. Its machine surface is agent-first: a live OAuth-protected remote MCP server at mcp.samaya.ai that connects ChatGPT, Claude and other AI applications to Samaya''s research capabilities, plus a small "Samaya Public API" for org/team/user provisioning and an authenticated GraphQL endpoint behind the app.'
image: https://cdn.prod.website-files.com/68d859e7b33c148e692a2d17/68e48e3a26edcad357d09fa9_open-graph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Samaya MCP Server
  slug: samaya-mcp-server
- description: ''
  name: Samaya AI MCP Server
  slug: samaya-ai-mcp-server
modified: '2026-08-26'
name: Samaya AI
nav: Providers
network: true
overview: 'Samaya AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Organizations API, Teams API, and Users API. Tagged areas include Artificial Intelligence, Financial-Services, Investment Research, AI Agents, and MCP.


  Samaya AI''s developer surface includes API reference, engineering blog, signup flow, support, authentication, and 23 more developer resources.'
plans:
- name: Samaya Ai Plans Pricing
  plan_count: 0
  slug: samaya-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Samaya Ai Rate Limits
  slug: samaya-ai-rate-limits
scopes:
- name: Samaya Ai Scopes
  scope_count: 0
  slug: samaya-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Samaya Ai Authentication
  slug: samaya-ai-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Samaya Ai Domain Security
  slug: samaya-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Samaya Ai Trust Center
  slug: samaya-ai-trust-center
  summary_line: SOC 2
slug: samaya-ai
tags:
- Artificial Intelligence
- Financial-Services
- Investment Research
- AI Agents
- MCP
- agent-native
- Capital Markets
- Enterprise Search
- Retrieval
- GraphQL
website: https://samaya.ai/
---
