---
access_model:
  confidence: high
  label: Self-service SaaS, no API
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://heyo.com/pricing/
  - https://platform.heyo.com/register
  trial: true
  try_now: true
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heyo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heyo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://heyo.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heyo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heyo.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://platform.heyo.com/login
- group: start
  title: ''
  type: SignUp
  url: https://platform.heyo.com/register
- group: operate
  title: ''
  type: Support
  url: https://support.heyo.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.heyo.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/heyo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heyo-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heyo-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Heyo ships only an end-user campaign builder — the words "Developer API" appear once on the heyo.com homepage as static headline copy with no link behind them, while /api, /developer, /developers, /docs and /api-docs all 404 and api.heyo.com, developer.heyo.com and docs.heyo.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://heyo.com/developer
  - status: 404
    url: https://heyo.com/api-docs
  - status: 404
    url: https://heyo.com/.well-known/api-catalog
  - status: 200
    url: https://heyo.com/pricing/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Heyo is a social marketing platform for building and running online promotions such as sweepstakes, contests, giveaways, quizzes, and coupons. Businesses use Heyo's drag-and-drop campaign builder and landing pages to create interactive campaign apps that publish to the web, mobile, and social networks including Facebook, Instagram, and Twitter. It is used to grow email marketing lists, generate sales leads, acquire new customers, reward existing customers, and increase social followers, with templated promotion apps and a free trial. Heyo is a portfolio company of 500 Global and was acquired by Votigo, Inc. in January 2016, continuing to operate as a stand-alone self-serve brand. Heyo publishes no public API, SDK or developer portal; the product is used entirely through the web dashboard at platform.heyo.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heyo.png
layout: provider
modified: '2026-08-13'
name: Heyo
nav: Providers
network: true
overview: 'Heyo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Social-Media, Promotions, and Contests.


  Heyo''s developer surface includes pricing, signup flow, support, engineering blog, and 8 more developer resources.'
plans:
- name: Heyo Plans Pricing
  plan_count: 4
  slug: heyo-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Heyo Rate Limits
  slug: heyo-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heyo/refs/heads/main/screenshots/heyo-2026-07-25T221123.png
security:
- kind: domain-security
  name: Heyo Domain Security
  slug: heyo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: heyo
tags:
- Company
- Marketing
- Social-Media
- Promotions
- Contests
- Sweepstakes
- Giveaways
- Lead Generation
- Email Marketing
- Campaigns
website: https://heyo.com
---
