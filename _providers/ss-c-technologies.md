---
api_count: 1
apis:
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: Cross-platform execution-management API for Eze EMS, published by SS&C Eze as a gRPC contract (three proto3 files, 64 RPCs across MarketDataService, SubmitOrderService and UtilityServices) with an equ
  name: SS&C Eze EMS xAPI
  slug: ssc-eze-ems-xapi
- description: SS&C's corporate API management portal, where clients register applications, request access to SS&C API products and manage consumers against a Kong gateway. The API catalog itself is behind authentic
  name: SS&C APIM Developer Portal
  slug: ssc-apim-developer-portal
- description: REST API and developer portal for the SS&C Advent Black Diamond wealth platform, covering portfolio, account and client data exchange for advisors and integration partners. The portal requires sign-in
  name: SS&C Black Diamond Wealth Platform API
  slug: ssc-black-diamond-wealth-platform-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.ssctech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ssctech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/ezesoft/xapi/blob/master/readme.md
- group: docs
  title: ''
  type: APIReference
  url: https://emsuatxapi.taltrade.com:9001/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ezesoft/xapi/blob/master/readme.md#how-do-i-get-started-with-xapi
- group: operate
  title: ''
  type: Support
  url: https://www.ssctech.com/about/support-client-portals
- group: company
  title: ''
  type: Blog
  url: https://www.ssctech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ezesoft
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/ssnc-eze-ems-xapi/ems-xapi-rest/collection/jeebiq6/ss-c-eze-ems-xapi
- group: start
  title: ''
  type: SignUp
  url: https://developer.ssctech.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ssctech.com/about/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ssctech.com/about/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.ssctech.com/about/disclosures/security-addendum-schedule3
- group: auth
  title: ''
  type: Authentication
  url: authentication/ss-c-technologies-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ss-c-technologies-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ss-c-technologies-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ss-c-technologies-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/ss-c-technologies-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ss-c-technologies-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ss-c-technologies-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ss-c-technologies-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ss-c-technologies-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ss-c-technologies-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ss-c-technologies-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ss-c-technologies-llms.txt
created: '2026-09-13'
description: 'SS&C Technologies Holdings (NASDAQ: SSNC) is a global provider of financial-services and healthcare software and outsourcing, headquartered in Windsor, Connecticut, operating under brands including SS&C Advent, SS&C Eze, SS&C GlobeOp, SS&C GIDS, SS&C Intralinks, SS&C Black Diamond, SS&C Algorithmics and SS&C Blue Prism. Most of the API surface is client-gated: the corporate SS&C APIM developer portal at developer.ssctech.com and the Black Diamond developer portal both require an account, and access is requested through a client relationship manager. The substantial public exception is SS&C Eze EMS xAPI, whose machine-readable contract SS&C Eze publishes openly on GitHub as three proto3 files — 64 gRPC RPCs across MarketDataService, SubmitOrderService and UtilityServices — alongside a matching REST projection described by a live OpenAPI 3.0.4 document with 73 operations covering order submission and amendment, pair and basket orders, allocations and trade reports, real-time
  and historical market data, and intraday balances, positions and activity.'
image: https://www.ssctech.com/hubfs/website/logos/ssc_logo_1200x630.png
layout: provider
modified: '2026-09-13'
name: SS&C Technologies
nav: Providers
network: true
overview: 'SS&C Technologies publishes 1 API on the [APIs.io](https://apis.io/) network: SS&C Eze EMS xAPI. Tagged areas include Financial Services, Investment Management, Fund Administration, Wealth Management, and Execution Management.


  SS&C Technologies'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Ss C Technologies Plans Pricing
  plan_count: 0
  slug: ss-c-technologies-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Ss C Technologies Rate Limits
  slug: ss-c-technologies-rate-limits
scopes:
- name: Ss C Technologies Scopes
  scope_count: 0
  slug: ss-c-technologies-scopes
  summary_line: OAuth 2.0 · no documented scopes
security:
- kind: authentication
  name: Ss C Technologies Authentication
  slug: ss-c-technologies-authentication
  summary_line: http/session-token/srp/openIdConnect · 5 schemes
- kind: domain-security
  name: Ss C Technologies Domain Security
  slug: ss-c-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ss C Technologies Trust Center
  slug: ss-c-technologies-trust-center
  summary_line: SOC 1 Type 2
slug: ss-c-technologies
tags:
- Financial Services
- Investment Management
- Fund Administration
- Wealth Management
- Execution Management
- Order Management
- Market Data
- Trading
- gRPC
- Enterprise Software
website: https://www.ssctech.com/
---
