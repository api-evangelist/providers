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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bobbie Agentic Access
  operation_count: 6
  slug: bobbie-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: The Shopify Storefront GraphQL API as served from Bobbie's own domain. Introspection is anonymous — the full schema (416 types, 35 query fields, 41 mutations) was retrieved without a Storefront access
  name: Bobbie Storefront GraphQL API
  slug: storefront-graphql
- description: A live Model Context Protocol server on Bobbie's storefront host. An anonymous JSON-RPC tools/list returned five tools with full JSON Schema input contracts — search_catalog, get_product_details, get_
  name: Bobbie Storefront MCP Server
  slug: storefront-mcp
- description: Bobbie implements the Universal Commerce Protocol for agent-driven commerce. The merchant profile at /.well-known/ucp declares UCP 2026-04-08 and 2026-01-23, the dev.ucp.shopping MCP service endpoint,
  name: Bobbie UCP Agentic Commerce
  slug: ucp-commerce
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.hibobbie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hibobbie.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bobbie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bobbie-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bobbie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bobbie-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bobbie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bobbie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bobbie-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bobbie-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bobbie-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.hibobbie.com/pages/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hibobbie.com/pages/help-center
- group: company
  title: ''
  type: Blog
  url: https://milk-drunk.com/
- group: company
  title: ''
  type: Press
  url: https://news.hibobbie.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.hibobbie.com/account/register
- group: start
  title: ''
  type: Login
  url: https://account.hibobbie.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hibobbie.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hibobbie.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.hibobbie.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://www.hibobbie.com/policies/shipping-policy
- group: company
  title: ''
  type: About
  url: https://www.hibobbie.com/pages/our-story
- group: operate
  title: ''
  type: ContactUs
  url: https://www.hibobbie.com/pages/contact
- group: company
  title: ''
  type: Careers
  url: https://www.hibobbie.com/pages/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bobbie_stock/
created: '2026-08-02'
description: 'Bobbie is an American organic infant formula company founded in 2018 by Laura Modi and Sarah Hardy — the only mom-founded, women-led infant formula manufacturer in the United States, selling direct to parents at hibobbie.com and through Bobbie Medical for healthcare professionals. Bobbie has no developer program, but its Shopify-hosted storefront exposes a substantial machine-readable surface from its own domain: an anonymously introspectable Storefront GraphQL API, a live Model Context Protocol server with five catalog and cart tools, a Universal Commerce Protocol merchant profile at /.well-known/ucp with UCP MCP commerce endpoints, OpenID Connect and RFC 8414 discovery for customer accounts, and a provider-authored /agents.md (mirrored at /llms.txt) that tells AI agents which surface to use and requires explicit buyer approval before any agent completes a payment.'
image: https://www.hibobbie.com/cdn/shop/files/Bobbie_Cardi_SocialShare_General_1dca0cca-95e0-467b-8eaa-5dd7f4df4675.jpg
layout: provider
mcp_servers:
- description: Bobbie serves TWO live MCP endpoints from its own storefront host. The Shopify Storefront MCP server at /api/mcp answered an anonymous tools/list with five real tools and full JSON Schema input contra
  name: Bobbie MCP Server
  slug: bobbie-mcp-server
modified: '2026-08-02'
name: Bobbie
nav: Providers
network: true
overview: 'Bobbie publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Infant Formula, E-Commerce, and Direct to Consumer.


  Bobbie''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 2
scopes:
- name: Bobbie Scopes
  scope_count: 4
  slug: bobbie-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bobbie/refs/heads/main/screenshots/bobbie-2026-08-07T162704.png
security:
- kind: authentication
  name: Bobbie Authentication
  slug: bobbie-authentication
  summary_line: none/openIdConnect/oauth2 · 5 schemes
- kind: domain-security
  name: Bobbie Domain Security
  slug: bobbie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bobbie
tags:
- Company
- Consumer Packaged Goods
- Infant Formula
- E-Commerce
- Direct to Consumer
- Retail
- Health
- Nutrition
- Agentic Commerce
- Shopify
- GraphQL
- MCP
website: https://www.hibobbie.com/
---
