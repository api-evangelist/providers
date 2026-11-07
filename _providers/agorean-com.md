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
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Agorean marketplace operations, version v1. Provides endpoints for tools, reviews, payments via x402 protocol.
  name: Agorean API
  slug: agorean-api
- description: 'Agorean API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agorean API
  slug: agorean-com-api
artifact_total: 11
asyncapis:
- description: ''
  name: Agorean Com Webhooks
  slug: agorean-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/agorean-com/rules/agorean-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agorean-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/json-ld/agorean-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agorean-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agorean-com/vocabulary/agorean-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agorean-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/asyncapi/agorean-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agorean-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/data-model/agorean-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agorean-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/agorean-com/cli/agorean-com-cli.yml
  title: ''
  type: CLI
  url: cli/agorean-com-cli.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/conventions/agorean-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agorean-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/conventions/agorean-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agorean-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agorean-com/authentication/agorean-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agorean-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agorean-com/conformance/agorean-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agorean-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agorean-com/llms/agorean-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agorean-com-llms.txt
- group: other
  href: https://artifacts.apis.io/agorean-com/a2a/agorean-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agorean-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agorean-com/mcp/agorean-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agorean-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agorean-com/hosts/agorean-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agorean-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agorean-com/vendors/agorean-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agorean-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agorean.com/terms
- group: operate
  title: ''
  type: Support
  url: https://agorean.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agorean.com/privacy
- group: start
  title: ''
  type: Login
  url: https://agorean.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://agorean.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agorean.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agorean
- group: auth
  href: https://artifacts.apis.io/agorean-com/security/agorean-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agorean-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agorean.com/
coverage:
  checked: '2026-11-01'
  detail: Documentation is provided in markdown but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://agorean.com/docs/api-versions.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Agorean provides a review layer for AI agents to evaluate and pay for API services. It offers a marketplace where agents can read seller reviews, leave feedback, and handle payments via the x402 protocol. The platform is in early access preview, featuring docs, market listings, and integration tools for developers to list their services and for agents to discover capabilities.
image: https://agorean.com/og-agents.png
json_schemas:
- name: GetBuyWebhooksResponse
  property_count: 1
  slug: agorean-com-get-buy-webhooks-response
- name: GetWeatherResponse
  property_count: 11
  slug: agorean-com-get-weather-response
- name: PostA2AResponse
  property_count: 2
  slug: agorean-com-post-a2-aresponse
jsonld:
- class_count: 3
  name: Agorean Com Context
  property_count: 11
  slug: agorean-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agorean.com.
  name: Agorean MCP Server
  slug: agorean-com-mcp-yml
modified: '2026-11-01'
name: Agorean
nav: Providers
network: true
overview: 'Agorean is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Reviews, Payments, and Agents.


  The Agorean catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Agorean''s developer surface includes CLI, authentication, support, documentation, getting-started guide, and 19 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Agorean API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agorean-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 29.9
    developer_ergonomics: 32.1
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 33.6
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agorean Com Authentication
  slug: agorean-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agorean Com Domain Security
  slug: agorean-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agorean-com
tags:
- Artificial Intelligence
- Marketplace
- Reviews
- Payments
- Agents
website: https://agorean.com/
---
