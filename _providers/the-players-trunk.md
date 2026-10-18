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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/the-players-trunk/refs/heads/main/llms/the-players-trunk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/the-players-trunk-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/the-players-trunk/refs/heads/main/well-known/the-players-trunk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/the-players-trunk-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/the-players-trunk/refs/heads/main/hosts/the-players-trunk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-players-trunk-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/the-players-trunk/refs/heads/main/vendors/the-players-trunk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-players-trunk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theplayerstrunk.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theplayerstrunk.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://theplayerstrunk.com/pages/media
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/the-players-trunk/refs/heads/main/security/the-players-trunk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-players-trunk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theplayerstrunk.com
- group: start
  title: ''
  type: SignUp
  url: https://theplayerstrunk.com/pages/seller-sign-up
- group: operate
  title: ''
  type: Support
  url: https://theplayerstrunk.com/pages/contact-us
coverage:
  checked: '2026-10-12'
  detail: The Players Trunk provides no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://theplayerstrunk.com
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: The Players Trunk is an e‑commerce platform offering weekly drops of sports‑team themed player trunks and related apparel. Featured on Shark Tank, the company ships orders on Sundays and provides a curated selection of jerseys, shorts, bags, gloves, footwear, and outerwear for college and professional teams. Customers can browse collections by school, sign up as sellers, and follow the brand on social media platforms including Instagram, Facebook, Twitter, and TikTok. The site emphasizes fast shipping, limited‑edition releases, and community engagement through its online store.
image: http://theplayerstrunk.com/cdn/shop/files/logo_6ab884ab-839b-4abd-81a1-1695c6d840d0.png?v=1624757287
layout: provider
modified: '2026-10-12'
name: The Players Trunk
nav: Providers
network: true
overview: 'The Players Trunk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Sports, Apparel, and WeeklyDrops.


  The Players Trunk''s developer surface includes signup flow, support, and 9 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
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
  name: The Players Trunk Domain Security
  slug: the-players-trunk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-players-trunk
tags:
- Company
- E-Commerce
- Sports
- Apparel
- WeeklyDrops
website: https://theplayerstrunk.com
---
