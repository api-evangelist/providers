---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Shiprust Agentic Access
  operation_count: 7
  slug: shiprust-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- description: The account behind the key
  name: ShipRust Account API
  slug: shiprust-account-api
- description: Generated projects
  name: ShipRust Projects API
  slug: shiprust-projects-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/shiprust/agentic-access/shiprust-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shiprust-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/shiprust/plans/shiprust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shiprust-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shiprust/rules/shiprust-rules.yml
  title: ''
  type: Spectral
  url: rules/shiprust-rules.yml
- group: design
  href: https://artifacts.apis.io/shiprust/json-ld/shiprust-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shiprust-context.jsonld
- group: design
  href: https://artifacts.apis.io/shiprust/vocabulary/shiprust-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shiprust-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/shiprust/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/shiprust/data-model/shiprust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shiprust-data-model.yml
- group: design
  href: https://artifacts.apis.io/shiprust/errors/shiprust-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shiprust-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shiprust/conformance/shiprust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shiprust-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shiprust/llms/shiprust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiprust-llms.txt
- group: build
  href: https://artifacts.apis.io/shiprust/mcp/shiprust-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/shiprust-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/shiprust/mcp/shiprust-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/shiprust-mcp.yml
- group: agent
  href: https://artifacts.apis.io/shiprust/well-known/shiprust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shiprust-well-known.yml
- group: other
  href: https://artifacts.apis.io/shiprust/hosts/shiprust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shiprust-hosts.yml
- group: auth
  href: https://artifacts.apis.io/shiprust/authentication/shiprust-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shiprust-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shiprust/security/shiprust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiprust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shiprust.com
- group: docs
  title: ''
  type: Documentation
  url: https://shiprust.com/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shiprust.com
- group: docs
  title: ''
  type: APIReference
  url: https://shiprust.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://shiprust.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://shiprust.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://shiprust.com/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://shiprust.com/sign-in
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://shiprust.com/openapi.json
  - status: 401
    url: https://shiprust.com/mcp
  - status: 200
    url: https://shiprust.com
  reason: partner-login
  state: gated
created: '2026-10-20'
description: ShipRust provides a Rust-based SaaS starter platform that includes a ready-to-use Axum web framework, Maud templating, PostgreSQL integration, authentication, Stripe billing, monitoring, and a full set of developer tools. It enables developers to launch a production-ready SaaS application in an afternoon, offering sign‑in, payments, analytics, and extensible codebase for building unlimited Rust web services.
image: https://shiprust.com/assets/og-image.png?v=b2dd1faf0277
json_schemas:
- name: Account
  property_count: 4
  slug: shiprust-account
- name: CreateRequest
  property_count: 16
  slug: shiprust-create-request
- name: Options
  property_count: 6
  slug: shiprust-options
- name: ProjectList
  property_count: 1
  slug: shiprust-project-list
- name: Project
  property_count: 21
  slug: shiprust-project
- name: ProjectZip
  property_count: 0
  slug: shiprust-project-zip
jsonld:
- class_count: 13
  name: Shiprust Context
  property_count: 34
  slug: shiprust-context
layout: provider
mcp_servers:
- description: Remote MCP server at shiprust.com requiring OAuth.
  name: ShipRust MCP Server
  slug: shiprust-mcp-yml
modified: '2026-10-20'
name: ShipRust
nav: Providers
network: true
overview: 'ShipRust publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Account API and Projects API. Tagged areas include Rust, Software-as-a-Service, Starter, Axum, and PostgreSQL.


  The ShipRust catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ShipRust''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Shiprust Plans Pricing
  plan_count: 1
  slug: shiprust-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ShipRust API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: shiprust-rules
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 27.6
    contract_governance: 22.0
    contract_quality: 54.9
    developer_ergonomics: 33.9
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shiprust/shiprust-2026-11-03T143124.png
security:
- kind: authentication
  name: Shiprust Authentication
  slug: shiprust-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shiprust Domain Security
  slug: shiprust-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: shiprust-create-and-download-project
  slug: shiprust-create-and-download-project
slug: shiprust
tags:
- Rust
- Software-as-a-Service
- Starter
- Axum
- PostgreSQL
website: https://shiprust.com
---
