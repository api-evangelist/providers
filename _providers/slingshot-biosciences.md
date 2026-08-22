---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Shopify Storefront GraphQL API for the Slingshot Bio online store, declared by the company in its own /.well-known/api-catalog. Serves products, collections, cart and checkout operations for the c
  name: Slingshot Bio Storefront GraphQL API
  slug: slingshot-bio-storefront-graphql-api
- description: The Sanity Content Lake GROQ query API for the Slingshot Bio editorial surface — pages, resources, blog posts, press releases, product sheets and webinars — declared by the company in its own /.well-k
  name: Slingshot Bio Content Lake GROQ API
  slug: slingshot-bio-content-lake-groq-api
- description: 'A live Model Context Protocol server for the Slingshot Bio store, answering anonymous tools/list over HTTP JSON-RPC with five tools: search_catalog, get_product_details, get_cart, update_cart and sear'
  name: Slingshot Bio Storefront MCP Server
  slug: slingshot-bio-storefront-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.slingshotbio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.slingshotbio.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.slingshotbio.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.slingshotbio.com/collections/catalog-products
- group: start
  title: ''
  type: SignUp
  url: https://www.slingshotbio.com/request-a-quote-for-cell-mimics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.slingshotbio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.slingshotbio.com/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/slingshot-biosciences-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/slingshot-biosciences-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/slingshot-biosciences-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/slingshot-biosciences-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/slingshot-biosciences-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/slingshot-biosciences-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/slingshot-biosciences-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/slingshot-biosciences-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/slingshot-biosciences-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/slingshot-biosciences-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slingshot-biosciences-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-05'
description: 'Slingshot Biosciences is an Emeryville, California biotechnology company that engineers synthetic cell mimics — hydrogel-based particles that behave like real cells — as reproducible reference materials and controls for flow cytometry, spectral unmixing, immunophenotyping, cell and gene therapy potency assays, and instrument standardization. Its product families include TruCytes biomarker controls, ViaComp cell health controls, FlowCytes and ScatterBridge calibration controls, SpectraComp compensation and unmixing controls, QuantCytes quantitation controls and StimCytes functional controls. The company sells direct through a Shopify-backed storefront and publishes an unusually complete agent-facing surface for a life-sciences vendor: an llms.txt, an RFC 9727 /.well-known/api-catalog naming its Shopify Storefront GraphQL and Sanity Content Lake GROQ endpoints, content negotiation that serves markdown twins of every canonical page to agents that send Accept: text/markdown, and
  a live Shopify Storefront MCP server.'
image: https://www.slingshotbio.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: slingshot-biosciences-mcp.yml
  slug: slingshot-biosciences-mcpyml
modified: '2026-08-05'
name: Slingshot Biosciences
nav: Providers
network: true
overview: 'Slingshot Biosciences publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Flow Cytometry, and Laboratory.


  Slingshot Biosciences'' developer surface includes engineering blog, support, pricing, signup flow, authentication, and 14 more developer resources.'
random_paper: 7
scopes:
- name: Slingshot Biosciences Scopes
  scope_count: 4
  slug: slingshot-biosciences-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 39.3
  delta: 2.3
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 38.9
    developer_ergonomics: 20.8
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 37.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Slingshot Biosciences Authentication
  slug: slingshot-biosciences-authentication
  summary_line: none/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Slingshot Biosciences Domain Security
  slug: slingshot-biosciences-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: slingshot-biosciences
tags:
- Company
- Biotechnology
- Life Sciences
- Flow Cytometry
- Laboratory
- Synthetic Biology
- Diagnostics
- Cell Therapy
- E-Commerce
- GraphQL
- MCP
website: https://www.slingshotbio.com/
---
