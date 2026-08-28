---
access_model:
  confidence: high
  label: Paid self-serve subscription with a 7-day trial; API access requires an account
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://api.usepomo.ai/api/payment/subscription/plans
  - https://usepomo.ai/llms.txt
  trial: true
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The FastAPI backend behind the Pomo application, published as an OpenAPI 3.1.0 contract at https://api.usepomo.ai/openapi.json with interactive Swagger UI and ReDoc renderings. 924 paths / 994 operati
  name: Pomo Platform API
  slug: pomo-platform-api
artifact_total: 6
asyncapis:
- description: ''
  name: Pomo Event Surface
  slug: pomo-event-surface
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pomo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usepomo.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pomo-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pomo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pomo-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://usepomo.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://usepomo.ai/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://usepomo.ai/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://usepomo.ai/
- group: start
  title: ''
  type: SignUp
  url: https://usepomo.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://usepomo.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usepomo.ai/pages/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usepomo.ai/pages/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pomohq/
created: '2026-07-17'
description: Pomo is an AI marketing platform that runs an always-on AI marketing team, turning continuous market, competitor, brand, and trend intelligence into strategy, creative direction, ad-placement planning, and launch-ready campaign workflows for lean growth, brand, and performance teams. It monitors signals daily, surfaces opportunity and whitespace, drafts approval-ready campaigns, briefs, and creatives, and supports AEO/GEO AI-search visibility and Marketing Mix Modeling. Pomo is also offered as a managed service where in-house marketing experts operate the platform on a customer's behalf. The platform runs on a public FastAPI backend at api.usepomo.ai that publishes an OpenAPI 3.1 contract covering 924 paths and 994 operations across campaigns, competitor tracking, market intelligence, earned media, influencer discovery, a unified data model, and connectors to Meta, Google, TikTok, LinkedIn, Shopify, Square, Stripe, QuickBooks, Klaviyo, HubSpot, and Slack, plus a bearer-gated
  programmatic API with self-service API keys and an internal MCP tool broker. The legal entity is MachFlow, Inc. dba Pomo. Founded in 2025 and based in Palo Alto, California, Pomo raised a $4.5M seed round led by Kindred Ventures with Databricks Ventures, SV Angel, and angel investors.
image: https://usepomo.ai/assets/landing-page/cta-demo.png
layout: provider
modified: '2026-08-13'
name: Pomo
nav: Providers
network: true
overview: 'Pomo publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Company, Marketing, Artificial Intelligence, Market Intelligence, and Competitive Intelligence.


  The Pomo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pomo''s developer surface includes engineering blog, support, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Pomo Plans Pricing
  plan_count: 5
  slug: pomo-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Pomo Rate Limits
  slug: pomo-rate-limits
score:
  band: developing
  composite: 49.2
  delta: 8.1
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 57.5
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 28.9
  previous_composite: 41.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/pomo/refs/heads/main/screenshots/pomo-2026-08-17T081321.png
security:
- kind: authentication
  name: Pomo Authentication
  slug: pomo-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Pomo Domain Security
  slug: pomo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pomo
tags:
- Company
- Marketing
- Artificial Intelligence
- Market Intelligence
- Competitive Intelligence
- Marketing Automation
- Generative AI
- Software-as-a-Service
- Answer Engine Optimization
- Advertising
- Social-Media
- Influencer Marketing
- Campaign Management
website: https://usepomo.ai/
---
