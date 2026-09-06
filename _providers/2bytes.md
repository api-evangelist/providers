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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/2bytes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.2bytescorp.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.2bytescorp.com/terms
- group: company
  title: ''
  type: Blog
  url: https://blog.2bytescorp.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/2bytes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/2bytes-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/2bytes-llms.txt
coverage:
  checked: '2026-09-05'
  detail: The 2bytes homepage markets its H5 game platform as adoptable "with SDK integration alone" (SDK 연동만으로), but no SDK reference, developer path, or machine-readable contract is published anywhere on the ten-page Framer site — /developers, /docs, /api and /openapi.json all 404, the one API-shaped host in DNS (api.2bytescorp.com) refuses connections from the public internet, and the only route to the platform is a mailto to contact@2bytescorp.com.
  evidence:
  - status: 404
    url: https://www.2bytescorp.com/developers
  - status: 404
    url: https://www.2bytescorp.com/openapi.json
  - status: 0
    url: https://api.2bytescorp.com/
  - status: 404
    url: https://www.2bytescorp.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: 2bytes Corporation (투바이트) is a South Korean game services and publishing company founded in 2020 in Seoul, providing game localization, QA testing, player support, content marketing, live operations and global launch support to more than 40 game company partners including Pearl Abyss and Kakao Games. The company also builds and operates an H5 (HTML5) game platform that runs in-app without installation, covering platform construction, global H5 game sourcing, localization and live operations, integrated by partner apps through an SDK. Its service brand is 2bytes Play. As of this profile 2bytes publishes no public developer portal, API reference, or machine-readable API contract; the H5 platform SDK is offered through a business contact channel rather than a self-serve developer program.
image: https://framerusercontent.com/assets/esLqfsUu8HoVFr7VTvvnhnOWvtY.png
layout: provider
modified: '2026-09-05'
name: 2bytes
nav: Providers
network: true
overview: '2bytes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Game Services, Localization, and Quality Assurance.


  2bytes'' developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: 2Bytes Plans Pricing
  plan_count: 0
  slug: 2bytes-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: 2Bytes Rate Limits
  slug: 2bytes-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 2Bytes Domain Security
  slug: 2bytes-domain-security
  summary_line: TLSv1.3 · HSTS
slug: 2bytes
tags:
- Company
- Gaming
- Game Services
- Localization
- Quality Assurance
- Publishing
- HTML5
- South Korea
website: https://www.2bytescorp.com/
---
