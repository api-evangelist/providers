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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avenue-one-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avenueone.com/
- group: operate
  title: ''
  type: Support
  url: https://avenueone.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avenueone.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avenueone.com/terms
- group: start
  title: ''
  type: Login
  url: https://partners.avenueone.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avenue1/
- group: company
  title: ''
  type: Careers
  url: https://avenueone.com/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/avenue-one_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avenue-one-llms.txt
- group: agent
  title: ''
  type: WellKnownIndex
  url: well-known/avenue-one-well-known.yml
- group: other
  title: ''
  type: IdentityProvider
  url: authentication/avenue-one-authentication.yml
coverage:
  checked: '2026-08-06'
  detail: Avenue One ships AvenueOS only as a login-gated product to institutional clients and vetted partners — partners.avenueone.com 302s straight to an Auth0 universal login, and the AvenueOS backend at api.credit.avenueone.com answers every docs path (/docs, /redoc, /openapi.json, /api/openapi.json) identically to a control path, so no OpenAPI, SDK, webhook or developer portal exists to profile.
  evidence:
  - status: 404
    url: https://api.credit.avenueone.com/api/openapi.json
  - status: 404
    url: https://api.credit.avenueone.com/openapi.json
  - status: 302
    url: https://partners.avenueone.com/
  - status: 403
    url: https://avenueone.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Avenue One is a New York-based technology service platform and investment marketplace for institutional owners, buyers, sellers, lenders and borrowers of residential rental real estate. Founded in 2020, it connects institutional debt and equity capital to local operating partners and property owners across 21+ U.S. markets, combining proprietary property data, automated valuation, and a vetted partner network to find, finance, buy, renovate, lease, manage and sell single-family rental homes at scale. Its service lines span lending (bridge and SFR portfolio loans), strategy development, acquisitions, renovations, asset management, title and brokerage or dispositions. The company reports $2.2B+ of capital deployed. Its software runs as a private, login-gated product suite ("AvenueOS") for internal, builder, investor and partner users; no public developer program, API reference, or machine-readable contract is published.
image: https://avenueone.com/_assets/Avenue_One_Horizontal_Logo_Digital_FullColor_1-b0ddb1c50f.svg
layout: provider
modified: '2026-08-06'
name: Avenue One
nav: Providers
network: true
overview: 'Avenue One is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Single-Family Rental, PropTech, and Institutional Investing.


  Avenue One''s developer surface includes support and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.6
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avenue-one/refs/heads/main/screenshots/avenue-one-2026-08-07T162022.png
security:
- kind: authentication
  name: Avenue One Authentication
  slug: avenue-one-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Avenue One Domain Security
  slug: avenue-one-domain-security
  summary_line: TLSv1.3 · DMARC
slug: avenue-one
tags:
- Company
- Real-Estate
- Single-Family Rental
- PropTech
- Institutional Investing
- Lending
- Asset Management
- Property Data
- Marketplace
website: https://avenueone.com/
---
