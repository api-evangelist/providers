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
    mcp_server: false
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
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Crimp API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Crimp API
  slug: crimp-studio-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/crimp-studio/rules/crimp-studio-rules.yml
  title: ''
  type: Spectral
  url: rules/crimp-studio-rules.yml
- group: design
  href: https://artifacts.apis.io/crimp-studio/json-ld/crimp-studio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crimp-studio-context.jsonld
- group: design
  href: https://artifacts.apis.io/crimp-studio/vocabulary/crimp-studio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crimp-studio-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crimp-studio/data-model/crimp-studio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crimp-studio-data-model.yml
- group: design
  href: https://artifacts.apis.io/crimp-studio/conformance/crimp-studio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crimp-studio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crimp-studio/llms/crimp-studio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crimp-studio-llms.txt
- group: other
  href: https://artifacts.apis.io/crimp-studio/hosts/crimp-studio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crimp-studio-hosts.yml
- group: other
  href: https://artifacts.apis.io/crimp-studio/vendors/crimp-studio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crimp-studio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crimp.studio/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crimp.studio/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://crimp.studio/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://crimp.studio/guides/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://crimp.studio/developers/
- group: auth
  href: https://artifacts.apis.io/crimp-studio/security/crimp-studio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crimp-studio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crimp.studio/
coverage:
  checked: '2026-11-04'
  detail: Developer portal provides HTML docs but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract.
  evidence:
  - status: 200
    url: https://crimp.studio/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Crimp provides 12 V and 24 V DC wiring diagram software that lets users plan, size wires and fuses, estimate battery runtime, and run over 130 checks for voltage drop and other issues. The tool is aimed at builders of boat, campervan, RV, over‑land rig and off‑grid cabin electrical systems. It runs in a browser on desktop, tablet or phone and offers a free, no‑account entry mode with optional paid credits for AI assistance and export of printable blueprints.
image: https://crimp.studio/og-default.png
json_schemas:
- name: PostApiAgentToolsRequest
  property_count: 2
  slug: crimp-studio-post-api-agent-tools-request
jsonld:
- class_count: 1
  name: Crimp Studio Context
  property_count: 2
  slug: crimp-studio-context
layout: provider
modified: '2026-11-04'
name: Crimp
nav: Providers
network: true
overview: 'Crimp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wiring Diagram Software, 12V Systems, Marine Electrical, Campervan, and Off-grid.


  The Crimp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crimp''s developer surface includes pricing, documentation, and 13 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 73
  extends:
  - spectral:oas
  name: Crimp API Rules
  rule_count: 32
  severity_counts:
    error: 30
    hint: 0
    info: 1
    warn: 1
  slug: crimp-studio-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 35.6
    contract_quality: 17.6
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crimp Studio Domain Security
  slug: crimp-studio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crimp-studio
tags:
- Wiring Diagram Software
- 12V Systems
- Marine Electrical
- Campervan
- Off-grid
- Electrical Simulation
website: https://crimp.studio/
---
