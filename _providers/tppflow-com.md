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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tppflow Com Agentic Access
  operation_count: 16
  slug: tppflow-com-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- description: The cbp API from tppflow-com — 1 operation(s) for cbp.
  name: tppflow-com Cbp API
  slug: tppflow-com-cbp-api
- description: The faa API from tppflow-com — 2 operation(s) for faa.
  name: tppflow-com Faa API
  slug: tppflow-com-faa-api
- description: The fcc API from tppflow-com — 2 operation(s) for fcc.
  name: tppflow-com Fcc API
  slug: tppflow-com-fcc-api
- description: The fda API from tppflow-com — 1 operation(s) for fda.
  name: tppflow-com Fda API
  slug: tppflow-com-fda-api
- description: The meta API from tppflow-com — 1 operation(s) for meta.
  name: tppflow-com Meta API
  slug: tppflow-com-meta-api
- description: The nppes API from tppflow-com — 2 operation(s) for nppes.
  name: tppflow-com Nppes API
  slug: tppflow-com-nppes-api
- description: The rrc API from tppflow-com — 3 operation(s) for rrc.
  name: tppflow-com Rrc API
  slug: tppflow-com-rrc-api
- description: The toll API from tppflow-com — 1 operation(s) for toll.
  name: tppflow-com Toll API
  slug: tppflow-com-toll-api
- description: The usda API from tppflow-com — 1 operation(s) for usda.
  name: tppflow-com Usda API
  slug: tppflow-com-usda-api
- description: The warn API from tppflow-com — 2 operation(s) for warn.
  name: tppflow-com Warn API
  slug: tppflow-com-warn-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/tppflow-com/overlays/tppflow-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tppflow-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tppflow-com/llms/tppflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tppflow-com-llms.txt
- group: other
  href: https://artifacts.apis.io/tppflow-com/vendors/tppflow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tppflow-com-vendors.yml
- group: agent
  href: https://artifacts.apis.io/tppflow-com/agentic-access/tppflow-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tppflow-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/tppflow-com/rules/tppflow-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tppflow-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tppflow-com/json-ld/tppflow-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tppflow-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tppflow-com/vocabulary/tppflow-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tppflow-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tppflow-com/data-model/tppflow-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tppflow-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/tppflow-com/errors/tppflow-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tppflow-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tppflow-com/conformance/tppflow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tppflow-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/tppflow-com/hosts/tppflow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tppflow-com-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://tppflow.com/
- group: auth
  href: https://artifacts.apis.io/tppflow-com/security/tppflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tppflow-com-domain-security.yml
coverage:
  checked: '2026-10-30'
  detail: OpenAPI spec found but cannot be verified as belonging to tppflow.com
  evidence:
  - status: 200
    url: https://api.tppflow.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: tppflow-com is a stub entry in the API Evangelist catalog, originating from the MCP registry harvest. The company’s public presence and API offerings are currently undocumented, and no verifiable website or API documentation has been identified. This profile aims to gather accurate identity information, including a proper description, tags, and link properties, once reliable sources become available.
json_schemas:
- name: AircraftRecord
  property_count: 9
  slug: tppflow-com-aircraft-record
- name: FccLicense
  property_count: 7
  slug: tppflow-com-fcc-license
- name: NppesProvider
  property_count: 8
  slug: tppflow-com-nppes-provider
- name: Price
  property_count: 7
  slug: tppflow-com-price
- name: Shortage
  property_count: 6
  slug: tppflow-com-shortage
- name: WellboresResponse
  property_count: 7
  slug: tppflow-com-wellbores-response
jsonld:
- class_count: 18
  name: Tppflow Com Context
  property_count: 92
  slug: tppflow-com-context
layout: provider
modified: '2026-10-30'
name: tppflow-com
nav: Providers
network: true
overview: 'tppflow-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cbp API, Faa API, Fcc API, and 7 more. Tagged areas include Company, Data, and Analytics.


  The tppflow-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: tppflow-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: tppflow-com-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 52.1
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/tppflow-com/tppflow-com-2026-11-03T144936.png
security:
- kind: domain-security
  name: Tppflow Com Domain Security
  slug: tppflow-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tppflow-com
tags:
- Company
- Data
- Analytics
website: https://tppflow.com/
---
