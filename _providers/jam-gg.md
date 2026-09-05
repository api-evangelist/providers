---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jam-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jam.gg/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/piepacker
- group: build
  title: ''
  type: Packages
  url: packages/jam-gg-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/jam-gg-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jam-gg-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jam-gg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jam-gg-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jam-gg-llms.txt
coverage:
  checked: '2026-08-17'
  detail: Jam.gg never shipped an HTTP API, and the company is now listed Inactive by Y Combinator — its own web property cannot complete a TLS handshake on either host (jam.gg answers the ClientHello with TLS alert 80 internal_error from Netlify/AWS Global Accelerator, www.jam.gg answers with alert 40 handshake_failure from the Webflow proxy), piepacker.com has left DNS, and no api/docs/developers subdomain resolves, so the only reachable artifacts are the first-party SDK repositories on GitHub.
  evidence:
  - status: 301
    url: http://jam.gg/
  - status: 0
    url: https://jam.gg/
  - status: 0
    url: https://www.jam.gg/
  - status: 200
    url: https://www.ycombinator.com/companies/jam-gg
  - status: 200
    url: https://github.com/piepacker
  - status: 200
    url: https://repo1.maven.org/maven2/io/github/piepacker/jampadcompose/maven-metadata.xml
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Jam.gg, founded in Paris in 2020 as Piepacker and rebranded in 2022, built a browser-based social cloud gaming platform for playing retro and indie multiplayer games with friends with no download or install, on patented streaming technology the company said cut bandwidth requirements by roughly 15x. It passed 8 million users before pivoting to selling its cloud gaming technology B2B to game developers and publishers. Backed by Makers Fund, Serena Capital, LEGO Ventures, Kima Ventures and Kickstarter (~$15.4M raised) and a Y Combinator W20 company. Jam.gg never published an HTTP API: its developer surface was a native game-integration SDK plus a Compose Multiplatform virtual gamepad library, both shipped from the GitHub organization still named piepacker. Y Combinator''s company directory now lists Jam.gg as Inactive, noting the business split into two entities in 2023 with Onibi emerging separately; the jam.gg web property no longer completes a TLS handshake and piepacker.com
  has left DNS.'
image: https://avatars.githubusercontent.com/u/51542573?v=4
layout: provider
modified: '2026-08-17'
name: Jam.gg
nav: Providers
network: true
overview: 'Jam.gg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Cloud Gaming, Games, and Game Development.


  Jam.gg''s developer surface includes sandbox and 8 more developer resources.'
plans:
- name: Jam Gg Plans Pricing
  plan_count: 0
  slug: jam-gg-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Jam Gg Rate Limits
  slug: jam-gg-rate-limits
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Jam Gg Domain Security
  slug: jam-gg-domain-security
  summary_line: DMARC
slug: jam-gg
tags:
- Company
- Gaming
- Cloud Gaming
- Games
- Game Development
- Emulation
- SDK
- WebRTC
- France
website: https://jam.gg/
---
