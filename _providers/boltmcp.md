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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The MCP server the BoltMCP Helm chart deploys into the customer's own Kubernetes cluster. Customers define their own servers and tools through the BoltMCP dashboard, so the tool surface is tenant-defi
  name: BoltMCP MCP Server
  slug: boltmcp-mcp-server
- description: The internal REST API service (boltmcp-rest-api, container port 3003) that backs the BoltMCP dashboard and the deployed MCP servers. It is deliberately NOT given a public ingress hostname by the chart
  name: BoltMCP REST API
  slug: boltmcp-rest-api
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/boltmcp/security/boltmcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boltmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.boltmcp.io/
- group: docs
  title: ''
  type: Documentation
  url: https://install.boltmcp.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://install.boltmcp.io/docs/prerequisites
- group: company
  title: ''
  type: Blog
  url: https://www.boltmcp.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boltmcp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boltmcp
- group: company
  title: ''
  type: Twitter
  url: https://x.com/boltmcp
- group: build
  href: https://artifacts.apis.io/boltmcp/packages/boltmcp-packages.yml
  title: ''
  type: Packages
  url: packages/boltmcp-packages.yml
- group: agent
  href: https://artifacts.apis.io/boltmcp/llms/boltmcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boltmcp-llms.txt
- group: agent
  href: https://artifacts.apis.io/boltmcp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/boltmcp/authentication/boltmcp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boltmcp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/boltmcp/scopes/boltmcp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/boltmcp-scopes.yml
- group: design
  href: https://artifacts.apis.io/boltmcp/conventions/boltmcp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boltmcp-conventions.yml
- group: design
  href: https://artifacts.apis.io/boltmcp/errors/boltmcp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boltmcp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boltmcp/lifecycle/boltmcp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/boltmcp-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/boltmcp/changelog/boltmcp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/boltmcp-changelog.yml
- group: design
  href: https://artifacts.apis.io/boltmcp/conformance/boltmcp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boltmcp-conformance.yml
- group: start
  href: https://artifacts.apis.io/boltmcp/sandbox/boltmcp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/boltmcp-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/boltmcp/plans/boltmcp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boltmcp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/boltmcp/rate-limits/boltmcp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boltmcp-rate-limits.yml
created: '2026-09-14'
description: 'BoltMCP is a UK company (BoltMCP Limited) selling a self-hosted platform for creating and managing secured Model Context Protocol (MCP) servers inside an organization''s own infrastructure. A single Helm chart deploys the full stack into one Kubernetes namespace - a web dashboard, an internal REST API, a "gold image" MCP server, the MCP Inspector playground, and optional bundled PostgreSQL, Keycloak and HashiCorp Vault. The product''s pitch is token-efficient MCP: progressive disclosure and lazy tool registration instead of preloading every tool into an agent''s context, with tools composed declaratively from existing REST/gRPC APIs, company docs and API hubs. Auth, RBAC, secrets and observability are delegated to infrastructure the customer already runs. Nothing is operated by BoltMCP as a cloud service - there is no vendor-hosted API, no public sign-up and no published pricing; access is by design-partner arrangement to a preview release.'
image: https://www.boltmcp.io/boltmcp-logo/icon/icon-mark-light-original.png
layout: provider
mcp_servers:
- description: Remote MCP server at server.{global.domain} over HTTP requiring OAuth.
  name: BoltMCP MCP Server
  slug: boltmcp-mcp-server
modified: '2026-09-14'
name: BoltMCP
nav: Providers
network: true
overview: 'BoltMCP is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Agents, Artificial Intelligence, and Kubernetes.


  BoltMCP''s developer surface includes documentation, getting-started guide, engineering blog, authentication, changelog, sandbox, and 15 more developer resources.'
plans:
- name: Boltmcp Plans Pricing
  plan_count: 0
  slug: boltmcp-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Boltmcp Rate Limits
  slug: boltmcp-rate-limits
scopes:
- name: Boltmcp Scopes
  scope_count: 1
  slug: boltmcp-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 22.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boltmcp/boltmcp-2026-10-11T102524.png
security:
- kind: authentication
  name: Boltmcp Authentication
  slug: boltmcp-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Boltmcp Domain Security
  slug: boltmcp-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: install-boltmcp
  slug: boltmcp-install-boltmcp
slug: boltmcp
tags:
- Company
- MCP
- Agents
- Artificial Intelligence
- Kubernetes
- Self-Hosted
- Enterprise
- Identity
- Developer Tools
website: https://www.boltmcp.io/
---
