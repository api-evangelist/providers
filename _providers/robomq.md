---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: RoboMQ provides a cloud‑based workforce lifecycle management and identity governance platform with integrations for HR and identity systems.
  name: RoboMQ API
  slug: robomq-api-2
- description: 'RoboMQ API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: RoboMQ API
  slug: robomq-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/robomq/plans/robomq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/robomq-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/robomq/rules/robomq-rules.yml
  title: ''
  type: Spectral
  url: rules/robomq-rules.yml
- group: design
  href: https://artifacts.apis.io/robomq/vocabulary/robomq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/robomq-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/robomq/changelog/robomq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/robomq-changelog.yml
- group: design
  href: https://artifacts.apis.io/robomq/conformance/robomq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/robomq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/robomq/llms/robomq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/robomq-llms.txt
- group: agent
  href: https://artifacts.apis.io/robomq/well-known/robomq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/robomq-well-known.yml
- group: other
  href: https://artifacts.apis.io/robomq/hosts/robomq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/robomq-hosts.yml
- group: other
  href: https://artifacts.apis.io/robomq/vendors/robomq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/robomq-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.robomq.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.robomq.io/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.robomq.io/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.robomq.io/news/
- group: company
  title: ''
  type: Blog
  url: https://www.robomq.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.robomq.io/Application/Paycom_Onboarding_Basic_Auth/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.robomq.io/
- group: auth
  href: https://artifacts.apis.io/robomq/security/robomq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/robomq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robomq.io/
coverage:
  checked: '2026-10-21'
  detail: Docs site renders via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://docs.robomq.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: RoboMQ offers a cloud‑based workforce lifecycle management and identity governance platform. It automates hiring, onboarding, role changes, and offboarding across HR systems, providing real‑time provisioning, access control, and compliance reporting. The service integrates with major HR and identity providers, delivering low‑latency, high‑throughput automation for enterprise HR and IT operations, helping organizations reduce manual workload and improve security.
image: https://www.robomq.io/wp-content/uploads/2023/11/RoboMQ-Featured-Image.webp
layout: provider
modified: '2026-10-21'
name: RoboMQ
nav: Providers
network: true
overview: 'RoboMQ is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, Cloud, Event-Driven, IoT, and Integration.


  The RoboMQ catalog on APIs.io includes 1 Spectral governance ruleset.


  RoboMQ''s developer surface includes changelog, pricing, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Robomq Plans Pricing
  plan_count: 1
  slug: robomq-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: RoboMQ API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: robomq-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 23.8
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Robomq Domain Security
  slug: robomq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: robomq
tags:
- Messaging
- Cloud
- Event-Driven
- IoT
- Integration
website: https://robomq.io/
---
