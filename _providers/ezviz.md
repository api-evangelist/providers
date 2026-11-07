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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer portal providing API reference for EZVIZ smart home devices.
  name: EZVIZ Developer API
  slug: ezviz-developer-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ezviz/hosts/ezviz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ezviz-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.ezviz.com/newsroom
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ezviz.com/developer/index?utm_source=us_footer&utm_medium=footer5_3&utm_campaign=web_us_footer
- group: auth
  href: https://artifacts.apis.io/ezviz/security/ezviz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ezviz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ezviz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ezviz.com/developer/index
- group: company
  title: ''
  type: Blog
  url: https://www.ezviz.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ezviz.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ezviz.com/us/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ezviz.com/us/p/legal/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ezviz.com/us/cloudplay
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ezviz.com/us/page/about-ezviz
coverage:
  checked: '2026-10-28'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.ezviz.com/developer/index
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: EZVIZ provides smart home security cameras, video doorbells, and related IoT devices, offering cloud storage, AI-powered motion detection, and mobile app control. The company operates globally, with regional sites for the US, Europe, and Asia, and publishes developer resources, API documentation, and support portals for integration with third‑party services.
layout: provider
modified: '2026-10-28'
name: EZVIZ
nav: Providers
network: true
overview: 'EZVIZ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security Cameras, Smart Home, Smart Entry, Smart Home Appliance, and CloudPlay.


  EZVIZ''s developer surface includes documentation, engineering blog, support, pricing, getting-started guide, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 54.5
    operational_transparency: 0.0
  previous_composite: 19.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ezviz/ezviz-2026-11-03T131753.png
security:
- kind: domain-security
  name: Ezviz Domain Security
  slug: ezviz-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ezviz
tags:
- Security Cameras
- Smart Home
- Smart Entry
- Smart Home Appliance
- CloudPlay
- Home Automation
website: https://ezviz.com/
---
