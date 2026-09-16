---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-09-15'
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
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/authentication/agriinfodesign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agriinfodesign-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/scopes/agriinfodesign-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agriinfodesign-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/conventions/agriinfodesign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agriinfodesign-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/data-model/agriinfodesign-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agriinfodesign-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/errors/agriinfodesign-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agriinfodesign-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/lifecycle/agriinfodesign-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agriinfodesign-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/conformance/agriinfodesign-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agriinfodesign-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/well-known/agriinfodesign-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agriinfodesign-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/llms/agriinfodesign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agriinfodesign-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/packages/agriinfodesign-packages.yml
  title: ''
  type: Packages
  url: packages/agriinfodesign-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/plans/agriinfodesign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agriinfodesign-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/rate-limits/agriinfodesign-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agriinfodesign-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/security/agriinfodesign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agriinfodesign-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/mcp/agriinfodesign-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agriinfodesign-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agriinfodesign/refs/heads/main/skills/_index.yml
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
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 49.2
    developer_ergonomics: 20.8
    discoverability: 74.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 39.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
