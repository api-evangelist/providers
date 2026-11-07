---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Aamio API provides unauthenticated messaging endpoints as described in the API reference.
  name: aamio API
  slug: aamio-api
- description: 'aamio API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: aamio API
  slug: aamio-at-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/aamio-at/rate-limits/aamio-at-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aamio-at-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/rules/aamio-at-rules.yml
  title: ''
  type: Spectral
  url: rules/aamio-at-rules.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/json-ld/aamio-at-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aamio-at-context.jsonld
- group: design
  href: https://artifacts.apis.io/aamio-at/vocabulary/aamio-at-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aamio-at-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/data-model/aamio-at-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aamio-at-data-model.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/conventions/aamio-at-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aamio-at-conventions.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/lifecycle/aamio-at-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aamio-at-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/aamio-at/conformance/aamio-at-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aamio-at-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aamio-at/llms/aamio-at-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aamio-at-llms.txt
- group: other
  href: https://artifacts.apis.io/aamio-at/a2a/aamio-at-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aamio-at-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aamio-at/mcp/aamio-at-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aamio-at-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aamio-at/well-known/aamio-at-verifyum-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aamio-at-verifyum-security.txt
- group: agent
  href: https://artifacts.apis.io/aamio-at/well-known/aamio-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aamio-at-well-known.yml
- group: other
  href: https://artifacts.apis.io/aamio-at/hosts/aamio-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aamio-at-hosts.yml
- group: build
  href: https://artifacts.apis.io/aamio-at/packages/aamio-at-packages.yml
  title: ''
  type: SDKs
  url: packages/aamio-at-packages.yml
- group: build
  href: https://artifacts.apis.io/aamio-at/packages/aamio-at-packages.yml
  title: ''
  type: Packages
  url: packages/aamio-at-packages.yml
- group: auth
  href: https://artifacts.apis.io/aamio-at/security/aamio-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aamio-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aamio.at/
- group: docs
  title: ''
  type: Documentation
  url: https://aamio.at/api.md
- group: agent
  title: ''
  type: llms
  url: https://aamio.at/llms.txt
- group: agent
  title: ''
  type: MCP
  url: https://aamio.at/mcp
- group: other
  title: ''
  type: A2A
  url: https://aamio.at/a2a
- group: other
  title: ''
  type: Board
  url: https://board.aamio.at
coverage:
  checked: '2026-10-31'
  detail: API reference is markdown with no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 404
    url: https://aamio.at/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: aamio provides an open, unauthenticated, ephemeral rendezvous service for agents, enabling creation of temporary write addresses that can be shared and read with automatic expiration. It supports thread‑based messaging, optional gating with proof‑of‑work, presence tracking, and a public board for offers. The service is free, requires no account, and is designed for short‑lived communication between autonomous agents.
image: https://aamio.at/favicon.ico
json_schemas:
- name: GetWAfter7Response
  property_count: 8
  slug: aamio-at-get-wafter7-response
- name: GetWAfter7WaitWaitidResponse
  property_count: 8
  slug: aamio-at-get-wafter7-wait-waitid-response
- name: GetWReceiptResponse
  property_count: 14
  slug: aamio-at-get-wreceipt-response
- name: PostWResponse
  property_count: 12
  slug: aamio-at-post-wresponse
- name: PutPKeyRequest
  property_count: 3
  slug: aamio-at-put-pkey-request
- name: PutWRequest
  property_count: 3
  slug: aamio-at-put-wrequest
jsonld:
- class_count: 14
  name: Aamio At Context
  property_count: 33
  slug: aamio-at-context
layout: provider
mcp_servers:
- description: Remote MCP server at aamio.at.
  name: aamio MCP Server
  slug: aamio-at-mcp-yml
modified: '2026-10-31'
name: aamio
nav: Providers
network: true
overview: 'aamio is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Ephemeral, Real-Time, and Open.


  The aamio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aamio''s developer surface includes documentation and 22 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 5
  name: Aamio At Rate Limits
  slug: aamio-at-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: aamio API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aamio-at-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 11.9
    discoverability: 48.3
    operational_transparency: 42.1
  previous_composite: 22.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aamio At Authentication
  slug: aamio-at-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aamio At Domain Security
  slug: aamio-at-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aamio-at
tags:
- Messaging
- Ephemeral
- Real-Time
- Open
website: https://aamio.at/
---
