---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Riskmodels App Agentic Access
  operation_count: 113
  slug: riskmodels-app-agentic-access
  summary_line: 113 operations · 31 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Compute-bearing 13F filer endpoints (D.8 Phase 1). Mirror the funds surface but partition by `filer_type × aum_tier` rather than `equity_style_9box`, and include a portfolio-derived 9-box style attrib
  name: riskmodels-app 13F Filers API
  slug: riskmodels-app-13f-filers-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Balance, billing, and invoice management.
  name: riskmodels-app Account API
  slug: riskmodels-app-account-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: API key provisioning and OAuth2 token management.
  name: riskmodels-app Authentication API
  slug: riskmodels-app-authentication-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: The Billing API from riskmodels-app — 1 operation(s) for billing.
  name: riskmodels-app Billing API
  slug: riskmodels-app-billing-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: AI marketplace compliance and discovery manifests.
  name: riskmodels-app Compliance API
  slug: riskmodels-app-compliance-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: The Deprecated API from riskmodels-app — 2 operation(s) for deprecated.
  name: riskmodels-app Deprecated API
  slug: riskmodels-app-deprecated-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Service discovery and capability manifests.
  name: riskmodels-app Discovery API
  slug: riskmodels-app-discovery-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: The Fundamentals API from riskmodels-app — 1 operation(s) for fundamentals.
  name: riskmodels-app Fundamentals API
  slug: riskmodels-app-fundamentals-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Compute-bearing fund endpoints. Latest metrics (Stage B.1) join `public.funds` with `public.funds_latest` and return a shaped response with bitemporal lineage. Per-fund time series, holdings, and hedg
  name: riskmodels-app Funds API
  slug: riskmodels-app-funds-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Raw-shape reads against the funds Supabase tables (`funds`, `funds_latest`). Latest knowledge-mode snapshot only — history reads via the per-fund Zarr endpoints in later stages. Public; soft Bearer au
  name: riskmodels-app Funds Data Plane API
  slug: riskmodels-app-funds-data-plane-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Model Context Protocol server endpoints for AI agents.
  name: riskmodels-app MCP API
  slug: riskmodels-app-mcp-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Live portfolio synchronization via Plaid Investments API.
  name: riskmodels-app Plaid Integration API
  slug: riskmodels-app-plaid-integration-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Data handling and privacy disclosure.
  name: riskmodels-app Privacy API
  slug: riskmodels-app-privacy-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: ERM3 factor hedge ratios, explained risk, and return decompositions.
  name: riskmodels-app Risk Metrics API
  slug: riskmodels-app-risk-metrics-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Ticker search, health, and service discovery.
  name: riskmodels-app Utility API
  slug: riskmodels-app-utility-api
- baseURL: https://riskmodels.app/api
  baseurl_source: declared
  description: Outbound webhook subscriptions (e.g. batch completion).
  name: riskmodels-app Webhooks API
  slug: riskmodels-app-webhooks-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/riskmodels-app/agentic-access/riskmodels-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/riskmodels-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/riskmodels-app/rate-limits/riskmodels-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/riskmodels-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/riskmodels-app/plans/riskmodels-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/riskmodels-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/riskmodels-app/rules/riskmodels-app-rules.yml
  title: ''
  type: Spectral
  url: rules/riskmodels-app-rules.yml
- group: design
  href: https://artifacts.apis.io/riskmodels-app/json-ld/riskmodels-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/riskmodels-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/riskmodels-app/vocabulary/riskmodels-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/riskmodels-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/riskmodels-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/riskmodels-app/data-model/riskmodels-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/riskmodels-app-data-model.yml
- group: build
  href: https://artifacts.apis.io/riskmodels-app/cli/riskmodels-app-cli.yml
  title: ''
  type: CLI
  url: cli/riskmodels-app-cli.yml
- group: operate
  href: https://artifacts.apis.io/riskmodels-app/changelog/riskmodels-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/riskmodels-app-changelog.yml
- group: auth
  href: https://artifacts.apis.io/riskmodels-app/authentication/riskmodels-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/riskmodels-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/riskmodels-app/errors/riskmodels-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/riskmodels-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/riskmodels-app/conformance/riskmodels-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/riskmodels-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/riskmodels-app/llms/riskmodels-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/riskmodels-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/riskmodels-app/mcp/riskmodels-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/riskmodels-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/riskmodels-app/well-known/riskmodels-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/riskmodels-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/riskmodels-app/hosts/riskmodels-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/riskmodels-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/riskmodels-app/vendors/riskmodels-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/riskmodels-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/riskmodels-app/packages/riskmodels-app-packages.yml
  title: ''
  type: Packages
  url: packages/riskmodels-app-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/BlueWaterCorp/RiskModels_API/tree/main/sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://riskmodels.app/docs/changelog
- group: auth
  href: https://artifacts.apis.io/riskmodels-app/security/riskmodels-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/riskmodels-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://riskmodels.app/
- group: docs
  title: ''
  type: Documentation
  url: https://riskmodels.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://riskmodels.app/api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://riskmodels.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://riskmodels.app/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlueWaterCorp
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://riskmodels.app/openapi.json
  - status: 401
    url: https://riskmodels.app/api/mcp
  - status: 200
    url: https://riskmodels.app/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: RiskModels provides a precision equity risk intelligence API that decomposes portfolio positions into market, sector, subsector, and residual risk, delivering model‑derived ETF hedge ratios per dollar of stock. The service offers real‑time risk analytics, historical data, and a suite of tools for developers, agents, and financial professionals, enabling data‑driven decision making without requiring extensive infrastructure.
image: https://riskmodels.app/transparent_logo.svg
json_schemas:
- name: ArtifactCapabilityResponse
  property_count: 10
  slug: riskmodels-app-artifact-capability-response
- name: DecomposeResponse
  property_count: 17
  slug: riskmodels-app-decompose-response
- name: FundHoldingsResponse
  property_count: 23
  slug: riskmodels-app-fund-holdings-response
- name: FundMetricsResponse
  property_count: 11
  slug: riskmodels-app-fund-metrics-response
- name: LstarResponse
  property_count: 16
  slug: riskmodels-app-lstar-response
- name: TickerReturnsResponseV3
  property_count: 16
  slug: riskmodels-app-ticker-returns-response-v3
jsonld:
- class_count: 99
  name: Riskmodels App Context
  property_count: 466
  slug: riskmodels-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at riskmodels.app.
  name: riskmodels-app MCP Server
  slug: riskmodels-app-mcp-yml
modified: '2026-10-31'
name: riskmodels-app
nav: Providers
network: true
overview: 'riskmodels-app publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including 13F Filers API, Account API, Authentication API, and 13 more. Tagged areas include Finance, Risk, Analytics, API, and Equity.


  The riskmodels-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  riskmodels-app''s developer surface includes CLI, changelog, authentication, documentation, API reference, pricing, and 22 more developer resources.'
plans:
- name: Riskmodels App Plans Pricing
  plan_count: 2
  slug: riskmodels-app-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Riskmodels App Rate Limits
  slug: riskmodels-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: riskmodels-app API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: riskmodels-app-rules
scopes:
- name: Riskmodels App Scopes
  scope_count: 0
  slug: riskmodels-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 92.1
    catalog_earned_first_party: 0.0
    catalog_gap: 22.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 40.0
    contract_governance: 79.1
    contract_quality: 61.9
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 40.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Riskmodels App Authentication
  slug: riskmodels-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Riskmodels App Domain Security
  slug: riskmodels-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: decompose-position
  slug: decompose-position
- name: get-fundamentals
  slug: get-fundamentals
- name: get-metrics
  slug: get-metrics
slug: riskmodels-app
tags:
- Finance
- Risk
- Analytics
- API
- Equity
website: https://riskmodels.app/
---
