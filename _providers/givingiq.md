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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/givingiq/plans/givingiq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/givingiq-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/givingiq/hosts/givingiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/givingiq-hosts.yml
- group: other
  href: https://artifacts.apis.io/givingiq/vendors/givingiq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/givingiq-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://givingiq.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://givingiq.com/for-nonprofits/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://givingiq.com/press/announce
- group: auth
  href: https://artifacts.apis.io/givingiq/security/givingiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/givingiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://givingiq.com/
created: '2026-10-27'
description: GivingIQ is a platform that enables donors, financial advisors, and nonprofits to give appreciated assets such as stocks, mutual funds, cryptocurrency, donor‑advised funds, and qualified charitable distributions. By facilitating non‑cash charitable contributions, GivingIQ helps donors maximize tax benefits while increasing the impact of their philanthropy. The service offers tools for donors to discover nonprofits, for advisors to manage client giving strategies, and for nonprofits to receive and process these asset donations efficiently.
image: https://givingiq.com/assets/og-5edc4f6ffe45.png
layout: provider
modified: '2026-10-27'
name: GivingIQ
nav: Providers
network: true
overview: 'GivingIQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, Charity, Donations, and AssetManagement.


  GivingIQ''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Givingiq Plans Pricing
  plan_count: 2
  slug: givingiq-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Givingiq Domain Security
  slug: givingiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: givingiq
tags:
- Company
- FinTech
- Charity
- Donations
- AssetManagement
website: https://givingiq.com/
---
