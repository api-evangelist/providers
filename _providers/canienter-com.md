---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/canienter-com/rules/canienter-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canienter-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canienter-com/json-ld/canienter-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canienter-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/canienter-com/vocabulary/canienter-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canienter-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/canienter-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/canienter-com/data-model/canienter-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canienter-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/canienter-com/security/canienter-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/canienter-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canienter-com/authentication/canienter-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canienter-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/canienter-com/errors/canienter-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canienter-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/canienter-com/conformance/canienter-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canienter-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canienter-com/llms/canienter-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canienter-com-llms.txt
- group: other
  href: https://artifacts.apis.io/canienter-com/a2a/canienter-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/canienter-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/canienter-com/well-known/canienter-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canienter-com-security.txt
- group: auth
  href: https://artifacts.apis.io/canienter-com/well-known/canienter-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canienter-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/canienter-com/well-known/canienter-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canienter-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canienter-com/hosts/canienter-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canienter-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canienter-com/vendors/canienter-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canienter-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canienter.com/terms
- group: docs
  title: ''
  type: APIReference
  url: https://canienter.com/developers
- group: auth
  href: https://artifacts.apis.io/canienter-com/security/canienter-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canienter-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canienter-com/security/canienter-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canienter-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canienter.com/
created: '2026-11-04'
description: 'canienter-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://canienter.com/og/default.png?v=2026-11-03
jsonld:
- class_count: 7
  name: Canienter Com Context
  property_count: 39
  slug: canienter-com-context
layout: provider
modified: '2026-11-04'
name: canienter-com
nav: Providers
network: true
overview: 'canienter-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Visa checks, Entry requirements, Travel, Data Service, and Immigration.


  The canienter-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  canienter-com''s developer surface includes authentication, API reference, and 19 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: canienter-com API Rules
  rule_count: 52
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 2
  slug: canienter-com-rules
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 38.8
    catalog_earned_first_party: 0.0
    catalog_gap: 76.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 17.3
    discoverability: 39.3
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Canienter Com Authentication
  slug: canienter-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Canienter Com Domain Security
  slug: canienter-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canienter Com Vulnerability Disclosure
  slug: canienter-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: canienter-com-evaluate-visa-trip
  slug: canienter-com-evaluate-visa-trip
slug: canienter-com
tags:
- Visa checks
- Entry requirements
- Travel
- Data Service
- Immigration
website: https://canienter.com/
---
