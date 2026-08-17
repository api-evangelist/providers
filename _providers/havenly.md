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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-17'
api_count: 11
apis:
- description: The Addresses API from Havenly — 1 operation(s) for addresses.
  name: Havenly Addresses API
  slug: havenly-addresses-api
- description: The Attribute Types API from Havenly — 1 operation(s) for attribute types.
  name: Havenly Attribute Types API
  slug: havenly-attribute-types-api
- description: The Authentication API from Havenly — 1 operation(s) for authentication.
  name: Havenly Authentication API
  slug: havenly-authentication-api
- description: The Board Feedback API from Havenly — 2 operation(s) for board feedback.
  name: Havenly Board Feedback API
  slug: havenly-board-feedback-api
- description: The Board Feedback Questions API from Havenly — 2 operation(s) for board feedback questions.
  name: Havenly Board Feedback Questions API
  slug: havenly-board-feedback-questions-api
- description: The Board Products API from Havenly — 3 operation(s) for board products.
  name: Havenly Board Products API
  slug: havenly-board-products-api
- description: The Searched Vendor Variants API from Havenly — 1 operation(s) for searched vendor variants.
  name: Havenly Searched Vendor Variants API
  slug: havenly-searched-vendor-variants-api
- description: The User Opinions API from Havenly — 2 operation(s) for user opinions.
  name: Havenly User Opinions API
  slug: havenly-user-opinions-api
- description: The User Profile API from Havenly — 2 operation(s) for user profile.
  name: Havenly User Profile API
  slug: havenly-user-profile-api
- description: The Users API from Havenly — 1 operation(s) for users.
  name: Havenly Users API
  slug: havenly-users-api
- description: The Vendor Variants API from Havenly — 1 operation(s) for vendor variants.
  name: Havenly Vendor Variants API
  slug: havenly-vendor-variants-api
artifact_total: 28
collections:
- collection_type: postman
  name: Havenly API
  slug: postman-havenly-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Havenly Addresses API
  slug: open-havenly-addresses-api
- collection_type: open
  name: Havenly Addresses Attribute Types API
  slug: open-havenly-attribute-types-api
- collection_type: open
  name: Havenly Addresses Authentication API
  slug: open-havenly-authentication-api
- collection_type: open
  name: Havenly Addresses Board Feedback API
  slug: open-havenly-board-feedback-api
- collection_type: open
  name: Havenly Addresses Board Feedback Questions API
  slug: open-havenly-board-feedback-questions-api
- collection_type: open
  name: Havenly Addresses Board Products API
  slug: open-havenly-board-products-api
- collection_type: open
  name: Havenly Addresses Searched Vendor Variants API
  slug: open-havenly-searched-vendor-variants-api
- collection_type: open
  name: Havenly Addresses User Opinions API
  slug: open-havenly-user-opinions-api
- collection_type: open
  name: Havenly Addresses User Profile API
  slug: open-havenly-user-profile-api
- collection_type: open
  name: Havenly Addresses Users API
  slug: open-havenly-users-api
- collection_type: open
  name: Havenly Addresses Vendor Variants API
  slug: open-havenly-vendor-variants-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/havenly-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/havenly-openapi-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/havenly-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://havenly.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.havenly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.havenly.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://havenly.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://havenly.com/interior-design-style-quiz/style-inspiration
- group: start
  title: ''
  type: Login
  url: https://havenly.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://havenly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://havenly.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://havenly.com/blog
- group: operate
  title: ''
  type: Support
  url: https://havenly.kustomer.help
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.havenly.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/havenly-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/havenly-domain-security.yml
created: '2026-07-17'
description: Havenly is an online interior-design platform that connects clients with professional designers for virtual and in-person home-decorating services. Clients take a style quiz, match with a designer, collaborate on 3D room renderings, and shop curated furniture and decor from partner brands at exclusive prices. Havenly also offers AI-assisted design. The company exposes a REST API (documented publicly via Postman at api-docs.havenly.com) covering users and profiles, addresses, design boards and board products, a vendor product catalog (vendor variants), attribute types, board feedback, and user opinions/likes. Authentication is OAuth2 (password grant) returning a Bearer token; HAL+JSON responses use page/limit pagination and zf-doctrine-querybuilder query filters. Havenly is backed by 500 Global and Foundry Group.
image: https://havenly.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: havenly-mcp.yml
  slug: havenly-mcpyml
modified: '2026-07-19'
name: Havenly
nav: Providers
network: true
overview: 'Havenly publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Attribute Types API, Authentication API, and 8 more. Tagged areas include Company, Interior Design, Home Decor, Furniture, and E-Commerce.


  Havenly''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, support, and 11 more developer resources.'
random_paper: 14
scopes:
- name: Havenly Scopes
  scope_count: 0
  slug: havenly-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 57.6
    developer_ergonomics: 25.5
    discoverability: 81.5
    governance: 8.3
    operational_transparency: 0.0
  previous_composite: 37.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/havenly/refs/heads/main/screenshots/havenly-2026-07-25T220807.png
security:
- kind: authentication
  name: Havenly Authentication
  slug: havenly-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Havenly Domain Security
  slug: havenly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: havenly
tags:
- Company
- Interior Design
- Home Decor
- Furniture
- E-Commerce
- Marketplace
- Design
- Retail
- AI
website: https://havenly.com
---
