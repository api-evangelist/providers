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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://aeronext.com/
- group: company
  title: ''
  type: Blog
  url: https://aeronext.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://aeronext.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://aeronext.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aeronext.com/policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aeronext
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeronext-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/aeronext-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aeronext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aeronext-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeronext-domain-security.yml
coverage:
  checked: '2026-09-10'
  detail: 'Aeronext licenses drone airframe technology (4D GRAVITY) to manufacturers and, through NEXT DELIVERY Inc., sells the SkyHub logistics service and its TMS to municipalities - it runs software but ships no developer program: /developers, /api and /docs all 404 on aeronext.com, the SkyHub TMS app at tms.skyhub.jp is a sign-in-only React SPA that returns the same index.html for /openapi.json and /api-docs, and its only public integration (SkyHub TMS to KDDI Smart Drone UTM) was arranged bilaterally with no published contract.'
  evidence:
  - status: 404
    url: https://aeronext.com/developers
  - status: 404
    url: https://aeronext.com/api
  - status: 404
    url: https://aeronext.com/docs/
  - status: 404
    url: https://aeronext.com/openapi.json
  - status: 404
    url: https://aeronext.co.jp/openapi.json
  - status: 200
    url: https://tms.skyhub.jp/openapi.json
  - status: 404
    url: https://skyhub.jp/.well-known/agent-card.json
  - status: 200
    url: https://aeronext.co.jp/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: Aeronext Inc. (株式会社エアロネクスト) is a Tokyo-based industrial drone technology startup, founded April 2017 by Keisuke Toji in Ebisu-Nishi, Shibuya-ku. Its core product is 4D GRAVITY(R), a patented airframe design that separates the flight unit from the payload unit and actively controls the center of gravity, improving stability, flight efficiency and payload performance. Aeronext monetizes through technology licensing and joint development — the Next-series airframes (AirTruck, LogiAir, PD4B-M-AN with PRODRONE) are built by licensee manufacturers — rather than through software. Its subsidiary NEXT DELIVERY Inc. operates SkyHub(R), a drone-plus-ground smart logistics platform co-developed with Seino Holdings and deployed across Japanese municipalities, with the SkyHub TMS system and a SkyHub Provider License program. Aeronext publishes no public developer program, API reference or machine-readable API contract.
image: https://aeronext.com/wp-content/themes/aeronext_re/public/assets/img/icon/aeronext-logo.png
layout: provider
modified: '2026-09-10'
name: Aeronext
nav: Providers
network: true
overview: 'Aeronext is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drones, UAV, Logistics, and Last Mile Delivery.


  Aeronext''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Aeronext Plans Pricing
  plan_count: 0
  slug: aeronext-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aeronext Rate Limits
  slug: aeronext-rate-limits
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeronext Domain Security
  slug: aeronext-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aeronext
tags:
- Company
- Drones
- UAV
- Logistics
- Last Mile Delivery
- Transportation
- Robotics
- Aerospace
- Supply Chain
- Japan
website: https://aeronext.com/
---
