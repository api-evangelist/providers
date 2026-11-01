---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Argus Town Agentic Access
  operation_count: 31
  slug: argus-town-agentic-access
  summary_line: 31 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Alerts API from argus-town — 3 operation(s) for alerts.
  name: argus-town Alerts API
  slug: argus-town-alerts-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Connect links API from argus-town — 2 operation(s) for connect links.
  name: argus-town Connect links API
  slug: argus-town-connect-links-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Connections API from argus-town — 2 operation(s) for connections.
  name: argus-town Connections API
  slug: argus-town-connections-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Events API from argus-town — 2 operation(s) for events.
  name: argus-town Events API
  slug: argus-town-events-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Negotiated pricing API from argus-town — 1 operation(s) for negotiated pricing.
  name: argus-town Negotiated pricing API
  slug: argus-town-negotiated-pricing-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Project API from argus-town — 1 operation(s) for project.
  name: argus-town Project API
  slug: argus-town-project-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Providers API from argus-town — 2 operation(s) for providers.
  name: argus-town Providers API
  slug: argus-town-providers-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Spend API from argus-town — 2 operation(s) for spend.
  name: argus-town Spend API
  slug: argus-town-spend-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Start API from argus-town — 5 operation(s) for start.
  name: argus-town Start API
  slug: argus-town-start-api
- baseURL: https://api.argus.town
  baseurl_source: declared
  description: The Syncs API from argus-town — 2 operation(s) for syncs.
  name: argus-town Syncs API
  slug: argus-town-syncs-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/argus-town/agentic-access/argus-town-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/argus-town-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/argus-town/plans/argus-town-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/argus-town-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/argus-town/rules/argus-town-rules.yml
  title: ''
  type: Spectral
  url: rules/argus-town-rules.yml
- group: design
  href: https://artifacts.apis.io/argus-town/json-ld/argus-town-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/argus-town-context.jsonld
- group: design
  href: https://artifacts.apis.io/argus-town/vocabulary/argus-town-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/argus-town-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/argus-town/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/argus-town/data-model/argus-town-data-model.yml
  title: ''
  type: DataModel
  url: data-model/argus-town-data-model.yml
- group: operate
  href: https://artifacts.apis.io/argus-town/changelog/argus-town-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/argus-town-changelog.yml
- group: auth
  href: https://artifacts.apis.io/argus-town/authentication/argus-town-authentication.yml
  title: ''
  type: Authentication
  url: authentication/argus-town-authentication.yml
- group: design
  href: https://artifacts.apis.io/argus-town/errors/argus-town-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/argus-town-problem-types.yml
- group: design
  href: https://artifacts.apis.io/argus-town/conformance/argus-town-conformance.yml
  title: ''
  type: Conformance
  url: conformance/argus-town-conformance.yml
- group: agent
  href: https://artifacts.apis.io/argus-town/llms/argus-town-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/argus-town-llms.txt
- group: build
  href: https://artifacts.apis.io/argus-town/mcp/argus-town-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/argus-town-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/argus-town/mcp/argus-town-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/argus-town-mcp.yml
- group: other
  href: https://artifacts.apis.io/argus-town/hosts/argus-town-hosts.yml
  title: ''
  type: Hosts
  url: hosts/argus-town-hosts.yml
- group: other
  href: https://artifacts.apis.io/argus-town/vendors/argus-town-vendors.yml
  title: ''
  type: Vendors
  url: vendors/argus-town-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://argus.town/changelog
- group: auth
  href: https://artifacts.apis.io/argus-town/security/argus-town-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/argus-town-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://argus.town/
- group: docs
  title: ''
  type: Documentation
  url: https://argus.town/docs
- group: docs
  title: ''
  type: APIReference
  url: https://argus.town/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://argus.town/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://argus.town/pricing
- group: start
  title: ''
  type: SignUp
  url: https://argus.town/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://argus.town/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://argus.town/privacy
created: '2026-10-30'
description: Argus lets your coding agent track API spend while you build. Over MCP it can check what a run costs, catch a loop burning credits, and see a provider running dry. You get one place for every metered API's balance, spend and runway, with alerts before one hits zero. The service offers free tier up to $1,000 monthly tracked spend and integrates with major LLM providers.
image: https://argus.town/opengraph-image.png?opengraph-image.05k6i4pd2ol6_.png
json_schemas:
- name: ApiIndex
  property_count: 7
  slug: argus-town-api-index
- name: ConnectLink
  property_count: 10
  slug: argus-town-connect-link
- name: Connection
  property_count: 19
  slug: argus-town-connection
- name: EventBatch
  property_count: 9
  slug: argus-town-event-batch
- name: EventInput
  property_count: 24
  slug: argus-town-event-input
- name: EventValidation
  property_count: 9
  slug: argus-town-event-validation
jsonld:
- class_count: 54
  name: Argus Town Context
  property_count: 177
  slug: argus-town-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.argus.town.
  name: argus-town MCP Server
  slug: argus-town-mcp-yml
modified: '2026-10-30'
name: argus-town
nav: Providers
network: true
overview: 'argus-town publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API, Connect links API, Connections API, and 7 more. Tagged areas include Company, API-Monitoring, Cost-Management, Developer-Tools, and MCP.


  The argus-town catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  argus-town''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 19 more developer resources.'
plans:
- name: Argus Town Plans Pricing
  plan_count: 3
  slug: argus-town-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Argus Town Rate Limits
  slug: argus-town-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: argus-town API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: argus-town-rules
scopes:
- name: Argus Town Scopes
  scope_count: 0
  slug: argus-town-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 63.3
    developer_ergonomics: 46.9
    discoverability: 65.0
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Argus Town Authentication
  slug: argus-town-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Argus Town Domain Security
  slug: argus-town-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: list-providers
  slug: argus-town-list-providers
slug: argus-town
tags:
- Company
- API-Monitoring
- Cost-Management
- Developer-Tools
- MCP
website: https://argus.town/
---
