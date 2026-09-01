---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The private HTTP API behind the Micro Connect Open Platform (滴灌通开放平台), the enterprise console brands and merchants use to register, submit daily revenue and order detail reports, review data, manage a
  name: Micro Connect Open Platform API
  slug: micro-connect-open-platform
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.microconnect.com/
- group: company
  title: ''
  type: Blog
  url: https://www.microconnect.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.microconnect.com/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://www.microconnect.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://mcex.mo/en/guide/market/fee
- group: agent
  title: ''
  type: WellKnown
  url: well-known/micro-connect-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/micro-connect-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/micro-connect-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/micro-connect-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/micro-connect-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/micro-connect-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/micro-connect-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/micro-connect-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/micro-connect-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/micro-connect-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/micro-connect-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/micro-connect-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/micro-connect-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Micro Connect's only API surface is the Open Platform (滴灌通开放平台) at open.microconnect.com, an enterprise console whose SPA calls an Apache ShenYu gateway at api.mcisaas.com behind a Keycloak login (realm numa-realm, client web-mcc-open-platform); there is no developer portal, no API reference and no spec at any path on any host, and the console's origin open.microconnect.cn has served an expired TLS certificate since 2024-11-27.
  evidence:
  - status: 301
    url: https://open.microconnect.com/
  - status: 200
    url: https://kc.mcisaas.com/auth/realms/numa-realm/.well-known/openid-configuration
  - status: 404
    url: https://www.microconnect.com/openapi.json
  - status: 200
    url: https://api.mcisaas.com/v3/api-docs
  - status: 404
    url: https://mcex.mo/.well-known/agent-card.json
  reason: partner-login
  state: gated
created: '2026-08-25'
description: Micro Connect (滴灌通) is a Hong Kong-founded financial market infrastructure group, established in 2021 by Charles Li (former CEO of Hong Kong Exchanges and Clearing) and Gary Zhang, that turns the daily revenue of micro, small and medium businesses into a standardised, tradable asset class. Its Daily Revenue Obligation (DRO) and revenue-based financing contracts are listed, cleared and settled on the Micro Connect (Macao) Financial Assets Exchange (MCEX) — a financial institution approved by Macao executive order Ordem Executiva n.º 47/2022 and regulated by the Monetary Authority of Macao, and wholly owned by Micro Connect Group. The group runs several operator-facing web platforms on its own SaaS stack — the Micro Connect Open Platform (open.microconnect.com) for brand and merchant data onboarding, the M-Terminal investor terminal (mt.microconnect.com), and the store/merchant consoles — all served from a single API gateway at api.mcisaas.com and authenticated by a Keycloak identity
  provider at kc.mcisaas.com. No public developer program, API reference or machine-readable API contract is published; the integration surface is reachable only after enterprise account registration and login.
image: https://www.microconnect.com/images/logo-dark.png
layout: provider
modified: '2026-08-25'
name: Micro Connect
nav: Providers
network: true
overview: 'Micro Connect publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Capital Markets, Exchanges, and Revenue-Based Financing.


  Micro Connect''s developer surface includes engineering blog, support, pricing, authentication, and 14 more developer resources.'
plans:
- name: Micro Connect Plans Pricing
  plan_count: 0
  slug: micro-connect-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Micro Connect Rate Limits
  slug: micro-connect-rate-limits
scopes:
- name: Micro Connect Scopes
  scope_count: 0
  slug: micro-connect-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 63.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Micro Connect Authentication
  slug: micro-connect-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Micro Connect Domain Security
  slug: micro-connect-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: micro-connect
tags:
- Company
- Financial-Services
- Capital Markets
- Exchanges
- Revenue-Based Financing
- Fintech
- Investing
- Small Business
- Hong Kong
- Macao
- China
website: https://www.microconnect.com/
---
