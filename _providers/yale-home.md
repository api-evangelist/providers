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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/yale-home/llms/yale-home-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yale-home-llms.txt
- group: agent
  href: https://artifacts.apis.io/yale-home/well-known/yale-home-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yale-home-well-known.yml
- group: other
  href: https://artifacts.apis.io/yale-home/hosts/yale-home-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yale-home-hosts.yml
- group: other
  href: https://artifacts.apis.io/yale-home/vendors/yale-home-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yale-home-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yalehome.com/hr/en/privacy-center/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shopyalehome.com/pages/privacy-center
- group: company
  title: ''
  type: Newsroom
  url: https://www.yalehome.com/tr/tr/stories/news/if2025
- group: start
  title: ''
  type: GettingStarted
  url: https://www.yalehome.com/tr/tr/support/products/safes/smart-safe/getting-started
- group: auth
  href: https://artifacts.apis.io/yale-home/security/yale-home-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yale-home-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shopyalehome.com/
- group: operate
  title: ''
  type: Support
  url: https://support.shopyalehome.com/
coverage:
  checked: '2026-10-28'
  detail: The website is a Shopify storefront with JavaScript‑rendered pages and no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.yalehome.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Yale Home (smart locks) designs, manufactures, and sells connected smart lock solutions for residential and commercial use. Their product line includes the Yale Assure Lock series, offering keyless entry via Bluetooth, Wi‑Fi, Z‑Wave, Apple Home Key, and Matter integration. The company provides a consumer‑focused e‑commerce storefront at shopyalehome.com and integrates with major smart‑home ecosystems such as Google Home, Amazon Alexa, and Samsung SmartThings.
image: https://shopyalehome.com/assets/logo.png
layout: provider
modified: '2026-10-28'
name: Yale Home (smart locks)
nav: Providers
network: true
overview: 'Yale Home (smart locks) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, smart-locks, IoT, Home Security, and Consumer Electronics.


  Yale Home (smart locks)''s developer surface includes getting-started guide, support, and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 56.3
    operational_transparency: 0.0
  previous_composite: 13.1
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yale-home/yale-home-2026-11-03T150320.png
security:
- kind: domain-security
  name: Yale Home Domain Security
  slug: yale-home-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yale-home
tags:
- Company
- smart-locks
- IoT
- Home Security
- Consumer Electronics
website: https://shopyalehome.com/
---
