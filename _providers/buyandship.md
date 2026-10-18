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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Buyandship provides parcel forwarding services; the developer portal documents pricing and shipping APIs but no machine‑readable contract was found.
  name: Buyandship API
  slug: buyandship-api
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buyandship/refs/heads/main/well-known/buyandship-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buyandship-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/buyandship/refs/heads/main/well-known/buyandship-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buyandship-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buyandship/refs/heads/main/hosts/buyandship-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buyandship-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buyandship/refs/heads/main/vendors/buyandship-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buyandship-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.buyandship.today/hc/zh-TW/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buyandship.today/shipping/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.buyandship.today/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buyandship.today/en/blog/2026-onboarding-shipping/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buyandship/refs/heads/main/security/buyandship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buyandship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.buyandship.today
- group: docs
  title: ''
  type: Documentation
  url: https://www.buyandship.today/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buyandship.today/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buyandship.today/en/terms/
coverage:
  checked: '2026-10-06'
  detail: Developer portal pages list pricing APIs but no OpenAPI or other machine‑readable contract is available.
  evidence:
  - status: 200
    url: https://www.buyandship.today/shipping/pricing
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Buyandship is a parcel forwarding and global shopping service based in Hong Kong. It allows users to shop from international retailers, consolidates shipments from over 10 countries, and provides affordable shipping, protection plans, and a user-friendly platform with mobile apps. The service supports major marketplaces like eBay, Mercari, and JDirectItems, offering price monitoring, coupons, and a help center for customers worldwide.
image: https://www.buyandship.today/contents/uploads/2015/10/bns1.png
layout: provider
modified: '2026-10-06'
name: Buyandship
nav: Providers
network: true
overview: 'Buyandship is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ParcelForwarding, GlobalShopping, HongKong, and E-Commerce.


  Buyandship''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buyandship Domain Security
  slug: buyandship-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buyandship
tags:
- Company
- ParcelForwarding
- GlobalShopping
- HongKong
- E-Commerce
website: https://www.buyandship.today
---
