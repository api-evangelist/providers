---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonnet-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sonnet.ca/
- group: company
  title: ''
  type: About
  url: https://www.sonnet.ca/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.sonnet.ca/blog
- group: company
  title: ''
  type: Partnerships
  url: https://www.sonnet.ca/partnerships
- group: start
  title: ''
  type: Login
  url: https://www.sonnet.ca/account-log-in
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonnet-insurance
- group: company
  title: ''
  type: Twitter
  url: https://x.com/sonnetinsurance
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/sonnetinsurance/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/sonnetinsurance
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCEOXIbT5710DW8JhHfD_qhw
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@sonnetinsurance
- group: operate
  title: ''
  type: Support
  url: https://www.sonnet.ca/contact-us
- group: operate
  title: ''
  type: FAQ
  url: https://www.sonnet.ca/faqs
- group: start
  title: ''
  type: SignUp
  url: https://www.sonnet.ca/get-a-quote
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonnet.ca/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonnet.ca/privacy
- group: other
  title: ''
  type: Accessibility
  url: https://www.sonnet.ca/accessibility
- group: company
  title: ''
  type: News
  url: https://www.sonnet.ca/news
- group: company
  title: ''
  type: Careers
  url: https://www.sonnet.ca/join-us
- group: company
  title: ''
  type: Newsletter
  url: https://www.sonnet.ca/newsletter
- group: other
  title: ''
  type: Sitemap
  url: https://www.sonnet.ca/sitemap.xml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonnet-insurance-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: llms/sonnet-insurance-llms.txt
- group: other
  title: ''
  type: EndpointInventory
  url: endpoints/sonnet-insurance-observed-endpoints.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/sonnet-insurance-well-known.yml
created: '2026-07-25'
description: Sonnet Insurance is a Canadian direct-to-consumer digital property and casualty insurer launched in 2016 and a member of the Definity family of companies, underwriting its own auto, home, condo, tenant, landlord and pet policies through Sonnet Insurance Company. It sells auto, home, condo, tenant and landlord coverage in Ontario, Quebec, New Brunswick, Nova Scotia and Prince Edward Island, and home-only coverage in British Columbia and Alberta, positioning itself as "Canada's original digital-first home and auto insurance company" with a fully online quote-and-buy flow and licensed agents for support. Sonnet is an explicit direct writer -- its own FAQ states that "a third party -- even a licensed broker -- cannot purchase a Sonnet policy on your behalf" -- so it operates no broker or agency distribution channel and therefore no ACORD/AL3 agency-download path. Its API posture is closed -- no developer, developers, docs or api subdomain resolves in DNS, every first-party developer
  path probed returns HTTP 404, and no OpenAPI, Swagger, GraphQL, Postman collection, webhook catalog or partner technical onboarding surface is published. The only third-party integrations Sonnet describes -- the Kanetix.ca (RATESDOTCA) quote-and-buy partnership and the Sonnet Connect brand referral program -- are privately negotiated commercial arrangements with no public technical documentation. Two machine-readable surfaces do exist and are captured here. Sonnet serves a real llms.txt at www.sonnet.ca/llms.txt that declares per-agent AI-Training, AI-Generation, AI-Summarization and AI-Crawling directives (Allow for OpenAI, Google-DeepMind and Anthropic) alongside a curated reference-content index -- an AI consent signal rather than an API contract. And the secure.sonnet.ca quote-and-buy application is driven by an undocumented first-party REST/JSON surface under /api/v1 covering quoting, binding, policy servicing, payments and identity; it is observable from Sonnet's own public JavaScript
  bundle but carries no documentation, no specification and no third-party terms of use, so it is recorded as observed evidence, not as an integratable API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Sonnet Insurance
nav: Providers
network: true
overview: 'Sonnet Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Property and Casualty, Auto Insurance, and Home Insurance.


  Sonnet Insurance''s developer surface includes engineering blog, YouTube channel, support, FAQ, signup flow, product news, and 20 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 15.9
  delta: -1.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Sonnet Insurance Domain Security
  slug: sonnet-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonnet-insurance
tags:
- Insurance
- Canada
- Property and Casualty
- Auto Insurance
- Home Insurance
- Insurtech
- Direct to Consumer
- Underwriting
- Claims
website: https://www.sonnet.ca/
---
