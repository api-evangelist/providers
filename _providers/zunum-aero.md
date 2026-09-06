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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://zunum.aero/
- group: company
  title: ''
  type: Blog
  url: https://zunum.aero/in-the-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://zunum.aero/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3679319/
- group: other
  title: ''
  type: X
  url: https://twitter.com/zunumaero
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zunum-aero-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zunum-aero-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Zunum Aero builds hybrid-electric regional aircraft; zunum.aero is a WordPress marketing and press site whose only machine-readable surfaces are the stock WordPress CMS endpoint at /wp-json and an RSS feed, and every developer-facing path probed (/openapi.json, /swagger.json, /api-docs, /docs, /graphql, /llms.txt and the /.well-known/ set) returns 404.
  evidence:
  - status: 200
    url: https://zunum.aero/
  - status: 404
    url: https://zunum.aero/openapi.json
  - status: 404
    url: https://zunum.aero/.well-known/security.txt
  - status: 404
    url: https://zunum.aero/llms.txt
  - status: 404
    url: https://zunum.aero/docs
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'Zunum Aero is an American aerospace company founded in 2013 and based in the Seattle area (Kirkland / Bothell, Washington) that set out to build hybrid-to-electric regional aircraft. Its ZA10 program targeted a six-to-twelve-seat hybrid-electric airplane with a 700-nautical-mile range, aimed at reviving short-haul point-to-point air travel from secondary airports, and it was backed by Boeing HorizonX and JetBlue Technology Ventures. The company laid off nearly all of its staff in late 2018 and paused operations, and it later pursued trade-secret litigation against Boeing. Zunum Aero is an aircraft manufacturer, not a software vendor: its public web presence is a marketing and press site with no developer program, no developer portal, no documentation, and no published machine-readable API contract of any kind.'
image: https://zunum.aero/wp-content/uploads/2017/03/zunum-aero-logo.png
layout: provider
modified: '2026-09-05'
name: Zunum Aero
nav: Providers
network: true
overview: 'Zunum Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Aviation, Aircraft Manufacturing, and Electric Aviation.


  Zunum Aero''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
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
  name: Zunum Aero Domain Security
  slug: zunum-aero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zunum-aero
tags:
- Company
- Aerospace
- Aviation
- Aircraft Manufacturing
- Electric Aviation
- Hybrid Electric Propulsion
- Regional Air Travel
- Transportation
- Hardware
- Startups
website: https://zunum.aero/
---
