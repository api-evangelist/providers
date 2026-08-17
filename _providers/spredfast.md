---
access_model:
  confidence: high
  label: Contact sales; API credentials issued by support
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans/spredfast-plans-pricing.yml
  - authentication/spredfast-authentication.yml
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-17'
api_count: 9
apis:
- description: 'The current Spredfast / Khoros Marketing publishing and content surface — 39 operations covering initiatives, account sets, message publishing and scheduling, the Content Center (assets and folders), '
  name: Spredfast Conversations API (v2)
  slug: spredfast-conversations-api-v2
- description: The original Spredfast Conversations API, still live alongside v2 on api.spredfast.com — 27 operations for publishing, assets, folders, initiatives, plans and privileges. Paths take the form /{environ
  name: Spredfast Conversations API (v1)
  slug: spredfast-conversations-api-v1
- description: Asynchronous analytics exports — 12 operations. Eight export endpoints (published posts, daily account metrics, daily post summary, ads net values, stream items, stream item actions, customer feedback
  name: Spredfast Analytics Reporting API
  slug: spredfast-analytics-reporting-api
- description: The event surface — six operations managing event subscriptions. A subscription binds one eventName; setting notificationUri makes delivery a push (with an optional subscriber-supplied bearerToken), o
  name: Spredfast Notifications (Events) API
  slug: spredfast-notifications-events-api
- description: Curated social stream data powering Khoros Marketing Experiences visualisations — 48 operations for stream items, leaderboards, stream meta, topic and hashtag counts, and volume comparison. Served fro
  name: Spredfast Experiences Stream API
  slug: spredfast-experiences-stream-api
- description: Two operations to register and update a customer-implemented Custom CRM so Khoros Marketing can call it — POST /admin/custom and PATCH /admin/custom/{crmId}. The paired contract the customer must impl
  name: Spredfast CRM Registration API
  slug: spredfast-crm-registration-api
- description: 'An INVERTED contract — 13 operations the CUSTOMER implements on their own domain and Khoros Marketing calls. Cases, customers, best-match lookup, a customer''s cases, list and asset resources, and GET '
  name: Spredfast Custom CRM Callback Contract
  slug: spredfast-custom-crm-callback-contract
- description: One operation returning a page of content labels nested within their label sets. Labels are applied to messages and to inbox stream items, and their application raises the stream-item-label-applied ev
  name: Spredfast Label Sets API
  slug: spredfast-label-sets-api
- description: Token introspection — a single GET returning the identity and company behind the presented access token. The whoami call for the Spredfast OAuth surface.
  name: Spredfast Introspection API
  slug: spredfast-introspection-api
artifact_total: 26
asyncapis:
- description: ''
  name: Spredfast Events Webhooks
  slug: spredfast-events-webhooks
collections:
- collection_type: open
  name: beta-analytics-api
  slug: open-spredfast-analytics-api
- collection_type: open
  name: Conversations API V1
  slug: open-spredfast-conversations-api-v1
- collection_type: open
  name: conversations
  slug: open-spredfast-conversations-api
- collection_type: open
  name: crm
  slug: open-spredfast-crm-api
- collection_type: open
  name: api-specifications
  slug: open-spredfast-custom-crm-callback-api
- collection_type: open
  name: stream-api
  slug: open-spredfast-experiences-stream-api
- collection_type: open
  name: introspection-api
  slug: open-spredfast-introspection-api
- collection_type: open
  name: labelsets-api
  slug: open-spredfast-labelsets-api
- collection_type: open
  name: notification-service
  slug: open-spredfast-notification-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.khoros.com/khorosmarketingdevdocs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.khoros.com/khorosmarketingdevdocs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.khoros.com/khorosmarketingdevdocs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.khoros.com/khorosmarketingdevdocs/docs/getting-started-with-the-conversations-api
- group: operate
  title: ''
  type: Support
  url: https://community.khoros.com/t5/Developer-Discussion/bd-p/studio
- group: company
  title: ''
  type: Blog
  url: https://community.khoros.com/t5/Developer-Blog/bg-p/developer-blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://khoros.ai/legal/customer-agreements/
- group: auth
  title: ''
  type: Authentication
  url: authentication/spredfast-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spredfast-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spredfast-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spredfast-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spredfast-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spredfast-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.khoros.com
- group: design
  title: ''
  type: Conformance
  url: conformance/spredfast-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/spredfast-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/spredfast-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spredfast-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/spredfast-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spredfast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spredfast-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spredfast-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spredfast-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spredfast-llms.txt
created: '2026-07-17'
description: 'Spredfast was an Austin-based social media marketing and management platform providing social publishing, engagement, listening, and analytics for enterprise brands and agencies. Backed by Battery Ventures, it acquired Mass Relevance in 2013, merged with Lithium Technologies in 2018, and the combined company rebranded as Khoros in 2019; the Spredfast product line is delivered today as Khoros Marketing and documented at developer.khoros.com. The API surface still carries the Spredfast name in production — the host is api.spredfast.com, OAuth 2.0 runs on login.spredfast.com, request headers use the x-sf- vendor prefix, and the Conversations v1 contract is still licensed as "Spredfast API Terms of Use". Nine OpenAPI documents covering 149 operations are published through the Khoros developer center: Conversations v2 and v1, an asynchronous Analytics Reporting API, a Notifications (Events) API with eleven documented event types, CRM registration, Label Sets, token introspection,
  the Experiences Stream API inherited from Mass Relevance, and an inverted Custom CRM contract the customer implements. The original devcenter.spredfast.com developer portal is dead and spredfast.com returns 503.'
image: https://raw.githubusercontent.com/api-evangelist/spredfast/refs/heads/main/apis.yml
layout: provider
modified: '2026-08-13'
name: Spredfast
nav: Providers
network: true
overview: 'Spredfast publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Conversations API (v2), Conversations API (v1), Analytics Reporting API, and 6 more. Tagged areas include Company, Social Media, Social Media Management, Marketing, and Social Marketing.


  The Spredfast catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spredfast''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 18 more developer resources.'
plans:
- name: Spredfast Plans Pricing
  plan_count: 0
  slug: spredfast-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 0
  name: Spredfast Rate Limits
  slug: spredfast-rate-limits
scopes:
- name: Spredfast Scopes
  scope_count: 1
  slug: spredfast-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 49.3
  delta: 35.5
  facets:
    commercial_clarity: 26.3
    contract_quality: 61.7
    developer_ergonomics: 58.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 13.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Spredfast Authentication
  slug: spredfast-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Spredfast Domain Security
  slug: spredfast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spredfast Vulnerability Disclosure
  slug: spredfast-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Spredfast Trust Center
  slug: spredfast-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701, ISO 22301, PCI DSS, TrustArc Privacy Seal
slug: spredfast
tags:
- Company
- Social Media
- Social Media Management
- Marketing
- Social Marketing
- Publishing
- Analytics
- Engagement
- Content Management
- Webhooks
- Events
- Enterprise
website: https://developer.khoros.com/khorosmarketingdevdocs
---
