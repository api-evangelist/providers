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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/signify/well-known/signify-signify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signify-signify-security.txt
- group: other
  href: https://artifacts.apis.io/signify/vendors/signify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/signify-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.signify.com/global/product-security/coordinated-vulnerability-disclosure
- group: auth
  href: https://artifacts.apis.io/signify/well-known/signify-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signify-www-security.txt
- group: auth
  href: https://artifacts.apis.io/signify/well-known/signify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signify-security.txt
- group: auth
  href: https://artifacts.apis.io/signify/well-known/signify-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/signify-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/signify/well-known/signify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signify-well-known.yml
- group: other
  href: https://artifacts.apis.io/signify/hosts/signify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/signify-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signify.com/en-us/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://www.signify.com/en-us/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signify.com/en-us/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://www.signify.com/en-us/our-company/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.signify.com/global
- group: company
  title: ''
  type: Blog
  url: https://www.signify.com/en-us/blog
- group: docs
  title: ''
  type: Documentation
  url: https://dev.signify.com/
- group: auth
  href: https://artifacts.apis.io/signify/security/signify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/signify-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signify/security/signify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://signify.com/
coverage:
  checked: '2026-10-28'
  detail: The developer portal at https://dev.signify.com/global provides only HTML documentation with no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://dev.signify.com/global
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Signify, formerly Philips Lighting, is a global leader in lighting solutions, offering professional, consumer, and IoT-enabled products such as Philips Hue and WiZ. The company provides smart lighting, LED technology, and digital services across residential, commercial, and industrial markets, focusing on sustainability and innovative lighting experiences.
image: https://www.signify.com/content/dam/signify/master/homepage/street-lighting-smart-iot-banner-thumb.jpg
layout: provider
modified: '2026-10-28'
name: Signify (Philips Hue, WiZ)
nav: Providers
network: true
overview: 'Signify (Philips Hue, WiZ) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lighting, IoT, Smart Home, and LED.


  Signify (Philips Hue, WiZ)''s developer surface includes support, engineering blog, documentation, and 15 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 49.1
    operational_transparency: 5.3
  previous_composite: 16.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/signify/signify-2026-11-03T143206.png
security:
- kind: domain-security
  name: Signify Domain Security
  slug: signify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Signify Vulnerability Disclosure
  slug: signify-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: signify
tags:
- Company
- Lighting
- IoT
- Smart Home
- LED
website: https://signify.com/
---
