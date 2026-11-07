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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cervejabarata Com Br Agentic Access
  operation_count: 27
  slug: cervejabarata-com-br-agentic-access
  summary_line: 27 operations · 10 acting
api_count: 1
apis:
- baseURL: https://cervejabarata.com.br
  baseurl_source: declared
  description: The datasets API from Cerveja Barata — 12 operation(s) for datasets.
  name: Cerveja Barata Datasets API
  slug: cervejabarata-com-br-datasets-api
- baseURL: https://cervejabarata.com.br
  baseurl_source: declared
  description: The mcp API from Cerveja Barata — 1 operation(s) for mcp.
  name: Cerveja Barata MCP API
  slug: cervejabarata-com-br-mcp-api
- baseURL: https://cervejabarata.com.br
  baseurl_source: declared
  description: The public API from Cerveja Barata — 13 operation(s) for public.
  name: Cerveja Barata Public API
  slug: cervejabarata-com-br-public-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/cervejabarata-com-br/agentic-access/cervejabarata-com-br-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cervejabarata-com-br-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/rules/cervejabarata-com-br-rules.yml
  title: ''
  type: Spectral
  url: rules/cervejabarata-com-br-rules.yml
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/json-ld/cervejabarata-com-br-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cervejabarata-com-br-context.jsonld
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/vocabulary/cervejabarata-com-br-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cervejabarata-com-br-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/data-model/cervejabarata-com-br-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cervejabarata-com-br-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cervejabarata-com-br/changelog/cervejabarata-com-br-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cervejabarata-com-br-changelog.yml
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/errors/cervejabarata-com-br-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cervejabarata-com-br-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cervejabarata-com-br/conformance/cervejabarata-com-br-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cervejabarata-com-br-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cervejabarata-com-br/llms/cervejabarata-com-br-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cervejabarata-com-br-llms.txt
- group: agent
  href: https://artifacts.apis.io/cervejabarata-com-br/mcp/cervejabarata-com-br-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cervejabarata-com-br-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cervejabarata-com-br/well-known/cervejabarata-com-br-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cervejabarata-com-br-well-known.yml
- group: other
  href: https://artifacts.apis.io/cervejabarata-com-br/hosts/cervejabarata-com-br-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cervejabarata-com-br-hosts.yml
- group: other
  href: https://artifacts.apis.io/cervejabarata-com-br/vendors/cervejabarata-com-br-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cervejabarata-com-br-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cervejabarata.com.br/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cervejabarata.com.br/en/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cervejabarata.com.br/en/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://cervejabarata.com.br/en/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://cervejabarata.com.br/en/developers
- group: auth
  href: https://artifacts.apis.io/cervejabarata-com-br/security/cervejabarata-com-br-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cervejabarata-com-br-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cervejabarata.com.br/
created: '2026-11-03'
description: Cerveja Barata provides a map of the cheapest beer prices across bars, supermarkets and depots in Brazil, currently covering Salvador and Lauro de Freitas. The site lists thousands of price entries, updated regularly, offering users detailed price per liter information and helping them find the best deals in their city.
image: https://cervejabarata.com.br/og/share-pt.png
json_schemas:
- name: BarOwnerRequest
  property_count: 9
  slug: cervejabarata-com-br-bar-owner-request
- name: CityRequest
  property_count: 5
  slug: cervejabarata-com-br-city-request
- name: DealsResponse
  property_count: 8
  slug: cervejabarata-com-br-deals-response
- name: MenuPhotoUpload
  property_count: 8
  slug: cervejabarata-com-br-menu-photo-upload
- name: PriceUpdateRequest
  property_count: 9
  slug: cervejabarata-com-br-price-update-request
- name: Submission
  property_count: 25
  slug: cervejabarata-com-br-submission
jsonld:
- class_count: 21
  name: Cervejabarata Com Br Context
  property_count: 84
  slug: cervejabarata-com-br-context
layout: provider
mcp_servers:
- description: Remote MCP server at cervejabarata.com.br.
  name: Cerveja Barata MCP Server
  slug: cervejabarata-com-br-mcp-yml
modified: '2026-11-03'
name: Cerveja Barata
nav: Providers
network: true
overview: 'Cerveja Barata publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Datasets API, MCP API, and Public API. Tagged areas include Beer, Price Comparison, Brazil, Salvador, and LauroDeFreitas.


  The Cerveja Barata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cerveja Barata''s developer surface includes changelog, API reference, and 18 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Cerveja Barata API Rules
  rule_count: 49
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 8
  slug: cervejabarata-com-br-rules
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 59.3
    developer_ergonomics: 3.6
    discoverability: 65.8
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
  name: Cervejabarata Com Br Domain Security
  slug: cervejabarata-com-br-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cervejabarata-com-br
tags:
- Beer
- Price Comparison
- Brazil
- Salvador
- LauroDeFreitas
website: https://cervejabarata.com.br/
---
