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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/life-is-tech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/life-is-tech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://life-is-tech.com/
- group: company
  title: ''
  type: About
  url: https://life-is-tech.com/about/
- group: other
  title: ''
  type: CompanyProfile
  url: https://life-is-tech.com/profile/
- group: other
  title: ''
  type: Products
  url: https://life-is-tech.com/product/
- group: company
  title: ''
  type: Blog
  url: https://note.com/lifeistech
- group: company
  title: ''
  type: News
  url: https://life-is-tech.com/news/
- group: operate
  title: ''
  type: PressRelease
  url: https://life-is-tech.com/news/pressrelease
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lifeistech
- group: operate
  title: ''
  type: Support
  url: https://form.run/@lifeistech-form
- group: start
  title: ''
  type: Login
  url: https://members.life-is-tech.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://life-is-tech.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://life-is-tech.com/terms-manabidx/
- group: company
  title: ''
  type: Careers
  url: https://jobs.life-is-tech.com/
coverage:
  checked: '2026-08-25'
  detail: 'Life is Tech sells finished digital-education products (camps, the Lesson school curriculum, corporate DX training) and runs no developer program at all: every /openapi.json, /graphql, /llms.txt and /.well-known/* path on all ten public hosts missed, its 16-repo GitHub org holds only Swift/Kotlin curriculum samples, and school sign-in is Microsoft/Google SSO issued by the school rather than a public OAuth app.'
  evidence:
  - status: 404
    url: https://life-is-tech.com/openapi.json
  - status: 403
    url: https://life-is-tech.com/.well-known/api-catalog
  - status: 403
    url: https://lifeistech-lesson.jp/openapi.json
  - status: 200
    url: https://dx.life-is-tech.com/zzz-control-9999
  - status: 200
    url: https://api.github.com/orgs/lifeistech
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Life is Tech, Inc. (ライフイズテック株式会社) is a Tokyo-based education technology company founded on 6 July 2010 by Yusuke Mizuno, delivering digital, programming and AI education to Japanese teenagers, schools, municipalities and employers. Its products are "Life is Tech !" IT camps and year-round schools for junior and senior high school students, "Life is Tech ! Lesson" — a cloud-based information and programming curriculum used by roughly 4,000 public and private schools across some 600 municipalities — "Life is Tech ! Leaders" for university students, "Life is Tech ! Career" digital job-hunting support, and DX Readiness corporate digital-skills training. The company is a certified B Corporation (October 2022, the first Japanese EdTech to certify) and holds the PrivacyMark. Life is Tech sells finished learning products to schools and consumers; it publishes no public developer program, API, SDK or machine-readable contract.
image: https://life-is-tech.com/assets/meta/ogp.png
layout: provider
modified: '2026-08-25'
name: Life is Tech
nav: Providers
network: true
overview: 'Life is Tech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Learning, and Training.


  Life is Tech''s developer surface includes engineering blog, product news, support, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.1
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Life Is Tech Domain Security
  slug: life-is-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: life-is-tech
tags:
- Company
- Education
- EdTech
- Learning
- Training
- Programming Education
- Digital Skills
- Japan
website: https://life-is-tech.com/
---
