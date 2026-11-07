---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Amnt Io Agentic Access
  operation_count: 6
  slug: amnt-io-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://amnt.io
  baseurl_source: declared
  description: Your credit balance.
  name: AMNT Account API
  slug: amnt-io-account-api
- baseURL: https://amnt.io
  baseurl_source: declared
  description: Discover agents and read their input contracts.
  name: AMNT Agents API
  slug: amnt-io-agents-api
- baseURL: https://amnt.io
  baseurl_source: declared
  description: Run an agent and get the result.
  name: AMNT Runs API
  slug: amnt-io-runs-api
- baseURL: https://amnt.io
  baseurl_source: declared
  description: 'AMNT 1.1 SVG: prompt or picture to a clean, editable SVG.'
  name: AMNT SVG API
  slug: amnt-io-svg-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/amnt-io/agentic-access/amnt-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amnt-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amnt-io/rules/amnt-io-rules.yml
  title: ''
  type: Spectral
  url: rules/amnt-io-rules.yml
- group: design
  href: https://artifacts.apis.io/amnt-io/json-ld/amnt-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amnt-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/amnt-io/vocabulary/amnt-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amnt-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/amnt-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/amnt-io/data-model/amnt-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amnt-io-data-model.yml
- group: auth
  href: https://artifacts.apis.io/amnt-io/authentication/amnt-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amnt-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/amnt-io/errors/amnt-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amnt-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/amnt-io/conformance/amnt-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amnt-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amnt-io/llms/amnt-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amnt-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/amnt-io/mcp/amnt-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amnt-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/amnt-io/well-known/amnt-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amnt-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/amnt-io/hosts/amnt-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amnt-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/amnt-io/vendors/amnt-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amnt-io-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amnt.io/use-cases/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amnt.io/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/amnt-io/security/amnt-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amnt-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amnt.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amnt.io/docs
- group: company
  title: ''
  type: Blog
  url: https://amnt.io/blog
- group: operate
  title: ''
  type: Support
  url: https://amnt.io/support
- group: commercial
  title: ''
  type: Pricing
  url: https://amnt.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amnt.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amnt.io/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amnt.io/docs/quickstart
created: '2026-11-01'
description: AMNT is a software company that builds AI tools for creators, developers, and AI agents. Their platform offers SVG art generation, studio headshots, NFT collections, a free UI kit for Next.js, and paid AI agents. Users can create, publish, and monetize AI agents, with integrated payment rails and marketplace features.
image: https://amnt.io/icon-512.png
json_schemas:
- name: AgentDetail
  property_count: 8
  slug: amnt-io-agent-detail
- name: AgentList
  property_count: 4
  slug: amnt-io-agent-list
- name: RunRequest
  property_count: 2
  slug: amnt-io-run-request
- name: RunResponse
  property_count: 6
  slug: amnt-io-run-response
- name: SvgGenerateRequest
  property_count: 13
  slug: amnt-io-svg-generate-request
- name: SvgResponse
  property_count: 17
  slug: amnt-io-svg-response
jsonld:
- class_count: 11
  name: Amnt Io Context
  property_count: 57
  slug: amnt-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at amnt.io.
  name: AMNT MCP Server
  slug: amnt-io-mcp-yml
modified: '2026-11-01'
name: AMNT
nav: Providers
network: true
overview: 'AMNT publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Runs API, and 1 more. Tagged areas include Artificial Intelligence, Tools, Creators, Developers, and Agents.


  The AMNT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AMNT''s developer surface includes authentication, API reference, documentation, engineering blog, support, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Amnt Io Plans Pricing
  plan_count: 0
  slug: amnt-io-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Amnt Io Rate Limits
  slug: amnt-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: AMNT API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: amnt-io-rules
scopes:
- name: Amnt Io Scopes
  scope_count: 0
  slug: amnt-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.2
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 67.2
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
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
  name: Amnt Io Authentication
  slug: amnt-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amnt Io Domain Security
  slug: amnt-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: get-agent
  slug: amnt-io-get-agent
- name: get-balance
  slug: amnt-io-get-balance
- name: list-agents
  slug: amnt-io-list-agents
- name: run-agent
  slug: amnt-io-run-agent
- name: svg-generate
  slug: amnt-io-svg-generate
- name: svg-vectorize
  slug: amnt-io-svg-vectorize
slug: amnt-io
tags:
- Artificial Intelligence
- Tools
- Creators
- Developers
- Agents
website: https://amnt.io/
---
