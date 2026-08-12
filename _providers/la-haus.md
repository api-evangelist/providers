---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-haus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lahaus.com/
- group: company
  title: ''
  type: About
  url: https://www.lahaus.com/quienes-somos
- group: company
  title: ''
  type: Blog
  url: https://www.lahaus.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lahaus.com/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/la-haus
- group: operate
  title: ''
  type: Support
  url: https://www.lahaus.com/centro-de-ayuda
- group: start
  title: ''
  type: Login
  url: https://www.lahaus.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lahaus.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lahaus.com/politicas-tratamiento-datos
- group: other
  title: ''
  type: Cookies
  url: https://www.lahaus.com/static/politica-cookies-co-v1
- group: company
  title: ''
  type: Careers
  url: https://www.lahaus.com/trabaja-con-nosotros
- group: build
  title: ''
  type: Tools
  url: https://www.lahaus.com/herramientas
- group: docs
  title: ''
  type: Guides
  url: https://www.lahaus.com/guias-inmobiliarias
- group: build
  title: ''
  type: Packages
  url: packages/la-haus-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/la-haus-llms.txt
created: '2026-08-04'
description: 'La Haus is a Latin American proptech company, founded in 2017 and headquartered in Medellín and Bogotá, Colombia, that operates the residential real-estate marketplaces lahaus.com (Colombia) and lahaus.mx (Mexico) together with an in-house brokerage. The platform lists de-duplicated, verified new-construction and resale housing from vetted developers, adds mortgage and down-payment simulators, buyer guides and an AI assistant, and takes buyers through negotiation and closing at no cost to the buyer. It has raised more than $135M in equity plus debt facilities from Kaszek, NFX, Acrew Capital, Greenspring Associates, SoftBank and Bezos Expeditions. La Haus publishes NO public developer portal, API documentation, SDK or machine-readable contract: the consumer sites are server-rendered applications whose /api/* paths are disallowed in robots.txt, and api.lahaus.com is a private AWS API Gateway that answers every anonymous request with MissingAuthenticationToken. Partner/portal
  syndication runs through access-controlled marketing feed integrations (Trovit). This profile therefore records the company''s public web surface and security posture rather than an API surface.'
image: https://media.lahaus.com/statics/static/images/open-graph-tags/Colombia.png
layout: provider
modified: '2026-08-04'
name: La Haus
nav: Providers
network: true
overview: 'La Haus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Proptech, Marketplace, and Housing.


  La Haus'' developer surface includes engineering blog, support, tooling, and 13 more developer resources.'
random_paper: 103
score:
  band: emerging
  composite: 15.9
  delta: -0.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: La Haus Domain Security
  slug: la-haus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: la-haus
tags:
- Company
- Real Estate
- Proptech
- Marketplace
- Housing
- Mortgages
- Brokerage
- Latin America
- Colombia
- Mexico
website: https://www.lahaus.com/
---
