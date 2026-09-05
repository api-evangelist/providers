---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/remarkable-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/remarkable-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remarkable-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.beremarkable.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.beremarkable.ai/blog
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.beremarkable.ai/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/remarkable-ai-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/remarkable-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/remarkable-ai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/remarkable-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/remarkable-ai-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://help.beremarkable.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatdesk.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.beremarkable.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beremarkable.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beremarkable.ai/legal/privacy-policy
coverage:
  checked: '2026-08-13'
  detail: 'Remarkable AI (Chatdesk, Inc.) sells an AI-plus-human customer-engagement service, not a developer product: its 34 "one-click integrations" all consume OTHER vendors'' APIs inbound, and across seven hosts on two domains the only API surfaces that exist are internal app plumbing — api.chatdesk.com answers HTTP 403 "Missing Authentication Token" on every path including the root, and the Spring Boot springdoc endpoint at trends.chatdesk.com/v3/api-docs HTTP 302s to /logout — while the marketing site, the 59-entry help-center llms.txt and the integrations page contain zero occurrences of "API", "webhook", "API key" or "developer".'
  evidence:
  - status: 403
    url: https://api.chatdesk.com/
  - status: 302
    url: https://trends.chatdesk.com/v3/api-docs
  - status: 404
    url: https://www.beremarkable.ai/openapi.json
  - status: 404
    url: https://www.chatdesk.com/openapi.json
  - status: 404
    url: https://www.beremarkable.ai/.well-known/agent-card.json
  - status: 200
    url: https://help.beremarkable.ai/llms.txt
  - status: 200
    url: https://www.chatdesk.com/integrations
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Remarkable AI is an AI-powered customer engagement platform for consumer and ecommerce brands, delivering 1:1 personalized messaging across email, SMS, and social channels. Its products span Retain (personalized win-back campaigns for lapsed customers), Support (24/7 AI-plus-human customer service that converts tickets into sales), and Acquire (AI-driven social engagement on TikTok, YouTube, X, and Reddit). The platform is used by 1,000+ ecommerce brands including SAXX, Hyper Skin, Nomadica, Kindra, StoryWorth, and Hot Topic, with plans starting at $1,500/month. Remarkable AI is the trading name of Chatdesk, Inc., which rebranded in 2024; its own terms of service state "We (Chatdesk, Inc. DBA Remarkable AI)", and the legacy chatdesk.com brand still carries the live pricing page, the responsible-disclosure program, and the Teams/Trends/Shift product surfaces. Remarkable AI was surfaced as a portfolio company of Partech and added to the API Evangelist network. It integrates INBOUND
  with roughly 34 third-party platforms (Shopify, Gorgias, Zendesk, Klaviyo, Kustomer, Freshdesk, Salesforce, TikTok and others) by consuming their APIs, but publishes no outbound API of its own: no OpenAPI, GraphQL SDL, MCP server, agent card, SDK, CLI, webhook catalog or developer portal was found across seven hosts on two domains.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/remarkable-ai.png
layout: provider
modified: '2026-08-13'
name: Remarkable AI
nav: Providers
network: true
overview: 'Remarkable AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Customer Engagement, Personalization, and E-Commerce.


  Remarkable AI''s developer surface includes engineering blog, support, pricing, and 13 more developer resources.'
plans:
- name: Remarkable Ai Plans Pricing
  plan_count: 6
  slug: remarkable-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Remarkable Ai Rate Limits
  slug: remarkable-ai-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remarkable-ai/refs/heads/main/screenshots/remarkable-ai-2026-09-02T153329.png
security:
- kind: domain-security
  name: Remarkable Ai Domain Security
  slug: remarkable-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Remarkable Ai Vulnerability Disclosure
  slug: remarkable-ai-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: remarkable-ai
tags:
- Company
- Applicative Saas
- Customer Engagement
- Personalization
- E-Commerce
- Artificial Intelligence
- Customer-Support
- Marketing
website: https://www.beremarkable.ai/
---
