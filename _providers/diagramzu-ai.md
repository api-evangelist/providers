---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Bearer-token REST API for a DiagramZu space, covering diagrams, folders, versions, decks and public shares, documented on the DiagramZu docs page under "REST API" (base URL https://diagramzu.ai, paths
  name: DiagramZu REST API
  slug: diagramzu-rest-api
- description: Hosted Streamable HTTP MCP endpoint exposing DiagramZu's diagram tools to MCP clients, authenticated with a dz_live_ Bearer API token; its protected-resource document names https://api.diagramzu.ai as
  name: DiagramZu MCP Server
  slug: diagramzu-mcp-server
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/diagramzu-ai/plans/diagramzu-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diagramzu-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/diagramzu-ai/components/diagramzu-ai-components.yml
  title: ''
  type: Components
  url: components/diagramzu-ai-components.yml
- group: design
  href: https://artifacts.apis.io/diagramzu-ai/conventions/diagramzu-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/diagramzu-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/diagramzu-ai/authentication/diagramzu-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/diagramzu-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/diagramzu-ai/errors/diagramzu-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/diagramzu-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/diagramzu-ai/mcp/diagramzu-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/diagramzu-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/diagramzu-ai/well-known/diagramzu-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diagramzu-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/diagramzu-ai/hosts/diagramzu-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diagramzu-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/diagramzu-ai/integrations/diagramzu-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/diagramzu-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/diagramzu-ai/vendors/diagramzu-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diagramzu-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/diagramzu-ai/packages/diagramzu-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/diagramzu-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/diagramzu-ai/packages/diagramzu-ai-packages.yml
  title: ''
  type: Packages
  url: packages/diagramzu-ai-packages.yml
- group: auth
  href: https://artifacts.apis.io/diagramzu-ai/security/diagramzu-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diagramzu-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diagramzu.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://diagramzu.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://diagramzu.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://diagramzu.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://diagramzu.ai/sign-in
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/yenchieh/diagramzu-mcp
created: '2026-11-05'
description: DiagramZu is an MCP server plus shared workspace where Claude Code, Cursor, ChatGPT and any other MCP client write Mermaid diagrams directly. Its fourteen MCP tools search, create, read and update diagrams, browse folders, trace version history, build presentation decks, leave comments and analyze a rendered diagram for problems. Teams get a versioned share link they can open, comment on and embed with no login needed to view, and no LLM runs inside the app. A hosted MCP endpoint is documented at https://mcp.diagramzu.ai/mcp.
image: https://diagramzu.ai/og-image.png
layout: provider
mcp_servers:
- description: 'Official DiagramZu MCP server: hosted Streamable HTTP endpoint plus an npm stdio package (@diagramzu/mcp), letting MCP clients search, create, read and update Mermaid diagrams, folders, versions, deck'
  name: DiagramZu MCP Server
  slug: diagramzu-mcp-server
modified: '2026-11-05'
name: DiagramZu
nav: Providers
network: true
overview: 'DiagramZu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diagramming, Mermaid, MCP, and Developer Tools.


  DiagramZu''s developer surface includes authentication, documentation, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Diagramzu Ai Plans Pricing
  plan_count: 2
  slug: diagramzu-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Diagramzu Ai Rate Limits
  slug: diagramzu-ai-rate-limits
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Diagramzu Ai Authentication
  slug: diagramzu-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Diagramzu Ai Domain Security
  slug: diagramzu-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: diagramzu-ai
tags:
- Company
- Diagramming
- Mermaid
- MCP
- Developer Tools
- Documentation
- Collaboration
- AI Agents
website: https://diagramzu.ai/
---
