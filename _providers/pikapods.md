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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'PikaPods API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: PikaPods API
  slug: pikapods-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/pikapods/rules/pikapods-rules.yml
  title: ''
  type: Spectral
  url: rules/pikapods-rules.yml
- group: design
  href: https://artifacts.apis.io/pikapods/vocabulary/pikapods-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pikapods-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/pikapods/security/pikapods-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pikapods-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/pikapods/conformance/pikapods-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pikapods-conformance.yml
- group: auth
  href: https://artifacts.apis.io/pikapods/well-known/pikapods-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pikapods-security.txt
- group: agent
  href: https://artifacts.apis.io/pikapods/well-known/pikapods-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pikapods-well-known.yml
- group: other
  href: https://artifacts.apis.io/pikapods/hosts/pikapods-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pikapods-hosts.yml
- group: other
  href: https://artifacts.apis.io/pikapods/vendors/pikapods-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pikapods-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pikapods.com/tos
- group: start
  title: ''
  type: SignUp
  url: https://www.pikapods.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pikapods.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pikapods.com/manage/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pikapods.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pikapods
- group: auth
  href: https://artifacts.apis.io/pikapods/security/pikapods-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pikapods-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pikapods/security/pikapods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pikapods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pikapods.com/
coverage:
  checked: '2026-10-26'
  detail: Documentation is served as HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.pikapods.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: PikaPods provides a platform for managing and distributing smart pet accessories, focusing on IoT-enabled pet care solutions. The company offers APIs for device provisioning, real-time telemetry, and integration with third‑party services such as payment processors and analytics platforms. Their services aim to simplify pet owners’ interaction with smart devices, enabling automated feeding, health monitoring, and activity tracking through a unified developer experience.
image: https://www.pikapods.com/static/og_image-v2.jpg
layout: provider
modified: '2026-10-26'
name: PikaPods
nav: Providers
network: true
overview: 'PikaPods is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, PetTech, SmartDevices, and APIPlatform.


  The PikaPods catalog on APIs.io includes 1 Spectral governance ruleset.


  PikaPods'' developer surface includes signup flow, getting-started guide, documentation, and 14 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: PikaPods API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: pikapods-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 21.4
    discoverability: 57.1
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
  name: Pikapods Domain Security
  slug: pikapods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pikapods Vulnerability Disclosure
  slug: pikapods-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pikapods
tags:
- Company
- IoT
- PetTech
- SmartDevices
- APIPlatform
website: https://www.pikapods.com/
---
