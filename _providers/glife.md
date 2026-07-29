---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: GraphQL API backing the Glife food-tech commerce and supply-chain platform. Exposes 535 queries, 870 mutations, and 139 subscriptions across ecommerce (customers, products, categories, orders, article
  name: Glife GraphQL API
  slug: graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glife-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://glife.com.sg
- group: company
  title: ''
  type: Blog
  url: https://glife.com.sg/articles
- group: start
  title: ''
  type: SignUp
  url: https://glife.com.sg/register
- group: start
  title: ''
  type: Login
  url: https://glife.com.sg/login
- group: operate
  title: ''
  type: Support
  url: https://glife.com.sg/contact-us
- group: auth
  title: ''
  type: Authentication
  url: authentication/glife-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glife-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/glife-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glife-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glife-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/glifetech
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/glifesg
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/glifegroup/
created: '2026-07-17'
description: Glife Technologies Pte Ltd is a Singapore-based food-tech company on a mission to grow a better food future across Southeast Asia. Glife operates a farm-to-table commerce and supply-chain platform that connects farmers and suppliers with restaurants, retailers, and consumers — spanning sourcing, pricing, ordering, inventory, warehousing, and delivery. Its web and mobile applications are backed by a GraphQL API (api-sg.glifeware.com) exposing commerce, content, and supply-chain operations. Glife is backed by 500 Global.
graphqls:
- description: GraphQL API backing the [Glife](https://glife.com.sg) food-tech commerce and supply-chain platform.
  name: Glife Technologies GraphQL API
  slug: glife-graphql
image: https://glife.com.sg/img/seo/og/Home.webp
layout: provider
mcp_servers:
- description: ''
  name: glife-mcp.yml
  slug: glife-mcpyml
modified: '2026-07-19'
name: Glife
nav: Providers
network: true
overview: 'Glife publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Tech, Grocery, Supply Chain, and E-Commerce.


  Glife''s developer surface includes engineering blog, signup flow, support, authentication, and 10 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 25.0
  delta: 7.9
  facets:
    commercial_clarity: 13.2
    contract_quality: 43.2
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.1
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/glife/refs/heads/main/screenshots/glife-2026-07-25T215902.png
security:
- kind: authentication
  name: Glife Authentication
  slug: glife-authentication
  summary_line: token · 0 schemes
- kind: domain-security
  name: Glife Domain Security
  slug: glife-domain-security
  summary_line: TLSv1.3 · DMARC
slug: glife
tags:
- Company
- Food Tech
- Grocery
- Supply Chain
- E-Commerce
- GraphQL
- Southeast Asia
- AgTech
- Logistics
website: https://glife.com.sg
---
