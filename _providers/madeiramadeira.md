---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-30'
api_count: 7
apis:
- description: The Callbacks API from Madeiramadeira — 2 operation(s) for callbacks.
  name: Madeiramadeira Callbacks API
  slug: madeiramadeira-callbacks-api
- description: The Categorias API from Madeiramadeira — 1 operation(s) for categorias.
  name: Madeiramadeira Categorias API
  slug: madeiramadeira-categorias-api
- description: The Financeiro API from Madeiramadeira — 1 operation(s) for financeiro.
  name: Madeiramadeira Financeiro API
  slug: madeiramadeira-financeiro-api
- description: The Frete API from Madeiramadeira — 1 operation(s) for frete.
  name: Madeiramadeira Frete API
  slug: madeiramadeira-frete-api
- description: The Mensageria API from Madeiramadeira — 12 operation(s) for mensageria.
  name: Madeiramadeira Mensageria API
  slug: madeiramadeira-mensageria-api
- description: The Pedido API from Madeiramadeira — 9 operation(s) for pedido.
  name: Madeiramadeira Pedido API
  slug: madeiramadeira-pedido-api
- description: The Produtos API from Madeiramadeira — 38 operation(s) for produtos.
  name: Madeiramadeira Produtos API
  slug: madeiramadeira-produtos-api
artifact_total: 12
asyncapis:
- description: ''
  name: Madeiramadeira Marketplace Webhooks
  slug: madeiramadeira-marketplace-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/madeiramadeira-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/madeiramadeira-marketplace-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.madeiramadeira.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documenter.getpostman.com/view/3341659/RztmqU19
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/3341659/RztmqU19
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/3341659/RztmqU19
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/3341659/RztmqU19
- group: start
  title: ''
  type: GettingStarted
  url: https://www.madeiramadeira.com.br/marketplace
- group: start
  title: ''
  type: SignUp
  url: https://www.madeiramadeira.com.br/verificar
- group: operate
  title: ''
  type: Support
  url: https://madeiramadeira.zendesk.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://parceiros.madeiramadeira.com.br/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/madeiramadeirabr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.madeiramadeira.com.br/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.madeiramadeira.com.br/termos-e-privacidade
- group: commercial
  title: ''
  type: Plans
  url: plans/madeiramadeira-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madeiramadeira-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/madeiramadeira-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madeiramadeira-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madeiramadeira-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/madeiramadeira-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madeiramadeira-llms.txt
created: '2026-08-25'
description: 'MadeiraMadeira (MadeiraMadeira Comercio Eletronico S/A, Curitiba, Parana) is one of Brazil''s largest online retailers and marketplaces for home goods - furniture, decor, appliances, building materials, bathroom and kitchen fixtures, and planned furniture - selling direct and through a third-party seller marketplace. Its developer surface is the seller-facing Marketplace MadeiraMadeira API: a versioned REST API over HTTPS at marketplace.madeiramadeira.com.br with a matching sandbox host, authenticated with a seller-bound TOKENMM header token issued in the Portal Marketplace. It covers product catalog submission and enrichment lifecycle, the category tree, price, stock and status updates, shipping (frete) tables plus a seller-hosted shipping-quote callback, the full order lifecycle from new through invoiced, shipped and delivered, financial ledger entries, and a JWT-authenticated Mensageria surface for buyer-seller messaging, attachments and tracking updates. Order and product
  events are delivered to seller-registered callback URLs.'
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-25'
name: Madeiramadeira
nav: Providers
network: true
overview: 'Madeiramadeira publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Callbacks API, Categorias API, Financeiro API, and 4 more. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Home Goods.


  The Madeiramadeira catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Madeiramadeira''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Madeiramadeira Plans Pricing
  plan_count: 0
  slug: madeiramadeira-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Madeiramadeira Rate Limits
  slug: madeiramadeira-rate-limits
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 64.7
    developer_ergonomics: 55.4
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 44.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Madeiramadeira Authentication
  slug: madeiramadeira-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Madeiramadeira Domain Security
  slug: madeiramadeira-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: madeiramadeira
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Home Goods
- Furniture
- Brazil
- Seller Integration
- Product Catalog
- Order
- Shipping
- Logistics
website: https://www.madeiramadeira.com.br/
---
