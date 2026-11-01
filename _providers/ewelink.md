---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/ewelink/llms/ewelink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ewelink-llms.txt
- group: agent
  href: https://artifacts.apis.io/ewelink/well-known/ewelink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ewelink-well-known.yml
- group: other
  href: https://artifacts.apis.io/ewelink/hosts/ewelink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ewelink-hosts.yml
- group: other
  href: https://artifacts.apis.io/ewelink/vendors/ewelink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ewelink-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.ewelink.cc/
- group: auth
  href: https://artifacts.apis.io/ewelink/security/ewelink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ewelink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ewelink.cc/
- group: company
  title: ''
  type: Blog
  url: https://ewelink.cc/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ewelink.cc/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ewelink.cc/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ewelink.cc/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://ewelink.cc/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoolKit-Technologies
coverage:
  checked: '2026-10-28'
  detail: Help Center pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://help.ewelink.cc/hc/en-us/search?q=openapi
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: eWeLink, developed by ITEAD and known for the Sonoff line, provides a cloud‑based platform that connects smart home devices to mobile apps, voice assistants, and third‑party services. Users can control lights, switches, sensors, cameras, and more through the eWeLink app, web portal, or integrations with Alexa, Google Home, Home Assistant, and other ecosystems. The service offers device management, scene automation, firmware updates, and remote access, serving millions of users worldwide across 170+ countries.
image: https://ewelink.cc/wp-content/uploads/2022/05/eWeLink-Camera-Plan.jpg
layout: provider
modified: '2026-10-28'
name: eWeLink (ITEAD / Sonoff)
nav: Providers
network: true
overview: 'eWeLink (ITEAD / Sonoff) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Smart Home, IoT, Cloud Platform, Automation, and Voice Assistant Integration.


  eWeLink (ITEAD / Sonoff)''s developer surface includes engineering blog, documentation, support, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ewelink Domain Security
  slug: ewelink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ewelink
tags:
- Smart Home
- IoT
- Cloud Platform
- Automation
- Voice Assistant Integration
- Company
website: https://ewelink.cc/
---
