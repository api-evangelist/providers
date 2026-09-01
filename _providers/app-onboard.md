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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.quvy.com
- group: other
  title: ''
  type: CompanyDomain
  url: https://apponboard.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quvy.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.quvy.com/all-blog-posts/
- group: operate
  title: ''
  type: Support
  url: https://www.quvy.com/contact/
- group: start
  title: ''
  type: Login
  url: https://www.quvy.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://public.quvy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://public.quvy.com/privacy
- group: other
  title: ''
  type: CaseStudies
  url: https://www.quvy.com/case-studies/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/app-onboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AppOnboard
- group: commercial
  title: ''
  type: Plans
  url: plans/app-onboard-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/app-onboard-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Quvy's entire published site is five sitemap URLs (home, pricing, contact, login, blog) with no developer page of any kind, and the product's only machine surface is the web app's own AWS AppSync GraphQL backend, which is undocumented and answers anonymous introspection with HTTP 401 UnauthorizedException.
  evidence:
  - status: 200
    url: https://www.quvy.com/sitemap.xml
  - status: 401
    url: https://evlns23x7jdknaffuzd6ittk7a.appsync-api.us-east-1.amazonaws.com/graphql
  - status: 404
    url: https://www.quvy.com/api/openapi.json
  - status: 404
    url: https://www.quvy.com/.well-known/agent-card.json
  - status: 404
    url: https://www.quvy.com/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AppOnBoard, Inc. is a Los Angeles-based technology company founded in 2016 that builds AI-driven creative and advertising tools for app and game marketers. Its best-known product is Buildbox, a no-code platform for making games and apps without programming, and its current flagship is Quvy, an AI ad-creation and testing platform that generates static, video, and concept ad variations and predicts their performance against synthetic audiences before any real ad spend. Quvy targets marketers, indie and studio game developers, SaaS companies, and brands that want to replace slow, expensive A/B testing and agencies with fast simulation-based creative optimization. AppOnBoard is backed by 500 Global; its original apponboard.com domain now redirects to the Quvy product at quvy.com. This profile carries the company identity and website properties; AppOnBoard publishes no public API, developer portal, SDKs, or OpenAPI at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/app-onboard.png
layout: provider
modified: '2026-08-12'
name: App Onboard
nav: Providers
network: true
overview: 'App Onboard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Artificial Intelligence, and Marketing.


  App Onboard''s developer surface includes pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: App Onboard Plans Pricing
  plan_count: 7
  slug: app-onboard-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: App Onboard Rate Limits
  slug: app-onboard-rate-limits
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/app-onboard/refs/heads/main/screenshots/app-onboard-2026-07-25T200734.png
security:
- kind: domain-security
  name: App Onboard Domain Security
  slug: app-onboard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: app-onboard
tags:
- Company
- Advertising
- AdTech
- Artificial Intelligence
- Marketing
- Creative
- Game Development
- No-Code
- Synthetic Data
website: https://www.quvy.com
---
