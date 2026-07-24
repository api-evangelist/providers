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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: The Chronicle API from Curated for You — 1 operation(s) for chronicle.
  name: Curated for You Chronicle API
  slug: curated-for-you-chronicle-api
- description: The Companies API from Curated for You — 1 operation(s) for companies.
  name: Curated for You Companies API
  slug: curated-for-you-companies-api
- description: The Curations API from Curated for You — 1 operation(s) for curations.
  name: Curated for You Curations API
  slug: curated-for-you-curations-api
- description: The Feedback API from Curated for You — 2 operation(s) for feedback.
  name: Curated for You Feedback API
  slug: curated-for-you-feedback-api
- description: The shopify API from Curated for You — 14 operation(s) for shopify.
  name: Curated for You shopify API
  slug: curated-for-you-shopify-api
- description: The Users API from Curated for You — 1 operation(s) for users.
  name: Curated for You Users API
  slug: curated-for-you-users-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://curatedforyou.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.curatedforyou.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.curatedforyou.io/redoc
- group: company
  title: ''
  type: Blog
  url: https://www.curatedforyou.io/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.curatedforyou.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curatedforyou.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curatedforyou.io/privacy-policy-1
- group: auth
  title: ''
  type: Authentication
  url: authentication/curated-for-you-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curated-for-you-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curated-for-you-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curated-for-you-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curated-for-you-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curated-for-you-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curated-for-you-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curated-for-you-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curated-for-you-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curated-for-you-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Curated for You is an Austin, Texas lifestyle-commerce platform (Techstars-backed) that matches retail products to shoppers' lifestyles — places, affinities, and trends — using a taxonomy of 1,000+ lifestyle concepts and AI to power product discovery across storefronts, Shopify, web, social, email, and organic search. The company works with retailers such as REVOLVE, Steve Madden, and Saks Off 5th, and has partnered with Microsoft to bring AI-powered curations into Copilot. The Curated for You API (v2, OpenAPI 3.1) lets integrators authenticate, discover the companies they can access, retrieve curations and exported curation snapshots, submit product feedback, and manage Shopify store installs, collections, and analysis/resync jobs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curated-for-you.png
layout: provider
mcp_servers:
- description: ''
  name: curated-for-you-mcp.yml
  slug: curated-for-you-mcpyml
modified: '2026-07-18'
name: Curated for You
nav: Providers
network: true
overview: 'Curated for You publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chronicle API, Companies API, Curations API, and 3 more. Tagged areas include Company, E-Commerce, Retail, Product Discovery, and Personalization.


  Curated for You''s developer surface includes documentation, API reference, engineering blog, signup flow, authentication, and 14 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 48.1
    developer_ergonomics: 52.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 39.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Curated For You Authentication
  slug: curated-for-you-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Curated For You Domain Security
  slug: curated-for-you-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: curated-for-you
tags:
- Company
- E-Commerce
- Retail
- Product Discovery
- Personalization
- Artificial Intelligence
- Curation
- Shopify
- Lifestyle Commerce
website: https://curatedforyou.io/
---
