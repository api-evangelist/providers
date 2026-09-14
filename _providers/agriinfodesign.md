---
api_count: 4
apis:
- baseURL: https://datastore.agribus-connect.net
  baseurl_source: declared
  description: Field, reference-line, work-record, planting, observation and elevation-map datastore behind AgriBus-NAVI and AgriBus-Web, plus Agri Info Design's implementation of the Japanese 農機オープンAPI (Agricultura
  name: AgriBus Datastore API
  slug: agribus-datastore-api
- baseURL: https://auth.agribus-connect.net
  baseurl_source: declared
  description: Identity service for the AgriBus platform - sign-up, sign-in, password reset, user profile and icon, group membership, Firebase custom tokens, RTK caster settings, impersonation for system admins, and
  name: AgriBus Authentication & OpenID Connect API
  slug: agribus-authentication-openid-connect-api
- baseURL: https://manager.agribus-connect.net
  baseurl_source: declared
  description: The AgriBus-Web Manager API - devices, users, tokens, teams/groups, web markers, search, system administration, RTK caster (base/rover) management and Stripe billing controllers, in v1 and v2 generati
  name: AgriBus-Web Manager API
  slug: agribus-web-manager-api
- baseURL: https://pay.agribus-connect.net
  baseurl_source: declared
  description: Subscription and purchase service for the AgriBus paid plans - Stripe cards, coupons, invoices, upcoming invoices, plans, subscriptions and payment-method changes, Google Play real-time developer noti
  name: AgriBus Billing & Payments API
  slug: agribus-billing-payments-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://agri-info-design.com/
- group: start
  title: ''
  type: Login
  url: https://app.agribus-connect.com/
- group: operate
  title: ''
  type: Support
  url: https://support.agri-info-design.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://agri-info-design.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://agri-info-design.com/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://agri-info-design.com/en/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://agri-info-design.com/paidplans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agri-info-design.com/term/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agri-info-design.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agri-info-design
- group: auth
  title: ''
  type: Authentication
  url: authentication/agriinfodesign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agriinfodesign-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agriinfodesign-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agriinfodesign-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agriinfodesign-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agriinfodesign-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agriinfodesign-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agriinfodesign-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agriinfodesign-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/agriinfodesign-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agriinfodesign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agriinfodesign-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agriinfodesign-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agriinfodesign-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-12'
description: Agri Info Design, Ltd. (株式会社農業情報設計社) is a Japanese agricultural-technology company founded 21 April 2014 in Obihiro, Hokkaido, building precision-farming guidance for tractors and other agricultural machinery. Its AgriBus product line pairs the AgriBus-NAVI Android GPS/GNSS guidance app (100,000+ downloads worldwide) with AgriBus-GMiniR and AgriBus-G2 RTK-GNSS receivers, the AgriBus-AutoSteer automatic steering package, and AgriBus-Web, a browser console for field boundaries, reference lines, work-record history, elevation maps and RTK base-station management. The company also sells ISOBUS / ISO 11783 / AG-PORT consulting. Its cloud platform is a set of Spring Boot microservices on agribus-connect.net, each of which publishes a machine-readable OpenAPI/Swagger contract anonymously, including an implementation of Japan's NARO-led 農機オープンAPI (Agricultural Machinery Open API) device and location surface.
image: https://agri-info-design.com/wp-content/uploads/2019/05/AID-logo_sq-06.png
layout: provider
mcp_servers:
- description: ''
  name: Agri Info Design MCP Server
  slug: agri-info-design-mcp-server
modified: '2026-09-12'
name: Agri Info Design
nav: Providers
network: true
overview: 'Agri Info Design publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AgriBus Datastore API, AgriBus Authentication & OpenID Connect API, AgriBus-Web Manager API, and 1 more. Tagged areas include Agriculture, AgTech, Precision Agriculture, Precision Farming, and GNSS.


  Agri Info Design''s developer surface includes support, engineering blog, pricing, authentication, and 21 more developer resources.'
plans:
- name: Agriinfodesign Plans Pricing
  plan_count: 4
  slug: agriinfodesign-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Agriinfodesign Rate Limits
  slug: agriinfodesign-rate-limits
scopes:
- name: Agriinfodesign Scopes
  scope_count: 14
  slug: agriinfodesign-scopes
  summary_line: 14 scopes
security:
- kind: authentication
  name: Agriinfodesign Authentication
  slug: agriinfodesign-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Agriinfodesign Domain Security
  slug: agriinfodesign-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agriinfodesign
tags:
- Agriculture
- AgTech
- Precision Agriculture
- Precision Farming
- GNSS
- GPS
- RTK
- Farm Management
- Agricultural Machinery
- ISOBUS
- Geospatial
- Japan
- Telematics
- Company
website: https://agri-info-design.com/
---
