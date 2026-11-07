---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Balancos Ai Agentic Access
  operation_count: 33
  slug: balancos-ai-agentic-access
  summary_line: 33 operations
api_count: 1
apis:
- baseURL: https://api.balancos.ai/v1
  baseurl_source: declared
  description: The BCB API from Balanços.AI — 9 operation(s) for bcb.
  name: Balanços.AI BCB API
  slug: balancos-ai-bcb-api
- baseURL: https://api.balancos.ai/v1
  baseurl_source: declared
  description: The CVM API from Balanços.AI — 18 operation(s) for cvm.
  name: Balanços.AI CVM API
  slug: balancos-ai-cvm-api
- baseURL: https://api.balancos.ai/v1
  baseurl_source: declared
  description: The Empresas API from Balanços.AI — 6 operation(s) for empresas.
  name: Balanços.AI Empresas API
  slug: balancos-ai-empresas-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/balancos-ai/agentic-access/balancos-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/balancos-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/balancos-ai/rules/balancos-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/balancos-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/balancos-ai/json-ld/balancos-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/balancos-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/balancos-ai/vocabulary/balancos-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/balancos-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/balancos-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/balancos-ai/data-model/balancos-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/balancos-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/balancos-ai/authentication/balancos-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/balancos-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/balancos-ai/errors/balancos-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/balancos-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/balancos-ai/conformance/balancos-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/balancos-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/balancos-ai/llms/balancos-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/balancos-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/balancos-ai/hosts/balancos-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/balancos-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/balancos-ai/vendors/balancos-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/balancos-ai-vendors.yml
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/48690591-fd6c01ed-d42b-4d2c-a958-6eddebebcb42?action=collection%2Ffork&source=rip_markdown
- group: start
  title: ''
  type: Login
  url: https://balancos.ai/login
- group: docs
  title: ''
  type: APIReference
  url: https://balancos.ai/api/docs
- group: auth
  href: https://artifacts.apis.io/balancos-ai/security/balancos-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/balancos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://balancos.ai/
- group: company
  title: ''
  type: Blog
  url: https://balancos.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://balancos.ai/documentos
created: '2026-11-02'
description: Balanços.AI provides free public access to Brazilian companies' financial statements, balance sheets (Balanços), income statements (DREs) and historical series. The portal aggregates structured data from official sources, offering searchable, traceable documents without registration, paywalls, or query limits. Users can explore over 38,000 companies and 333,000 documents, with up-to-date collections refreshed daily. The service also includes an AI assistant for data queries and integrates with MCP for automated workflows.
image: https://balancos.ai/og-image-v2.png
json_schemas:
- name: EnvelopeCatalogo
  property_count: 2
  slug: balancos-ai-apps-api-bcb-modelos-envelope-catalogo
- name: EnvelopeRanking
  property_count: 2
  slug: balancos-ai-apps-api-bcb-modelos-envelope-ranking
- name: EnvelopeBalancos
  property_count: 2
  slug: balancos-ai-apps-api-cvm-modelos-envelope-balancos
- name: EnvelopeCatalogo
  property_count: 2
  slug: balancos-ai-apps-api-cvm-modelos-envelope-catalogo
- name: EnvelopeRanking
  property_count: 2
  slug: balancos-ai-apps-api-cvm-modelos-envelope-ranking
- name: EnvelopeBalancos
  property_count: 2
  slug: balancos-ai-apps-api-modelos-envelope-balancos
jsonld:
- class_count: 114
  name: Balancos Ai Context
  property_count: 203
  slug: balancos-ai-context
layout: provider
modified: '2026-11-02'
name: Balanços.AI
nav: Providers
network: true
overview: 'Balanços.AI publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: BCB API, CVM API, and Empresas API. Tagged areas include Finance, Brazil, Public Data, and Financial Statements.


  The Balanços.AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Balanços.AI''s developer surface includes authentication, API reference, engineering blog, documentation, and 15 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 0
  name: Balancos Ai Rate Limits
  slug: balancos-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Balanços.AI API Rules
  rule_count: 47
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 3
  slug: balancos-ai-rules
scopes:
- name: Balancos Ai Scopes
  scope_count: 0
  slug: balancos-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 55.9
    developer_ergonomics: 30.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Balancos Ai Authentication
  slug: balancos-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Balancos Ai Domain Security
  slug: balancos-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: balances
  slug: balancos-ai-balances
- name: company-profile
  slug: balancos-ai-company-profile
- name: documents
  slug: balancos-ai-documents
- name: income-statements
  slug: balancos-ai-income-statements
- name: search-companies
  slug: balancos-ai-search-companies
slug: balancos-ai
tags:
- Finance
- Brazil
- Public Data
- Financial Statements
website: https://balancos.ai/
---
