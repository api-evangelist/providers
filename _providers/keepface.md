---
access_model:
  confidence: high
  label: Self-service with a free tier
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://keepface.com/pricing
  - https://keepface.com/ai-info
  - https://keepface.com/signup
  - https://help.keepface.com/brand/integrations/manage-with-claude-code/
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.9
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The public server-side affiliate tracking API for Keepface. Brands POST sale and refund events from their own backend (or from Shopify, or from the browser JS pixel) and Keepface attributes them to th
  name: Keepface Affiliate API v2
  slug: affiliate
- description: A hosted, remote Model Context Protocol server that exposes 94 actions across the Keepface brand workspace — discovery, lists, campaigns, outreach, reporting, affiliate, wallet (read-only), CRM, brand
  name: Keepface MCP Server
  slug: mcp
artifact_total: 9
asyncapis:
- description: ''
  name: Keepface Affiliate Webhooks
  slug: keepface-affiliate-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://keepface.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.keepface.com
- group: operate
  title: ''
  type: Support
  url: https://help.keepface.com
- group: commercial
  title: ''
  type: Pricing
  url: https://keepface.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://keepface.com/signup
- group: start
  title: ''
  type: Login
  url: https://keepface.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keepface.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keepface.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keepface-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://help.keepface.com/brand/affiliate-program/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.keepface.com/brand/getting-started/welcome/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.keepface.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keepface-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keepface-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keepface-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/keepface-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keepface-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/keepface-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/keepface-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/keepface-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keepface-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.keepface.com/brand/affiliate-program/api-reference/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/keepface-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/keepface-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/keepface-affiliate-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/keepface-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/keepface-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/keepface-plans-pricing.yml
- group: other
  title: ''
  type: CookiePolicy
  url: https://keepface.com/cookie-policy
- group: commercial
  title: ''
  type: UserAgreement
  url: https://keepface.com/user-agreement
- group: auth
  title: ''
  type: GDPR
  url: https://keepface.com/gdpr
- group: other
  title: ''
  type: Glossary
  url: https://keepface.com/resources/glossary
- group: docs
  title: ''
  type: Guides
  url: https://keepface.com/resources/guides
created: '2026-07-17'
description: KeepFace is an all-in-one influencer marketing platform that helps brands, agencies, and enterprises discover, manage, and measure creator campaigns at scale. The platform spans creator discovery and CRM across 2M+ influencers in 43 countries, campaign management from brief through outreach, contract, and content approval, AI-driven brand-safety scoring and sentiment analysis of posts, real-time performance reporting (engagement rate, estimated media value, deletion-proof post archives), affiliate link tracking with pay-on-attributed-sales commissioning, and customer and employee advocacy programs. KeepFace is a portfolio company of 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keepface.png
layout: provider
mcp_servers:
- description: ''
  name: KeepFace MCP Server
  slug: keepface-mcp-server
modified: '2026-08-13'
name: KeepFace
nav: Providers
network: true
overview: 'KeepFace publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Economy, Marketing, and Social-Media.


  The KeepFace catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KeepFace''s developer surface includes documentation, support, pricing, signup flow, API reference, getting-started guide, authentication, and 26 more developer resources.'
plans:
- name: Keepface Plans Pricing
  plan_count: 0
  slug: keepface-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Keepface Rate Limits
  slug: keepface-rate-limits
scopes:
- name: Keepface Scopes
  scope_count: 11
  slug: keepface-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 63.2
  previous_composite: 37.4
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keepface/refs/heads/main/screenshots/keepface-2026-07-25T223555.png
security:
- kind: authentication
  name: Keepface Authentication
  slug: keepface-authentication
  summary_line: hmac/bearer/origin-allowlist/none · 5 schemes
- kind: domain-security
  name: Keepface Domain Security
  slug: keepface-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: keepface
tags:
- Company
- Influencer Marketing
- Creator Economy
- Marketing
- Social-Media
- Affiliate Marketing
- Advocacy
- Campaign Management
- MCP
- AI Agents
- Attribution
- Webhook
website: https://keepface.com
---
