---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    idempotency: documented
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
  score: 30.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server (Streamable HTTP, JSON-RPC 2.0, MCP 2026-07-28 and 2025-11-25) through which AI agents operate Dilohost hosting. It exposes one tool per area, each with several ac
  name: Dilohost MCP Server
  slug: dilohost-mcp-server
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/dilohost-es/rate-limits/dilohost-es-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dilohost-es-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dilohost-es/plans/dilohost-es-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dilohost-es-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dilohost-es/conventions/dilohost-es-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dilohost-es-conventions.yml
- group: design
  href: https://artifacts.apis.io/dilohost-es/conventions/dilohost-es-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dilohost-es-conventions.yml
- group: auth
  href: https://artifacts.apis.io/dilohost-es/authentication/dilohost-es-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dilohost-es-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dilohost-es/scopes/dilohost-es-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dilohost-es-scopes.yml
- group: operate
  href: https://artifacts.apis.io/dilohost-es/lifecycle/dilohost-es-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dilohost-es-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dilohost-es/lifecycle/dilohost-es-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dilohost-es-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dilohost-es/errors/dilohost-es-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dilohost-es-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dilohost-es/conformance/dilohost-es-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dilohost-es-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dilohost-es/llms/dilohost-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dilohost-es-llms.txt
- group: agent
  href: https://artifacts.apis.io/dilohost-es/well-known/dilohost-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dilohost-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/dilohost-es/hosts/dilohost-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dilohost-es-hosts.yml
- group: build
  href: https://artifacts.apis.io/dilohost-es/integrations/dilohost-es-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/dilohost-es-integration-edges.yml
- group: company
  title: ''
  type: Website
  url: https://dilohost.es/
- group: docs
  title: ''
  type: Documentation
  url: https://dilohost.es/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dilohost.es/docs/inicio-rapido
- group: docs
  title: ''
  type: APIReference
  url: https://dilohost.es/docs/referencia/herramientas
- group: agent
  title: ''
  type: MCPServer
  url: https://dilohost.es/docs/referencia/servidor-mcp
- group: operate
  title: ''
  type: RateLimits
  url: https://dilohost.es/docs/referencia/limites
- group: commercial
  title: ''
  type: Pricing
  url: https://dilohost.es/docs/cuenta/planes
- group: operate
  title: ''
  type: Support
  url: https://dilohost.es/docs/ayuda/soporte
- group: operate
  title: ''
  type: StatusPage
  url: https://dilohost.es/estado
- group: company
  title: ''
  type: Blog
  url: https://dilohost.es/blog
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dilohost.es/llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://dilohost.es/register
- group: start
  title: ''
  type: Login
  url: https://dilohost.es/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dilohost.es/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dilohost.es/privacy-policy
- group: auth
  href: https://artifacts.apis.io/dilohost-es/security/dilohost-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dilohost-es-domain-security.yml
created: '2026-11-05'
description: Dilohost is a Spanish-language managed hosting service built to be operated entirely by AI agents over the Model Context Protocol (MCP). Users ask an agent such as Claude, Codex, ChatGPT, OpenCode, Cursor, GitHub Copilot or Gemini CLI to publish websites and server apps, create PostgreSQL databases, connect or buy domains and set up email mailboxes, and Dilohost carries it out with HTTPS, daily backups and servers in the European Union, with no control panel, servers or FTP to manage.
image: https://dilohost.es/images/dilohost-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Dilohost MCP Server
  slug: servidor-mcp
modified: '2026-11-05'
name: Dilohost
nav: Providers
network: true
overview: 'Dilohost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hosting, Web Hosting, MCP, and AI Agents.


  Dilohost''s developer surface includes authentication, documentation, getting-started guide, API reference, pricing, support, engineering blog, and 23 more developer resources.'
plans:
- name: Dilohost Es Plans Pricing
  plan_count: 4
  slug: dilohost-es-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 8
  name: Dilohost Es Rate Limits
  slug: dilohost-es-rate-limits
scopes:
- name: Dilohost Es Scopes
  scope_count: 1
  slug: dilohost-es-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 71.7
    operational_transparency: 55.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dilohost Es Authentication
  slug: dilohost-es-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Dilohost Es Domain Security
  slug: dilohost-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dilohost-es
tags:
- Company
- Hosting
- Web Hosting
- MCP
- AI Agents
- Database
- Domains
- Email
- European Union
website: https://dilohost.es/
---
