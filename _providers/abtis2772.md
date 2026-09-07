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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abtis2772-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abtis2772-llms.txt
- group: company
  title: ''
  type: Website
  url: https://abtis.co.kr/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/abtis2772/
- group: company
  title: ''
  type: About
  url: https://abtis.co.kr/en/company/overview.php
- group: operate
  title: ''
  type: Contact
  url: https://abtis.co.kr/en/company/contact.php
- group: operate
  title: ''
  type: PressReleases
  url: https://abtis.co.kr/en/pr-center/press-release.php
coverage:
  checked: '2026-09-06'
  detail: 'AbTis sells ADC linker chemistry — AbClick platform licences, collaborative research and fee-for-service conjugation work — so there is no software product to expose: its only web property is a gnuboard5 corporate site whose entire navigation is Company, Science, Business and News, and behind the site''s CUPID JavaScript cookie challenge (which answers HTTP 200 with a ~780-byte script on every path, then the real status on the cookied retry) /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt, /robots.txt, /sitemap.xml and all eight /.well-known/ paths return a genuine Apache 404.'
  evidence:
  - status: 200
    url: https://abtis.co.kr/en/
  - status: 404
    url: https://abtis.co.kr/openapi.json
  - status: 404
    url: https://abtis.co.kr/swagger.json
  - status: 404
    url: https://abtis.co.kr/graphql
  - status: 404
    url: https://abtis.co.kr/.well-known/agent-card.json
  - status: 404
    url: https://abtis.co.kr/.well-known/api-catalog
  - status: 404
    url: https://abtis.co.kr/llms.txt
  - status: 403
    url: https://www.abtis.co.kr/openapi.json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=abtis
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'AbTis Co., Ltd. (앱티스) is a South Korean biotechnology company founded in 2016 and headquartered in Yongin-si, Gyeonggi-do, inside the Dong-A Socio Holdings R&D Center. It develops AbClick, a third-generation site-selective antibody conjugation platform that attaches payloads to the Fc Lys248 residue of native IgG antibodies with no enzyme and no Fc engineering, giving a controlled drug-to-antibody ratio and batch-to-batch consistency across ADC, DAC, AOC, ARC, ISAC and dual-payload designs. AbTis licenses the platform, runs collaborative research and fee-for-service ADC development, and advances its own pipeline led by AT-211, a Claudin 18.2-targeting MMAE ADC. Acquired by Dong-A ST in 2023, it now operates as that company''s ADC-specialised subsidiary. Its product is licensed chemistry and drug intellectual property, not software: it runs no developer program, public API, SDK or machine-readable contract.'
image: https://abtis.co.kr/assets/favicon/favicon-96x96.png
layout: provider
modified: '2026-09-06'
name: AbTis
nav: Providers
network: true
overview: AbTis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Antibody-Drug Conjugates, and Bioconjugation.
random_paper: 6
score:
  band: minimal
  composite: 4.1
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Abtis2772 Domain Security
  slug: abtis2772-domain-security
  summary_line: TLSv1.2
slug: abtis2772
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Antibody-Drug Conjugates
- Bioconjugation
- Drug Discovery
- Oncology
- Life Sciences
- Healthcare
- South Korea
website: https://abtis.co.kr/en/
---
