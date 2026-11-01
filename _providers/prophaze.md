---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Prophaze provides an AI‑powered application security platform with APIs for API discovery, security scoring and reporting.
  name: Prophaze API
  slug: prophaze-api-2
- description: 'prophaze API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: prophaze API
  slug: prophaze-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/prophaze/rules/prophaze-rules.yml
  title: ''
  type: Spectral
  url: rules/prophaze-rules.yml
- group: design
  href: https://artifacts.apis.io/prophaze/vocabulary/prophaze-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/prophaze-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/prophaze/changelog/prophaze-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/prophaze-changelog.yml
- group: design
  href: https://artifacts.apis.io/prophaze/conformance/prophaze-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prophaze-conformance.yml
- group: agent
  href: https://artifacts.apis.io/prophaze/llms/prophaze-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prophaze-llms.txt
- group: agent
  href: https://artifacts.apis.io/prophaze/well-known/prophaze-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/prophaze-well-known.yml
- group: other
  href: https://artifacts.apis.io/prophaze/hosts/prophaze-hosts.yml
  title: ''
  type: Hosts
  url: hosts/prophaze-hosts.yml
- group: other
  href: https://artifacts.apis.io/prophaze/vendors/prophaze-vendors.yml
  title: ''
  type: Vendors
  url: vendors/prophaze-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.prophaze.com/waf-onboarding/prophaze-waf-registration
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prophaze.com/
- group: auth
  href: https://artifacts.apis.io/prophaze/security/prophaze-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prophaze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prophaze.com/
created: '2026-10-21'
description: Prophaze provides an AI‑based Web Application and API Protection (WAAP) platform that stops OWASP Top 10, zero‑day attacks, bots, and Layer‑7 DDoS. Backed by 24×7 security analysts, it secures enterprise web traffic and APIs with real‑time threat detection, policy enforcement, and automated response, offering free demos and comprehensive resources for developers and security teams.
layout: provider
modified: '2026-10-21'
name: prophaze
nav: Providers
network: true
overview: 'prophaze is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, AI, WAAP, and Enterprise.


  The prophaze catalog on APIs.io includes 1 Spectral governance ruleset.


  prophaze''s developer surface includes changelog, getting-started guide, documentation, and 9 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: prophaze API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: prophaze-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Prophaze Domain Security
  slug: prophaze-domain-security
  summary_line: DNSSEC · DMARC
slug: prophaze
tags:
- Company
- Security
- AI
- WAAP
- Enterprise
website: https://prophaze.com/
---
