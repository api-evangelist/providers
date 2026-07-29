---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The agent-facing commerce API for the Leaft Foods storefront. The store implements the Universal Commerce Protocol (ucp.dev) natively through Shopify, exposing a UCP merchant profile at /.well-known/u
  name: Leaft Foods Universal Commerce Protocol (UCP) API
  slug: ucp-commerce
- description: The agent-facing commerce API for leaftblade.com, the direct-to-consumer storefront for the Leaft Blade protein beverage and a second Shopify shop operated by Leaft Foods (shop leaft-lightgrove.myshop
  name: Leaft Blade Universal Commerce Protocol (UCP) API
  slug: leaftblade-ucp-commerce
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leaftfoods-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.leaftfoods.com/
- group: company
  title: ''
  type: Blog
  url: https://www.leaftfoods.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.leaftfoods.com/blogs/news.atom
- group: operate
  title: ''
  type: Support
  url: https://www.leaftfoods.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.leaftfoods.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.leaftfoods.com/policies/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://nz.linkedin.com/company/leaft-foods
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leaftfoods-lifecycle.yml
created: '2026-07-17'
description: Leaft Foods is a New Zealand food-technology company, founded in 2019 by John Penno and Maury Leyland Penno and headquartered in Rolleston in the Selwyn district near Christchurch, that extracts Rubisco — the protein that drives photosynthesis and the most abundant protein on Earth — from green leafy crops such as lucerne. Its proprietary platform turns leaves into a neutral-tasting, highly digestible protein sold as the Leaft Blade consumer beverage, as a Rubisco protein isolate ingredient for food manufacturers, and as an Alfalfa Protein Concentrate for pet nutrition. The company raised a US$15M Series A led by Khosla Ventures. Its digital surface is a Shopify storefront that publishes a real agent-facing commerce API — a Universal Commerce Protocol (UCP) discovery document, an MCP endpoint for catalog, cart and checkout, an llms.txt / agents.md agent instruction set, and OpenID Connect discovery for customer accounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leaftfoods.png
layout: provider
mcp_servers:
- description: ''
  name: leaftfoods-mcp.yml
  slug: leaftfoods-mcpyml
- description: ''
  name: leaftblade-mcp.yml
  slug: leaftblade-mcpyml
modified: '2026-07-19'
name: Leaft Foods
nav: Providers
network: true
overview: 'Leaft Foods publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, AgTech, Alternative Protein, and Ingredients.


  Leaft Foods'' developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 62
scopes:
- name: Leaftfoods Scopes
  scope_count: 0
  slug: leaftfoods-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.2
  delta: 0.9
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Leaftfoods Authentication
  slug: leaftfoods-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Leaftfoods Domain Security
  slug: leaftfoods-domain-security
  summary_line: TLSv1.3 · HSTS
slug: leaftfoods
tags:
- Company
- Food
- AgTech
- Alternative Protein
- Ingredients
- Pet Nutrition
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- New Zealand
website: https://www.leaftfoods.com/
---
