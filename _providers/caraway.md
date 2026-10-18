---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Caraway provides an e‑commerce API for product listings, orders, and customer accounts as described in their developer documentation.
  name: Caraway API
  slug: caraway-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caraway/refs/heads/main/llms/caraway-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caraway-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/caraway/refs/heads/main/well-known/caraway-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caraway-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caraway/refs/heads/main/hosts/caraway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caraway-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caraway/refs/heads/main/vendors/caraway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caraway-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.carawayhome.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carawayhome.com/pages/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carawayhome
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caraway/refs/heads/main/security/caraway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caraway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carawayhome.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.carawayhome.com/pages/our-story
- group: company
  title: ''
  type: Blog
  url: https://www.carawayhome.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carawayhome.com/pages/terms-and-conditions
coverage:
  checked: '2026-10-07'
  detail: Developer documentation is rendered via JavaScript on a Shopify custom site, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.carawayhome.com/pages/our-story
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Caraway designs and sells non‑stick ceramic cookware, bakeware, and kitchen accessories. The brand focuses on sustainable, chemical‑free products, offering a range of cookware sets, coffee makers, and kitchen tools. Their mission is to replace traditional non‑stick coatings with safer, environmentally friendly alternatives while providing stylish, functional home goods.
layout: provider
modified: '2026-10-06'
name: Caraway
nav: Providers
network: true
overview: 'Caraway is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cookware, Sustainable, HomeGoods, and E-Commerce.


  Caraway''s developer surface includes support, documentation, engineering blog, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: first-party
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
  name: Caraway Domain Security
  slug: caraway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: caraway
tags:
- Company
- Cookware
- Sustainable
- HomeGoods
- E-Commerce
website: https://www.carawayhome.com
---
