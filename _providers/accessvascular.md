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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.accessvascularinc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.accessvascularinc.com/take-action
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accessvascularinc.com/take-action?format=rss
- group: company
  title: ''
  type: Newsroom
  url: https://www.accessvascularinc.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accessvascularinc.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accessvascularinc.com/terms-and-conditions
- group: company
  title: ''
  type: About
  url: https://www.accessvascularinc.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.accessvascularinc.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/access-vascular-inc-/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/accessvascular
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accessvascular-domain-security.yml
coverage:
  checked: '2026-09-06'
  detail: Access Vascular, Inc. is a Billerica, Massachusetts catheter manufacturer whose entire public surface is a Squarespace marketing site about HydroPICC and HydroMID (company, products, news, take-action, careers, IFU pages), with no developer, docs, portal or integration link anywhere in the nav, footer or sitemap; every REST/GraphQL/MCP/agent-card, /llms.txt and /.well-known/ path probed on both www.accessvascularinc.com and accessvascularinc.com returns a hard 404 (verified against a random control path returning the identical 153,854-byte 404 body), and api./docs./developer./portal./app.accessvascularinc.com do not resolve in DNS at all. The accessvascular.com domain in the harvest lead is unrelated — it is parked for sale at $4,950 on Spaceship.com and is not operated by this company.
  evidence:
  - status: 200
    url: https://www.accessvascularinc.com/
  - status: 404
    url: https://www.accessvascularinc.com/openapi.json
  - status: 404
    url: https://www.accessvascularinc.com/swagger.json
  - status: 404
    url: https://www.accessvascularinc.com/api-docs
  - status: 404
    url: https://www.accessvascularinc.com/graphql
  - status: 404
    url: https://www.accessvascularinc.com/llms.txt
  - status: 404
    url: https://www.accessvascularinc.com/developers
  - status: 404
    url: https://www.accessvascularinc.com/.well-known/agent-card.json
  - status: 404
    url: https://www.accessvascularinc.com/.well-known/agent.json
  - status: 404
    url: https://www.accessvascularinc.com/.well-known/api-catalog
  - status: 404
    url: https://accessvascularinc.com/.well-known/security.txt
  - status: 404
    url: https://www.accessvascularinc.com/zz-api-evangelist-control-9f3a
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Access Vascular, Inc. is a Billerica, Massachusetts medical device manufacturer that designs and builds vascular access catheters from a proprietary hydrophilic biomaterial engineered to retain water and mimic the chemistry of the body, with the goal of reducing thrombosis, infection and phlebitis in intravenous therapy. Its FDA-cleared products include HydroPICC, a peripherally inserted central catheter cleared in 2018 and later extended to a dual-lumen configuration, and HydroMID, a midline catheter cleared in 2021, both carrying an anti-thrombogenic indication. The company is a device manufacturer rather than a software or platform business, and publishes no developer program, public API, or machine-readable API contract on any host it operates.
image: http://static1.squarespace.com/static/6221f3828dc3c91f338d47ed/t/65bacd55b532e27a3ad54ad9/1706741077575/AV_logo_white.png?format=1500w
layout: provider
modified: '2026-09-06'
name: Access Vascular, Inc.
nav: Providers
network: true
overview: 'Access Vascular, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Vascular Access, and Catheters.


  Access Vascular, Inc.''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Accessvascular Domain Security
  slug: accessvascular-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accessvascular
tags:
- Company
- Medical Devices
- Healthcare
- Vascular Access
- Catheters
- Biomaterials
- Manufacturing
website: https://www.accessvascularinc.com/
---
