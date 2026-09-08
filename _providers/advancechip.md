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
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancechip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.advancechip.com/
- group: company
  title: ''
  type: WebsiteEnglish
  url: http://en.advancechip.com/
- group: operate
  title: ''
  type: Support
  url: http://en.advancechip.com/technology/technology
- group: other
  title: ''
  type: Downloads
  url: http://en.advancechip.com/download/download
- group: build
  title: ''
  type: DevelopmentTools
  url: http://en.advancechip.com/development/development
- group: company
  title: ''
  type: News
  url: http://en.advancechip.com/news/news
- group: company
  title: ''
  type: Careers
  url: http://en.advancechip.com/join/job
- group: operate
  title: ''
  type: ContactUs
  url: http://en.advancechip.com/cont/contect
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/advancechip/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancechip-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Advancechip is a Changsha fabless DSP chip designer whose entire developer surface is silicon and hardware — its "Development tools" page lists evaluation boards and its "Download materials" page serves chip data manuals as PDFs from a bare-IP file host (http://42.48.83.242:25662/), with no API, no developer portal and no machine-readable contract anywhere on the domain; the only JSON endpoint the site touches is its web agency's multi-tenant CMS backend at jxdzkj.api.hnjwglobal.com, which is not an Advancechip product and rejects off-domain callers with {"StatusCode":408,"Message":"访问域名无效"}.
  evidence:
  - status: 200
    url: http://en.advancechip.com/development/development
  - status: 200
    url: http://en.advancechip.com/download/download
  - status: 404
    url: http://www.advancechip.com/openapi.json
  - status: 404
    url: http://www.advancechip.com/.well-known/api-catalog
  - status: 404
    url: http://www.advancechip.com/llms.txt
  - status: 200
    url: https://jxdzkj.api.hnjwglobal.com/
  - status: 404
    url: https://api.github.com/users/advancechip
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'Advancechip Technology (Hunan) Co., Ltd. — 进芯科技（湖南）股份有限公司, formerly Hunan Jinxin Electronic Technology Co., Ltd. — is a fabless integrated-circuit design company founded in October 2012 and headquartered in Changsha, Hunan, China. It develops digital signal processor (DSP) chips and embedded solutions, and states that it has taken three DSP families to mass production: 16-bit fixed-point (ADP16), 32-bit fixed-point (ADP32) and 32-bit floating-point (AVP32), alongside single-core and multi-core SoC parts such as the ADM32F036 motor-control family. The company describes its core technologies as DSP core design, compilation technology, large-scale SoC digital integration and core drive algorithms, held as a fully independent intellectual-property stack, and targets automotive electronics, thermal management, smart home and white goods, small household appliances, health equipment and power tools. Its developer-facing surface is hardware, not web software: evaluation and development
  boards (AVP32F379QP176, AVP32F00157QP80, AVP32F0039QP100S, ADM32F036A5Q/A6Q/A7Q low-voltage motor boards), a technical-support page and a download section that serves chip data manuals as PDFs from a third-party file host. As probed on 2026-09-07 Advancechip publishes no public web API, no developer portal or API reference, no OpenAPI/AsyncAPI/GraphQL contract, no SDK in any public package registry, no GitHub organization and no /.well-known documents; the corporate site itself is served over plaintext HTTP only.'
image: https://oss-usa.jingwxcx.com/jxdzkj/upload_files/2025/10/14/9d78c00f818c49a3a65c1ff0f8d3830e.png
layout: provider
modified: '2026-09-07'
name: Advancechip Technology (Hunan) Co., Ltd.
nav: Providers
network: true
overview: 'Advancechip Technology (Hunan) Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Integrated Circuits, Digital Signal Processing, and Embedded Systems.


  Advancechip Technology (Hunan) Co., Ltd.''s developer surface includes support, product news, and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.7
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advancechip Domain Security
  slug: advancechip-domain-security
  summary_line: DMARC
slug: advancechip
tags:
- Company
- Semiconductors
- Integrated Circuits
- Digital Signal Processing
- Embedded Systems
- System On Chip
- Automotive Electronics
- Motor Control
- Industrial Control
- Hardware
- China
website: http://www.advancechip.com/
---
