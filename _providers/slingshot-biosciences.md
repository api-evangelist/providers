---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
  name: Slingshot Biosciences MCP Server
  slug: slingshot-biosciences-mcp-server
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
screenshot: https://raw.githubusercontent.com/api-evangelist/slingshot-biosciences/refs/heads/main/screenshots/slingshot-biosciences-2026-09-02T155853.png
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
