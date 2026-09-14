---
api_count: 1
apis:
- baseURL: https://websiteapi.agorareal.com/wp-json
  baseurl_source: declared
  description: The anonymous, read-mostly content API behind agorareal.com. The marketing site is a headless WordPress install at websiteapi.agorareal.com fronted by a Next.js application, and its WordPress REST API
  name: Agora Website Content API
  slug: agora-website-content-api
- description: 'The tenant-scoped HTTPS API behind Agora''s client platform and investor portal. Its existence and shape are established from Agora''s own production surface: certificate transparency shows per-tenant h'
  name: Agora Client Platform API
  slug: agora-client-platform-api
- description: Agora's OAuth 2.0 / OpenID Connect authorization server, served on its own domain at auth.agorareal.com and reached by redirect from the Cortex sign-in host (cortex.agorareal.com → auth.agorareal.com/
  name: Agora Authorization Server
  slug: agora-authorization-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agora-real-estate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agorareal.com/
- group: company
  title: ''
  type: Blog
  url: https://agorareal.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://agorareal.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agorareal.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agorareal.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://agorareal.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://demo.portal.agorareal.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://agorareal.com/season-of-innovation/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.agorareal.com/
- group: auth
  title: ''
  type: Compliance
  url: security/agora-real-estate-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agora-real-estate-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agora-real-estate-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agora-real-estate-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agora-real-estate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agora-real-estate-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/agora-real-estate-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agora-real-estate-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agora-real-estate-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agora-real-estate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agora-real-estate-scopes.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-12'
description: 'Agora (agorareal.com) is a real estate investment management platform for general partners, syndicators, owners/operators and investment firms, covering fundraising and investor onboarding, an investor portal and investor CRM, digital subscriptions and e-signature, data rooms, cap table and transaction management, distribution waterfall automation, capital calls, ACH and cross-border payments, K-1 and document management, investor reporting, and integrated fund accounting, bookkeeping and tax services. It is sold as a subscription starting at $749/month for the Essential tier, with Pro and Enterprise tiers quoted, and its customer-facing platform is multi-tenant — every client firm gets its own investor portal and client-platform host under agorareal.com. Agora publishes no developer portal and no public reference for that platform API: "API Access" is an Enterprise line item priced separately, and the tenant API answers nothing anonymously. What it does publish anonymously
  is the first-party content API behind its own website, a headless WordPress install whose route index and custom agora/v1 namespace are served in the open, plus a full OAuth 2.0 / OpenID Connect authorization server on its own domain for the new Cortex AI product. Its own release feed schedules an "API + MCP" launch for 22 September 2026.'
image: https://res.cloudinary.com/de1ep59a0/images/v1731398288/logo-primary-blue/logo-primary-blue.png
layout: provider
modified: '2026-09-12'
name: Agora Real Estate
nav: Providers
network: true
overview: 'Agora Real Estate publishes 1 API on the [APIs.io](https://apis.io/) network: Agora Website Content API. Tagged areas include Real Estate, Investment Management, Private Equity, Fund Administration, and Investor Relations.


  Agora Real Estate''s developer surface includes engineering blog, pricing, support, changelog, authentication, and 17 more developer resources.'
plans:
- name: Agora Real Estate Plans Pricing
  plan_count: 3
  slug: agora-real-estate-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Agora Real Estate Rate Limits
  slug: agora-real-estate-rate-limits
scopes:
- name: Agora Real Estate Scopes
  scope_count: 0
  slug: agora-real-estate-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Agora Real Estate Authentication
  slug: agora-real-estate-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agora Real Estate Domain Security
  slug: agora-real-estate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Agora Real Estate Trust Center
  slug: agora-real-estate-trust-center
  summary_line: SOC 2 Type II, SOC 1, ISO 27001:2022, GDPR
slug: agora-real-estate
tags:
- Real Estate
- Investment Management
- Private Equity
- Fund Administration
- Investor Relations
- Capital Raising
- Syndication
- Fund Accounting
- Investor Portal
- CRM
- Payments
- Content Management
- Software-as-a-Service
website: https://agorareal.com/
---
