---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
api_count: 2
apis:
- description: Provides local‑first agent intelligence layer with AI integration, data privacy, and operational resilience.
  name: Context Lattice API
  slug: context-lattice-api
- description: 'Context Lattice API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Context Lattice API
  slug: contextlattice-io-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/contextlattice-io/plans/contextlattice-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextlattice-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contextlattice-io/rules/contextlattice-io-rules.yml
  title: ''
  type: Spectral
  url: rules/contextlattice-io-rules.yml
- group: design
  href: https://artifacts.apis.io/contextlattice-io/json-ld/contextlattice-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contextlattice-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/contextlattice-io/vocabulary/contextlattice-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contextlattice-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/contextlattice-io/data-model/contextlattice-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contextlattice-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/contextlattice-io/conformance/contextlattice-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contextlattice-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/contextlattice-io/llms/contextlattice-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextlattice-io-llms.txt
- group: other
  href: https://artifacts.apis.io/contextlattice-io/hosts/contextlattice-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextlattice-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextlattice-io/vendors/contextlattice-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextlattice-io-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://contextlattice.io/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://contextlattice.io/docs/releases/
- group: start
  title: ''
  type: GettingStarted
  url: https://contextlattice.io/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/contextlattice-io/security/contextlattice-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextlattice-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextlattice.io/
coverage:
  checked: '2026-11-04'
  detail: Docs are served as HTML rendered by JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://contextlattice.io/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: Context Lattice provides a local‑first agent intelligence layer that ensures AI agents retain durable continuity, explainable retrieval, portable context, and verified learning across multiple harnesses. The platform enables seamless integration of AI capabilities while preserving data privacy and operational resilience.
image: https://contextlattice.io/assets/social/contextlattice-architecture-social-v2-2026-04-28.png?v=20260428a
json_schemas:
- name: PostMemorySearchRequest
  property_count: 2
  slug: contextlattice-io-post-memory-search-request
- name: PostMemoryWriteRequest
  property_count: 3
  slug: contextlattice-io-post-memory-write-request
jsonld:
- class_count: 2
  name: lattice Io Context
  property_count: 5
  slug: contextlattice-io-context
layout: provider
modified: '2026-11-04'
name: Context Lattice
nav: Providers
network: true
overview: 'Context Lattice is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, Local-First, Intelligence, and Platform.


  The Context Lattice catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Context Lattice''s developer surface includes documentation, changelog, getting-started guide, and 11 more developer resources.'
plans:
- name: Contextlattice Io Plans Pricing
  plan_count: 5
  slug: contextlattice-io-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Context Lattice API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: contextlattice-io-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
  name: Contextlattice Io Domain Security
  slug: contextlattice-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: contextlattice-io
tags:
- Artificial Intelligence
- Agents
- Local-First
- Intelligence
- Platform
website: https://contextlattice.io/
---
