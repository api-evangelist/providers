---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Copper Cow Coffee e‑commerce platform.
  name: Copper Cow Coffee API
  slug: copper-cow-coffee-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-cow-coffee/refs/heads/main/llms/copper-cow-coffee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/copper-cow-coffee-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/copper-cow-coffee/refs/heads/main/well-known/copper-cow-coffee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/copper-cow-coffee-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copper-cow-coffee/refs/heads/main/hosts/copper-cow-coffee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/copper-cow-coffee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/copper-cow-coffee/refs/heads/main/vendors/copper-cow-coffee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/copper-cow-coffee-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/copper-cow-coffee/refs/heads/main/security/copper-cow-coffee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/copper-cow-coffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coppercowcoffee.com/
- group: company
  title: ''
  type: AboutUs
  url: https://coppercowcoffee.com/pages/our-story
- group: company
  title: ''
  type: Blog
  url: https://coppercowcoffee.com/blogs/blog-posts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coppercowcoffee.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coppercowcoffee.com/policies/terms-of-service
created: '2026-10-10'
description: Copper Cow Coffee is a specialty Vietnamese coffee brand founded by Debbie, a Vietnamese‑Californian entrepreneur. The company sources climate‑resilient beans from Vietnam’s first organic‑certified farms, pays farmers double market rates, and blends coffee with real herbs and spices for unique flavors. Their e‑commerce store offers coffee, creamers, seasonal flavors, and subscription plans, emphasizing sustainability, zero‑fake ingredients, and AAPI woman‑owned leadership.
image: http://coppercowcoffee.com/cdn/shop/files/CCC-SocialSharing-Preview_5e0a5cbf-326a-4480-a685-6195a625d4e3.png?v=1631562010
layout: provider
modified: '2026-10-10'
name: Copper Cow Coffee
nav: Providers
network: true
overview: 'Copper Cow Coffee is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, E-Commerce, Sustainability, and Vietnamese.


  Copper Cow Coffee''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 29.8
    developer_ergonomics: 2.4
    discoverability: 73.2
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
  name: Copper Cow Coffee Domain Security
  slug: copper-cow-coffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: copper-cow-coffee
tags:
- Company
- Coffee
- E-Commerce
- Sustainability
- Vietnamese
website: https://coppercowcoffee.com/
---
