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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Company intelligence API
  name: echoloc
  slug: echoloc
- baseURL: https://api.echoloc.ai
  baseurl_source: declared
  description: Company intelligence API — technographics with adoption context (adopting / replacing / evaluating), hiring activity, and firmographics for 800K+ companies. External clients use the Corporate API unde
  name: echoloc API API
  slug: echoloc-api-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/echoloc-ai/rules/echoloc-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/echoloc-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/echoloc-ai/json-ld/echoloc-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/echoloc-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/echoloc-ai/vocabulary/echoloc-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/echoloc-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/echoloc-ai/conformance/echoloc-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/echoloc-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/echoloc-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/echoloc-ai/data-model/echoloc-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/echoloc-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/echoloc-ai/errors/echoloc-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/echoloc-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/echoloc-ai/llms/echoloc-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/echoloc-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/echoloc-ai/mcp/echoloc-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/echoloc-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/echoloc-ai/hosts/echoloc-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/echoloc-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/echoloc-ai/vendors/echoloc-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/echoloc-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/echoloc-ai/security/echoloc-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/echoloc-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://echoloc.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://echoloc.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://echoloc.ai/about/
- group: docs
  title: ''
  type: APIReference
  url: https://echoloc.ai/api
- group: commercial
  title: ''
  type: Pricing
  url: https://echoloc.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://echoloc.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://echoloc.ai/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://echoloc.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://echoloc.ai/about/
- group: docs
  title: ''
  type: APIReference
  url: https://echoloc.ai/api
- group: commercial
  title: ''
  type: Pricing
  url: https://echoloc.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://echoloc.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://echoloc.ai/privacy
created: '2026-11-06'
description: Echoloc is a company‑intelligence platform that helps B2B sales, research, and partnership teams discover and understand companies by the technologies they use, the problems they solve, and the projects they are building. It aggregates public signals such as hiring data, tech stacks, and company‑issued research to provide evidence‑based technographic and intent data via an API for enrichment and data licensing.
json_schemas:
- name: CorporateCompany
  property_count: 18
  slug: echoloc-ai-corporate-company
- name: ExportV2Request
  property_count: 13
  slug: echoloc-ai-export-v2-request
- name: SaveFromSearchV2Request
  property_count: 14
  slug: echoloc-ai-save-from-search-v2-request
- name: SearchV2Request
  property_count: 16
  slug: echoloc-ai-search-v2-request
- name: TechSearchRequest
  property_count: 9
  slug: echoloc-ai-tech-search-request
- name: TechSearchResponse
  property_count: 11
  slug: echoloc-ai-tech-search-response
jsonld:
- class_count: 23
  name: Echoloc Ai Context
  property_count: 71
  slug: echoloc-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.echoloc.ai.
  name: Echoloc MCP Server
  slug: echoloc-ai-mcp-yml
modified: '2026-11-06'
name: Echoloc
nav: Providers
network: true
overview: 'Echoloc publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include B2B, Data, Intelligence, and Technographics.


  The Echoloc catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Echoloc''s developer surface includes documentation, API reference, pricing, and 22 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Echoloc API Rules
  rule_count: 50
  severity_counts:
    error: 39
    hint: 0
    info: 4
    warn: 7
  slug: echoloc-ai-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 28.0
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Echoloc Ai Domain Security
  slug: echoloc-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-company
  slug: echoloc-ai-get-company
slug: echoloc-ai
tags:
- B2B
- Data
- Intelligence
- Technographics
website: https://echoloc.ai/
---
