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
api_count: 1
apis:
- description: API for PlayStation services and integration (details not publicly available)
  name: PlayStation Developer API
  slug: playstation-developer-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/playstation/llms/playstation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/playstation-llms.txt
- group: other
  href: https://artifacts.apis.io/playstation/hosts/playstation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/playstation-hosts.yml
- group: other
  href: https://artifacts.apis.io/playstation/vendors/playstation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/playstation-vendors.yml
- group: auth
  href: https://artifacts.apis.io/playstation/security/playstation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playstation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.playstation.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partners.playstation.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.playstation.com/en-us/support/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.playstation.com
- group: company
  title: ''
  type: Blog
  url: https://blog.playstation.com
- group: operate
  title: ''
  type: Support
  url: https://www.playstation.com/en-us/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.playstation.com/en-us/ps-plus/
- group: start
  title: ''
  type: SignUp
  url: https://www.playstation.com/en-us/ps-plus/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.playstation.com/en-us/legal/psn-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.playstation.com/en-us/privacy-security-safety/
coverage:
  checked: '2026-10-13'
  detail: Developer portal pages render via JavaScript and hide API specifications.
  evidence:
  - status: null
    url: https://developer.playstation.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: PlayStation, a brand of Sony Interactive Entertainment, is a leading global provider of interactive entertainment hardware, software, and services. It offers the PlayStation consoles, a vast library of games, subscription services like PlayStation Plus, and a developer ecosystem. The company engages millions of players worldwide through innovative gaming experiences, community features, and a robust digital marketplace.
layout: provider
modified: '2026-10-13'
name: PlayStation
nav: Providers
network: true
overview: 'PlayStation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Entertainment, Console, and DigitalMarketplace.


  PlayStation''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 0.0
  previous_composite: 21.5
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/playstation/playstation-2026-11-03T141306.png
security:
- kind: domain-security
  name: Playstation Domain Security
  slug: playstation-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: playstation
tags:
- Company
- Gaming
- Entertainment
- Console
- DigitalMarketplace
website: https://www.playstation.com
---
