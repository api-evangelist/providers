---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.frete.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.fretebras.com.br/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.fretebras.com.br/feed/
- group: operate
  title: ''
  type: Support
  url: https://fretebras2.zendesk.com/hc/pt-br
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fretebras.com.br/planos-e-precos-para-empresas
- group: start
  title: ''
  type: SignUp
  url: https://www.fretebras.com.br/planos-e-precos-15-dias-gratis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fretebras.com.br/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fretebras.com.br/politica-de-privacidade
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/frete-com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/frete-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/frete-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/frete-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/frete-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Fretebras' developer portal at developer.fretebras.com.br 301-redirects to a customer Zendesk help center that itself refuses anonymous requests, and the API host api.fretebras.com.br no longer resolves, so the OAuth-based Fretebras integration API that TOTVS Protheus ships a connector for is reachable only under a partner or ERP agreement.
  evidence:
  - status: 301
    url: https://developer.fretebras.com.br/
  - status: 403
    url: https://fretebras2.zendesk.com/hc/pt-br
  - status: 404
    url: https://www.frete.com/.well-known/api-catalog
  - status: 404
    url: https://www.frete.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-16'
description: 'Frete.com is the Brazilian road-freight technology group formed in January 2023 when CargoX merged with Fretebras and FretePago, becoming Latin America''s largest freight-matching platform and one of Brazil''s logistics unicorns after a US$200M round led by SoftBank and Tencent. The group operates three consumer-facing brands: Fretebras, the freight marketplace that connects shippers and carriers with autonomous truck drivers; CargoX Brasil, which bundles working-capital credit, cargo insurance, document issuance and truck tracking for trucking companies; and FretePago, a fintech offering a digital account and freight payment rails for drivers and fleets. It also acquired Rotas Brasil for route mapping and toll pricing. The platform applies machine learning to freight matching, fraud and cargo-theft prevention, and pricing intelligence. Frete.com does not currently publish a public developer portal or machine-readable API contract; the Fretebras integration API is reached through
  partner and ERP/TMS channels rather than an open reference.'
image: https://avatars.githubusercontent.com/u/94481101?v=4
layout: provider
modified: '2026-08-16'
name: Frete.com
nav: Providers
network: true
overview: 'Frete.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Freight, Transportation, Trucking, and Marketplace.


  Frete.com''s developer surface includes engineering blog, support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Frete Plans Pricing
  plan_count: 0
  slug: frete-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 15.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Frete Domain Security
  slug: frete-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: frete
tags:
- Logistics
- Freight
- Transportation
- Trucking
- Marketplace
- Supply Chain
- Fintech
- Brazil
- Latin America
- Machine-Learning
website: https://www.frete.com/
---
