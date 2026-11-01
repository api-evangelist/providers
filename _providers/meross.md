---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API for Meross smart home devices as described in the developer documentation.
  name: Meross API
  slug: meross-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/meross/security/meross-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/meross-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/meross/llms/meross-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meross-llms.txt
- group: agent
  href: https://artifacts.apis.io/meross/well-known/meross-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meross-well-known.yml
- group: other
  href: https://artifacts.apis.io/meross/hosts/meross-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meross-hosts.yml
- group: other
  href: https://artifacts.apis.io/meross/vendors/meross-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meross-vendors.yml
- group: auth
  href: https://artifacts.apis.io/meross/security/meross-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/meross-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/meross/security/meross-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meross-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meross.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.meross.com/en-gc/developer
- group: company
  title: ''
  type: Blog
  url: https://www.meross.com/en-gc/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meross.com/en-gc/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meross.com/en-gc/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meross.com/en-gc/pricing
coverage:
  checked: '2026-10-28'
  detail: Developer documentation page loads a large JavaScript bundle and does not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.meross.com/en-gc/developer
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Meross is a global smart home and IoT device manufacturer offering a wide range of Wi‑Fi, Bluetooth, and Thread‑enabled products such as smart plugs, switches, lighting, thermostats, cameras, and sensors. The company provides a public API for developers to integrate device control, status monitoring, and automation into third‑party applications and platforms, supporting standards like HomeKit, Alexa, and Google Assistant.
layout: provider
modified: '2026-10-28'
name: Meross
nav: Providers
network: true
overview: 'Meross is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SmartHome, IoT, Automation, Consumer, and Hardware.


  Meross'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Meross Domain Security
  slug: meross-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Meross Vulnerability Disclosure
  slug: meross-vulnerability-disclosure
  summary_line: no policy recorded
slug: meross
tags:
- SmartHome
- IoT
- Automation
- Consumer
- Hardware
website: https://meross.com/
---
