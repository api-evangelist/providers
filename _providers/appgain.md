---
access_model:
  confidence: high
  label: Self-serve signup with a 14-day free trial; pricing quoted by sales
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans/appgain-plans-pricing.yml
  - sandbox/appgain-sandbox.yml
  - authentication/appgain-authentication.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: REST API for sending multi-channel campaigns (rich push notifications, email, SMS, web push), creating smart deep links, managing a media library, and logging user events/purchases into the Appgain CD
  name: Appgain OmniChannel Messaging API
  slug: appgain-omnichannel-messaging-api
- baseURL: https://notify.appgain.io
  baseurl_source: declared
  description: The messaging send service. A single POST /{projectId}/send endpoint whose channel is selected by the top-level body key (appPush, email, SMS, webPush, WHATSAPP, UOWHATSAPP), plus SMS target-list subs
  name: Appgain Notify API
  slug: appgain-notify-api
- baseURL: https://automator.appgain.io
  baseurl_source: declared
  description: 'The marketing-automation service. Fires and cancels dashboard-configured automation journeys at a named trigger point, for one user or a batch of users via the v2 form. Authenticated with the project '
  name: Appgain Automator API
  slug: appgain-automator-api
artifact_total: 13
asyncapis:
- description: ''
  name: Appgain Webhooks
  slug: appgain-webhooks
collections:
- collection_type: postman
  name: Appgain.io
  slug: postman-appgain-omnichannel
common:
- group: company
  title: ''
  type: Website
  url: https://appgain.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.appgain.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appgain.io/complete-knowledge-base/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.appgain.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.appgain.io/SDK/gettingStarted/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/4679101/T17KeScV?version=latest
- group: operate
  title: ''
  type: ChangeLog
  url: https://headwayapp.co/appgain-changelog
- group: company
  title: ''
  type: Blog
  url: https://www.appgain.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appgain.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.appgain.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appgain.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appgain.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://p.appgain.io/slack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appgain
- group: build
  href: https://artifacts.apis.io/appgain/packages/appgain-packages.yml
  title: ''
  type: Packages
  url: packages/appgain-packages.yml
- group: build
  href: https://artifacts.apis.io/appgain/packages/appgain-packages.yml
  title: ''
  type: SDKs
  url: packages/appgain-packages.yml
- group: auth
  href: https://artifacts.apis.io/appgain/authentication/appgain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appgain-authentication.yml
- group: design
  href: https://artifacts.apis.io/appgain/conventions/appgain-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appgain-conventions.yml
- group: operate
  href: https://artifacts.apis.io/appgain/changelog/appgain-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appgain-changelog.yml
- group: design
  href: https://artifacts.apis.io/appgain/data-model/appgain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appgain-data-model.yml
- group: auth
  href: https://artifacts.apis.io/appgain/security/appgain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appgain-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/appgain/llms/appgain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appgain-llms.txt
- group: build
  href: https://artifacts.apis.io/appgain/postman/appgain-omnichannel.postman_collection.json
  title: ''
  type: PostmanCollection
  url: postman/appgain-omnichannel.postman_collection.json
- group: design
  href: https://artifacts.apis.io/appgain/errors/appgain-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appgain-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appgain/lifecycle/appgain-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appgain-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/appgain/conformance/appgain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appgain-conformance.yml
- group: start
  href: https://artifacts.apis.io/appgain/sandbox/appgain-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/appgain-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/appgain/plans/appgain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appgain-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appgain/rate-limits/appgain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appgain-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/appgain/asyncapi/appgain-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appgain-webhooks.yml
- group: design
  href: https://artifacts.apis.io/appgain/components/appgain-components.yml
  title: ''
  type: Components
  url: components/appgain-components.yml
- group: agent
  href: https://artifacts.apis.io/appgain/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/appgain/well-known/appgain-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/appgain-well-known.yml
created: '2026-07-17'
description: Appgain is an omnichannel messaging and mobile marketing automation platform, originally out of the MENA region, that lets marketers acquire, engage, and retain mobile and web users across push notifications, in-app messaging, email, SMS, WhatsApp, and web push from a single cloud. Its REST API and mobile SDKs power smart deep links, micro landing pages, behavior-triggered automation journeys, a customer data platform (CDP) with real-time event logging and purchase tracking, and multi-channel campaign delivery, with marketplace apps for Shopify, Zid, and Salla and no-code integrations via Zapier and n8n. The backend is built on the open-source Parse Server stack, and first-party SDKs cover Android, iOS, Flutter, React Native, Cordova/Ionic, and web. Since 2026 the company positions itself as an "AI Workforce Platform" for MENA businesses, adding AI agent products - a RAG-powered customer bot, AI call intelligence with Arabic and English transcription, a visual bot builder, and
  a unified inbox - on top of the messaging core. The only machine-readable contract Appgain publishes is a public Postman collection served from its own apidocs subdomain; there is no OpenAPI.
image: https://appgain.io/og-image-blog.jpg
layout: provider
modified: '2026-08-13'
name: Appgain
nav: Providers
network: true
overview: 'Appgain is listed with 3 APIs on the [APIs.io](https://apis.io/) network: OmniChannel Messaging API, Notify API, and Automator API. Tagged areas include Company, Mobile Marketing, Marketing Automation, Omnichannel Messaging, and Push Notifications.


  The Appgain catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Appgain''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Appgain Plans Pricing
  plan_count: 0
  slug: appgain-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Appgain Rate Limits
  slug: appgain-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.8
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 78.0
    discoverability: 78.6
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - mena
  previous_composite: 36.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 26.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appgain/appgain-2026-07-25T200731.png
security:
- kind: authentication
  name: Appgain Authentication
  slug: appgain-authentication
  summary_line: apiKey · 6 schemes
- kind: domain-security
  name: Appgain Domain Security
  slug: appgain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Fire and cancel an Appgain automation journey
  slug: appgain-fire-automation-journey
- name: Log events and purchases into the Appgain CDP
  slug: appgain-log-cdp-events
- name: Send an Appgain omnichannel campaign
  slug: appgain-send-omnichannel-campaign
- name: Create an Appgain smart deep link and read its attribution
  slug: appgain-smart-deep-link-attribution
slug: appgain
tags:
- Company
- Mobile Marketing
- Marketing Automation
- Omnichannel Messaging
- Push Notifications
- SMS
- Email
- WhatsApp
- Customer Data Platform
- Deep Linking
- Customer Engagement
- AI Agents
- Conversational AI
- MENA
website: https://appgain.io
---
