---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Abloatai Agentic Access
  operation_count: 32
  slug: abloatai-agentic-access
  summary_line: 32 operations · 19 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: A public, anonymous, stateless Streamable-HTTP MCP server Ablo runs on its own domain so an AI coding assistant writing an Ablo integration can search the real docs, inspect the actual SDK export surf
  name: Ablo Integration-Helper MCP Server
  slug: ablo-integration-helper-mcp-server
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The branches API from Ablo — 4 operation(s) for branches.
  name: Ablo Branches API
  slug: ablo-branches-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The claims API from Ablo — 7 operation(s) for claims.
  name: Ablo Claims API
  slug: ablo-claims-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The commits API from Ablo — 2 operation(s) for commits.
  name: Ablo Commits API
  slug: ablo-commits-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The credentials API from Ablo — 5 operation(s) for credentials.
  name: Ablo Credentials API
  slug: ablo-credentials-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The logs API from Ablo — 2 operation(s) for logs.
  name: Ablo Logs API
  slug: ablo-logs-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The models API from Ablo — 2 operation(s) for models.
  name: Ablo Models API
  slug: ablo-models-api
- baseURL: https://api.abloatai.com/api
  baseurl_source: declared
  description: The schema API from Ablo — 1 operation(s) for schema.
  name: Ablo Schema API
  slug: ablo-schema-api
artifact_total: 20
asyncapis:
- description: ''
  name: Abloatai Webhooks
  slug: abloatai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.abloatai.com/
- group: commercial
  title: ''
  type: License
  url: https://github.com/Abloatai/ablo/blob/main/LICENSE
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.abloatai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abloatai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.abloatai.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.abloatai.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://github.com/Abloatai/abloatai/issues
- group: company
  title: ''
  type: Blog
  url: https://www.abloatai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abloatai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Abloatai/ablo
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.abloatai.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.abloatai.com
- group: start
  title: ''
  type: Login
  url: https://dashboard.abloatai.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abloatai.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abloatai.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Abloatai/abloatai/blob/main/CHANGELOG.md
- group: operate
  href: https://artifacts.apis.io/abloatai/changelog/abloatai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/abloatai-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.abloatai.com/migration
- group: design
  href: https://artifacts.apis.io/abloatai/lifecycle/abloatai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/abloatai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/abloatai/authentication/abloatai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abloatai-authentication.yml
- group: design
  href: https://artifacts.apis.io/abloatai/conventions/abloatai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/abloatai-conventions.yml
- group: design
  href: https://artifacts.apis.io/abloatai/conventions/abloatai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/abloatai-conventions.yml
- group: design
  href: https://artifacts.apis.io/abloatai/errors/abloatai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/abloatai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/abloatai/data-model/abloatai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abloatai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/abloatai/rate-limits/abloatai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/abloatai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/abloatai/plans/abloatai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/abloatai-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/abloatai/packages/abloatai-packages.yml
  title: ''
  type: Packages
  url: packages/abloatai-packages.yml
- group: build
  href: https://artifacts.apis.io/abloatai/packages/abloatai-packages.yml
  title: ''
  type: SDKs
  url: packages/abloatai-packages.yml
- group: build
  href: https://artifacts.apis.io/abloatai/cli/abloatai-cli.yml
  title: ''
  type: CLI
  url: cli/abloatai-cli.yml
- group: start
  href: https://artifacts.apis.io/abloatai/sandbox/abloatai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/abloatai-sandbox.yml
- group: design
  href: https://artifacts.apis.io/abloatai/asyncapi/abloatai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/abloatai-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/abloatai/mcp/abloatai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abloatai-mcp.yml
- group: build
  href: https://artifacts.apis.io/abloatai/mcp/abloatai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abloatai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/abloatai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/abloatai/llms/abloatai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abloatai-llms.txt
- group: other
  href: https://artifacts.apis.io/abloatai/overlays/abloatai-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/abloatai-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/abloatai/conformance/abloatai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abloatai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abloatai/agentic-access/abloatai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abloatai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/abloatai/security/abloatai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abloatai-domain-security.yml
created: '2026-08-19'
description: 'Ablo is collaboration infrastructure for AI agents: one API that lets agents, apps and people claim, change and confirm the same database rows without clobbering each other. Rows stay in the customer''s own Postgres — Ablo holds only an ordered transaction log and the coordination state — while durable claims (leases with a wait-line, which make a second writer wait and then hand it the fresh row rather than lock), guarded idempotent writes with stale premises, atomic batch commits and signed webhook delivery turn concurrent multi-agent editing into something that serializes instead of racing. The surface is a 32-operation OpenAPI 3.1 REST API, a WSS realtime stream, a TypeScript SDK and CLI released in lockstep with the API, and two MCP servers.'
finops:
- has_sources: true
  method: derived
  name: Abloatai Finops
  primary_unit: operations
  service_category: ''
  slug: abloatai-finops
  template: false
image: https://www.abloatai.com/logo-black.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.abloatai.com; 17 tools listed.
  name: Ablo MCP Server
  slug: abloatai-mcp-yml
modified: '2026-08-19'
name: Ablo
nav: Providers
network: true
overview: 'Ablo publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Branches API, Claims API, Commits API, and 5 more. Tagged areas include Agent Infrastructure, multi-agent-coordination, concurrency-control, State Management, and Database.


  The Ablo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ablo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Abloatai Plans Pricing
  plan_count: 3
  slug: abloatai-plans-pricing
- name: Abloatai Price Estimates
  plan_count: 0
  slug: abloatai-price-estimates
random_paper: 13
rate_limits:
- limit_count: 6
  name: Abloatai Rate Limits
  slug: abloatai-rate-limits
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 80.4
    discoverability: 71.7
    operational_transparency: 68.4
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/abloatai/abloatai-2026-09-02T144107.png
security:
- kind: authentication
  name: Abloatai Authentication
  slug: abloatai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abloatai Domain Security
  slug: abloatai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Claim, read, write, release a shared row
  slug: abloatai-claim-read-write-release
- name: Commit a batch of changes atomically
  slug: abloatai-commit-batch-atomically
- name: Mint a scoped, expiring credential for an agent
  slug: abloatai-mint-scoped-agent-credential
slug: abloatai
tags:
- Agent Infrastructure
- multi-agent-coordination
- concurrency-control
- State Management
- Database
- PostgreSQL
- real-time-sync
- MCP
- Developer Tools
- backend-infrastructure
website: https://www.abloatai.com/
---
