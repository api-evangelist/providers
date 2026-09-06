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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.westock.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.westock.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/westock-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.westock.io/resources
- group: operate
  title: ''
  type: HelpCenter
  url: https://westock.helpscoutdocs.com/
- group: operate
  title: ''
  type: Support
  url: https://westock.helpscoutdocs.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westock.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westock.io/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.westock.io/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/westock-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/westock-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: WeStock runs a real first-party backend at api.westock.io that answers HTTP 401 "Unauthorized" on every path including the root, but ships nothing for developers — the marketing site has no /developers, /docs or /api page anywhere in its 92-URL sitemap, and the Help Scout knowledge base's only "API key" article is about pasting a customer's own Klaviyo key into the WeStock dashboard.
  evidence:
  - status: 401
    url: https://api.westock.io/openapi.json
  - status: 401
    url: https://api.westock.io/
  - status: 503
    url: https://api.labs.westock.io/
  - status: 200
    url: https://www.westock.io/sitemap.xml
  - status: 404
    url: https://westock.io/.well-known/agent-card.json
  - status: 404
    url: https://westock.io/llms.txt
  - status: 502
    url: https://webapi.westock.io/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'WeStock is a shopper-marketing platform that helps consumer packaged goods (CPG) brands drive product trial, build first-party retail audiences, and manage trade and shopper marketing strategy from a single dashboard. It combines digital rebates and promotional campaigns, paid social advertising (primarily Meta), in-store sampling and demos, retail media management across Amazon, Walmart, and Instacart, email/SMS automation, and influencer marketing, alongside a consumer discovery web app used by 600,000+ shoppers to browse new products. Campaign data — trials, conversions, and repeat behavior — is unified in one place. A Techstars-backed company; its entire public surface is a Webflow marketing site, a Help Scout knowledge base of product how-tos, and login-gated dashboard and consumer apps. WeStock runs a real first-party backend at api.westock.io — hardened Node/Express that answers HTTP 401 on every path including the root — but ships no developer program: no API reference,
  no OpenAPI or GraphQL schema, no SDK on any registry, no webhooks, and no API pricing. Its documented integrations run the other way: WeStock consumes Klaviyo and Attentive using keys the customer pastes into the WeStock dashboard.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/westock.png
layout: provider
modified: '2026-08-12'
name: WeStock
nav: Providers
network: true
overview: 'WeStock is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shopper Marketing, Consumer Packaged Goods, Retail Media, and Marketing.


  WeStock''s developer surface includes pricing, engineering blog, support, signup flow, and 7 more developer resources.'
plans:
- name: Westock Plans Pricing
  plan_count: 3
  slug: westock-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/westock/refs/heads/main/screenshots/westock-2026-09-02T170634.png
security:
- kind: domain-security
  name: Westock Domain Security
  slug: westock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: westock
tags:
- Company
- Shopper Marketing
- Consumer Packaged Goods
- Retail Media
- Marketing
- Rebates
- Audience Building
- Trade Promotion
- First-Party Data
- Retail
- Advertising
website: https://www.westock.io/
---
