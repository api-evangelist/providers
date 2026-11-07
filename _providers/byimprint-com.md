---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Byimprint Com Agentic Access
  operation_count: 1
  slug: byimprint-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://byimprint.com
  baseurl_source: declared
  description: The MCP API from byImprint — 1 operation(s) for mcp.
  name: byImprint MCP API
  slug: byimprint-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/byimprint-com/agentic-access/byimprint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/byimprint-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/byimprint-com/plans/byimprint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/byimprint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/rules/byimprint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/byimprint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/json-ld/byimprint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/byimprint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/byimprint-com/vocabulary/byimprint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/byimprint-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/data-model/byimprint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/byimprint-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/byimprint-com/lifecycle/byimprint-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/byimprint-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/lifecycle/byimprint-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/byimprint-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/errors/byimprint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/byimprint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/byimprint-com/conformance/byimprint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/byimprint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/byimprint-com/llms/byimprint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/byimprint-com-llms.txt
- group: build
  href: https://artifacts.apis.io/byimprint-com/mcp/byimprint-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/byimprint-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/byimprint-com/mcp/byimprint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/byimprint-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/byimprint-com/well-known/byimprint-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/byimprint-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/byimprint-com/hosts/byimprint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byimprint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/byimprint-com/vendors/byimprint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/byimprint-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byimprint.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byimprint.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://byimprint.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://byimprint.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://byimprint.com/developers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/byimprint
- group: auth
  href: https://artifacts.apis.io/byimprint-com/security/byimprint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byimprint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://byimprint.com/
created: '2026-11-03'
description: byImprint offers workflow automation, website development, and practical AI consulting services based in Squamish, Canada. They work directly with clients on projects starting from CA$2,500, focusing on tailored solutions that integrate AI, design, and efficient processes. The company emphasizes clear scope agreements and hands‑on collaboration to deliver measurable results for businesses seeking digital transformation.
image: https://byimprint.com/opengraph-image
json_schemas:
- name: JsonRpcErrorResponse
  property_count: 3
  slug: byimprint-com-json-rpc-error-response
- name: JsonRpcRequest
  property_count: 4
  slug: byimprint-com-json-rpc-request
- name: JsonRpcSuccessResponse
  property_count: 3
  slug: byimprint-com-json-rpc-success-response
jsonld:
- class_count: 4
  name: Byimprint Com Context
  property_count: 8
  slug: byimprint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at byimprint.com.
  name: byImprint MCP Server
  slug: byimprint-com-mcp-yml
modified: '2026-11-03'
name: byImprint
nav: Providers
network: true
overview: 'byImprint publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Website Design and Customer Experience.


  The byImprint catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  byImprint''s developer surface includes pricing, documentation, API reference, and 21 more developer resources.'
plans:
- name: Byimprint Com Plans Pricing
  plan_count: 3
  slug: byimprint-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: byImprint API Rules
  rule_count: 58
  severity_counts:
    error: 54
    hint: 0
    info: 3
    warn: 1
  slug: byimprint-com-rules
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 61.0
    developer_ergonomics: 8.3
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Byimprint Com Domain Security
  slug: byimprint-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: byimprint-com
tags:
- Website Design
- Customer Experience
website: https://byimprint.com/
---
