---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Stackresolve Dev Agentic Access
  operation_count: 12
  slug: stackresolve-dev-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Account API from stackresolve-dev — 1 operation(s) for account.
  name: stackresolve-dev Account API
  slug: stackresolve-dev-account-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Audit API from stackresolve-dev — 1 operation(s) for audit.
  name: stackresolve-dev Audit API
  slug: stackresolve-dev-audit-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Company API from stackresolve-dev — 1 operation(s) for company.
  name: stackresolve-dev Company API
  slug: stackresolve-dev-company-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Compare API from stackresolve-dev — 1 operation(s) for compare.
  name: stackresolve-dev Compare API
  slug: stackresolve-dev-compare-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Competitors API from stackresolve-dev — 1 operation(s) for competitors.
  name: stackresolve-dev Competitors API
  slug: stackresolve-dev-competitors-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Find Tools API from stackresolve-dev — 1 operation(s) for find tools.
  name: stackresolve-dev Find Tools API
  slug: stackresolve-dev-find-tools-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Plans API from stackresolve-dev — 1 operation(s) for plans.
  name: stackresolve-dev Plans API
  slug: stackresolve-dev-plans-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Pricing API from stackresolve-dev — 1 operation(s) for pricing.
  name: stackresolve-dev Pricing API
  slug: stackresolve-dev-pricing-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Profile API from stackresolve-dev — 1 operation(s) for profile.
  name: stackresolve-dev Profile API
  slug: stackresolve-dev-profile-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Registry API from stackresolve-dev — 1 operation(s) for registry.
  name: stackresolve-dev Registry API
  slug: stackresolve-dev-registry-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Research API from stackresolve-dev — 1 operation(s) for research.
  name: stackresolve-dev Research API
  slug: stackresolve-dev-research-api
- baseURL: https://api.stackresolve.dev
  baseurl_source: declared
  description: The Search API from stackresolve-dev — 1 operation(s) for search.
  name: stackresolve-dev Search API
  slug: stackresolve-dev-search-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/stackresolve-dev/agentic-access/stackresolve-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stackresolve-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/stackresolve-dev/rate-limits/stackresolve-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackresolve-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stackresolve-dev/plans/stackresolve-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackresolve-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/rules/stackresolve-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/stackresolve-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/json-ld/stackresolve-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/stackresolve-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/vocabulary/stackresolve-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/stackresolve-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/stackresolve-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/data-model/stackresolve-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stackresolve-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/stackresolve-dev/cli/stackresolve-dev-cli.yml
  title: ''
  type: CLI
  url: cli/stackresolve-dev-cli.yml
- group: auth
  href: https://artifacts.apis.io/stackresolve-dev/authentication/stackresolve-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stackresolve-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/errors/stackresolve-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stackresolve-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/stackresolve-dev/conformance/stackresolve-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stackresolve-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/stackresolve-dev/llms/stackresolve-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stackresolve-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/stackresolve-dev/mcp/stackresolve-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stackresolve-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stackresolve-dev/mcp/stackresolve-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stackresolve-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/stackresolve-dev/hosts/stackresolve-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stackresolve-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/stackresolve-dev/vendors/stackresolve-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stackresolve-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/stackresolve-dev/packages/stackresolve-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/stackresolve-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/stackresolve-dev/packages/stackresolve-dev-packages.yml
  title: ''
  type: Packages
  url: packages/stackresolve-dev-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://stackresolve.dev/categories/webhooks
- group: auth
  href: https://artifacts.apis.io/stackresolve-dev/security/stackresolve-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackresolve-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stackresolve.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stackresolve.dev/developers
- group: docs
  title: ''
  type: Documentation
  url: https://stackresolve.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://stackresolve.dev/docs/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://stackresolve.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://stackresolve.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://stackresolve.dev/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackresolve.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackresolve.dev/privacy
created: '2026-10-31'
description: StackResolve is an independent registry that scores how ready software is for AI agents, offering a web‑intelligence API that compresses web research into structured calls. It provides a REST API and MCP endpoint for searching, auditing, comparing, and researching software tools, with free public reads and paid tiers. The platform includes a developer portal, documentation, pricing, terms, and privacy pages.
image: https://stackresolve.dev/stackresolve-icon-1024.png
json_schemas:
- name: ApiKey
  property_count: 2
  slug: stackresolve-dev-api-key
- name: AuditReport
  property_count: 5
  slug: stackresolve-dev-audit-report
- name: CompanyRecord
  property_count: 5
  slug: stackresolve-dev-company-record
- name: RegistryRow
  property_count: 4
  slug: stackresolve-dev-registry-row
jsonld:
- class_count: 6
  name: Stackresolve Dev Context
  property_count: 16
  slug: stackresolve-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.stackresolve.dev requiring an API key.
  name: stackresolve-dev MCP Server
  slug: stackresolve-dev-mcp-yml
modified: '2026-10-31'
name: stackresolve-dev
nav: Providers
network: true
overview: 'stackresolve-dev publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Audit API, Company API, and 9 more. Tagged areas include AI Agents, Software Registry, Web Intelligence, API Platform, and Developer Tools.


  The stackresolve-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  stackresolve-dev''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Stackresolve Dev Plans Pricing
  plan_count: 4
  slug: stackresolve-dev-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Stackresolve Dev Rate Limits
  slug: stackresolve-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: stackresolve-dev API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: stackresolve-dev-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 59.7
    developer_ergonomics: 51.7
    discoverability: 65.0
    operational_transparency: 25.0
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/stackresolve-dev/stackresolve-dev-2026-11-03T143716.png
security:
- kind: authentication
  name: Stackresolve Dev Authentication
  slug: stackresolve-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Stackresolve Dev Domain Security
  slug: stackresolve-dev-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 7
skills:
- name: audit
  slug: stackresolve-dev-audit
- name: compare
  slug: stackresolve-dev-compare
- name: find-tools
  slug: stackresolve-dev-find-tools
- name: get-company
  slug: stackresolve-dev-get-company
- name: get-profile
  slug: stackresolve-dev-get-profile
- name: list-registry
  slug: stackresolve-dev-list-registry
- name: search
  slug: stackresolve-dev-search
slug: stackresolve-dev
tags:
- AI Agents
- Software Registry
- Web Intelligence
- API Platform
- Developer Tools
website: https://stackresolve.dev/
---
