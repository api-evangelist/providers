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
- baseURL: https://api.bymason.com
  baseurl_source: declared
  description: 'By Mason API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: By Mason API
  slug: by-mason-api
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/by-mason/well-known/by-mason-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/by-mason-status-security.txt
- group: design
  href: https://artifacts.apis.io/by-mason/rules/by-mason-rules.yml
  title: ''
  type: Spectral
  url: rules/by-mason-rules.yml
- group: design
  href: https://artifacts.apis.io/by-mason/json-ld/by-mason-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/by-mason-context.jsonld
- group: design
  href: https://artifacts.apis.io/by-mason/vocabulary/by-mason-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/by-mason-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/by-mason/data-model/by-mason-data-model.yml
  title: ''
  type: DataModel
  url: data-model/by-mason-data-model.yml
- group: build
  href: https://artifacts.apis.io/by-mason/cli/by-mason-cli.yml
  title: ''
  type: CLI
  url: cli/by-mason-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bymason.com/security
- group: design
  href: https://artifacts.apis.io/by-mason/conformance/by-mason-conformance.yml
  title: ''
  type: Conformance
  url: conformance/by-mason-conformance.yml
- group: agent
  href: https://artifacts.apis.io/by-mason/well-known/by-mason-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/by-mason-well-known.yml
- group: other
  href: https://artifacts.apis.io/by-mason/hosts/by-mason-hosts.yml
  title: ''
  type: Hosts
  url: hosts/by-mason-hosts.yml
- group: other
  href: https://artifacts.apis.io/by-mason/vendors/by-mason-vendors.yml
  title: ''
  type: Vendors
  url: vendors/by-mason-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bymason.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.bymason.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bymason.com/
- group: auth
  title: ''
  type: Security
  url: https://www.bymason.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bymason.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bymason.com/mason-os/release-notes/os6
- group: company
  title: ''
  type: Blog
  url: https://www.bymason.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bymason.com/setup-guide
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bymason.com/
- group: auth
  href: https://artifacts.apis.io/by-mason/security/by-mason-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/by-mason-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/by-mason/security/by-mason-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/by-mason-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/by-mason/security/by-mason-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/by-mason-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bymason.com
created: '2026-10-22'
description: Mason offers an enterprise platform that combines purpose‑built IoT hardware with a device management console. The company provides devices such as Mini 400, Scan 600, Radio 600T, Body 600, Smartphone 300 and SmartTab 300, and supports fleet management, automated updates, and remote monitoring for customers in healthcare, logistics, retail and other industries.
json_schemas:
- name: PostV1DefaultDeviceBroadcastRequest
  property_count: 4
  slug: by-mason-post-v1-default-device-broadcast-request
jsonld:
- class_count: 1
  name: By Mason Context
  property_count: 4
  slug: by-mason-context
layout: provider
modified: '2026-10-22'
name: By Mason
nav: Providers
network: true
overview: 'By Mason is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Device Management, Enterprise Hardware, Fleet Management, and Rugged Devices.


  The By Mason catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  By Mason''s developer surface includes CLI, support, changelog, engineering blog, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: By Mason API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: by-mason-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 18.3
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/by-mason/by-mason-2026-11-03T122842.png
security:
- kind: domain-security
  name: By Mason Domain Security
  slug: by-mason-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: By Mason Vulnerability Disclosure
  slug: by-mason-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: By Mason Trust Center
  slug: by-mason-trust-center
  summary_line: SOC 2
slug: by-mason
tags:
- IoT
- Device Management
- Enterprise Hardware
- Fleet Management
- Rugged Devices
- Healthcare
- Logistics
- Retail
website: https://www.bymason.com
---
