---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: HyBird provides APIs for industrial spatial AI integration, but no machine‑readable contract was discovered.
  name: HyBird API
  slug: hybird-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://hybird.ai/security
- group: other
  href: https://artifacts.apis.io/hybirdtech-com/hosts/hybirdtech-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hybirdtech-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hybirdtech-com/vendors/hybirdtech-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hybirdtech-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://hybird.ai/security/
- group: auth
  href: https://artifacts.apis.io/hybirdtech-com/security/hybirdtech-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hybirdtech-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hybirdtech-com/security/hybirdtech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hybirdtech-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hybird.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hybird.ai/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hybird.ai/legal/
- group: operate
  title: ''
  type: Support
  url: https://hybird.ai/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://hybird.ai/journey/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found despite probing documented hosts.
  evidence:
  - status: 200
    url: https://hybird.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: HyBird is an emerging technology platform focused on providing seamless integration solutions for IoT devices and enterprise workflows. Founded with backing from Techstars, the company offers a suite of APIs that enable developers to connect, manage, and automate hardware and software services across cloud and edge environments. HyBird’s mission is to simplify complex integration challenges, accelerate time‑to‑market, and empower businesses to build scalable, secure, and intelligent solutions. The platform emphasizes robust security, real‑time data processing, and extensible tooling to support a wide range of industry use cases, from smart manufacturing to connected consumer products.
layout: provider
modified: '2026-10-29'
name: HyBird
nav: Providers
network: true
overview: 'HyBird is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Integration, Automation, and Cloud.


  HyBird''s developer surface includes support, getting-started guide, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.6
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hybirdtech Com Domain Security
  slug: hybirdtech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Hybirdtech Com Trust Center
  slug: hybirdtech-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: hybirdtech-com
tags:
- Company
- IoT
- Integration
- Automation
- Cloud
- Edge
website: https://hybird.ai/
---
