---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-17'
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
random_paper: 135
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
  composite: 46.2
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 51.6
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 46.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- Events
- CRM
- Lead Generation
- Automation
- Identity
- OAuth
- SaaS
website: https://easywebinar.com/
---
