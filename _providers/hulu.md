---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 19.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Public API information not accessible; developer portal requires authentication.
  name: Hulu API
  slug: hulu-api
artifact_total: 3
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://help.hulu.com/category/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.hulu.com/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/plans/hulu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hulu-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/llms/hulu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hulu-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/well-known/hulu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hulu-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/hosts/hulu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hulu-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/vendors/hulu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hulu-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/packages/hulu-packages.yml
  title: ''
  type: SDKs
  url: packages/hulu-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/packages/hulu-packages.yml
  title: ''
  type: Packages
  url: packages/hulu-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.hulu.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hulu/refs/heads/main/security/hulu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hulu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hulu.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hulu
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hulu
- group: operate
  title: ''
  type: Support
  url: https://help.hulu.com
- group: company
  title: ''
  type: Blog
  url: https://www.hulu.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.hulu.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hulu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hulu.com/privacy
coverage:
  checked: '2026-10-13'
  detail: Developer API page returns 403 and no machine‑readable spec is available.
  evidence:
  - status: 403
    url: https://www.hulu.com/developers/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Hulu is an American subscription streaming service offering live and on-demand TV shows, movies, and original content. Operated by Hulu LLC, a joint venture between Disney and Comcast, it provides various plans including ad-supported and ad-free options, as well as a bundle with Disney+ and ESPN+. The platform streams across web, mobile, and connected TV devices, delivering a broad library of entertainment for subscribers.
image: https://assetshuluimcom-a.akamaihd.net/h3o/facebook_share_thumb_default_hulu.jpg
layout: provider
modified: '2026-10-13'
name: Hulu
nav: Providers
network: true
overview: 'Hulu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Streaming, Video, Entertainment, and Subscription.


  Hulu''s developer surface includes getting-started guide, documentation, support, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Hulu Plans Pricing
  plan_count: 6
  slug: hulu-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hulu Domain Security
  slug: hulu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hulu
tags:
- Company
- Streaming
- Video
- Entertainment
- Subscription
website: https://www.hulu.com
---
