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
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: 402Oracle Com Agentic Access
  operation_count: 10
  slug: 402oracle-com-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 1
apis:
- baseURL: https://402oracle.com
  baseurl_source: declared
  description: The Verify API from 402 Oracle — 5 operation(s) for verify.
  name: 402 Oracle Verify API
  slug: 402oracle-com-verify-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/402oracle-com/agentic-access/402oracle-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/402oracle-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/402oracle-com/rules/402oracle-com-rules.yml
  title: ''
  type: Spectral
  url: rules/402oracle-com-rules.yml
- group: design
  href: https://artifacts.apis.io/402oracle-com/json-ld/402oracle-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/402oracle-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/402oracle-com/vocabulary/402oracle-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/402oracle-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/402oracle-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/402oracle-com/data-model/402oracle-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/402oracle-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/402oracle-com/errors/402oracle-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/402oracle-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/402oracle-com/conformance/402oracle-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/402oracle-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/402oracle-com/llms/402oracle-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/402oracle-com-llms.txt
- group: other
  href: https://artifacts.apis.io/402oracle-com/hosts/402oracle-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/402oracle-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/402oracle-com/vendors/402oracle-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/402oracle-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/402oracle-com/security/402oracle-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/402oracle-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://402oracle.com/
created: '2026-10-31'
description: 402 Oracle provides independent, cryptographically signed attestations that AI agents can cite before taking actions. It offers verification of business legitimacy, domain authenticity, price accuracy, and URL liveliness, with pay-per-call pricing in USDC on multiple blockchains (Base, Polygon, Arbitrum). The service delivers verifiable trust scores and evidence URLs, supporting bulk verification for vendor screening and fraud prevention, all without requiring accounts or API keys.
json_schemas:
- name: SignedAttestation
  property_count: 2
  slug: 402oracle-com-signed-attestation
jsonld:
- class_count: 3
  name: 402Oracle Com Context
  property_count: 7
  slug: 402oracle-com-context
layout: provider
modified: '2026-10-31'
name: 402 Oracle
nav: Providers
network: true
overview: '402 Oracle publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Verify API. Tagged areas include Verification, Blockchain, Artificial Intelligence, Trust, and Finance.


  The 402 Oracle catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: 402 Oracle API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: 402oracle-com-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 6.4
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 402Oracle Com Domain Security
  slug: 402oracle-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 402oracle-com
tags:
- Verification
- Blockchain
- Artificial Intelligence
- Trust
- Finance
website: https://402oracle.com/
---
