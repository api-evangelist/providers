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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'aeoess API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: aeoess API
  slug: aeoess-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/aeoess-com/rules/aeoess-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aeoess-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aeoess-com/vocabulary/aeoess-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aeoess-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://aeoess.com/contact.html#security
- group: design
  href: https://artifacts.apis.io/aeoess-com/conformance/aeoess-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeoess-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aeoess-com/llms/aeoess-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeoess-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/aeoess-com/well-known/aeoess-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aeoess-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aeoess-com/well-known/aeoess-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aeoess-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aeoess-com/hosts/aeoess-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aeoess-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aeoess-com/vendors/aeoess-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aeoess-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aeoess.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeoess.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/aeoess-com/security/aeoess-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aeoess-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aeoess-com/security/aeoess-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeoess-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aeoess.com/
created: '2026-10-31'
description: aeoess is an open‑source governance operating system for AI agents, providing an Agent Passport System that defines authority, delegation, and enforcement semantics. The platform offers tools for verifiable agent identity, cryptographic delegation, and compliance testing, enabling secure interactions between agents and organizations. It includes the Model Citizen pilot, the Mingle service for people discovery, and a suite of open tests for authority conformance, all under the Apache 2.0 license.
layout: provider
modified: '2026-10-31'
name: aeoess
nav: Providers
network: true
overview: 'aeoess is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Governance, Open Source, AgentAuthority, and Platform.


  The aeoess catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: aeoess API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: aeoess-com-rules
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 5.3
  previous_composite: 17.1
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeoess Com Domain Security
  slug: aeoess-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Aeoess Com Vulnerability Disclosure
  slug: aeoess-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aeoess-com
tags:
- Artificial Intelligence
- Governance
- Open Source
- AgentAuthority
- Platform
website: https://aeoess.com/
---
