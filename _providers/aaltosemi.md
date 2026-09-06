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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aaltosemi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aaltosemi.com/en/
- group: company
  title: ''
  type: About
  url: https://www.aaltosemi.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.aaltosemi.com/en/h-col-106.html
- group: company
  title: ''
  type: Careers
  url: https://www.aaltosemi.com/en/h-col-113.html
- group: operate
  title: ''
  type: Contact
  url: https://www.aaltosemi.com/en/h-col-107.html
- group: other
  title: ''
  type: Sustainability
  url: https://www.aaltosemi.com/en/h-col-105.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aaltosemi-inc
- group: other
  title: ''
  type: X-SecondaryMarketListing
  url: https://equityzen.com/company/aaltosemi/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aaltosemi-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 'AaltoSemi is an IC packaging-substrate fab in Nanjing that sells physical BT and ABF substrates to chip makers, not software: www.aaltosemi.com is a six-page corporate CMS site with a Product Center, ESG, News, Careers and Contact section and no developer, API, or download area anywhere in it, and api./developer./developers./docs./portal. aaltosemi.com do not resolve in DNS.'
  evidence:
  - status: 200
    url: https://www.aaltosemi.com/en/
  - status: 404
    url: https://www.aaltosemi.com/openapi.json
  - status: 404
    url: https://www.aaltosemi.com/api-docs
  - status: 404
    url: https://www.aaltosemi.com/graphql
  - status: 404
    url: https://www.aaltosemi.com/llms.txt
  - status: 404
    url: https://www.aaltosemi.com/.well-known/agent-card.json
  - status: 404
    url: https://www.aaltosemi.com/.well-known/api-catalog
  - status: 0
    url: https://api.aaltosemi.com/openapi.json
  - status: 404
    url: https://github.com/aaltosemi
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'AaltoSemi (Chinese name 芯爱科技（南京）有限公司) is an integrated-circuit packaging substrate manufacturer founded on 8 May 2021 and headquartered in the Pukou Economic Development Zone in Nanjing, Jiangsu, China. The company designs and fabricates the organic substrates that carry the electrical connection between a semiconductor die and the printed circuit board, covering both BT and ABF material systems across Coreless, ETS, FCCSP, FCBGA (BT) and FCBGA (ABF) product families for consumer electronics, high-performance computing, communications, automotive and medical applications, and it offers those as an end-to-end service spanning R&D, design, production and test. Its Nanjing fab is a high-automation plant with a stated annual capacity of roughly 1.45 million substrate panels, and the company holds IATF 16949 and VDA 6.3 quality certifications and has filed more than twenty patents since founding. The name is taken from the Finnish designer Alvar Aalto. AaltoSemi is a hardware manufacturer:
  it sells physical substrates to chip makers and OSATs, and it publishes no public API, developer portal, SDK or machine-readable contract of any kind.'
image: https://www.aaltosemi.com/favicon.ico
layout: provider
modified: '2026-09-05'
name: Aaltosemi
nav: Providers
network: true
overview: 'Aaltosemi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Semiconductor Packaging, IC Substrates, and Advanced Packaging.


  Aaltosemi''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.5
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Aaltosemi Domain Security
  slug: aaltosemi-domain-security
  summary_line: TLSv1.2
slug: aaltosemi
tags:
- Company
- Semiconductors
- Semiconductor Packaging
- IC Substrates
- Advanced Packaging
- Electronics Manufacturing
- Hardware
- FCBGA
- Nanjing
- China
website: https://www.aaltosemi.com/en/
---
