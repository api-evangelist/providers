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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-09-23'
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
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/security/rewardful-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/plans/rewardful-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rewardful-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/rate-limits/rewardful-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rewardful-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/finops/rewardful-finops.yml
  title: ''
  type: FinOps
  url: finops/rewardful-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/json-ld/rewardful-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/rewardful-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/vocabulary/rewardful-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rewardful-vocabulary.yml
- group: company
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/blogs/blogs.json
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
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/changelog/rewardful-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rewardful-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/lifecycle/rewardful-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rewardful-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/authentication/rewardful-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rewardful-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/conventions/rewardful-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rewardful-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/errors/rewardful-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/rewardful-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/data-model/rewardful-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rewardful-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/asyncapi/rewardful-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rewardful-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/conformance/rewardful-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rewardful-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.rewardful.com/trust-center
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/security/rewardful-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/rewardful-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/packages/rewardful-packages.yml
  title: ''
  type: Packages
  url: packages/rewardful-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/components/rewardful-components.yml
  title: ''
  type: Components
  url: components/rewardful-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/mcp/rewardful-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rewardful-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/mcp/rewardful-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rewardful-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rewardful/refs/heads/main/llms/rewardful-llms.txt
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
- description: Rewardful serves a live, anonymous, remote MCP server from its own developer docs host. It is the GitBook documentation MCP (GitBook is Rewardful's docs platform), so its four tools operate over the D
  name: Rewardful Developer Center MCP Server
  slug: rewardful-developer-center-mcp-server
modified: '2026-08-14'
name: Rewardful
nav: Providers
network: true
overview: 'Rewardful publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliate Tracking, Referral Programs, Software-as-a-Service, Stripe, and Commissions.


  The Rewardful catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Rewardful''s developer surface includes documentation, engineering blog, pricing, getting-started guide, support, signup flow, changelog, and 32 more developer resources.'
plans:
- name: Rewardful Plans Pricing
  plan_count: 3
  slug: rewardful-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Rewardful Rate Limits
  slug: rewardful-rate-limits
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 76.0
    catalog_earned_first_party: 20.0
    catalog_gap: 39.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 33.3
    contract_quality: 55.8
    developer_ergonomics: 64.3
    discoverability: 75.9
    operational_transparency: 65.8
  previous_composite: 66.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- Software-as-a-Service
- Stripe
- Commissions
- Payouts
- Affiliate Marketing
- Partner Programs
- Attribution
- Webhook
- Paddle
- Marketing
website: https://www.rewardful.com/
---
