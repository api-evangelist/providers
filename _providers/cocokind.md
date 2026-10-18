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
- description: GraphQL API for Cocokind storefront
  name: Cocokind GraphQL API
  slug: cocokind-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cocokind/refs/heads/main/llms/cocokind-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cocokind-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cocokind/refs/heads/main/well-known/cocokind-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cocokind-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cocokind/refs/heads/main/hosts/cocokind-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cocokind-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cocokind/refs/heads/main/vendors/cocokind-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cocokind-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cocokind.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cocokind.com/pages/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cocokind.com/blogs/news/price-increases-for-select-products
- group: company
  title: ''
  type: Newsroom
  url: https://www.cocokind.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.cocokind.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cocokind/refs/heads/main/security/cocokind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cocokind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cocokind.com
created: '2026-10-09'
description: 'Cocokind is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: http://www.cocokind.com/cdn/shop/files/cocokind_share_642bcbf5-237a-4f4b-9bf6-f402b5b0057e.jpg?v=1630050637
layout: provider
modified: '2026-10-09'
name: Cocokind
nav: Providers
network: true
overview: 'Cocokind is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sensitive Skin and Beauty Products.


  Cocokind''s developer surface includes pricing and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
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
  name: Cocokind Domain Security
  slug: cocokind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cocokind
tags:
- Sensitive Skin
- Beauty Products
website: https://www.cocokind.com
---
