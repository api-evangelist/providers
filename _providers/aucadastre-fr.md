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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API providing French cadastral and urban planning data.
  name: Aucadastre API
  slug: aucadastre-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/rules/aucadastre-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/aucadastre-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/json-ld/aucadastre-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aucadastre-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/vocabulary/aucadastre-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aucadastre-fr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/data-model/aucadastre-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aucadastre-fr-data-model.yml
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/errors/aucadastre-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aucadastre-fr-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/aucadastre-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aucadastre-fr/conformance/aucadastre-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aucadastre-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aucadastre-fr/llms/aucadastre-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aucadastre-fr-llms.txt
- group: build
  href: https://artifacts.apis.io/aucadastre-fr/mcp/aucadastre-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aucadastre-fr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aucadastre-fr/mcp/aucadastre-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aucadastre-fr-mcp.yml
- group: other
  href: https://artifacts.apis.io/aucadastre-fr/hosts/aucadastre-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aucadastre-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/aucadastre-fr/vendors/aucadastre-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aucadastre-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aucadastre-fr/security/aucadastre-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aucadastre-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aucadastre.fr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aucadastre.fr/api
- group: docs
  title: ''
  type: Documentation
  url: https://aucadastre.fr/api
- group: docs
  title: ''
  type: APIReference
  url: https://aucadastre.fr/api
- group: start
  title: ''
  type: GettingStarted
  url: https://aucadastre.fr/api
created: '2026-11-02'
description: Aucadastre provides free public access to French cadastral and urban planning data. Users can query address parcels, commune information, building permits, and zoning details without authentication or quota. The service returns JSON data sourced from official French datasets, offering details on parcel size, land use, construction permits, and associated risks. All data is openly available and the API is documented at https://aucadastre.fr/api.
image: https://aucadastre.fr/apple-touch-icon.png
jsonld:
- class_count: 12
  name: Aucadastre Fr Context
  property_count: 121
  slug: aucadastre-fr-context
layout: provider
mcp_servers:
- description: Remote MCP server at aucadastre.fr.
  name: Aucadastre MCP Server
  slug: aucadastre-fr-mcp-yml
modified: '2026-11-02'
name: Aucadastre
nav: Providers
network: true
overview: 'Aucadastre publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include cadastre, urbanisme, Geospatial, France, and Public Data.


  The Aucadastre catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Aucadastre''s developer surface includes documentation, API reference, getting-started guide, and 15 more developer resources.'
plans:
- name: Aucadastre Fr Plans Pricing
  plan_count: 0
  slug: aucadastre-fr-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Aucadastre Fr Rate Limits
  slug: aucadastre-fr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Aucadastre API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: aucadastre-fr-rules
scopes:
- name: Aucadastre Fr Scopes
  scope_count: 0
  slug: aucadastre-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 22.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aucadastre Fr Authentication
  slug: aucadastre-fr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aucadastre Fr Domain Security
  slug: aucadastre-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: getting-started
  slug: aucadastre-fr-getting_started
slug: aucadastre-fr
tags:
- cadastre
- urbanisme
- Geospatial
- France
- Public Data
website: https://aucadastre.fr/
---
