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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acrove-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acrove.co.jp/
- group: company
  title: ''
  type: About
  url: https://acrove.co.jp/about/
- group: other
  title: ''
  type: x-company-profile
  url: https://acrove.co.jp/company/
- group: other
  title: ''
  type: Services
  url: https://acrove.co.jp/service/
- group: other
  title: ''
  type: CaseStudies
  url: https://acrove.co.jp/works/
- group: other
  title: ''
  type: x-group-companies
  url: https://acrove.co.jp/group/
- group: company
  title: ''
  type: Blog
  url: https://acrove.co.jp/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://acrove.co.jp/news/feed/
- group: company
  title: ''
  type: Careers
  url: https://acrove.co.jp/recruit/
- group: operate
  title: ''
  type: Contact
  url: https://acrove.co.jp/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acrove.co.jp/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Digital-Free
- group: company
  title: ''
  type: LinkedIn
  url: https://jp.linkedin.com/company/anoma-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/acrove_HR
- group: other
  title: ''
  type: x-secondary-market
  url: https://equityzen.com/company/acrove/
- group: other
  title: ''
  type: x-commerce-services
  url: https://commerce.acrove.co.jp/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acrove-llms.txt
coverage:
  checked: '2026-09-06'
  detail: 'ACROVE, Inc. ships software — the ACROVE FORCE / ACROVE INSIGHT EC analytics engine, ACROVE MDM and the ACROVE Knowledge Base — but only as internal and client-facing end-user applications behind a login, and its entire public surface across acrove.co.jp (a WordPress corporate site of 19 pages: about, service, works, company, group, news, recruit, contact, privacy) and commerce.acrove.co.jp (the Magento / Adobe Commerce services arm, formerly Digital-Free K.K.) carries no developer, API, docs or integration link anywhere in the nav, sitemap or llms.txt; every REST/GraphQL/OpenAPI/MCP/agent-card and /.well-known/ path probed on all five hosts the company operates returns a hard 404 (verified against a control path returning the identical 404 body and status) or, on kb.acrove.co.jp, a 307 to its own login, and the company markets no API product, so this is an absent developer program rather than a gated one.'
  evidence:
  - status: 200
    url: https://acrove.co.jp/
  - status: 404
    url: https://acrove.co.jp/openapi.json
  - status: 404
    url: https://acrove.co.jp/swagger.json
  - status: 404
    url: https://acrove.co.jp/api-docs
  - status: 404
    url: https://acrove.co.jp/graphql
  - status: 404
    url: https://acrove.co.jp/developers
  - status: 404
    url: https://acrove.co.jp/llms.txt
  - status: 403
    url: https://acrove.co.jp/wp-json/
  - status: 404
    url: https://acrove.co.jp/.well-known/agent-card.json
  - status: 404
    url: https://acrove.co.jp/.well-known/agent.json
  - status: 404
    url: https://acrove.co.jp/.well-known/api-catalog
  - status: 404
    url: https://acrove.co.jp/.well-known/security.txt
  - status: 404
    url: https://acrove.co.jp/zz-api-evangelist-control-7c21
  - status: 200
    url: https://commerce.acrove.co.jp/llms.txt
  - status: 404
    url: https://commerce.acrove.co.jp/openapi.json
  - status: 404
    url: https://commerce.acrove.co.jp/rest/all/schema?services=all
  - status: 404
    url: https://mdm.acrove.co.jp/openapi.json
  - status: 307
    url: https://kb.acrove.co.jp/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'ACROVE, Inc. (株式会社ACROVE) is a Tokyo e-commerce platform and brand roll-up company, founded 15 November 2018 as Anoma, Inc. and renamed ACROVE in October 2020, led by representative director Shunsuke Arai and headquartered in Nishi-Shinjuku. It runs two businesses: a Commerce Transformation practice that grows client brand sales on Amazon, Rakuten, Qoo10 and other Japanese marketplaces using its proprietary EC analytics engine ACROVE FORCE (now presented as ACROVE INSIGHT), and an EC roll-up business that acquires and operates consumer brands. It reports support for 170+ client companies and raised a Series C in September 2024. Its commerce arm — the former Digital-Free K.K., now 株式会社Acrove at commerce.acrove.co.jp — is a Magento / Adobe Commerce implementation specialist. ACROVE FORCE, ACROVE MDM and the ACROVE Knowledge Base are login-gated applications; the company publishes no public API, SDK, webhook surface, machine-readable contract or developer portal on any host it
  operates.'
image: https://acrove.co.jp/wp/wp-content/themes/site-theme-corp-01/library/images/common/ogp.png
layout: provider
modified: '2026-09-06'
name: ACROVE, Inc.
nav: Providers
network: true
overview: 'ACROVE, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Marketplaces, Business Intelligence, and Retail.


  ACROVE, Inc.''s developer surface includes engineering blog and 17 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 8.7
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Acrove Domain Security
  slug: acrove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acrove
tags:
- Company
- E-commerce
- Marketplaces
- Business Intelligence
- Retail
- Consumer Brands
- Adobe Commerce
- Japan
website: https://acrove.co.jp/
---
