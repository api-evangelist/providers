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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashtag-paid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hashtagpaid.com/
- group: operate
  title: ''
  type: Support
  url: https://support.hashtagpaid.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://hashtagpaid.com/banknotes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hashtagpaid.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hashtagpaid.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.hashtagpaid.app/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashtagpaid
- group: other
  title: ''
  type: AIPrinciples
  url: https://hashtagpaid.com/ai-principles
- group: commercial
  title: ''
  type: Plans
  url: plans/hashtag-paid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hashtag-paid-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hashtag-paid-llms.txt
coverage:
  checked: '2026-08-22'
  detail: '#paid ships only end-user brand and creator web apps — hashtagpaid.com has no /developers, /api or /docs route (all 404), its two public GitHub repos are an org README and a 2023 notion-tracker, and the private backend at api.hashtagpaid.app 404s every spec path — the company consumes the TikTok/Meta advertising APIs rather than publishing one of its own.'
  evidence:
  - status: 404
    url: https://hashtagpaid.com/developers
  - status: 404
    url: https://hashtagpaid.com/docs
  - status: 404
    url: https://hashtagpaid.com/openapi.json
  - status: 404
    url: https://api.hashtagpaid.app/openapi.json
  - status: 200
    url: https://creator.hashtagpaid.app/openapi.json
  - status: 404
    url: https://hashtagpaid.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: 'Hashtag Paid Inc., which trades as #paid, is a Toronto-headquartered creator marketing platform that connects brands and agencies with social media creators. The product is a marketplace and campaign workspace: brands brief a campaign, are matched to vetted creators, review and approve content, license and amplify that content as paid social advertising across Meta, TikTok, YouTube, Snapchat and Pinterest, then measure results and pay creators automatically. #paid is a badged TikTok Marketing Partner and consumes the social platforms'' advertising APIs on its customers'' behalf. It runs as an end-user SaaS product with brand and creator web applications; as of this profile it publishes no public developer program, API reference, or machine-readable contract.'
image: https://cdn.prod.website-files.com/5c34f4c0ee3329913fc72eac/651c65cce2071a7de8b14a73_open-graph.webp
layout: provider
modified: '2026-08-22'
name: Hashtag Paid
nav: Providers
network: true
overview: 'Hashtag Paid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Marketing, Influencer Marketing, Marketing, and Advertising.


  Hashtag Paid''s developer surface includes support, engineering blog, and 10 more developer resources.'
plans:
- name: Hashtag Paid Plans Pricing
  plan_count: 0
  slug: hashtag-paid-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Hashtag Paid Rate Limits
  slug: hashtag-paid-rate-limits
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Hashtag Paid Domain Security
  slug: hashtag-paid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hashtag-paid
tags:
- Company
- Creator Marketing
- Influencer Marketing
- Marketing
- Advertising
- Social-Media
- Content
- Marketplace
- Creator Economy
website: https://hashtagpaid.com/
---
