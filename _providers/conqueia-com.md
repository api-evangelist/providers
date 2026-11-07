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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Conqueia Com Agentic Access
  operation_count: 2
  slug: conqueia-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://conqueia.com
  baseurl_source: declared
  description: Buscar fichas y leerlas enteras.
  name: conqueia-com Directorio API
  slug: conqueia-com-directorio-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/conqueia-com/agentic-access/conqueia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/conqueia-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/conqueia-com/rules/conqueia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/conqueia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/conqueia-com/json-ld/conqueia-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/conqueia-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/conqueia-com/vocabulary/conqueia-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/conqueia-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/conqueia-com/data-model/conqueia-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/conqueia-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/conqueia-com/errors/conqueia-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/conqueia-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/conqueia-com/conformance/conqueia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conqueia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/conqueia-com/llms/conqueia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conqueia-com-llms.txt
- group: other
  href: https://artifacts.apis.io/conqueia-com/hosts/conqueia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conqueia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/conqueia-com/vendors/conqueia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conqueia-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/conqueia-com/security/conqueia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conqueia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conqueia.com/
created: '2026-11-04'
description: 'conqueia-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://conqueia.com/opengraph-image?42607533e1b0f305
json_schemas:
- name: Ficha
  property_count: 10
  slug: conqueia-com-ficha
- name: RespuestaBusqueda
  property_count: 5
  slug: conqueia-com-respuesta-busqueda
jsonld:
- class_count: 4
  name: Conqueia Com Context
  property_count: 17
  slug: conqueia-com-context
layout: provider
modified: '2026-11-04'
name: conqueia-com
nav: Providers
network: true
overview: 'conqueia-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Directorio API. Tagged areas include Artificial Intelligence and Skills.


  The conqueia-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: conqueia-com API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: conqueia-com-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.5
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Conqueia Com Domain Security
  slug: conqueia-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: conqueia-com
tags:
- Artificial Intelligence
- Skills
website: https://conqueia.com/
---
