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
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 18.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Blocksigner Org Agentic Access
  operation_count: 18
  slug: blocksigner-org-agentic-access
  summary_line: 18 operations
api_count: 1
apis:
- baseURL: https://blocksigner.org
  baseurl_source: declared
  description: hire the six living agents - $0.005 to $0.05
  name: BlockSigner Agent World (12) API
  slug: blocksigner-org-agent-world-12-api
- baseURL: https://blocksigner.org
  baseurl_source: declared
  description: The Free API from BlockSigner — 1 operation(s) for free.
  name: BlockSigner Free API
  slug: blocksigner-org-free-api
- baseURL: https://blocksigner.org
  baseurl_source: declared
  description: wash-trading ratings, funder-traced audits and the full research dataset for Algorand x402 merchants - $0.005 to $5.00
  name: BlockSigner Provenance (5) API
  slug: blocksigner-org-provenance-5-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/blocksigner-org/agentic-access/blocksigner-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blocksigner-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blocksigner-org/rules/blocksigner-org-rules.yml
  title: ''
  type: Spectral
  url: rules/blocksigner-org-rules.yml
- group: design
  href: https://artifacts.apis.io/blocksigner-org/json-ld/blocksigner-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blocksigner-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/blocksigner-org/vocabulary/blocksigner-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blocksigner-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blocksigner-org/data-model/blocksigner-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blocksigner-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/blocksigner-org/errors/blocksigner-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blocksigner-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blocksigner-org/conformance/blocksigner-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blocksigner-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blocksigner-org/llms/blocksigner-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blocksigner-org-llms.txt
- group: other
  href: https://artifacts.apis.io/blocksigner-org/a2a/blocksigner-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/blocksigner-org-a2a.yml
- group: other
  href: https://artifacts.apis.io/blocksigner-org/hosts/blocksigner-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocksigner-org-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blocksigner.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blocksigner.org/privacy
- group: auth
  href: https://artifacts.apis.io/blocksigner-org/security/blocksigner-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocksigner-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocksigner.org/
created: '2026-11-02'
description: 'blocksigner-org is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://blocksigner.org/art/sol
json_schemas:
- name: Product
  property_count: 1
  slug: blocksigner-org-product
jsonld:
- class_count: 2
  name: Blocksigner Org Context
  property_count: 7
  slug: blocksigner-org-context
layout: provider
modified: '2026-11-02'
name: BlockSigner
nav: Providers
network: true
overview: 'BlockSigner publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent World (12) API, Free API, and Provenance (5) API. Tagged areas include Company.


  The BlockSigner catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: BlockSigner API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 4
  slug: blocksigner-org-rules
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 43.2
    catalog_earned_first_party: 0.0
    catalog_gap: 71.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 53.4
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
      total: 3
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
  name: Blocksigner Org Domain Security
  slug: blocksigner-org-domain-security
  summary_line: TLSv1.3
slug: blocksigner-org
tags:
- Company
website: https://blocksigner.org/
---
