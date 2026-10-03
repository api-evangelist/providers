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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL API endpoint discovered at shop.ballislife.com, but ownership could not be verified as belonging to Ballislife.
  name: Ballislife API
  slug: ballislife-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballislife/refs/heads/main/llms/ballislife-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ballislife-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ballislife/refs/heads/main/well-known/ballislife-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ballislife-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ballislife/refs/heads/main/hosts/ballislife-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ballislife-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ballislife/refs/heads/main/vendors/ballislife-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ballislife-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ballislife.com/tos/
- group: start
  title: ''
  type: SignUp
  url: https://ballislife.com/betting/bonus/sign-up/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ballislife.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://ballislife.com/price-upsets-17-hs-team-in-the-country-sierra-canyon/
- group: company
  title: ''
  type: Newsroom
  url: https://ballislife.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ballislife/refs/heads/main/security/ballislife-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ballislife-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ballislife.com/
created: '2026-09-27'
description: Ballislife.com is a basketball media platform offering news, highlights, player profiles, and community content for fans. It serves as a one‑stop shop for everything basketball, featuring articles, videos, and interactive features that engage the basketball community.
image: https://dsz7vodgjx60a.cloudfront.net/wp-content/uploads/2024/04/01095139/post-placeholder.jpg
layout: provider
modified: '2026-09-27'
name: Ballislife
nav: Providers
network: true
overview: 'Ballislife publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sports, Media, Basketball, and Community.


  Ballislife''s developer surface includes signup flow, pricing, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ballislife Domain Security
  slug: ballislife-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ballislife
tags:
- Company
- Sports
- Media
- Basketball
- Community
website: https://ballislife.com/
---
