---
access_model:
  confidence: medium
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 3
  name: Monid Agentic Access
  operation_count: 33
  slug: monid-agentic-access
  summary_line: 33 operations · 7 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The API Keys API from Monid — 2 operation(s) for api keys.
  name: Monid API Keys API
  slug: monid-api-keys-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Auth API from Monid — 2 operation(s) for auth.
  name: Monid Auth API
  slug: monid-auth-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Controls API from Monid — 6 operation(s) for controls.
  name: Monid Controls API
  slug: monid-controls-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Discover API from Monid — 1 operation(s) for discover.
  name: Monid Discover API
  slug: monid-discover-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Endpoints API from Monid — 1 operation(s) for endpoints.
  name: Monid Endpoints API
  slug: monid-endpoints-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Inspect API from Monid — 1 operation(s) for inspect.
  name: Monid Inspect API
  slug: monid-inspect-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Public Registry API from Monid — 5 operation(s) for public registry.
  name: Monid Public Registry API
  slug: monid-public-registry-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Resources API from Monid — 5 operation(s) for resources.
  name: Monid Resources API
  slug: monid-resources-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Runs API from Monid — 5 operation(s) for runs.
  name: Monid Runs API
  slug: monid-runs-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Wallet API from Monid — 2 operation(s) for wallet.
  name: Monid Wallet API
  slug: monid-wallet-api
- baseURL: https://api.monid.ai
  baseurl_source: declared
  description: The Identities API from Monid — 2 operation(s) for identities.
  name: Monid Identities API
  slug: monid-identities-api
- description: Pay-per-run execution surface on x402.monid.ai — POST /v1/run answers HTTP 402 with an accepts[] array of CAIP-2 networks (Base eip155:8453, Monad eip155:143), the client signs a USDC authorization an
  name: Monid x402 Run API
  slug: monid-x402-run-api
artifact_total: 63
collections:
- collection_type: open
  name: Monid API
  slug: open-monid
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/rate-limits/monid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monid-rate-limits.yml
- group: company
  title: ''
  type: Newsroom
  url: https://monid.ai/tools/news
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/plans/monid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monid-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/rules/monid-rules.yml
  title: ''
  type: Spectral
  url: rules/monid-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/json-ld/monid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monid-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/vocabulary/monid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monid-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/hosts/monid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/vendors/monid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monid-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://monid.ai/rss.xml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/capabilities/monid-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/monid-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/agentic-access/monid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monid-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/authentication/monid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monid-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/scopes/monid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/monid-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/security/monid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monid-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/mcp/monid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/monid-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/errors/monid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/monid-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/conventions/monid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/monid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/conformance/monid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monid-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/well-known/monid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monid-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/lifecycle/monid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/monid-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monid.ai
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/data-model/monid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monid-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/overlays/monid-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/monid-openapi-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/cli/monid-cli.yml
  title: ''
  type: CLI
  url: cli/monid-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/llms/monid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monid-llms.txt
- group: company
  title: ''
  type: Website
  url: https://monid.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://monid.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://monid.ai/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://monid.ai/docs/guide/quickstart-api.md
- group: company
  title: ''
  type: Blog
  url: https://monid.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monid-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.monid.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://monid.ai/docs/guide/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monid.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monid.ai/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/rQzztcgJV8
created: '2026-07-23'
description: Monid is a San Francisco-based data-access and agent-tool integration platform that gives developers and AI agents on-demand, pay-per-use access to hundreds of web data endpoints and 1,300+ tools across 13+ providers (Semrush, Apollo, ElevenLabs, web scrapers, and more) through a single integration. Agents discover, inspect, compare, and execute tools at runtime and pay only for actual usage, with a unified balance and no per-tool API key management or subscriptions. Monid exposes its catalog through four connection methods — an MCP (Model Context Protocol) server for Claude and other AI assistants, a Skill integration for Claude Code and Cursor, a CLI for shell access, and an HTTP API for programmatic integration — with OAuth, proxy, and master API key options for embedded use.
image: https://monid.ai/share-card.png
json_schemas:
- name: ApiKey
  property_count: 12
  slug: monid-api-key
- name: DiscoverCategoriesRequest
  property_count: 6
  slug: monid-discover-categories-request
- name: DiscoverEndpointsRequest
  property_count: 8
  slug: monid-discover-endpoints-request
- name: DiscoverProvidersRequest
  property_count: 6
  slug: monid-discover-providers-request
- name: DiscoverRequest
  property_count: 8
  slug: monid-discover-request
- name: ExternalResourceDetail
  property_count: 4
  slug: monid-external-resource-detail
- name: IdentityLinkCompleteRequest
  property_count: 2
  slug: monid-identity-link-complete-request
- name: IdentityLinkCompleteResponse
  property_count: 4
  slug: monid-identity-link-complete-response
- name: IdentityLinkStartRequest
  property_count: 1
  slug: monid-identity-link-start-request
- name: IdentityLinkStartResponse
  property_count: 2
  slug: monid-identity-link-start-response
- name: InspectRequest
  property_count: 2
  slug: monid-inspect-request
- name: InspectResponse
  property_count: 14
  slug: monid-inspect-response
- name: ProviderResourcesResponse
  property_count: 1
  slug: monid-provider-resources-response
- name: PublicCategoriesResponse
  property_count: 2
  slug: monid-public-categories-response
- name: PublicEndpointDetail
  property_count: 0
  slug: monid-public-endpoint-detail
- name: PublicEndpointInfo
  property_count: 10
  slug: monid-public-endpoint-info
- name: PublicProviderEntry
  property_count: 6
  slug: monid-public-provider-entry
- name: PublicRegistryStats
  property_count: 2
  slug: monid-public-registry-stats
- name: ResourceEvent
  property_count: 6
  slug: monid-resource-event
- name: ResourceReleaseAccepted
  property_count: 3
  slug: monid-resource-release-accepted
- name: Resource
  property_count: 35
  slug: monid-resource
- name: RunAccepted
  property_count: 7
  slug: monid-run-accepted
- name: RunBlocked
  property_count: 10
  slug: monid-run-blocked
- name: RunCompleted
  property_count: 15
  slug: monid-run-completed
- name: RunListItem
  property_count: 16
  slug: monid-run-list-item
- name: RunRequest
  property_count: 3
  slug: monid-run-request
- name: Run
  property_count: 22
  slug: monid-run
- name: ScopeCatalog
  property_count: 1
  slug: monid-scope-catalog
- name: UpdateApiKeyRequest
  property_count: 1
  slug: monid-update-api-key-request
- name: WalletBalanceResponse
  property_count: 3
  slug: monid-wallet-balance-response
- name: WalletTopupConfigResponse
  property_count: 9
  slug: monid-wallet-topup-config-response
- name: WalletTopupRequest
  property_count: 5
  slug: monid-wallet-topup-request
- name: WalletTopupSessionResponse
  property_count: 3
  slug: monid-wallet-topup-session-response
- name: WhoamiResponse
  property_count: 5
  slug: monid-whoami-response
- name: WorkspaceBudgetPatchRequest
  property_count: 2
  slug: monid-workspace-budget-patch-request
- name: WorkspaceBudgetRun
  property_count: 9
  slug: monid-workspace-budget-run
- name: WorkspaceBudget
  property_count: 12
  slug: monid-workspace-budget
- name: WorkspaceListResponse
  property_count: 1
  slug: monid-workspace-list-response
- name: WorkspaceRunCapPatchRequest
  property_count: 2
  slug: monid-workspace-run-cap-patch-request
- name: WorkspaceRunCapRun
  property_count: 7
  slug: monid-workspace-run-cap-run
- name: WorkspaceRunCap
  property_count: 7
  slug: monid-workspace-run-cap
jsonld:
- class_count: 71
  name: Monid Context
  property_count: 189
  slug: monid-context
layout: provider
mcp_servers:
- description: Official hosted Monid MCP server (Streamable HTTP). Gives an AI client tools to discover, inspect, and run hundreds of data endpoints across the web, with pay-per-use billing against a Monid workspace
  name: Monid MCP Server
  slug: monid-mcp-server
modified: '2026-10-07'
name: Monid
nav: Providers
network: true
overview: 'Monid publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Auth API, Controls API, and 9 more. Tagged areas include Company, Agents, MCP, Tools, and Data.


  The Monid catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Monid''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, signup flow, and 31 more developer resources.'
plans:
- name: Monid Plans Pricing
  plan_count: 1
  slug: monid-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Monid Rate Limits
  slug: monid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Monid API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 3
  slug: monid-rules
scopes:
- name: Monid Scopes
  scope_count: 5
  slug: monid-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 52.6
    contract_governance: 35.6
    contract_quality: 63.6
    developer_ergonomics: 71.4
    discoverability: 76.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/monid/refs/heads/main/screenshots/monid-2026-08-07T184201.png
security:
- kind: authentication
  name: Monid Authentication
  slug: monid-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Monid Domain Security
  slug: monid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: monid
tags:
- Company
- Agents
- MCP
- Tools
- Data
- API Marketplace
website: https://monid.ai
---
