---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://ground.news/
- group: company
  title: ''
  type: About
  url: https://ground.news/about
- group: company
  title: ''
  type: Blog
  url: https://ground.news/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://ground.news/blog/rss
- group: company
  title: ''
  type: Careers
  url: https://ground.news/careers
- group: commercial
  title: ''
  type: Pricing
  url: https://ground.news/subscribe
- group: start
  title: ''
  type: SignUp
  url: https://ground.news/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ground.news/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ground.news/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://ground.news/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ground.news
- group: operate
  title: ''
  type: FAQ
  url: https://ground.news/frequently-asked-questions
- group: company
  title: ''
  type: Newsletter
  url: https://ground.news/newsletters/daily-ground
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/app/apple-store/id1324203419
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.checkitt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ground-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/ground-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ground-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ground-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ground-llms.txt
coverage:
  checked: '2026-08-13'
  detail: 'Ground News ships only a consumer news app: its single live machine surface, api.ground.news, is the private Express backend of that app and answers HTTP 418 "I''m a Teapot" to every path including the root, while developer., developers., docs., status. and trust.ground.news do not resolve at all and every well-known, OpenAPI and agent-card path on the four hosts it does serve returns 404 — the only third-party integration point it publishes is a single unauthenticated iframe story widget.'
  evidence:
  - status: 418
    url: https://api.ground.news/openapi.json
  - status: 418
    url: https://api.ground.news/
  - status: 404
    url: https://ground.news/openapi.json
  - status: 404
    url: https://ground.news/graphql
  - status: 404
    url: https://ground.news/.well-known/agent-card.json
  - status: 404
    url: https://ground.news/.well-known/agent.json
  - status: 404
    url: https://ground.news/llms.txt
  - status: 404
    url: https://about.ground.news/.well-known/security.txt
  - status: 404
    url: https://help.ground.news/openapi.json
  - status: 404
    url: https://api.github.com/orgs/groundnews
  - status: 200
    url: https://ground.news/widget/story?offset=1
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Ground News is a news aggregation platform, built by Snapwise Inc. and backed by Techstars, that helps readers see every side of every story. It gathers coverage of each news event from across the political spectrum and pairs every story with media bias ratings, factuality assessments, and source-ownership transparency. Signature features include the Blindspot Feed that surfaces stories disproportionately covered by the left or right, a per-story bias-distribution bar, local news customization, daily briefing newsletters, browser extensions, and iOS/Android apps. Ground News does not currently publish a public developer API, developer portal, or API documentation, and its one live machine surface, api.ground.news, is the private backend of its own apps. The single integration point it does publish is an unauthenticated embeddable iframe story widget. This profile captures that widget, the company's public web and commercial surface, the contract-discovery probe record, and its
  domain-security posture.
image: https://groundnews.b-cdn.net/assets/logo4/GN_Square.png
layout: provider
modified: '2026-08-13'
name: Ground
nav: Providers
network: true
overview: 'Ground is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, News, Media, Media Bias, and News Aggregation.


  Ground''s developer surface includes engineering blog, pricing, signup flow, support, FAQ, and 15 more developer resources.'
plans:
- name: Ground Plans Pricing
  plan_count: 2
  slug: ground-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ground Rate Limits
  slug: ground-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ground/refs/heads/main/screenshots/ground-2026-07-25T220344.png
security:
- kind: domain-security
  name: Ground Domain Security
  slug: ground-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ground
tags:
- Company
- News
- Media
- Media Bias
- News Aggregation
- Journalism
- Media Monitoring
- Consumer Apps
website: https://ground.news/
---
