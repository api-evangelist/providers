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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://financesec.api.caleralabs.com
  baseurl_source: declared
  description: 'Calera Labs API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Calera Labs API
  slug: caleralabs-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/caleralabs-com/rules/caleralabs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/caleralabs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/caleralabs-com/json-ld/caleralabs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/caleralabs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/caleralabs-com/vocabulary/caleralabs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/caleralabs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/caleralabs-com/data-model/caleralabs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/caleralabs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/caleralabs-com/conformance/caleralabs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caleralabs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caleralabs-com/llms/caleralabs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caleralabs-com-llms.txt
- group: build
  href: https://artifacts.apis.io/caleralabs-com/mcp/caleralabs-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/caleralabs-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/caleralabs-com/mcp/caleralabs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caleralabs-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/caleralabs-com/well-known/caleralabs-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caleralabs-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/caleralabs-com/hosts/caleralabs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caleralabs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caleralabs-com/vendors/caleralabs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caleralabs-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/caleralabs-com/packages/caleralabs-com-packages.yml
  title: ''
  type: SDKs
  url: packages/caleralabs-com-packages.yml
- group: build
  href: https://artifacts.apis.io/caleralabs-com/packages/caleralabs-com-packages.yml
  title: ''
  type: Packages
  url: packages/caleralabs-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://caleralabs.com/status
- group: auth
  href: https://artifacts.apis.io/caleralabs-com/security/caleralabs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caleralabs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caleralabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://caleralabs.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://caleralabs.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caleralabs.com/legal/a2b-tos.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caleralabs.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@caleralabs.com
created: '2026-11-03'
description: Calera Labs builds a sovereign AI Memory Substrate and deterministic LLM infrastructure, offering zero‑hallucination SEC financial intelligence, USPTO patent prosecution intelligence, and persistent 4D lattice memory for enterprise LLMs and autonomous AI agents via FinanceSec, PatentSec, and Infinite Context (ICX).
image: https://caleralabs.com/assets/og/calera-labs-og.png
json_schemas:
- name: PostApiPacksValuationInputsResponse
  property_count: 2
  slug: caleralabs-com-post-api-packs-valuation-inputs-response
- name: PostApiQueryResponse
  property_count: 3
  slug: caleralabs-com-post-api-query-response
- name: PostV1FinsecFirewallVerifyPayloadResponse
  property_count: 1
  slug: caleralabs-com-post-v1-finsec-firewall-verify-payload-response
- name: PostV1FinsecHftVerifyRouteResponse
  property_count: 2
  slug: caleralabs-com-post-v1-finsec-hft-verify-route-response
- name: PostV1FinsecScenarioStressTestRequest
  property_count: 1
  slug: caleralabs-com-post-v1-finsec-scenario-stress-test-request
- name: PostV1HftOrderbookSettleRequest
  property_count: 1
  slug: caleralabs-com-post-v1-hft-orderbook-settle-request
jsonld:
- class_count: 18
  name: Caleralabs Com Context
  property_count: 1
  slug: caleralabs-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at icx.caleralabs.com.
  name: Calera Labs MCP Server
  slug: caleralabs-com-mcp-yml
modified: '2026-11-03'
name: Calera Labs
nav: Providers
network: true
overview: 'Calera Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, LLM, Infrastructure, and FinanceSec.


  The Calera Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Calera Labs'' developer surface includes documentation, API reference, support, and 18 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Calera Labs API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: caleralabs-com-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 22.8
    developer_ergonomics: 20.2
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caleralabs Com Domain Security
  slug: caleralabs-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caleralabs-com
tags:
- Artificial Intelligence
- Memory
- LLM
- Infrastructure
- FinanceSec
- PatentSec
- ICX
- Company
website: https://caleralabs.com/
---
