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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cloudofgoods/refs/heads/main/llms/cloudofgoods-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudofgoods-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudofgoods/refs/heads/main/hosts/cloudofgoods-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudofgoods-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cloudofgoods/refs/heads/main/vendors/cloudofgoods-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudofgoods-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudofgoods.com/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudofgoods.com/privacy_policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudofgoods.com/price-list
- group: company
  title: ''
  type: Blog
  url: https://www.cloudofgoods.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cloudofgoods/refs/heads/main/security/cloudofgoods-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudofgoods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudofgoods.com
coverage:
  checked: '2026-10-09'
  detail: The website renders content via JavaScript, providing no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.cloudofgoods.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-09'
description: Cloudofgoods operates an online rental marketplace offering a wide range of equipment such as scooters, wheelchairs, strollers, bikes, tools, and party supplies. The platform enables travelers and locals to rent essential gear on demand across over 600 cities worldwide, aiming to simplify travel and provide seamless delivery experiences.
image: https://images.cloudofgoods.com/images/banners/cloud-of-goods-social-share.jpg
layout: provider
modified: '2026-10-09'
name: Cloudofgoods
nav: Providers
network: true
overview: 'Cloudofgoods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Rentals, Marketplace, Travel, and Equipment.


  Cloudofgoods'' developer surface includes pricing, engineering blog, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cloudofgoods Domain Security
  slug: cloudofgoods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudofgoods
tags:
- Company
- Rentals
- Marketplace
- Travel
- Equipment
website: https://www.cloudofgoods.com
---
