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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Chaletiste Fr Agentic Access
  operation_count: 15
  slug: chaletiste-fr-agentic-access
  summary_line: 15 operations · 3 acting
api_count: 1
apis:
- baseURL: https://chaletiste.fr
  baseurl_source: declared
  description: Budget total et formalité d'urbanisme.
  name: Chaletiste Calculs API
  slug: chaletiste-fr-calculs-api
- baseURL: https://chaletiste.fr
  baseurl_source: declared
  description: Fichiers JSON statiques, régénérés chaque nuit.
  name: Chaletiste Données API
  slug: chaletiste-fr-donn-es-api
- baseURL: https://chaletiste.fr
  baseurl_source: declared
  description: Recherche, comparaison et serveur MCP (fonctions serverless).
  name: Chaletiste Recherche API
  slug: chaletiste-fr-recherche-api
- baseURL: https://chaletiste.fr
  baseurl_source: declared
  description: Consentement humain explicite obligatoire.
  name: Chaletiste Transactions API
  slug: chaletiste-fr-transactions-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/chaletiste-fr/agentic-access/chaletiste-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chaletiste-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/rules/chaletiste-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/chaletiste-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/json-ld/chaletiste-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chaletiste-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/vocabulary/chaletiste-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chaletiste-fr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/data-model/chaletiste-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chaletiste-fr-data-model.yml
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/errors/chaletiste-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chaletiste-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chaletiste-fr/conformance/chaletiste-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chaletiste-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chaletiste-fr/llms/chaletiste-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chaletiste-fr-llms.txt
- group: build
  href: https://artifacts.apis.io/chaletiste-fr/mcp/chaletiste-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/chaletiste-fr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/chaletiste-fr/mcp/chaletiste-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chaletiste-fr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/chaletiste-fr/well-known/chaletiste-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chaletiste-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/chaletiste-fr/hosts/chaletiste-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chaletiste-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/chaletiste-fr/vendors/chaletiste-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chaletiste-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chaletiste-fr/security/chaletiste-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chaletiste-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chaletiste.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chaletiste.fr/developpeurs/
- group: docs
  title: ''
  type: Documentation
  url: https://chaletiste.fr/developpeurs/
- group: docs
  title: ''
  type: APIReference
  url: https://chaletiste.fr/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://chaletiste.fr/developpeurs/
- group: agent
  title: ''
  type: llms
  url: https://chaletiste.fr/llms.txt
created: '2026-11-03'
description: Chaletiste is a French platform that aggregates and compares kit chalets, garden shelters, tiny houses and similar wooden structures sold in France. It provides a searchable dataset with prices, dimensions, assembly time, delivery delays and other specifications, all sourced from manufacturers and regularly updated. The site offers an open API delivering product data in JSON and CSV formats, enabling developers to integrate chalet information into their applications or services.
image: https://chaletiste.fr/static/og.png
json_schemas:
- name: Ack
  property_count: 6
  slug: chaletiste-fr-ack
- name: BudgetResponse
  property_count: 7
  slug: chaletiste-fr-budget-response
- name: PermitResponse
  property_count: 7
  slug: chaletiste-fr-permit-response
- name: Product
  property_count: 45
  slug: chaletiste-fr-product
- name: SearchResponse
  property_count: 10
  slug: chaletiste-fr-search-response
jsonld:
- class_count: 7
  name: Chaletiste Fr Context
  property_count: 71
  slug: chaletiste-fr-context
layout: provider
mcp_servers:
- description: Remote MCP server at chaletiste.fr.
  name: Chaletiste MCP Server
  slug: chaletiste-fr-mcp-yml
modified: '2026-11-03'
name: Chaletiste
nav: Providers
network: true
overview: 'Chaletiste publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calculs API, Données API, Recherche API, and 1 more. Tagged areas include Company, Data, Real Estate, Construction, and Open Data.


  The Chaletiste catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chaletiste''s developer surface includes documentation, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Chaletiste API Rules
  rule_count: 54
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 4
  slug: chaletiste-fr-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.4
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chaletiste Fr Domain Security
  slug: chaletiste-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chaletiste-fr
tags:
- Company
- Data
- Real Estate
- Construction
- Open Data
website: https://chaletiste.fr/
---
