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
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Rael's agent-facing commerce interface. The store implements the Universal Commerce Protocol (UCP) 2026-04-08 and exposes it over MCP at https://www.getrael.com/api/ucp/mcp. An anonymous tools/list re
  name: Rael UCP Commerce MCP
  slug: rael-ucp-mcp
- description: The Shopify Storefront GraphQL API as served on Rael's own domain, anonymous and fully introspectable. A live IntrospectionQuery returned 422 types with QueryRoot (34 query fields) and Mutation (41 mu
  name: Rael Storefront GraphQL API
  slug: rael-storefront-graphql
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.getrael.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rael-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rael-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rael-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rael-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rael-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rael-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rael-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rael-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rael-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rael-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rael-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rael-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rael-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.getrael.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.getrael.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://www.getrael.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.getrael.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getrael.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getrael.com/policies/privacy-policy
- group: docs
  title: ''
  type: GraphQL
  url: graphql/rael-storefront.graphql
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rael-tool-crosswalk.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rael-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/rael-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.getrael.com/agents.md
created: '2026-08-26'
description: 'Rael is a holistic personal-care brand founded in 2017 by three Korean-American women and led by co-founder and CEO Yanghee Paik, selling organic-cotton period care, intimate care, skincare and cycle supplements direct to consumers at getrael.com and through Target, Amazon, Walmart and Thrive Market. Rael runs no developer program, publishes no OpenAPI and ships no SDK — but its storefront serves two live, anonymous, machine-readable contracts on its own domain. The first is an agentic commerce surface Rael documents itself: a hand-written llms.txt and agents.md, a Universal Commerce Protocol merchant profile at /.well-known/ucp declaring UCP 2026-04-08, and an MCP endpoint at /api/ucp/mcp that answers tools/list with thirteen catalog, cart, checkout and order tools carrying full JSON Schema inputs and a required idempotency key on checkout completion. The second is the Shopify Storefront GraphQL API at /api/graphql, fully introspectable without a credential — 422 types, 34
  queries and 41 mutations resolving against Rael''s own catalog.'
image: https://www.getrael.com/cdn/shop/files/Rael_Logo_Forest-Green.png?height=628&pad_color=fff&v=1682534336&width=1200
layout: provider
mcp_servers:
- description: Rael's storefront exposes a live, anonymous MCP server implementing the Universal Commerce Protocol (UCP) shopping service. An unauthenticated POST of {"jsonrpc":"2.0","id":1, "method":"tools/list"} r
  name: Rael UCP Commerce MCP Server
  slug: rael-ucp-commerce-mcp-server
modified: '2026-08-26'
name: Rael
nav: Providers
network: true
overview: 'Rael publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Consumer Goods, and Health and Wellness.


  Rael''s developer surface includes authentication, support, engineering blog, signup flow, documentation, and 21 more developer resources.'
plans:
- name: Rael Plans Pricing
  plan_count: 0
  slug: rael-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rael Rate Limits
  slug: rael-rate-limits
scopes:
- name: Rael Scopes
  scope_count: 0
  slug: rael-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.1
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rael/refs/heads/main/screenshots/rael-2026-09-02T152824.png
security:
- kind: authentication
  name: Rael Authentication
  slug: rael-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rael Domain Security
  slug: rael-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rael
tags:
- Company
- Retail
- E-Commerce
- Consumer Goods
- Health and Wellness
- Personal Care
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
website: https://www.getrael.com/
---
