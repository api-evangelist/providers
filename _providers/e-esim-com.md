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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: E Esim Com Agentic Access
  operation_count: 1
  slug: e-esim-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://e-esim.com/wp-json/e-esim
  baseurl_source: declared
  description: MCP JSON-RPC API for e‑SIM travel data plans
  name: e-eSIM Catalog API
  slug: e-esim-catalog-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/e-esim-com/agentic-access/e-esim-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/e-esim-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/e-esim-com/rules/e-esim-com-rules.yml
  title: ''
  type: Spectral
  url: rules/e-esim-com-rules.yml
- group: design
  href: https://artifacts.apis.io/e-esim-com/json-ld/e-esim-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/e-esim-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/e-esim-com/vocabulary/e-esim-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/e-esim-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/e-esim-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/e-esim-com/data-model/e-esim-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/e-esim-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/e-esim-com/security/e-esim-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/e-esim-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/e-esim-com/conformance/e-esim-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/e-esim-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/e-esim-com/llms/e-esim-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/e-esim-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/e-esim-com/mcp/e-esim-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/e-esim-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/e-esim-com/well-known/e-esim-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/e-esim-com-security.txt
- group: agent
  href: https://artifacts.apis.io/e-esim-com/well-known/e-esim-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/e-esim-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/e-esim-com/hosts/e-esim-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/e-esim-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/e-esim-com/vendors/e-esim-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/e-esim-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://e-esim.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e-esim.com/privacy/
- group: auth
  href: https://artifacts.apis.io/e-esim-com/security/e-esim-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/e-esim-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/e-esim-com/security/e-esim-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/e-esim-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://e-esim.com/
created: '2026-11-06'
description: IbiPoint Ltd offers prepaid travel eSIMs that provide mobile data coverage in 162 countries and regions. Customers can purchase single‑country, regional or worldwide data plans online, receive an activation link or QR code, and connect their phone instantly upon arrival. The service is targeted at travelers who need data abroad without roaming charges from their home carrier.
image: https://e-esim.com/assets/OG-e-esim.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: e-esim-com-json-rpc-request
jsonld:
- class_count: 1
  name: E Esim Com Context
  property_count: 4
  slug: e-esim-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at e-esim.com.
  name: IbiPoint Ltd MCP Server
  slug: e-esim-com-mcp-yml
modified: '2026-11-06'
name: IbiPoint Ltd
nav: Providers
network: true
overview: 'IbiPoint Ltd is listed with 1 API on the [APIs.io](https://apis.io/) network: e-eSIM Catalog API. Tagged areas include eSIM, Travel Data, Prepaid Mobile, and Mobile Data.


  The IbiPoint Ltd catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: IbiPoint Ltd API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: e-esim-com-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 18.8
    developer_ergonomics: 1.8
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
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: E Esim Com Domain Security
  slug: e-esim-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: E Esim Com Vulnerability Disclosure
  slug: e-esim-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: e-esim-com-mcp
  slug: e-esim-com-mcp
slug: e-esim-com
tags:
- eSIM
- Travel Data
- Prepaid Mobile
- Mobile Data
website: https://e-esim.com/
---
