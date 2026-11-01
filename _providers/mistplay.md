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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/mistplay/hosts/mistplay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mistplay-hosts.yml
- group: other
  href: https://artifacts.apis.io/mistplay/vendors/mistplay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mistplay-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mistplay.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mistplay.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mistplay
- group: auth
  href: https://artifacts.apis.io/mistplay/security/mistplay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mistplay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mistplay.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mistplay.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.mistplay.com/hc/en-us
- group: other
  title: ''
  type: Business
  url: https://business.mistplay.com/
coverage:
  checked: '2026-10-28'
  detail: Provider's website renders documentation via JavaScript, preventing machine-readable extraction.
  evidence:
  - status: 200
    url: https://www.mistplay.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Mistplay is a mobile gaming platform that lets users earn real money and gift cards by playing free games. Players accumulate points for time spent gaming, which can be redeemed for popular gift cards from Amazon, Visa, Starbucks, and more. The service targets casual gamers looking to monetize their playtime while offering a curated selection of games and a rewards marketplace.
image: https://assets.mistplay.com/assets/tp/images/og-mistplay-new.png
layout: provider
modified: '2026-10-28'
name: Mistplay
nav: Providers
network: true
overview: 'Mistplay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Rewards, Mobile, Casual, and GiftCards.


  Mistplay''s developer surface includes engineering blog, support, and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Mistplay Domain Security
  slug: mistplay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mistplay
tags:
- Gaming
- Rewards
- Mobile
- Casual
- GiftCards
- Company
website: https://www.mistplay.com/
---
