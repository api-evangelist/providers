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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only public API for searching eSIM plans and retrieving catalog data.
  name: AeroCell API
  slug: aerocell-api
- baseURL: https://aerocell.app
  baseurl_source: declared
  description: Live country and multi-country travel eSIM searches from AeroCell (aerocell.app). Public and credential-free. Shared business logic with https://aerocell.app/mcp (Streamable HTTP). Purchases remain on
  name: 'AeroCell: Affordable eSIMs — Read-only API API'
  slug: aerocell-affordable-esims-read-only-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/aerocell-app/rules/aerocell-app-rules.yml
  title: ''
  type: Spectral
  url: rules/aerocell-app-rules.yml
- group: design
  href: https://artifacts.apis.io/aerocell-app/json-ld/aerocell-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aerocell-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/aerocell-app/vocabulary/aerocell-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aerocell-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aerocell-app/conformance/aerocell-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aerocell-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aerocell-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aerocell-app/data-model/aerocell-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aerocell-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/aerocell-app/errors/aerocell-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aerocell-app-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/aerocell-app/llms/aerocell-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aerocell-app-llms.txt
- group: build
  href: https://artifacts.apis.io/aerocell-app/mcp/aerocell-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aerocell-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aerocell-app/mcp/aerocell-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aerocell-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/aerocell-app/hosts/aerocell-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aerocell-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aerocell-app/vendors/aerocell-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aerocell-app-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://aerocell.app/login
- group: auth
  href: https://artifacts.apis.io/aerocell-app/security/aerocell-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerocell-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aerocell.app/
- group: docs
  title: ''
  type: Documentation
  url: https://aerocell.app/developers
- group: company
  title: ''
  type: Blog
  url: https://aerocell.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aerocell.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aerocell.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://aerocell.app/support
- group: commercial
  title: ''
  type: Pricing
  url: https://aerocell.app/plans
created: '2026-10-31'
description: AeroCell provides affordable eSIM data plans for international travelers, covering over 190 countries. The service offers a digital catalogue of prepaid, data‑only eSIM plans with clear pricing, allowances, and validity periods. Users can compare plans, purchase, and instantly activate eSIMs on compatible devices without needing a physical SIM. AeroCell’s platform includes detailed methodology, support resources, and a blog with travel connectivity guides.
image: https://aerocell.app/og-image
json_schemas:
- name: ComparisonCatalog
  property_count: 10
  slug: aerocell-app-comparison-catalog
- name: CountrySearch
  property_count: 8
  slug: aerocell-app-country-search
- name: PartnerComparisonCatalog
  property_count: 11
  slug: aerocell-app-partner-comparison-catalog
- name: PlanDetail
  property_count: 5
  slug: aerocell-app-plan-detail
- name: RegionalSearch
  property_count: 9
  slug: aerocell-app-regional-search
jsonld:
- class_count: 10
  name: Aerocell App Context
  property_count: 45
  slug: aerocell-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at aerocell.app.
  name: AeroCell MCP Server
  slug: aerocell-app-mcp-yml
modified: '2026-10-31'
name: AeroCell
nav: Providers
network: true
overview: 'AeroCell publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including AeroCell: Affordable eSIMs — Read-only API API, and 1 more. Tagged areas include Travel, eSIM, Mobile Data, International, and Connectivity.


  The AeroCell catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AeroCell''s developer surface includes documentation, engineering blog, support, pricing, and 17 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AeroCell API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: aerocell-app-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 50.7
    developer_ergonomics: 10.1
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 33.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerocell App Domain Security
  slug: aerocell-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: find-esim-plans
  slug: aerocell-app-find-esim-plans
slug: aerocell-app
tags:
- Travel
- eSIM
- Mobile Data
- International
- Connectivity
- Telecommunications
website: https://aerocell.app/
---
