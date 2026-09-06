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
  url: security/ababa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hr.ababa.co.jp/
- group: company
  title: ''
  type: Blog
  url: https://hr.ababa.co.jp/article
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hr.ababa.co.jp/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ababa.co.jp/terms_of_service
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/ababa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ababa-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 'ABABA runs two real first-party hosts — a Bubble.io end-user application at ababa.co.jp whose robots.txt is Disallow:/ for every user agent, and an undocumented Go API at api.ababa.co.jp (AWS ap-northeast-1, permissive CORS, /health 200) that backs it — but the company publishes no developer program at all: every OpenAPI/Swagger/GraphQL/agent-card/apis.json path on all three hosts 404s against a clean negative control, api./docs./developer subdomains either 404 or do not resolve, and the corporate site''s own sitemap lists only company, article, whitepaper, news, privacy and job-posting-policy routes with nothing developer-facing.'
  evidence:
  - status: 404
    url: https://api.ababa.co.jp/openapi.json
  - status: 404
    url: https://api.ababa.co.jp/graphql
  - status: 404
    url: https://api.ababa.co.jp/docs
  - status: 200
    url: https://api.ababa.co.jp/health
  - status: 404
    url: https://api.ababa.co.jp/.well-known/agent-card.json
  - status: 404
    url: https://api.ababa.co.jp/.well-known/ababa-negative-control-7f3ab91c.json
  - status: 404
    url: https://ababa.co.jp/openapi.json
  - status: 404
    url: https://ababa.co.jp/apis.json
  - status: 404
    url: https://ababa.co.jp/llms.txt
  - status: 200
    url: https://ababa.co.jp/robots.txt
  - status: 200
    url: https://hr.ababa.co.jp/sitemap-static.xml
  - status: 200
    url: https://hr.ababa.co.jp/zzz-does-not-exist-9f3a
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 'ABABA (株式会社ABABA) is a Tokyo-based Japanese HR technology company operating a new-graduate direct-recruiting platform built on an unusual premise: only students who have already reached the FINAL interview stage at another company may register, and each submits evidence of that selection history, so every candidate in the database arrives pre-qualified by someone else''s hiring bar. Employers then scout those near-miss finalists into abbreviated selection flows — the company reports that 94% of adopting employers waive the entry sheet or the first interview for an ABABA candidate. A second product, REALME, runs AI mock interviews and matching. Founded 19 October 2020 and led by co-representatives Shunki Kubo (CEO) and Tatsuya Nakai, ABABA raised a 1.25 billion yen Series B in March 2025 led by DBJ Capital (1.82 billion yen total to date) and reported passing 3,000 cumulative adopting companies in November 2025. The product ships purely as an end-user web application: ABABA
  publishes no developer portal, API documentation, SDK, webhook catalog or machine-readable specification of any kind.'
image: https://storage.googleapis.com/production-os-assets/assets/d1928efe-3d67-4bc2-ba43-8608be43531f
layout: provider
modified: '2026-09-05'
name: ABABA
nav: Providers
network: true
overview: 'ABABA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Recruiting, Talent Acquisition, and HR Technology.


  ABABA''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Ababa Plans Pricing
  plan_count: 0
  slug: ababa-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ababa Rate Limits
  slug: ababa-rate-limits
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 5
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Ababa Domain Security
  slug: ababa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ababa
tags:
- Company
- Human Resources
- Recruiting
- Talent Acquisition
- HR Technology
- Job Search
- Artificial Intelligence
- Japan
- SaaS
website: https://hr.ababa.co.jp/
---
