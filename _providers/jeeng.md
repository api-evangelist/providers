---
access_model:
  confidence: high
  label: Sales-gated partner API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.jeeng.com/docs/publisher-overview
  - https://developers.jeeng.com/docs/advertiser-overview
  trial: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Advertiser-side campaign management and reporting for the Jeeng / OpenWeb Email Monetization platform. Update campaign lines (daily spend goal and CPC/CPM/CPA pricing), transition campaign line and cr
  name: Jeeng Email Monetization — Advertisers API
  slug: jeeng-email-monetization-advertisers-api
- description: Publisher-side inventory reporting for the Jeeng / OpenWeb Email Monetization platform. Retrieve container and placement reports at a daily grain using OData V4 $filter queries, and a flexible publish
  name: Jeeng Email Monetization — Publishers API
  slug: jeeng-email-monetization-publishers-api
- description: OAuth 2.0 client-credentials token endpoint for the Jeeng / OpenWeb Email Monetization partner APIs, published by Jeeng as its own OpenAPI definition. Tokens are issued by the Microsoft Entra ID (Azur
  name: Jeeng Email Monetization — Authentication
  slug: jeeng-email-monetization-authentication
artifact_total: 12
collections:
- collection_type: open
  name: Jeeng Email Monetization — Advertisers API
  slug: open-jeeng-advertisers
- collection_type: open
  name: Jeeng Email Monetization — Authentication (OAuth 2.0 token)
  slug: open-jeeng-authentication
- collection_type: open
  name: Jeeng Email Monetization — Publishers API
  slug: open-jeeng-publishers
common:
- group: company
  title: ''
  type: Website
  url: https://jeeng.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.jeeng.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.jeeng.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.jeeng.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.jeeng.com/docs/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jeeng.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jeeng.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.jeeng.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.jeeng.com/news/
- group: start
  title: ''
  type: Login
  url: https://manage.jeeng.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jeeng-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jeeng-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/jeeng-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jeeng-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jeeng-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jeeng-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jeeng-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jeeng-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jeeng-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/jeeng-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jeeng-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jeeng-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jeeng-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/jeeng-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Jeeng (formerly PowerInbox, acquired by OpenWeb in 2022 and now marketed as OpenWeb Email Monetization) is a multichannel monetization and audience-engagement platform for digital publishers. It helps publishers grow first-party, opt-in audiences and generate advertising revenue across email newsletters, websites, push notifications, and newsreader apps, reaching more than 150M opt-in subscribers. Its products — AdFill, AdServe, AdMarket, and Renderer — fill vacant ad inventory with monetized content, extend direct ad campaigns into email through existing ad servers, connect advertisers to opt-in audiences, and streamline Google Ad Manager ad-ops workflows. Publisher integration is handled through merge tags, per-newsletter ad tags, and cs_email tracking parameters plus direct Google Ad Manager integration; campaigns and reporting are managed through the portal at manage.jeeng.com. Jeeng also publishes partner Reporting & Management APIs at developers.jeeng.com — an advertiser
  API for campaign line and creative management plus campaign/performance reporting, and a publisher API for container, placement and publisher performance reporting — served from powerinbox.azure-api.net behind Microsoft Entra ID OAuth 2.0 client-credentials tokens. API access is not self-serve: an account manager provisions the client id and client secret.'
image: https://www.jeeng.com/wp-content/uploads/2022/04/Jeeng_w_OW.png
layout: provider
mcp_servers:
- description: ''
  name: jeeng-mcp.yml
  slug: jeeng-mcpyml
modified: '2026-08-12'
name: Jeeng
nav: Providers
network: true
overview: 'Jeeng publishes 3 APIs on the [APIs.io](https://apis.io/) network: Email Monetization — Advertisers API, Email Monetization — Publishers API, and Email Monetization — Authentication. Tagged areas include Company, Advertising, Publishing, Email, and Push Notifications.


  Jeeng''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 19 more developer resources.'
plans:
- name: Jeeng Plans Pricing
  plan_count: 0
  slug: jeeng-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 0
  name: Jeeng Rate Limits
  slug: jeeng-rate-limits
scopes:
- name: Jeeng Scopes
  scope_count: 1
  slug: jeeng-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 54.5
    developer_ergonomics: 67.4
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 44.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jeeng/refs/heads/main/screenshots/jeeng-2026-07-25T223120.png
security:
- kind: authentication
  name: Jeeng Authentication
  slug: jeeng-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Jeeng Domain Security
  slug: jeeng-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jeeng
tags:
- Company
- Advertising
- Publishing
- Email
- Push Notifications
- Monetization
- AdTech
- Newsletters
- Audience Engagement
- Reporting
- Analytics
- OData
- OAuth
website: https://jeeng.com
---
