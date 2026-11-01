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
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/fetchrewards-com/well-known/fetchrewards-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fetchrewards-com-security.txt
- group: agent
  href: https://artifacts.apis.io/fetchrewards-com/well-known/fetchrewards-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fetchrewards-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fetchrewards-com/hosts/fetchrewards-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fetchrewards-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fetchrewards-com/vendors/fetchrewards-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fetchrewards-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/fetchrewards-com/security/fetchrewards-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetchrewards-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fetch.com/
- group: company
  title: ''
  type: Blog
  url: https://fetch.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://fetch.com/
- group: operate
  title: ''
  type: Support
  url: https://help.fetch.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fetch.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fetch.com/privacy-policy
created: '2026-10-22'
description: Fetch Rewards, LLC operates a consumer loyalty platform that turns everyday receipt scanning into points redeemable for gift cards. Users earn rewards on groceries, shopping, and gaming, and can redeem for free gift cards.
image: https://prod-static-content.fetchrewards.com/content-service/opengraph_Share_image_4_2ea5e519da.png
layout: provider
modified: '2026-10-22'
name: Fetch
nav: Providers
network: true
overview: 'Fetch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, ConsumerRewards, MobileApp, Retail, and FinTech.


  Fetch''s developer surface includes engineering blog, documentation, support, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
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
  name: Fetchrewards Com Domain Security
  slug: fetchrewards-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fetchrewards-com
tags:
- Loyalty
- ConsumerRewards
- MobileApp
- Retail
- FinTech
website: https://fetch.com/
---
