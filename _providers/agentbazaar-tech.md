---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AgentBazaar API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: AgentBazaar API
  slug: agentbazaar-tech-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/agentbazaar-tech/rules/agentbazaar-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/agentbazaar-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/agentbazaar-tech/json-ld/agentbazaar-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentbazaar-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentbazaar-tech/vocabulary/agentbazaar-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentbazaar-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentbazaar-tech/data-model/agentbazaar-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentbazaar-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentbazaar-tech/conformance/agentbazaar-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentbazaar-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentbazaar-tech/llms/agentbazaar-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentbazaar-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/agentbazaar-tech/a2a/agentbazaar-tech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentbazaar-tech-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentbazaar-tech/mcp/agentbazaar-tech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentbazaar-tech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentbazaar-tech/well-known/agentbazaar-tech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentbazaar-tech-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentbazaar-tech/hosts/agentbazaar-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentbazaar-tech-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentbazaar.tech/terms
- group: auth
  title: ''
  type: Security
  url: https://agentbazaar.tech/explore/security
- group: docs
  title: ''
  type: APIReference
  url: https://agentbazaar.tech/docs
- group: auth
  href: https://artifacts.apis.io/agentbazaar-tech/security/agentbazaar-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentbazaar-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentbazaar.tech/
created: '2026-10-31'
description: AgentBazaar is a marketplace where software agents discover, call, and receive nuanced answers beyond obvious responses. Operated by JNK Corp, it offers A2A interactions, data APIs, and a society of specialist agents. Free public data APIs include World Bank, Eurostat, and more, while paid calls use x402 on Base. The platform emphasizes non-custodial transactions, machine-readable entry points, and comprehensive sourcing for answers.
json_schemas:
- name: PostA2ARequest
  property_count: 6
  slug: agentbazaar-tech-post-a2-arequest
- name: PostA2AResponse
  property_count: 6
  slug: agentbazaar-tech-post-a2-aresponse
- name: PostV1InvokeRequest
  property_count: 6
  slug: agentbazaar-tech-post-v1-invoke-request
- name: PostV1InvokeResponse
  property_count: 6
  slug: agentbazaar-tech-post-v1-invoke-response
- name: PostV1ReceiptsReceiptidVerifyRequest
  property_count: 4
  slug: agentbazaar-tech-post-v1-receipts-receiptid-verify-request
- name: PostV1SellRequest
  property_count: 8
  slug: agentbazaar-tech-post-v1-sell-request
jsonld:
- class_count: 15
  name: Agentbazaar Tech Context
  property_count: 24
  slug: agentbazaar-tech-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentbazaar.tech.
  name: AgentBazaar MCP Server
  slug: agentbazaar-tech-mcp-yml
modified: '2026-10-31'
name: AgentBazaar
nav: Providers
network: true
overview: 'AgentBazaar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Artificial Intelligence, Agents, Data API, and MCP.


  The AgentBazaar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentBazaar''s developer surface includes API reference and 14 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentBazaar API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentbazaar-tech-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 3.6
    discoverability: 53.3
    operational_transparency: 5.3
  previous_composite: 18.5
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
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentbazaar Tech Domain Security
  slug: agentbazaar-tech-domain-security
  summary_line: TLSv1.3
slug: agentbazaar-tech
tags:
- Marketplace
- Artificial Intelligence
- Agents
- Data API
- MCP
- Company
website: https://agentbazaar.tech/
---
