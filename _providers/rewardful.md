---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://www.rewardful.com/pricing
  - https://www.rewardful.com/llms.txt
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: REST API for programmatically managing campaigns, affiliates, referrals, commissions, payouts, and webhooks within a Rewardful account.
  name: Rewardful REST API
  slug: rewardful-rest-api
artifact_total: 10
asyncapis:
- description: ''
  name: Rewardful Webhooks
  slug: rewardful-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rewardful-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rewardful.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.rewardful.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/rewardful
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rewardful/
- group: company
  title: ''
  type: Blog
  url: https://www.rewardful.com/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rewardful.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rewardful.com/
- group: other
  title: ''
  type: X
  url: https://x.com/getrewardful
- group: commercial
  title: ''
  type: Plans
  url: plans/rewardful-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rewardful-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rewardful-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rewardful-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rewardful-vocabulary.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rewardful.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.rewardful.com/readme
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.rewardful.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.rewardful.com/en/collections/1092743-frequently-asked-questions
- group: start
  title: ''
  type: SignUp
  url: https://app.getrewardful.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.getrewardful.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rewardful.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rewardful.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rewardful-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rewardful-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rewardful-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rewardful-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rewardful-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rewardful-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rewardful-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rewardful-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.rewardful.com/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/rewardful-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/rewardful-packages.yml
- group: design
  title: ''
  type: Components
  url: components/rewardful-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rewardful-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rewardful-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rewardful-llms.txt
created: '2026-06-13'
description: Rewardful is affiliate and referral management software for SaaS, connecting to Stripe or Paddle to track referrals and commissions automatically — adjusting for upgrades, downgrades, cancellations and refunds — and paying affiliates in bulk through PayPal or Wise. Its v1 REST API exposes campaigns, affiliates, affiliate links, affiliate coupons, referrals, commissions and payouts over HTTP Basic auth, alongside 33 signed webhook event types and a browser tracking script with a client-side JavaScript conversion API. A Stripe Premier Partner used by 3,000+ SaaS, tech and AI teams.
finops:
- name: Rewardful Finops
  service_category: ''
  slug: rewardful-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rewardful.png
jsonld:
- class_count: 15
  name: Rewardful Context
  property_count: 59
  slug: rewardful-context
layout: provider
mcp_servers:
- description: ''
  name: rewardful-mcp.yml
  slug: rewardful-mcpyml
modified: '2026-08-14'
name: Rewardful
nav: Providers
network: true
overview: 'Rewardful publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliate Tracking, Referral Programs, SaaS, Stripe, and Commissions.


  The Rewardful catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Rewardful''s developer surface includes documentation, engineering blog, pricing, getting-started guide, support, signup flow, changelog, and 32 more developer resources.'
plans:
- name: Rewardful Plans Pricing
  plan_count: 3
  slug: rewardful-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 1
  name: Rewardful Rate Limits
  slug: rewardful-rate-limits
score:
  band: exemplar
  composite: 68.4
  delta: 31.1
  facets:
    commercial_clarity: 100.0
    contract_quality: 69.4
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 22.9
    operational_transparency: 65.8
  previous_composite: 37.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/screenshots/rewardful-2026-06-20T193058.png
security:
- kind: authentication
  name: Rewardful Authentication
  slug: rewardful-authentication
  summary_line: http-basic · 4 schemes
- kind: domain-security
  name: Rewardful Domain Security
  slug: rewardful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Rewardful Trust Center
  slug: rewardful-trust-center
  summary_line: trust center published
slug: rewardful
tags:
- Affiliate Tracking
- Referral Programs
- SaaS
- Stripe
- Commissions
- Payouts
- Affiliate Marketing
- Partner Programs
- Attribution
- Webhooks
- Paddle
- Marketing
website: https://www.rewardful.com/
---
