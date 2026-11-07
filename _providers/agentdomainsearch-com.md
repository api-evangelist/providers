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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent-first domain registration and DNS management API.
  name: Agent Domain Search API
  slug: agent-domain-search-api
- baseURL: https://agentdomainsearch.com
  baseurl_source: declared
  description: Agent-first domain registration and DNS management. Pay with USDC on Base via x402.
  name: Agent Domain Search Api API
  slug: agent-domain-search-api-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/rules/agentdomainsearch-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentdomainsearch-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/json-ld/agentdomainsearch-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentdomainsearch-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/vocabulary/agentdomainsearch-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentdomainsearch-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/conformance/agentdomainsearch-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdomainsearch-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/data-model/agentdomainsearch-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdomainsearch-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agentdomainsearch-com/security/agentdomainsearch-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentdomainsearch-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentdomainsearch-com/errors/agentdomainsearch-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdomainsearch-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agentdomainsearch-com/llms/agentdomainsearch-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdomainsearch-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentdomainsearch-com/mcp/agentdomainsearch-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdomainsearch-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentdomainsearch-com/well-known/agentdomainsearch-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdomainsearch-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentdomainsearch-com/hosts/agentdomainsearch-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentdomainsearch-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentdomainsearch-com/security/agentdomainsearch-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdomainsearch-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdomainsearch-com/security/agentdomainsearch-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdomainsearch-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentdomainsearch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentdomainsearch.com/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdomainsearch.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdomainsearch.com/terms
created: '2026-10-31'
description: Agent Domain Search provides an agent‑first domain registration and DNS management service. Users can check domain availability, register, renew, and manage DNS records via a JSON API, paying with USDC on Base through the x402 protocol. Authentication is performed via EIP‑191 signed bearer tokens tied to an Ethereum wallet, eliminating traditional accounts and passwords. The service emphasizes decentralised identity and blockchain‑backed payments, offering features such as domain suggestions, price queries, and full DNS control.
image: https://agentdomainsearch.com/logo.svg
json_schemas:
- name: DomainCheck
  property_count: 5
  slug: agentdomainsearch-com-domain-check
- name: RegisterRequest
  property_count: 3
  slug: agentdomainsearch-com-register-request
- name: RegisterResponse
  property_count: 7
  slug: agentdomainsearch-com-register-response
jsonld:
- class_count: 3
  name: Agentdomainsearch Com Context
  property_count: 13
  slug: agentdomainsearch-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at agentdomainsearch.com.
  name: Agent Domain Search MCP Server
  slug: agentdomainsearch-com-mcp-yml
modified: '2026-10-31'
name: Agent Domain Search
nav: Providers
network: true
overview: 'Agent Domain Search publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api API, and 1 more. Tagged areas include Domain Registration and DNS Management.


  The Agent Domain Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Domain Search''s developer surface includes documentation and 16 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Agent Domain Search API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentdomainsearch-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 52.4
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 30.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentdomainsearch Com Domain Security
  slug: agentdomainsearch-com-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Agentdomainsearch Com Vulnerability Disclosure
  slug: agentdomainsearch-com-vulnerability-disclosure
  summary_line: no policy recorded
slug: agentdomainsearch-com
tags:
- Domain Registration
- DNS Management
website: https://agentdomainsearch.com/
---
