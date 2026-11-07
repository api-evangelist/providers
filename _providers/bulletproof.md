---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: The Shopify Storefront GraphQL API served from the Bulletproof store host. Anonymous introspection succeeded on 2026-08-08 (424 types, QueryRoot + Mutation), and anonymous queries against shop, produc
  name: Bulletproof Storefront GraphQL API
  slug: bulletproof-storefront-graphql-api
- description: A live Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) for agent-driven commerce. An anonymous tools/list returned 13 tools with complete JSON Schema input contracts
  name: Bulletproof UCP Agentic Commerce MCP
  slug: bulletproof-ucp-agentic-commerce-mcp
- description: 'The unauthenticated Shopify storefront JSON catalog endpoints (/products.json, /collections.json, /products/{handle}.json, /collections/{handle}/products.json) documented in the store''s own agents.md '
  name: Bulletproof Storefront JSON Catalog
  slug: bulletproof-storefront-json-catalog
- description: 'The public WordPress REST API (wp-json) of the BulletProof website at www.bulletproof.com: the route index of the site''s content management system, catalogued as one site surface rather than as separa'
  name: BulletProof Website (WordPress REST)
  slug: bulletproof-com-website-wordpress-rest
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.bulletproof.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bulletproof_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.bulletproof.com/agents.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bulletproof360
- group: company
  title: ''
  type: Blog
  url: https://www.bulletproof.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bulletproof.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://shop.bulletproof.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://shop.bulletproof.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.bulletproof.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.bulletproof.com/policies/privacy-policy
- group: agent
  href: https://artifacts.apis.io/bulletproof/llms/bulletproof-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bulletproof-llms.txt
- group: agent
  href: https://artifacts.apis.io/bulletproof/well-known/bulletproof-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bulletproof-well-known.yml
- group: auth
  href: https://artifacts.apis.io/bulletproof/authentication/bulletproof-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bulletproof-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bulletproof/scopes/bulletproof-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bulletproof-scopes.yml
- group: design
  href: https://artifacts.apis.io/bulletproof/conventions/bulletproof-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bulletproof-conventions.yml
- group: design
  href: https://artifacts.apis.io/bulletproof/conventions/bulletproof-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bulletproof-conventions.yml
- group: design
  href: https://artifacts.apis.io/bulletproof/errors/bulletproof-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bulletproof-problem-types.yml
- group: build
  href: https://artifacts.apis.io/bulletproof/errors/bulletproof-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/bulletproof-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/bulletproof/lifecycle/bulletproof-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bulletproof-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bulletproof/conformance/bulletproof-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bulletproof-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bulletproof/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/bulletproof/security/bulletproof-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bulletproof-domain-security.yml
created: '2026-08-08'
description: 'Bulletproof (Bulletproof 360, Inc.) is a Seattle-founded functional nutrition and health-and-wellness brand — toxin-tested coffee, C8 MCT oil, collagen, creamers and supplements — founded in 2013 by Dave Asprey and sold direct-to-consumer and through national retail. Bulletproof is not a software vendor and publishes no developer program, yet its commerce and content stacks expose a real, callable, unauthenticated machine surface: a Shopify Storefront GraphQL API that answers introspection anonymously at shop.bulletproof.com, a live UCP (Universal Commerce Protocol) MCP endpoint whose tools/list returns 13 agent tools with full JSON Schema input contracts, OAuth 2.0 / OpenID Connect discovery documents for customer accounts, agent-facing llms.txt and agents.md instructions on the storefront, and a 384-route WordPress REST API behind the editorial site.'
examples:
- key_count: 2
  name: Bulletproof Storefront Graphql Response
  slug: bulletproof-storefront-graphql-response
- key_count: 1
  name: Bulletproof Storefront Products Json
  slug: bulletproof-storefront-products-json
- key_count: 3
  name: Bulletproof Ucp Mcp Initialize
  slug: bulletproof-ucp-mcp-initialize
image: https://cdn.shopify.com/s/files/1/0004/3470/0319/files/bp-logo-large.png?v=1785948157
layout: provider
mcp_servers:
- description: Remote MCP server at shop.bulletproof.com over HTTP; 13 tools listed.
  name: BulletProof MCP Server
  slug: universal-commerce
modified: '2026-08-08'
name: BulletProof
nav: Providers
network: true
overview: 'BulletProof is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Food and Beverage, Health and Wellness, and Supplements.


  BulletProof''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 22
scopes:
- name: Bulletproof Scopes
  scope_count: 4
  slug: bulletproof-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.5
    developer_ergonomics: 30.4
    discoverability: 71.7
    operational_transparency: 2.6
  previous_composite: 27.7
  provenance:
    conformance: derived
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bulletproof/bulletproof-2026-09-02T144956.png
security:
- kind: authentication
  name: Bulletproof Authentication
  slug: bulletproof-authentication
  summary_line: none/oauth2/openIdConnect/bearer · 6 schemes
- kind: domain-security
  name: Bulletproof Domain Security
  slug: bulletproof-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Buy from the Bulletproof store as an agent
  slug: bulletproof-agentic-purchase
- name: Read the Bulletproof catalog without credentials
  slug: bulletproof-catalog-read
slug: bulletproof
tags:
- Company
- Consumer Packaged Goods
- Food and Beverage
- Health and Wellness
- Supplements
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
website: https://www.bulletproof.com/
---
