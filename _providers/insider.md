---
access_model:
  confidence: high
  label: Enterprise · Contact sales
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans/insider-plans-pricing.yml
  - https://insiderone.com/request-a-demo/
  - authentication/insider-authentication.yml
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-19'
api_count: 19
apis:
- description: The Unified Customer Database. Upsert user profiles, attributes and behavioural events, read profiles back with a sparse fieldset, manage identifiers, export raw data, and run the GDPR delete/anonymiz
  name: Insider One Unification API
  slug: insider-one-unification-api
- description: Per-channel subscription state and first-party segment upload. v1 unsubscribes from the channel database; v2 adds global-versus-group scope and bulk ingestion, and both versions run side by side.
  name: Insider One Contact API
  slug: insider-one-contact-api
- description: Transactional email sending (9,000 requests/second) with dynamic fields, attachments and customer-supplied unique_args for correlation, plus email campaign creation.
  name: Insider One Mail API
  slug: insider-one-mail-api
- description: Transactional single and bulk SMS sending, plus SMS campaign, overall, transactional and OTP/Verify analytics. Bulk send carries up to 50 messages per request at 5 requests/second.
  name: Insider One SMS API
  slug: insider-one-sms-api
- description: Transactional and conversational WhatsApp sending — template, text, media, location, button-reply and carousel messages. Each send returns an Insider tracking key that is echoed in every webhook event
  name: Insider One WhatsApp API
  slug: insider-one-whatsapp-api
- description: 'The OAuth 2.0 gateway: WhatsApp v2 transactional and conversational send, plus webhook settings registration. gw.useinsider.com is also the OAuth 2.0 authorization server for the whole Insider One pla'
  name: Insider One Gateway API (OAuth 2.0)
  slug: insider-one-gateway-api-oauth-20
- description: Create, launch and delete single web push campaigns from your own backend, plus web push top-metrics, overall-metrics and campaign-metrics statistics.
  name: Insider One Web Push API
  slug: insider-one-web-push-api
- description: Bulk, targeted and advanced app push, Message Center retrieval, app push analytics, custom segment upload and the mobile GDPR data-processing consent endpoint.
  name: Insider One Mobile App API
  slug: insider-one-mobile-app-api
- description: InApp campaign detail retrieval (90-day window, YYYY-MM-DD dates) and FCM certificate upload for the mobile app channel.
  name: Insider One Mobile Settings API
  slug: insider-one-mobile-settings-api
- description: 'iOS Live Activity lifecycle: register, start, update and end an activity, and add or remove users from a running one.'
  name: Insider One Live Activity API
  slug: insider-one-live-activity-api
- description: 'One-time-passcode channels and templates for SMS and WhatsApp: create and update channels, manage OTP templates, generate codes and verify them.'
  name: Insider One Verify (OTP) API
  slug: insider-one-verify-otp-api
- description: Product catalog ingestion and update in flat and nested formats, plus locale configuration. Products are keyed on item_id + locale, with currency-keyed price maps and groupcode variant grouping. All e
  name: Insider One Catalog API
  slug: insider-one-catalog-api
- description: 'Smart Recommender served over HTTP: nineteen named algorithms (similar, complementary, substitute, visually-similar, purchased-together, trending, top-sellers, user-based and more) on one path templat'
  name: Insider One Recommendation API
  slug: insider-one-recommendation-api
- description: 'Eureka product discovery: search results with facets, category and brand merchandising collections, and type-ahead suggestions (served from a per-customer host Insider One issues).'
  name: Insider One Eureka Search API
  slug: insider-one-eureka-search-api
- description: 'Search event collection for Eureka ranking: search, product click, product list view, add to cart and purchase interactions.'
  name: Insider One Eureka Event Collection API
  slug: insider-one-eureka-event-collection-api
- description: Email campaign lists, campaign statistics and overall analytics (v1 and v2 side by side), plus OnSite campaign and overall analytics. Epoch-second time windows; one year of retained history.
  name: Insider One Analytics API
  slug: insider-one-analytics-api
- description: 'Architect journey analytics: overall, per-journey, per-element/channel, conversion goals and journey list export. Takes statDate as a dd/MM/yyyy range string.'
  name: Insider One Architect Analytics API
  slug: insider-one-architect-analytics-api
- description: 'The On API Call starter: enter a user into a transactional Architect journey from your backend and send in real time.'
  name: Insider One Architect Transactional Journey API
  slug: insider-one-architect-transactional-journey-api
- description: First-party remote Model Context Protocol server exposing 35 tools across Email, SMS, WhatsApp, Web Push, Mobile App and Architect — 28 read-only and 7 that create drafts for human review. Authenticat
  name: Insider One MCP Server
  slug: insider-one-mcp-server
artifact_total: 46
asyncapis:
- description: ''
  name: Insider Whatsapp Webhooks
  slug: insider-whatsapp-webhooks
collections:
- collection_type: postman
  name: Insider One APIs
  slug: postman-insider-one-apis
- collection_type: open
  name: Insider One Analytics API
  slug: open-insider-analytics
- collection_type: open
  name: Insider One Architect Analytics API
  slug: open-insider-architect-analytics
- collection_type: open
  name: Insider One Architect Transactional Journey API
  slug: open-insider-architect-transactional
- collection_type: open
  name: Insider One Catalog API
  slug: open-insider-catalog
- collection_type: open
  name: Insider One Contact API
  slug: open-insider-contact
- collection_type: open
  name: Insider One Eureka Event Collection API
  slug: open-insider-eureka-events
- collection_type: open
  name: Insider One Eureka Search API
  slug: open-insider-eureka-search
- collection_type: open
  name: Insider One Gateway API (OAuth 2.0)
  slug: open-insider-gateway
- collection_type: open
  name: Insider One Live Activity API
  slug: open-insider-live-activity
- collection_type: open
  name: Insider One Mail API
  slug: open-insider-mail
- collection_type: open
  name: Insider One Mobile Settings API
  slug: open-insider-mobile-settings
- collection_type: open
  name: Insider One Mobile App API
  slug: open-insider-mobile
- collection_type: open
  name: Insider One Recommendation API
  slug: open-insider-recommendation
- collection_type: open
  name: Insider One SMS API
  slug: open-insider-sms
- collection_type: open
  name: Insider One Unification API
  slug: open-insider-unification
- collection_type: open
  name: Insider One Verify (OTP) API
  slug: open-insider-verify
- collection_type: open
  name: Insider One Web Push API
  slug: open-insider-web-push
- collection_type: open
  name: Insider One WhatsApp API
  slug: open-insider-whatsapp
common:
- group: company
  title: ''
  type: Website
  url: https://insiderone.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.insiderone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://academy.insiderone.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://academy.insiderone.com/docs/api-reference-welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.insiderone.com/docs/insider-one-apis-1
- group: operate
  title: ''
  type: Support
  url: https://useinsiderhelp.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://insiderone.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useinsider
- group: commercial
  title: ''
  type: Pricing
  url: https://insiderone.com/request-a-demo/
- group: start
  title: ''
  type: SignUp
  url: https://inone.useinsider.com/login
- group: start
  title: ''
  type: Login
  url: https://inone.useinsider.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insiderone.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insiderone.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://developers.insiderone.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insider-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/insider-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/insider-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insider-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/insider-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insider-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/insider-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insider-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insider-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/insider-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/insider-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insider-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/insider-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/insider-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insider-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insider-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/insider-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/insider-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/insider-whatsapp-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/insider-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/insider-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Insider (rebranded Insider One; useinsider.com now redirects to insiderone.com) is an AI-native customer engagement and personalization platform used by 2,000+ global brands. It unifies a Customer Data Platform, cross-channel journey orchestration (Architect), personalization, predictive segmentation, product discovery (Eureka) and behavioural analytics across Web, Email, SMS/RCS, WhatsApp, Web Push, Mobile App, Site Search, InStory and conversational CX. Its developer surface is substantial and public: 113 REST operations across 18 hosts, published as a public Postman collection at developers.insiderone.com, covering the Unified Customer Database, consent and subscription management, transactional email/SMS/WhatsApp, web and app push, iOS Live Activities, OTP verification, product catalog, recommendations, Eureka search and campaign and journey analytics. Insider One also ships a first-party remote MCP server at mcp.insiderone.com with 35 OAuth-scoped tools, an llms.txt indexing
  ~2,800 markdown-retrievable doc pages, and an account-generated Agent Skill (SKILL.md) for Claude Code. It publishes per-endpoint rate limits, a cross-API status-and-error-code reference, and SOC 2 / ISO 27001 / ISO 27701 / CSA STAR attestations — but no OpenAPI, no pricing, no status page and no deprecation policy.'
image: https://logo.clearbit.com/useinsider.com
layout: provider
mcp_servers:
- description: ''
  name: insider-mcp.yml
  slug: insider-mcpyml
modified: '2026-08-13'
name: Insider
nav: Providers
network: true
overview: 'Insider publishes 18 APIs on the [APIs.io](https://apis.io/) network, including One Unification API, One Contact API, One Mail API, and 15 more. Tagged areas include Company, Customer Engagement, Personalization, Customer Data Platform, and Marketing.


  The Insider catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Insider''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Insider Plans Pricing
  plan_count: 0
  slug: insider-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 60
  name: Insider Rate Limits
  slug: insider-rate-limits
scopes:
- name: Insider Scopes
  scope_count: 0
  slug: insider-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.0
  delta: 1.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 55.7
    developer_ergonomics: 70.8
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 64.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 22.2
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insider/refs/heads/main/screenshots/insider-2026-07-25T222527.png
security:
- kind: authentication
  name: Insider Authentication
  slug: insider-authentication
  summary_line: apiKey/oauth2 · 7 schemes
- kind: domain-security
  name: Insider Domain Security
  slug: insider-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Insider Trust Center
  slug: insider-trust-center
  summary_line: SOC 2, ISO 27001:2013, ISO 27701, CSA STAR
slug: insider
tags:
- Company
- Customer Engagement
- Personalization
- Customer Data Platform
- Marketing
- Journey Orchestration
- Omnichannel
- CDP
- Artificial Intelligence
- Messaging
- WhatsApp
- Email
- SMS
- Push Notifications
- Recommendations
- Search
- Product Catalog
- Analytics
- MCP
- Agents
- Consent
- GDPR
website: https://insiderone.com
---
