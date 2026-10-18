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
- description: The JWX platform provides video streaming, monetization, and analytics APIs as described on the pricing page.
  name: JWX API
  slug: jwx-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/plans/connatix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connatix-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/well-known/connatix-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/connatix-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/well-known/connatix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/connatix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/hosts/connatix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connatix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/vendors/connatix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/connatix-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jwx.com/
- group: company
  title: ''
  type: Newsroom
  url: https://jwx.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://jwx.com/guides
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connatix/refs/heads/main/security/connatix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connatix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jwx.com
- group: company
  title: ''
  type: Blog
  url: https://jwx.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://jwx.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jwx.com/legal/saas-tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jwx.com/legal/privacy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://jwx.com/mcp
  - status: 403
    url: https://status.jwx.com/mcp
  - status: 200
    url: https://jwx.com
  - status: 403
    url: https://equityzen.com/company/connatix
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Connatix, now operating under the JWX brand, provides a video technology and monetization platform for streamers, publishers, and advertisers. Their solutions include streaming, video on demand, server‑side ad insertion, DRM, and data‑intelligence tools to help content creators maximize revenue and audience engagement across multiple channels.
image: https://jwx.com/hubfs/JWX_Featured_Image-1.jpg
layout: provider
modified: '2026-10-10'
name: Connatix
nav: Providers
network: true
overview: 'Connatix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Monetization, Advertising, Streaming, and Platform.


  Connatix''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Connatix Plans Pricing
  plan_count: 5
  slug: connatix-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.9
    operational_transparency: 15.8
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
  name: Connatix Domain Security
  slug: connatix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connatix
tags:
- Video
- Monetization
- Advertising
- Streaming
- Platform
website: https://jwx.com
---
