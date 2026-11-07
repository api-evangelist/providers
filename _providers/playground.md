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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL gateway providing stateful mock query and mutation access to the same dataset, with an interactive explorer.
  name: Playground GraphQL API
  slug: playground-graphql-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Auth API from Playground API — Free Stateful Mock REST & GraphQL Service — 4 operation(s) for auth.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Auth API
  slug: playground-auth-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Avatars API from Playground API — Free Stateful Mock REST & GraphQL Service — 1 operation(s) for avatars.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Avatars API
  slug: playground-avatars-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Comments API from Playground API — Free Stateful Mock REST & GraphQL Service — 2 operation(s) for comments.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Comments API
  slug: playground-comments-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Custom API from Playground API — Free Stateful Mock REST & GraphQL Service — 4 operation(s) for custom.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Custom API
  slug: playground-custom-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Posts API from Playground API — Free Stateful Mock REST & GraphQL Service — 2 operation(s) for posts.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Posts API
  slug: playground-posts-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Session API from Playground API — Free Stateful Mock REST & GraphQL Service — 3 operation(s) for session.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Session API
  slug: playground-session-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Thumbnails API from Playground API — Free Stateful Mock REST & GraphQL Service — 1 operation(s) for thumbnails.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Thumbnails API
  slug: playground-thumbnails-api
- baseURL: https://playground.nileslabs.com/api/v1
  baseurl_source: declared
  description: The Users API from Playground API — Free Stateful Mock REST & GraphQL Service — 2 operation(s) for users.
  name: Playground API — Free Stateful Mock REST & GraphQL Service Users API
  slug: playground-users-api
- baseURL: https://playground.nileslabs.com/api/v1/graphql
  baseurl_source: declared
  description: The To Dos API from Playground API — Free Stateful Mock REST & GraphQL Service — 2 operation(s) for to dos.
  name: Playground API — Free Stateful Mock REST & GraphQL Service To Dos API
  slug: playground-to-dos-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Blog
  url: https://playground.nileslabs.com/blog
- group: company
  title: ''
  type: Website
  url: https://playground.nileslabs.com
- group: start
  title: ''
  type: GettingStarted
  url: https://playground.nileslabs.com/docs/quickstart
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/nileslabs/playground_api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nileslabs
- group: agent
  href: https://artifacts.apis.io/playground/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/playground/overlays/playground-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/playground-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/playground/mcp/playground-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/playground-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/playground/mcp/playground-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/playground-mcp.yml
- group: build
  href: https://artifacts.apis.io/playground/packages/playground-packages.yml
  title: ''
  type: Packages
  url: packages/playground-packages.yml
- group: start
  href: https://artifacts.apis.io/playground/sandbox/playground-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/playground-sandbox.yml
- group: design
  href: https://artifacts.apis.io/playground/conformance/playground-conformance.yml
  title: ''
  type: Conformance
  url: conformance/playground-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/playground/plans/playground-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/playground-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/playground/rate-limits/playground-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/playground-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/playground/data-model/playground-data-model.yml
  title: ''
  type: DataModel
  url: data-model/playground-data-model.yml
- group: design
  href: https://artifacts.apis.io/playground/lifecycle/playground-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/playground-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/playground/errors/playground-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/playground-problem-types.yml
- group: design
  href: https://artifacts.apis.io/playground/conventions/playground-conventions.yml
  title: ''
  type: Conventions
  url: conventions/playground-conventions.yml
- group: auth
  href: https://artifacts.apis.io/playground/authentication/playground-authentication.yml
  title: ''
  type: Authentication
  url: authentication/playground-authentication.yml
- group: auth
  href: https://artifacts.apis.io/playground/security/playground-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playground-domain-security.yml
created: '2026-09-14'
description: A free, zero-configuration, stateful mock REST and GraphQL API sandbox by Nilesh Kumar / Niles Labs. Unlike static mock APIs, it provides stateful per-session virtual mutation overlays where POST/PUT/PATCH/DELETE mutations persist across GET queries within a session, while the global baseline dataset remains read-only. Includes chaos/network simulation, dynamic collections, avatar/thumbnail generators, and simulated JWT auth loops. MIT licensed, no auth or signup required.
layout: provider
mcp_servers:
- description: ''
  name: Playground API — Free Stateful Mock REST & GraphQL Service MCP Server
  slug: playground-mcp-yml
modified: '2026-10-06'
name: Playground API — Free Stateful Mock REST & GraphQL Service
nav: Providers
network: true
overview: 'Playground API — Free Stateful Mock REST & GraphQL Service publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Avatars API, Comments API, and 7 more. Tagged areas include Developer Tools, Testing, Mock API, api-sandbox, and REST.


  The Playground API — Free Stateful Mock REST & GraphQL Service catalog on APIs.io includes 1 Spectral governance ruleset.


  Playground API — Free Stateful Mock REST & GraphQL Service''s developer surface includes engineering blog, getting-started guide, sandbox, authentication, and 16 more developer resources.'
plans:
- name: Playground Plans Pricing
  plan_count: 1
  slug: playground-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Playground Rate Limits
  slug: playground-rate-limits
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Playground API — Free Stateful Mock REST & GraphQL Service API Rules
  rule_count: 40
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 4
  slug: playground-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 44.5
    catalog_earned_first_party: 8.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 48.2
    developer_ergonomics: 49.4
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 33.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/playground/playground-2026-10-11T112622.png
security:
- kind: authentication
  name: Playground Authentication
  slug: playground-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Playground Domain Security
  slug: playground-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: playground-chaos-simulation
  slug: playground-chaos-simulation
- name: playground-parallel-e2e
  slug: playground-parallel-e2e
- name: playground-stateful-crud
  slug: playground-stateful-crud
slug: playground
tags:
- Developer Tools
- Testing
- Mock API
- api-sandbox
- REST
- GraphQL
- E2E Testing
website: https://playground.nileslabs.com
---
