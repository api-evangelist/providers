---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The only anonymously reachable, machine-readable EasyWebinar API surface. The application host publishes a complete OpenID Connect discovery document and RFC 8414 authorization-server metadata, with l
  name: EasyWebinar OAuth 2.0 / OpenID Connect
  slug: easywebinar-oauth-20-openid-connect
artifact_total: 7
asyncapis:
- description: ''
  name: Easywebinar Webhooks
  slug: easywebinar-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/easywebinar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easywebinar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.easywebinar.com/en/
- group: operate
  title: ''
  type: Support
  url: https://support.easywebinar.com/en/
- group: company
  title: ''
  type: Blog
  url: https://easywebinar.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://easywebinar.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://easywebinar.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.easywebinar.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easywebinar.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easywebinar.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://easywebinar.com/enterprise/
- group: commercial
  title: ''
  type: Plans
  url: plans/easywebinar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/easywebinar-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/easywebinar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/easywebinar-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/easywebinar-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/easywebinar-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/easywebinar-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/easywebinar-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/easywebinar-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/easywebinar-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/easywebinar-llms.txt
created: '2026-08-12'
description: EasyWebinar is a live and automated webinar platform for course creators, marketers, coaches and enterprise teams, combining live webinars, automated/simulive and evergreen webinars, an AI webinar funnel builder, EasyCast multistreaming to YouTube, LinkedIn, Facebook and custom RTMP destinations, built-in checkout for paid webinars, and Easy Suite — a native CRM with lead scoring, email sequences and automated follow-up. The platform scales to 100,000 live attendees on Dolby OptiView (Millicast) WebRTC infrastructure and is SOC 2 Type II certified (audited by Scrut Automation) with GDPR controls, SAML 2.0 SSO and SCIM provisioning on the Enterprise tier. EasyWebinar publicly serves an OAuth 2.0 / OpenID Connect authorization server at app.easywebinar.com and markets a REST API and webhooks covering registration, attendance, lead data, CRM sync and event lifecycle events — but that API is a Scale-plan and Enterprise entitlement, and no public reference, OpenAPI or webhook catalogue
  is published.
image: https://easywebinar.com/images/og-image.png
layout: provider
modified: '2026-08-12'
name: EasyWebinar
nav: Providers
network: true
overview: 'EasyWebinar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Webinars, Video, Live Streaming, and Marketing.


  The EasyWebinar catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EasyWebinar''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Easywebinar Plans Pricing
  plan_count: 5
  slug: easywebinar-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Easywebinar Rate Limits
  slug: easywebinar-rate-limits
scopes:
- name: Easywebinar Scopes
  scope_count: 4
  slug: easywebinar-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials/implicit
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 43.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/easywebinar/refs/heads/main/screenshots/easywebinar-2026-08-17T080912.png
security:
- kind: authentication
  name: Easywebinar Authentication
  slug: easywebinar-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Easywebinar Domain Security
  slug: easywebinar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easywebinar
tags:
- Company
- Webinars
- Video
- Live Streaming
- Marketing
- Event
- CRM
- Lead Generation
- Automation
- Identity
- Authentication
- Software-as-a-Service
website: https://easywebinar.com/
---
