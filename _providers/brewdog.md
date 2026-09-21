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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.6
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: BrewDog's Universal Commerce Protocol shopping service, exposed over MCP at https://brewdog.com/api/ucp/mcp and advertised by the store's own /.well-known/ucp merchant profile and /agents.md. Supports
  name: BrewDog Agentic Commerce (UCP over MCP)
  slug: brewdog-agentic-commerce-ucp-over-mcp
- description: 'The unauthenticated, read-only product and collection JSON surface of the brewdog.com Shopify storefront, documented by BrewDog for agents in /llms.txt and /agents.md: GET /products.json, GET /product'
  name: BrewDog Storefront Product JSON
  slug: brewdog-storefront-product-json
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/security/brewdog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brewdog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brewdog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://brewdog.com/agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/llms/brewdog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brewdog-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://brewdog.com/account
- group: start
  title: ''
  type: Login
  url: https://brewdog.com/account
- group: operate
  title: ''
  type: Support
  url: https://brewdog.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://brewdog-ijnwidpa3ld.gorgias.help/en-GB
- group: company
  title: ''
  type: Blog
  url: https://brewdog.com/blogs/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brewdog.com/pages/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brewdog.com/pages/cookie-and-privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://jobs.brewdog.com/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/brewdog
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/BrewDogBeer
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/brewdogofficial
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/mcp/brewdog-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brewdog-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/well-known/brewdog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brewdog-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/authentication/brewdog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brewdog-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/scopes/brewdog-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/brewdog-scopes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/well-known/brewdog-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/brewdog-openid-configuration.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/conventions/brewdog-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brewdog-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/conformance/brewdog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brewdog-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/errors/brewdog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brewdog-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/lifecycle/brewdog-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brewdog-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/data-model/brewdog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brewdog-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/examples/brewdog-products-json.json
  title: ''
  type: Examples
  url: examples/brewdog-products-json.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/packages/brewdog-packages.yml
  title: ''
  type: Packages
  url: packages/brewdog-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'BrewDog PLC (company no. SC311560) is a Scottish craft brewer, bar and hotel operator headquartered at Balmacassie Commercial Park, Ellon, Aberdeenshire, known for Punk IPA, Hazy Jane and Lost Lager, its Equity for Punks crowdfunding rounds, and its openly published DIY Dog recipe archive. BrewDog does not run a conventional developer program, but its direct-to-consumer store at brewdog.com is a Shopify storefront that ships a real agent-facing API surface: a published /llms.txt and /agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP-over-MCP endpoint at /api/ucp/mcp, Shopify Customer Account OpenID Connect discovery at /.well-known/openid-configuration, and unauthenticated read-only storefront product JSON endpoints that BrewDog documents for agents itself.'
examples:
- key_count: 1
  name: Brewdog Products Json
  slug: brewdog-products-json
image: https://cdn.shopify.com/s/files/1/0822/7281/3382/files/BrewDogLogo.png?v=1724795739
layout: provider
mcp_servers:
- description: ''
  name: BrewDog MCP Server
  slug: brewdog-mcp-server
modified: '2026-08-02'
name: BrewDog
nav: Providers
network: true
overview: 'BrewDog publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Beer, Brewing, and Retail.


  BrewDog''s developer surface includes documentation, signup flow, support, engineering blog, YouTube channel, authentication, code examples, and 21 more developer resources.'
random_paper: 20
scopes:
- name: Brewdog Scopes
  scope_count: 4
  slug: brewdog-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/brewdog/refs/heads/main/screenshots/brewdog-2026-08-07T162802.png
security:
- kind: authentication
  name: Brewdog Authentication
  slug: brewdog-authentication
  summary_line: openIdConnect/oauth2/none · 3 schemes
- kind: domain-security
  name: Brewdog Domain Security
  slug: brewdog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brewdog
tags:
- Company
- Food and Beverage
- Beer
- Brewing
- Retail
- E-Commerce
- Consumer Packaged Goods
- Hospitality
- Agentic Commerce
- Shopify
website: https://www.brewdog.com/
---
