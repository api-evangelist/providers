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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.eargo.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://lxehearing.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@eargo.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.eargo.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eargo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eargo-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eargo-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/eargo-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eargo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eargo-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: 'Round two enumerated eargo.com by DNS and found four hosts the first pass missed — app.eargo.com still serves a live Rails "Eargo Web App" storefront and help.eargo.com serves a real 16.6KB llms.txt of 106 consumer support articles — but there is still no API anywhere: api.eargo.com answers 403 on /openapi.json, /swagger.json, /api-docs and /graphql behind a Cloudflare bot challenge, and every other host is a soft-404 shell or an unreachable retired storefront.'
  evidence:
  - status: 200
    url: https://help.eargo.com/llms.txt
  - status: 200
    url: https://app.eargo.com/
  - status: 403
    url: https://api.eargo.com/openapi.json
  - status: 403
    url: https://api.eargo.com/graphql
  - status: 200
    url: https://www.eargo.com/
  - status: 301
    url: https://shop.eargo.com/
  - status: 0
    url: https://store.eargo.com/
  - status: 0
    url: https://developer.eargo.com/
  - status: 404
    url: https://api.github.com/orgs/eargo
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Eargo was a San Jose, California direct-to-consumer medical device company that designed and sold rechargeable, virtually invisible in-canal hearing aids for adults with mild to moderate hearing loss, founded in 2010 as Aria Innovations and listed on Nasdaq in 2020. In 2025 Eargo merged with South Africa''s hearX Group to form LXE Hearing, combining Eargo''s direct-to-consumer platform with the Lexie and Go Hearing over-the-counter brands. In 2026 LXE Hearing began winding down its US operations after restructuring efforts failed, and the eargo.com website has been reduced to a single wind-down notice page. Eargo never operated a public developer program, developer portal, or documented API: the hearing aids paired with a consumer mobile application backed by a private, undocumented service host at api.eargo.com.'
image: https://www.eargo.com/assets/content/dam/eargo/samples/logo_white.png
layout: provider
modified: '2026-08-12'
name: Eargo
nav: Providers
network: true
overview: 'Eargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hearing Aids, Medical Devices, Consumer Health, and Direct to Consumer.


  Eargo''s developer surface includes support and 9 more developer resources.'
plans:
- name: Eargo Plans Pricing
  plan_count: 0
  slug: eargo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Eargo Rate Limits
  slug: eargo-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Eargo Domain Security
  slug: eargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eargo
tags:
- Company
- Hearing Aids
- Medical Devices
- Consumer Health
- Direct to Consumer
- Hearing Health
- Digital Health
- Defunct
website: https://www.eargo.com/
---
