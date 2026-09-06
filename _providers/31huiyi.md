---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://31api.31huiyi.com
  baseurl_source: declared
  description: The 31huiyi (31会议) OpenAPI — an OAuth 2.0 bearer-protected REST surface documented in the public developer center at api-help.31huiyi.com. It exposes attendee registration and lifecycle, check-in, sch
  name: 31 OpenAPI
  slug: 31huiyi-openapi
artifact_total: 8
asyncapis:
- description: ''
  name: 31Huiyi Webhooks
  slug: 31huiyi-webhooks
collections:
- collection_type: postman
  name: OpenAPI
  slug: postman-31huiyi-openapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/31huiyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.31huiyi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-help.31huiyi.com/zh/home
- group: docs
  title: ''
  type: Documentation
  url: https://api-help.31huiyi.com/zh/home
- group: docs
  title: ''
  type: APIReference
  url: https://api-help.31huiyi.com/zh/home
- group: start
  title: ''
  type: GettingStarted
  url: https://api-help.31huiyi.com/zh/oauth
- group: operate
  title: ''
  type: HelpCenter
  url: https://lite-help.31huiyi.com
- group: operate
  title: ''
  type: Support
  url: https://www.31huiyi.com/home/about#concat
- group: company
  title: ''
  type: Blog
  url: https://www.31huiyi.com/article/newslist_hy/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.31huiyi.com/price
- group: start
  title: ''
  type: SignUp
  url: https://lite.31huiyi.com/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.31huiyi.com/special/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.31huiyi.com/special/privacyclause
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.31huiyi.com/article/newslist_hy/update
- group: build
  title: ''
  type: Postman
  url: postman/31huiyi-openapi.postman_collection.json
- group: commercial
  title: ''
  type: Plans
  url: plans/31huiyi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/31huiyi-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/31huiyi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/31huiyi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/31huiyi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/31huiyi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/31huiyi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/31huiyi-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/31huiyi-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/31huiyi-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/31huiyi-openid-configuration.json
- group: start
  title: ''
  type: Sandbox
  url: sandbox/31huiyi-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/31huiyi-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/31huiyi-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/31huiyi-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/31huiyi-llms.txt
created: '2026-09-05'
description: 31huiyi (31会议 / 31Event) is the digital event and exhibition SaaS platform operated by Shanghai Bayantu Information Technology Co., Ltd. (上海八彦图信息科技有限公司), founded 2010 and headquartered in Shanghai, China. It runs a product family covering conference management (31大会易), lightweight event management (31轻会), exhibition management (31展览云), on-site smart check-in and reception (31智慧现场), virtual events and an event AI assistant. It publishes a public developer center at api-help.31huiyi.com documenting an OAuth 2.0 / OpenID Connect protected REST OpenAPI at 31api.31huiyi.com, covering attendee registration, check-in, schedules, speakers, exhibitors, tickets, reception and CMS, plus a set of outbound push (webhook) callbacks a customer implements to receive check-in, attendee and exhibitor data.
image: https://api-help.31huiyi.com/system-image/logo.png
layout: provider
modified: '2026-09-05'
name: 31huiyi
nav: Providers
network: true
overview: '31huiyi publishes 1 API on the [APIs.io](https://apis.io/) network: 31 OpenAPI. Tagged areas include Company, Events, Event Management, Conferences, and Exhibitions.


  The 31huiyi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  31huiyi''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: 31Huiyi Plans Pricing
  plan_count: 5
  slug: 31huiyi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: 31Huiyi Rate Limits
  slug: 31huiyi-rate-limits
scopes:
- name: 31Huiyi Scopes
  scope_count: 0
  slug: 31huiyi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 66.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 31Huiyi Authentication
  slug: 31huiyi-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: 31Huiyi Domain Security
  slug: 31huiyi-domain-security
  summary_line: TLSv1.2
slug: 31huiyi
tags:
- Company
- Events
- Event Management
- Conferences
- Exhibitions
- Registration
- Check-In
- Scheduling
- Ticketing
- SaaS
- China
website: https://www.31huiyi.com/
---
