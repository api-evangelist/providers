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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.adoc.co.kr/
- group: company
  title: ''
  type: About
  url: https://www.adoc.co.kr/1738bf80b49d8013b8d6fc1ebe7b5c6c
- group: other
  title: ''
  type: Products
  url: https://www.adoc.co.kr/kindoccare-cms
- group: company
  title: ''
  type: Careers
  url: https://www.adoc.co.kr/recruit
- group: company
  title: ''
  type: Blog
  url: https://post.naver.com/my.naver?memberNo=45438006
- group: operate
  title: ''
  type: Support
  url: https://n481v.channel.io/support-bots/71968
- group: commercial
  title: ''
  type: TermsOfService
  url: https://team.adoc.co.kr/services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://team.adoc.co.kr/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://kr.linkedin.com/company/%EC%A3%BC-%EB%B9%84%EB%B0%94%EC%9D%B4%EB%85%B8%EB%B2%A0%EC%9D%B4%EC%85%98-vivainnovation
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/adoc2d3b/
- group: auth
  title: ''
  type: Compliance
  url: https://kindoclabs.adoc.co.kr/
- group: design
  title: ''
  type: Conformance
  url: conformance/adoc2d3b-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adoc2d3b-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adoc2d3b-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/adoc2d3b-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adoc2d3b-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adoc2d3b-rate-limits.yml
coverage:
  checked: '2026-09-07'
  detail: Adoc is the brand of Viva Innovation Inc. (비바이노베이션), a Seoul health-checkup platform whose entire public surface is consumer- and hospital-facing — the 착한의사 booking app, ~150 partner landing subdomains, an imweb-built corporate site, a Notion policy workspace and the Kindoc AI chat app — with no developer, docs, portal or integration link anywhere in the nav, footer or the 154-name certificate-transparency subdomain set for adoc.co.kr, which contains no api., docs. or developer. host at all; every OpenAPI, GraphQL, MCP tools/list, agent-card, apis.json and /.well-known/ path probed on adoc.co.kr and chat.kindoc.ai returns a hard 404, and the only 2xx on any company host is checkup.adoc.co.kr's Next.js catch-all, which also answers 200 to a random negative-control path.
  evidence:
  - status: 200
    url: https://www.adoc.co.kr/
  - status: 404
    url: https://www.adoc.co.kr/openapi.json
  - status: 404
    url: https://chat.kindoc.ai/openapi.json
  - status: 404
    url: https://www.adoc.co.kr/.well-known/agent-card.json
  - status: 200
    url: https://checkup.adoc.co.kr/.well-known/adoc2d3b-negative-control-7f3ab91c.json
  - status: 200
    url: https://www.adoc.co.kr/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'Adoc is the corporate web presence of Viva Innovation Inc. (주식회사 비바이노베이션), a Seoul, South Korea health-technology company founded in January 2018 and based in Gangnam-gu, which operates the health-checkup and medical-records platform 착한의사 (Chakan Uisa / Kindoc). Consumers use the Kindoc mobile and web apps to pull scattered personal medical records into one place, run an AI symptom check against personal and Health Insurance Review and Assessment Service data, compare hospital examination packages and their costs, and book discounted health screenings; employers buy the same screenings as corporate checkup programs, and partner hospitals join through a hospital-affiliation program. For providers the company sells a medical cloud — Kindoc Care CMS and Kindoc Care PMS for checkup centres — alongside a medical AI line it splits into Preventive AI (test-item recommendation, plain-language result explanation, biomarker and biological-age analysis), Clinical AI (comprehensive findings
  generation, abnormal-finding triage, follow-up test recommendation) and Decision Support AI (disease-risk analysis from repeated checkup results, endoscopy anaesthesia-risk prediction, real-time endoscopic polyp detection), plus a generative "주치의 AI" assistant published as Dr.Patch at chat.kindoc.ai and a research arm, Kindoc Labs. Everything the company ships is a consumer app, a partner landing page or hospital-side software: as of this profile it publishes no developer portal, no API reference, no SDK and no machine-readable API contract on any host it operates.'
image: https://cdn.imweb.me/upload/S2023082254a034e705567/24610c2048096.png
layout: provider
modified: '2026-09-07'
name: Adoc (Viva Innovation)
nav: Providers
network: true
overview: 'Adoc (Viva Innovation) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Checkup, Medical Records, and Preventive Medicine.


  Adoc (Viva Innovation)''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Adoc2D3B Plans Pricing
  plan_count: 0
  slug: adoc2d3b-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Adoc2D3B Rate Limits
  slug: adoc2d3b-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 10.7
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adoc2D3B Domain Security
  slug: adoc2d3b-domain-security
  summary_line: TLSv1.3
slug: adoc2d3b
tags:
- Company
- Healthcare
- Health Checkup
- Medical Records
- Preventive Medicine
- Artificial Intelligence
- Digital Health
- Clinical Data
- Hospital Software
- South Korea
website: https://www.adoc.co.kr/
---
