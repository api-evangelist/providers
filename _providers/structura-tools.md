---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server (streamable HTTP) that lets AI coding agents such as Claude Code, Codex, OpenCode and VS Code list, create, load, update, delete and share Structura projects, quer
  name: Structura MCP Server
  slug: structura-mcp-server
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/structura-tools/changelog/structura-tools-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/structura-tools-changelog.yml
- group: design
  href: https://artifacts.apis.io/structura-tools/conventions/structura-tools-conventions.yml
  title: ''
  type: Conventions
  url: conventions/structura-tools-conventions.yml
- group: auth
  href: https://artifacts.apis.io/structura-tools/authentication/structura-tools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/structura-tools-authentication.yml
- group: auth
  href: https://artifacts.apis.io/structura-tools/scopes/structura-tools-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/structura-tools-scopes.yml
- group: design
  href: https://artifacts.apis.io/structura-tools/lifecycle/structura-tools-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/structura-tools-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/structura-tools/conformance/structura-tools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/structura-tools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/structura-tools/llms/structura-tools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/structura-tools-llms.txt
- group: agent
  href: https://artifacts.apis.io/structura-tools/mcp/structura-tools-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/structura-tools-mcp.yml
- group: agent
  href: https://artifacts.apis.io/structura-tools/well-known/structura-tools-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/structura-tools-well-known.yml
- group: other
  href: https://artifacts.apis.io/structura-tools/hosts/structura-tools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/structura-tools-hosts.yml
- group: build
  href: https://artifacts.apis.io/structura-tools/integrations/structura-tools-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/structura-tools-integration-edges.yml
- group: auth
  href: https://artifacts.apis.io/structura-tools/security/structura-tools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/structura-tools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://structura.tools/
- group: docs
  title: ''
  type: Documentation
  url: https://structura.tools/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://structura.tools/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.structura.tools/
- group: other
  title: ''
  type: RSSFeed
  url: https://blog.structura.tools/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://structura.tools/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://structura.tools/legal/privacy
- group: other
  title: ''
  type: Team
  url: https://structura.tools/team
- group: operate
  title: ''
  type: ContactSales
  url: https://structura.tools/request-demo?source=enterprise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/structura-tools/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@structura-tools
- group: other
  title: ''
  type: X
  url: https://x.com/structura_tools
- group: other
  title: ''
  type: ParentCompany
  url: https://metadev.pro
created: '2026-11-03'
description: Structura is a web-based visual domain modeling and code generation tool built by Metadev (metadev.pro). Architecture teams and software factories design class/domain models graphically or textually, refine them with the Zeus voice/text AI assistant, validate them for compliance and architectural consistency, and export deterministic, production-ready code for stacks such as Angular, .NET and Java, including custom generators that codify a team's conventions and policies. Its documentation also describes an MCP server for connecting AI tools to models.
image: https://structura.tools/favicon.ico
layout: provider
mcp_servers:
- description: Official remote Model Context Protocol server from Structura (Metadev) that lets MCP clients (Claude Code, Codex, OpenCode, VS Code, Claude Desktop, MCP Inspector) manage Structura projects and models
  name: Structura MCP Server
  slug: structura-mcp-server
modified: '2026-11-03'
name: Structura
nav: Providers
network: true
overview: 'Structura is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code Generation, Domain Modeling, UML, and Software Architecture.


  Structura''s developer surface includes changelog, authentication, documentation, engineering blog, YouTube channel, and 20 more developer resources.'
plans:
- name: Structura Tools Plans Pricing
  plan_count: 0
  slug: structura-tools-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Structura Tools Rate Limits
  slug: structura-tools-rate-limits
scopes:
- name: Structura Tools Scopes
  scope_count: 2
  slug: structura-tools-scopes
  summary_line: 2 scopes
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Structura Tools Authentication
  slug: structura-tools-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Structura Tools Domain Security
  slug: structura-tools-domain-security
  summary_line: TLSv1.3
slug: structura-tools
tags:
- Company
- Code Generation
- Domain Modeling
- UML
- Software Architecture
- Low-Code
- Compliance
- MCP
website: https://structura.tools/
---
