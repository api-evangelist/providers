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
  band: agent-ready
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'REST API v1.1: list blank products, create campaigns, place orders, test mode available.'
  name: Hoplix Print-on-Demand API
  slug: hoplix-print-on-demand-api
- baseURL: https://api.hoplix.com
  baseurl_source: declared
  description: 'REST API of Hoplix, an Italian print-on-demand and dropshipping platform: read the catalog of 230+ blank products, create campaigns with your designs, place orders that Hoplix prints and ships worldwi'
  name: Hoplix Print-on-Demand API V1 API
  slug: hoplix-print-on-demand-api-v1-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/hoplix-com/rules/hoplix-com-rules.yml
  title: ''
  type: Spectral
  url: rules/hoplix-com-rules.yml
- group: design
  href: https://artifacts.apis.io/hoplix-com/json-ld/hoplix-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hoplix-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/hoplix-com/vocabulary/hoplix-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hoplix-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hoplix-com/conformance/hoplix-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hoplix-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/hoplix-com/data-model/hoplix-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hoplix-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/hoplix-com/llms/hoplix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hoplix-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/hoplix-com/mcp/hoplix-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hoplix-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hoplix-com/well-known/hoplix-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hoplix-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hoplix-com/hosts/hoplix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hoplix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hoplix-com/vendors/hoplix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hoplix-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hoplix.com/it/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hoplix.com/it/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://hoplix.com/en/custom/news/8
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hoplix.shop/
- group: auth
  href: https://artifacts.apis.io/hoplix-com/security/hoplix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hoplix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hoplix.com
- group: docs
  title: ''
  type: Documentation
  url: https://hoplix.com/api/v1/documentation
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://hoplix.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Hoplix is an Italian print‑on‑demand and dropshipping platform. Sellers, brands and creators put their designs on over 230 blank products such as t‑shirts, hoodies, mugs, bags and phone cases, sell them via their own store or marketplaces, and Hoplix prints and ships every order worldwide. The company provides a REST API (v1.1, OpenAPI 3.1) for catalog, campaigns and orders, including a test mode and an official remote MCP server for AI assistants.
image: https://hoplix.com/img/og-hoplix.png
json_schemas:
- name: CampaignInput
  property_count: 14
  slug: hoplix-com-campaign-input
- name: Campaign
  property_count: 8
  slug: hoplix-com-campaign
- name: CampaignSummary
  property_count: 9
  slug: hoplix-com-campaign-summary
- name: OrderInfo
  property_count: 9
  slug: hoplix-com-order-info
- name: OrderInput
  property_count: 6
  slug: hoplix-com-order-input
- name: Product
  property_count: 11
  slug: hoplix-com-product
jsonld:
- class_count: 13
  name: Hoplix Com Context
  property_count: 56
  slug: hoplix-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.hoplix.com.
  name: Hoplix MCP Server
  slug: hoplix-com-mcp-yml
modified: '2026-11-05'
name: Hoplix
nav: Providers
network: true
overview: 'Hoplix publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Print-on-Demand API V1 API, and 1 more. Tagged areas include Company, Print on Demand, Dropshipping, E-Commerce, and Merchandise.


  The Hoplix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hoplix''s developer surface includes documentation and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Hoplix API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: hoplix-com-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 19.0
    discoverability: 66.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
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
  name: Hoplix Com Domain Security
  slug: hoplix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hoplix-com
tags:
- Company
- Print on Demand
- Dropshipping
- E-Commerce
- Merchandise
website: https://hoplix.com
---
