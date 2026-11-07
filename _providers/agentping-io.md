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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent Ping API provides endpoints for pinging agents, retrieving usage metrics, and managing alerts as documented in the API reference.
  name: Agent Ping API
  slug: agent-ping-api
- baseURL: https://eu.ingest.agentping.io
  baseurl_source: declared
  description: 'Agent Ping API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agent Ping API
  slug: agentping-io-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/agentping-io/rate-limits/agentping-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentping-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentping-io/plans/agentping-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentping-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentping-io/rules/agentping-io-rules.yml
  title: ''
  type: Spectral
  url: rules/agentping-io-rules.yml
- group: design
  href: https://artifacts.apis.io/agentping-io/json-ld/agentping-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentping-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentping-io/vocabulary/agentping-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentping-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentping-io/data-model/agentping-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentping-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentping-io/changelog/agentping-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentping-io-changelog.yml
- group: auth
  href: https://artifacts.apis.io/agentping-io/authentication/agentping-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentping-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentping-io/conformance/agentping-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentping-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentping-io/llms/agentping-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentping-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentping-io/mcp/agentping-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentping-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentping-io/well-known/agentping-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentping-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentping-io/hosts/agentping-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentping-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentping-io/vendors/agentping-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentping-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentping-io/packages/agentping-io-packages.yml
  title: ''
  type: SDKs
  url: packages/agentping-io-packages.yml
- group: build
  href: https://artifacts.apis.io/agentping-io/packages/agentping-io-packages.yml
  title: ''
  type: Packages
  url: packages/agentping-io-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentping.io/terms
- group: auth
  title: ''
  type: Security
  url: https://agentping.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentping.io/privacy
- group: start
  title: ''
  type: Login
  url: https://agentping.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentping.io/docs/changelog
- group: auth
  href: https://artifacts.apis.io/agentping-io/security/agentping-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentping-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentping.io/
- group: docs
  title: ''
  type: Documentation
  url: https://agentping.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentping.io/docs/api/heartbeats
- group: start
  title: ''
  type: GettingStarted
  url: https://agentping.io/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://agentping.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://agentping.io/blog
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC specifications were found on the provider's documented hosts.
  evidence:
  - status: 0
    url: https://api.agentping.io/openapi.json
  - status: 0
    url: https://api.agentping.io/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agent Ping provides AI agent observability, cost tracking, uptime monitoring, and quality scoring. It offers dashboards for spend attribution, pulse monitoring, verification of AI outputs, and integrations with major AI SDKs like OpenAI, LangChain, and Vercel AI. Users can start free, view detailed run logs, and set alerts for cost or performance anomalies across SaaS teams, automation agencies, and product engineering.
image: https://agentping.io/og/title?eyebrow=Agent%20Ping&subtitle=See%20which%20customer%20and%20feature%20caused%20your%20OpenAI%20and%20Anthropic%20bill.%20Agent%20Ping%20ties%20every%20agent%20run%20to%20a%20cost%2C%20and%20alerts%20you%20when%20one%20drifts.&title=Agent%20Ping%3A%20AI%20Agent%20Observability%2C%20Cost%20and%20Uptime&signature=2db2c7e98f053edff215e37df9e96cdabd590a1c228c94fd4ed2d2249b53004e
json_schemas:
- name: GetV1RunsIdResponse
  property_count: 14
  slug: agentping-io-get-v1-runs-id-response
- name: PostV1PingRequest
  property_count: 7
  slug: agentping-io-post-v1-ping-request
- name: PostV1RunsIdEventsRequest
  property_count: 6
  slug: agentping-io-post-v1-runs-id-events-request
- name: PostV1RunsIdFinishRequest
  property_count: 4
  slug: agentping-io-post-v1-runs-id-finish-request
- name: PostV1RunsRequest
  property_count: 10
  slug: agentping-io-post-v1-runs-request
- name: PostV1RunsResponse
  property_count: 5
  slug: agentping-io-post-v1-runs-response
jsonld:
- class_count: 14
  name: Agentping Io Context
  property_count: 30
  slug: agentping-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentping.io requiring OAuth.
  name: Agent Ping MCP Server
  slug: agentping-io-mcp-yml
modified: '2026-11-01'
name: Agent Ping
nav: Providers
network: true
overview: 'Agent Ping is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Observability, Monitoring, Cost Management, and Software-as-a-Service.


  The Agent Ping catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Ping''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Agentping Io Plans Pricing
  plan_count: 5
  slug: agentping-io-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 11
  name: Agentping Io Rate Limits
  slug: agentping-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Agent Ping API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agentping-io-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 34.5
    discoverability: 56.7
    operational_transparency: 44.7
  previous_composite: 48.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentping Io Authentication
  slug: agentping-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentping Io Domain Security
  slug: agentping-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentping-io
tags:
- Artificial Intelligence
- Observability
- Monitoring
- Cost Management
- Software-as-a-Service
website: https://agentping.io/
---
