---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 38
  human_in_the_loop: 2
  name: Atlas Compiler Com Agentic Access
  operation_count: 70
  slug: atlas-compiler-com-agentic-access
  summary_line: 70 operations · 38 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The API Keys API from Atlas — 5 operation(s) for api keys.
  name: Atlas API Keys API
  slug: atlas-compiler-com-api-keys-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Billing API from Atlas — 9 operation(s) for billing.
  name: Atlas Billing API
  slug: atlas-compiler-com-billing-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Execution API from Atlas — 5 operation(s) for execution.
  name: Atlas Execution API
  slug: atlas-compiler-com-execution-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Identity API from Atlas — 2 operation(s) for identity.
  name: Atlas Identity API
  slug: atlas-compiler-com-identity-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Invitations API from Atlas — 4 operation(s) for invitations.
  name: Atlas Invitations API
  slug: atlas-compiler-com-invitations-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Jobs API from Atlas — 5 operation(s) for jobs.
  name: Atlas Jobs API
  slug: atlas-compiler-com-jobs-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Members API from Atlas — 4 operation(s) for members.
  name: Atlas Members API
  slug: atlas-compiler-com-members-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Projects API from Atlas — 3 operation(s) for projects.
  name: Atlas Projects API
  slug: atlas-compiler-com-projects-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The System API from Atlas — 1 operation(s) for system.
  name: Atlas System API
  slug: atlas-compiler-com-system-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Usage API from Atlas — 2 operation(s) for usage.
  name: Atlas Usage API
  slug: atlas-compiler-com-usage-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Webhooks API from Atlas — 11 operation(s) for webhooks.
  name: Atlas Webhooks API
  slug: atlas-compiler-com-webhooks-api
- baseURL: https://api.atlas-compiler.com
  baseurl_source: declared
  description: The Workspaces API from Atlas — 5 operation(s) for workspaces.
  name: Atlas Workspaces API
  slug: atlas-compiler-com-workspaces-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/atlas-compiler-com/agentic-access/atlas-compiler-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atlas-compiler-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/atlas-compiler-com/rate-limits/atlas-compiler-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atlas-compiler-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/rules/atlas-compiler-com-rules.yml
  title: ''
  type: Spectral
  url: rules/atlas-compiler-com-rules.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/json-ld/atlas-compiler-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlas-compiler-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/vocabulary/atlas-compiler-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlas-compiler-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/atlas-compiler-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/data-model/atlas-compiler-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlas-compiler-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/atlas-compiler-com/changelog/atlas-compiler-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atlas-compiler-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/conventions/atlas-compiler-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/atlas-compiler-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/conventions/atlas-compiler-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atlas-compiler-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/atlas-compiler-com/authentication/atlas-compiler-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlas-compiler-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/errors/atlas-compiler-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlas-compiler-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/atlas-compiler-com/conformance/atlas-compiler-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlas-compiler-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/atlas-compiler-com/llms/atlas-compiler-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlas-compiler-com-llms.txt
- group: other
  href: https://artifacts.apis.io/atlas-compiler-com/a2a/atlas-compiler-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/atlas-compiler-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/atlas-compiler-com/mcp/atlas-compiler-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atlas-compiler-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/atlas-compiler-com/mcp/atlas-compiler-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlas-compiler-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/atlas-compiler-com/well-known/atlas-compiler-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlas-compiler-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlas-compiler-com/hosts/atlas-compiler-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-compiler-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlas-compiler-com/vendors/atlas-compiler-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-compiler-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/atlas-compiler-com/packages/atlas-compiler-com-packages.yml
  title: ''
  type: SDKs
  url: packages/atlas-compiler-com-packages.yml
- group: build
  href: https://artifacts.apis.io/atlas-compiler-com/packages/atlas-compiler-com-packages.yml
  title: ''
  type: Packages
  url: packages/atlas-compiler-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://atlas-compiler.com/changelog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atlas-compiler.com\
- group: auth
  href: https://artifacts.apis.io/atlas-compiler-com/security/atlas-compiler-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-compiler-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlas-compiler.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlas-compiler.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atlas-compiler.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://atlas-compiler.com/blog/getting-started-with-atlas/
- group: commercial
  title: ''
  type: Pricing
  url: https://atlas-compiler.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://atlas-compiler.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlas-compiler.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlas-compiler.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.atlas-compiler.com/sign-up
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Atlas-Compiler
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.atlas-compiler.com/mcp
  - status: null
    url: https://api.atlas-compiler.com/openapi.json
  - status: 401
    url: https://api.atlas-compiler.com/mcp
  - status: 200
    url: https://atlas-compiler.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Atlas compiles public web content into clean Markdown and typed intermediate representation (IR) for search, data pipelines, knowledge systems, automation, and AI applications. It provides a deterministic web intelligence infrastructure that enables developers to transform web pages into structured data, facilitating integration, analysis, and AI-driven workflows across the internet.
image: https://atlas-compiler.com/atlas-logo.png
json_schemas:
- name: ExecutionResultArtifact
  property_count: 6
  slug: atlas-compiler-com-execution-result-artifact
- name: HealthResponse
  property_count: 3
  slug: atlas-compiler-com-health-response
- name: JsonValue
  property_count: 0
  slug: atlas-compiler-com-json-value
- name: PlanCatalog
  property_count: 0
  slug: atlas-compiler-com-plan-catalog
jsonld:
- class_count: 5
  name: Atlas Compiler Com Context
  property_count: 30
  slug: atlas-compiler-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.atlas-compiler.com.
  name: Atlas MCP Server
  slug: atlas-compiler-com-mcp-yml
modified: '2026-11-01'
name: Atlas
nav: Providers
network: true
overview: 'Atlas publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Billing API, Execution API, and 9 more. Tagged areas include Web Intelligence, Data Pipeline, Automation, Artificial Intelligence, and Developer Tools.


  The Atlas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Atlas'' developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 28 more developer resources.'
plans:
- name: Atlas Compiler Com Plans Pricing
  plan_count: 0
  slug: atlas-compiler-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Atlas Compiler Com Rate Limits
  slug: atlas-compiler-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Atlas API Rules
  rule_count: 50
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 7
  slug: atlas-compiler-com-rules
scopes:
- name: Atlas Compiler Com Scopes
  scope_count: 0
  slug: atlas-compiler-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 35.6
    contract_quality: 58.6
    developer_ergonomics: 45.7
    discoverability: 65.0
    operational_transparency: 42.1
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlas Compiler Com Authentication
  slug: atlas-compiler-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atlas Compiler Com Domain Security
  slug: atlas-compiler-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: compile-url
  slug: atlas-compiler-com-compile-url
slug: atlas-compiler-com
tags:
- Web Intelligence
- Data Pipeline
- Automation
- Artificial Intelligence
- Developer Tools
website: https://atlas-compiler.com/
---
