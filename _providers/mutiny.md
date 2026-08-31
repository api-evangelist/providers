---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Mutiny''s first-party hosted, remote Model Context Protocol server — the company''s only machine-callable surface. It lets an MCP-compatible assistant (Claude web, Claude Desktop, Claude Code, ChatGPT) '
  name: Mutiny MCP Server
  slug: mutiny-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.mutinyhq.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mutiny-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mutiny-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mutiny-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mutiny-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mutiny-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mutiny-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mutiny-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/mutiny-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mutiny-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mutiny-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mutiny-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mutiny-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mutiny-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/mutiny-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.mutinyhq.com
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mutinyhq.com/articles/5003451538-connecting-mutiny-to-claude
- group: operate
  title: ''
  type: Support
  url: https://help.mutinyhq.com
- group: company
  title: ''
  type: Blog
  url: https://www.mutinyhq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mutinyhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mutinyhq.com/register
- group: start
  title: ''
  type: Login
  url: https://app.mutinyhq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutinyhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutinyhq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MutinyHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mutinyhq
created: '2026-07-17'
description: Mutiny (mutinyhq.com) is the GTM assistant built for customer-facing work and workflow automation — vertical AI built specifically for sales execution. Founded in 2018 as part of Y Combinator's S18 batch by Jaleh Rezaei (CEO) and Nikhil Mathew (CTO) and headquartered in New York City, Mutiny helps B2B revenue teams generate on-brand, deal-ready assets (self-updating deal rooms, pitch decks, pricing proposals, business cases, competitive comparisons, and AI-generated ABM campaigns) and automate the repetitive work around deals through agents, skills, and routines. The platform advertises Model Context Protocol (MCP) interoperability with Claude and other MCP-compatible tools and integrates with common GTM systems (CRM, email, the wider revenue stack). It is used by revenue teams at Snowflake, Uber, Rippling, GitLab, Figma, and BMC. Mutiny has raised $72M from Sequoia Capital, Insight Partners, Tiger Global, Cowboy Ventures, and Y Combinator. Mutiny's machine-callable surface
  is a first-party hosted, remote Model Context Protocol server at https://mcp.mutinyhq.com/mcp, protected by OAuth 2.1 with PKCE and dynamic client registration and publishing five scopes covering asset creation, publication, and content-library management. There is no public REST API, no OpenAPI, no GraphQL endpoint, and no developer portal — MCP is the whole contract. (Its earlier website-personalization / A/B-testing product has been retired, along with the React SDK that served it.)
image: https://framerusercontent.com/assets/Ec1hAhKLtluxlMfLydNP0NTrIA.png
layout: provider
mcp_servers:
- description: Mutiny ships a first-party hosted, remote MCP server so any MCP-compatible assistant (Claude web, Claude Desktop, Claude Code, ChatGPT) can create and publish Mutiny customer-facing assets, browse tem
  name: Mutiny MCP Server
  slug: mutiny-mcp-server
modified: '2026-08-13'
name: Mutiny
nav: Providers
network: true
overview: 'Mutiny publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Sales, Marketing, and Go-To-Market.


  Mutiny''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Mutiny Plans Pricing
  plan_count: 3
  slug: mutiny-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Mutiny Rate Limits
  slug: mutiny-rate-limits
scopes:
- name: Mutiny Scopes
  scope_count: 0
  slug: mutiny-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 37.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mutiny/refs/heads/main/screenshots/mutiny-2026-08-07T184451.png
security:
- kind: authentication
  name: Mutiny Authentication
  slug: mutiny-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mutiny Domain Security
  slug: mutiny-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutiny
tags:
- Company
- Enterprise
- Sales
- Marketing
- Go-To-Market
- Artificial Intelligence
- AI Agents
- Sales Enablement
- Account Based Marketing
- Workflow-Automation
- MCP
website: https://www.mutinyhq.com
---
