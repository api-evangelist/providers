---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  score: 20.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BuyerAware API provides car risk scoring and pricing estimates.
  name: BuyerAware API
  slug: buyeraware-api
- description: 'BuyerAware API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BuyerAware API
  slug: buyerawareapp-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/buyerawareapp-com/plans/buyerawareapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buyerawareapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buyerawareapp-com/rules/buyerawareapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buyerawareapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buyerawareapp-com/json-ld/buyerawareapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buyerawareapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buyerawareapp-com/vocabulary/buyerawareapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buyerawareapp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buyerawareapp-com/data-model/buyerawareapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buyerawareapp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/buyerawareapp-com/conformance/buyerawareapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buyerawareapp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buyerawareapp-com/llms/buyerawareapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buyerawareapp-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/buyerawareapp-com/mcp/buyerawareapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buyerawareapp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/buyerawareapp-com/hosts/buyerawareapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyerawareapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buyerawareapp-com/vendors/buyerawareapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyerawareapp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/buyerawareapp-com/security/buyerawareapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyerawareapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buyerawareapp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://buyerawareapp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buyerawareapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buyerawareapp.com/privacy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://buyerawareapp.com/how-it-works
coverage:
  checked: '2026-11-03'
  detail: Provider documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://buyerawareapp.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BuyerAware provides a free Quick Check for used cars, delivering a mechanical risk score and price fairness estimate within minutes. Users can pay $29 for a detailed Full Report read by an expert, offering negotiation scripts, repair cost ranges, and inspection recommendations. The service aims to empower car buyers with data-driven insights to negotiate better or walk away.
json_schemas:
- name: PostV1SignupRequest
  property_count: 1
  slug: buyerawareapp-com-post-v1-signup-request
- name: PostV1VerdictRequest
  property_count: 2
  slug: buyerawareapp-com-post-v1-verdict-request
jsonld:
- class_count: 2
  name: Buyerawareapp Com Context
  property_count: 3
  slug: buyerawareapp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.buyerawareapp.com.
  name: BuyerAware MCP Server
  slug: buyerawareapp-com-mcp-yml
modified: '2026-11-03'
name: BuyerAware
nav: Providers
network: true
overview: 'BuyerAware is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Used Cars, Vehicle Inspection, Pricing, and Data Analytics.


  The BuyerAware catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuyerAware''s developer surface includes pricing, getting-started guide, and 14 more developer resources.'
plans:
- name: Buyerawareapp Com Plans Pricing
  plan_count: 4
  slug: buyerawareapp-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BuyerAware API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: buyerawareapp-com-rules
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 6.0
    discoverability: 53.3
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyerawareapp Com Domain Security
  slug: buyerawareapp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buyerawareapp-com
tags:
- Automotive
- Used Cars
- Vehicle Inspection
- Pricing
- Data Analytics
website: https://buyerawareapp.com/
---
