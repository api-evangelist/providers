---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - https://admagica.ai/pricing
  - https://admagica.ai/register
  - https://api.admagica.ai/api/payments/bundled-plans
  trial: true
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/admagica-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://admagica.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://admagica.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://admagica.ai/blogs
- group: start
  title: ''
  type: SignUp
  url: https://admagica.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://admagica.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://admagica.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdMagica
- group: commercial
  title: ''
  type: Plans
  url: plans/admagica-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/admagica-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/admagica-ai-llms.txt
coverage:
  checked: '2026-08-12'
  detail: AdMagica AI ships an end-user marketing SaaS with no developer program at all — the sitemap lists only marketing, blog, case-study and signup routes, /docs and /redoc return the site's 200-with-404 Next.js shell, and the one live backend host (api.admagica.ai) is disallowed to crawlers in robots.txt, serves no OpenAPI at any conventional path, and answers 401 Authentication required on every non-pricing route.
  evidence:
  - status: 404
    url: https://api.admagica.ai/openapi.json
  - status: 404
    url: https://api.admagica.ai/api/docs
  - status: 200
    url: https://admagica.ai/docs
  - status: 404
    url: https://admagica.ai/llms.txt
  - status: 404
    url: https://admagica.ai/.well-known/agent-card.json
  - status: 401
    url: https://api.admagica.ai/api/credits/trial-status
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: AdMagica.ai is an AI-powered creative advertising platform founded in 2023 and headquartered in London, United Kingdom, that helps e-commerce brands, marketers, and creators generate high-performing ad creatives and manage campaigns at scale. Its "AI marketing agents" automate ad-creative generation, campaign management, and multi-channel publishing to networks such as Meta, Google, LinkedIn, and Instagram, replacing expensive agency and design workflows with template-driven, product-specific ad production. The platform is an end-user marketing SaaS; it currently publishes no public developer API, OpenAPI, or developer documentation. This profile was surfaced as a portfolio company of 500 Global and enriched from the company's public website.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/admagica-ai.png
layout: provider
modified: '2026-08-12'
name: AdMagica AI
nav: Providers
network: true
overview: 'AdMagica AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Marketing, Artificial Intelligence, and Creative.


  AdMagica AI''s developer surface includes pricing, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Admagica Ai Plans Pricing
  plan_count: 37
  slug: admagica-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Admagica Ai Rate Limits
  slug: admagica-ai-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/admagica-ai/refs/heads/main/screenshots/admagica-ai-2026-07-25T181639.png
security:
- kind: domain-security
  name: Admagica Ai Domain Security
  slug: admagica-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: admagica-ai
tags:
- Company
- Advertising
- Marketing
- Artificial Intelligence
- Creative
- AdTech
- Software-as-a-Service
website: https://admagica.ai
---
