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
- group: company
  title: ''
  type: Website
  url: https://8percent.kr/
- group: company
  title: ''
  type: About
  url: https://about.8percent.kr/
- group: company
  title: ''
  type: Blog
  url: https://blog.8percent.kr/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.8percent.kr/feed
- group: operate
  title: ''
  type: PressReleases
  url: https://blog.8percent.kr/category/newsroom/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/8percent
- group: company
  title: ''
  type: Careers
  url: https://8percent.careers.team/
- group: other
  title: ''
  type: X
  url: https://x.com/8percent_kr
- group: operate
  title: ''
  type: Support
  url: https://8percent.kr/board/faq/
- group: start
  title: ''
  type: Login
  url: https://8percent.kr/user/login/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/8percent-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/8percent-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/8percent-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/8percent-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 8percent ships only an end-user Korean consumer lending and investing product; the JSON API host its own site bundle names, https://core-api.8percent.kr/api, answers /openapi.json, /swagger.json, /graphql and /api-docs with HTTP 404 and denies the entire /.well-known/ prefix with 403, and neither developers.8percent.kr nor docs.8percent.kr resolves in DNS, no SDK on npm or PyPI, and no API mentioned anywhere on 8percent.kr or about.8percent.kr.
  evidence:
  - status: 404
    url: https://core-api.8percent.kr/openapi.json
  - status: 200
    url: https://core-api.8percent.kr/health
  - status: 403
    url: https://core-api.8percent.kr/.well-known/oauth-authorization-server
  - status: 404
    url: https://api.8percent.kr/openapi.json
  - status: 404
    url: https://8percent.kr/llms.txt
  - status: 404
    url: https://8percent.kr/.well-known/agent-card.json
  - status: 200
    url: https://8percent.kr/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 8percent (에잇퍼센트) is a Seoul-based fintech company, founded in November 2014, that built Korea's first-generation peer-to-peer lending marketplace and in June 2021 became the country's first company registered as an Online Investment-linked Finance Business operator (온라인투자연계금융업 registration 2021-2) under the Financial Services Commission. Its platform matches retail and institutional investors with mid-credit borrowers, and has expanded from unsecured personal credit loans into real-estate-backed lending, stock-purchase loans, gig-worker financing, small-business loans and rental-deposit loans, underwriting them with an in-house AI credit-assessment model the company markets as "E-index". Cumulative originations are reported at roughly ₩1.4 trillion, and in July 2026 8percent acquired security-token operator A-Panda Partners to tokenize loan receivables. The service ships as a Korean-language consumer web app plus iOS and Android apps, served by a private first-party API host
  (core-api.8percent.kr) that the site's own production JavaScript names as its base. 8percent publishes no developer portal, no API reference, no SDK and no machine-readable contract of any kind; its public GitHub organization carries internal engineering tooling and study repos rather than API client libraries.
image: https://cdn-media.8percent.kr/meta/8percent-meta.png
layout: provider
modified: '2026-09-05'
name: 8percent
nav: Providers
network: true
overview: '8percent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Lending, and P2P Lending.


  8percent''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: 8Percent Plans Pricing
  plan_count: 0
  slug: 8percent-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: 8Percent Rate Limits
  slug: 8percent-rate-limits
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 8Percent Domain Security
  slug: 8percent-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 8percent
tags:
- Company
- Financial Services
- Fintech
- Lending
- P2P Lending
- Marketplace Lending
- Credit Scoring
- Investing
- Consumer Finance
- Real Estate Lending
- Tokenization
- South Korea
website: https://8percent.kr/
---
