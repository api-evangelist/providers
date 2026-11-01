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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.nuki.io
  baseurl_source: declared
  description: 'Nuki API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Nuki API
  slug: nuki-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/nuki/vendors/nuki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nuki-vendors.yml
- group: design
  href: https://artifacts.apis.io/nuki/rules/nuki-rules.yml
  title: ''
  type: Spectral
  url: rules/nuki-rules.yml
- group: design
  href: https://artifacts.apis.io/nuki/vocabulary/nuki-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nuki-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nuki/conformance/nuki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nuki-conformance.yml
- group: auth
  href: https://artifacts.apis.io/nuki/well-known/nuki-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuki-status-security.txt
- group: auth
  href: https://artifacts.apis.io/nuki/well-known/nuki-shop-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuki-shop-security.txt
- group: auth
  href: https://artifacts.apis.io/nuki/well-known/nuki-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nuki-security.txt
- group: agent
  href: https://artifacts.apis.io/nuki/well-known/nuki-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nuki-well-known.yml
- group: other
  href: https://artifacts.apis.io/nuki/hosts/nuki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nuki-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuki.io/en/legal/terms-of-use-nuki-apis
- group: operate
  title: ''
  type: Support
  url: https://help.nuki.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuki.io/
- group: auth
  title: ''
  type: Security
  url: https://nuki.io/en/blog/security/av-test
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuki.io/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://nuki.io/company/press
- group: start
  title: ''
  type: Login
  url: https://id.nuki.io/login
- group: company
  title: ''
  type: Blog
  url: https://nuki.io/en/blog/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nuki.io/
- group: auth
  href: https://artifacts.apis.io/nuki/security/nuki-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nuki-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nuki/security/nuki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nuki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuki.io/
coverage:
  checked: '2026-10-28'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://developer.nuki.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Nuki develops smart lock solutions that enable secure, keyless access to homes and businesses. Their products integrate with mobile apps, voice assistants, and smart home ecosystems, offering remote control, automatic locking, and activity logs. The company focuses on user-friendly design, robust security, and compatibility with various door types, aiming to modernize entry management for consumers and enterprises.
image: https://media.crystallize.com/nuki-production/25/3/11/7/nuki-smart-lock_lineup.png
layout: provider
modified: '2026-10-28'
name: Nuki
nav: Providers
network: true
overview: 'Nuki is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SmartLock, IoT, HomeAutomation, and Security.


  The Nuki catalog on APIs.io includes 1 Spectral governance ruleset.


  Nuki''s developer surface includes support, engineering blog, documentation, and 18 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Nuki API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nuki-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 67.9
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nuki Domain Security
  slug: nuki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nuki Vulnerability Disclosure
  slug: nuki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nuki
tags:
- Company
- SmartLock
- IoT
- HomeAutomation
- Security
website: https://nuki.io/
---
