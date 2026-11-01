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
    mcp_server: false
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Yandex Ads developer documentation
  name: Yandex Ads API
  slug: yandex-ads-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://ya.cc/t/1cSZixjB3gkSva
- group: auth
  href: https://artifacts.apis.io/yandex-ads/well-known/yandex-ads-yandex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yandex-ads-yandex-security.txt
- group: agent
  href: https://artifacts.apis.io/yandex-ads/well-known/yandex-ads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yandex-ads-well-known.yml
- group: other
  href: https://artifacts.apis.io/yandex-ads/hosts/yandex-ads-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yandex-ads-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://ads.yandex.com/help/bundle-id
- group: build
  title: ''
  type: SDKs
  url: https://ads.yandex.com/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yandex.com/company/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://ads.yandex.com/newsroom
- group: auth
  href: https://artifacts.apis.io/yandex-ads/security/yandex-ads-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-ads-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yandex-ads/security/yandex-ads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yandex-ads-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ads.yandex.com/
coverage:
  checked: '2026-10-28'
  detail: Developer portal https://yandex.com/dev/ redirects to a captcha page, preventing access to machine‑readable specs.
  evidence:
  - status: 302
    url: https://yandex.com/dev/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Yandex Ads provides advertising solutions through Yandex, the leading Russian internet company. Their platform enables advertisers to reach audiences across Yandex Search, Yandex Display Network, and partner sites. The service offers targeting options, performance analytics, and integration via RESTful APIs for campaign management, reporting, and budgeting. Yandex Ads supports various ad formats, including text, image, video, and dynamic ads, catering to businesses of all sizes seeking to maximize online visibility and conversion rates.
image: https://avatars.mds.yandex.net/get-lpc/16405748/9a2cca51-7037-4895-9c46-c9dc6e39722d/orig
layout: provider
modified: '2026-10-28'
name: Yandex Ads
nav: Providers
network: true
overview: 'Yandex Ads is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, App Monetization, Web Analytics, User Acquisition, and DSP.


  Yandex Ads'' developer surface includes support and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yandex Ads Domain Security
  slug: yandex-ads-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Yandex Ads Vulnerability Disclosure
  slug: yandex-ads-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-ads
tags:
- Advertising
- App Monetization
- Web Analytics
- User Acquisition
- DSP
- SSP
website: https://ads.yandex.com/
---
