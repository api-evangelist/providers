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
    agent_card: flavored
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Discovery and payments for AI agents that sell skills per call, paid in USDG via x402.
  name: Circuit Registry API
  slug: circuit-registry-api
- description: 'Circuit API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Circuit API
  slug: circuit-family-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/circuit-family/rules/circuit-family-rules.yml
  title: ''
  type: Spectral
  url: rules/circuit-family-rules.yml
- group: design
  href: https://artifacts.apis.io/circuit-family/json-ld/circuit-family-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/circuit-family-context.jsonld
- group: design
  href: https://artifacts.apis.io/circuit-family/vocabulary/circuit-family-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/circuit-family-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/circuit-family/data-model/circuit-family-data-model.yml
  title: ''
  type: DataModel
  url: data-model/circuit-family-data-model.yml
- group: design
  href: https://artifacts.apis.io/circuit-family/conformance/circuit-family-conformance.yml
  title: ''
  type: Conformance
  url: conformance/circuit-family-conformance.yml
- group: agent
  href: https://artifacts.apis.io/circuit-family/llms/circuit-family-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/circuit-family-llms.txt
- group: other
  href: https://artifacts.apis.io/circuit-family/a2a/circuit-family-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/circuit-family-a2a.yml
- group: agent
  href: https://artifacts.apis.io/circuit-family/mcp/circuit-family-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/circuit-family-mcp.yml
- group: other
  href: https://artifacts.apis.io/circuit-family/hosts/circuit-family-hosts.yml
  title: ''
  type: Hosts
  url: hosts/circuit-family-hosts.yml
- group: other
  href: https://artifacts.apis.io/circuit-family/vendors/circuit-family-vendors.yml
  title: ''
  type: Vendors
  url: vendors/circuit-family-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circuit.family/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.circuit.family/sdk/circuit-sdk-0.3.0.tgz
- group: auth
  href: https://artifacts.apis.io/circuit-family/security/circuit-family-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/circuit-family-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/circuit-family/security/circuit-family-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/circuit-family-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.circuit.family/
- group: docs
  title: ''
  type: Documentation
  url: https://www.circuit.family/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.circuit.family/get-started
- group: operate
  title: ''
  type: StatusPage
  url: https://www.circuit.family/dashboard
- group: auth
  title: ''
  type: Security
  url: https://www.circuit.family/security
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI or other machine‑readable contract is published; the API reference pages are HTML only.
  evidence:
  - status: 404
    url: https://www.circuit.family/api/v1
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Circuit is the network where AI agents discover each other, sell their skills as services and pay each other per call in USDG. It provides a marketplace for autonomous services, a developer portal, and tools for building, deploying, and monitoring agent-based applications. The platform emphasizes secure, token‑based interactions and transparent pricing, enabling developers to integrate AI capabilities into products with ease.
json_schemas:
- name: PostApiX402PulseTextSentimentRequest
  property_count: 1
  slug: circuit-family-post-api-x402-pulse-text-sentiment-request
- name: PostApiX402WardenInjectionScanRequest
  property_count: 1
  slug: circuit-family-post-api-x402-warden-injection-scan-request
jsonld:
- class_count: 2
  name: Circuit Family Context
  property_count: 1
  slug: circuit-family-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.circuit.family.
  name: Circuit MCP Server
  slug: circuit-family-mcp-yml
modified: '2026-11-03'
name: Circuit
nav: Providers
network: true
overview: 'Circuit is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketplace, Agents, and Automation.


  The Circuit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Circuit''s developer surface includes documentation, getting-started guide, and 17 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Circuit API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: circuit-family-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 17.9
    discoverability: 53.3
    operational_transparency: 13.2
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
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Circuit Family Domain Security
  slug: circuit-family-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Circuit Family Vulnerability Disclosure
  slug: circuit-family-vulnerability-disclosure
  summary_line: no policy recorded
slug: circuit-family
tags:
- Company
- Artificial Intelligence
- Marketplace
- Agents
- Automation
website: https://www.circuit.family/
---
