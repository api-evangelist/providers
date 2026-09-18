---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-09-17'
api_count: 4
apis:
- description: Universal Commerce Protocol (UCP) shopping service, exposed over MCP at https://offgridstores.com/api/ucp/mcp. The server identifies itself as "universal-commerce" 0.1.0 speaking MCP protocol 2025-06-
  name: Off Grid Stores UCP Commerce MCP Server
  slug: offgridstores-ucp-commerce-mcp
- description: Shopify Storefront MCP server at https://offgridstores.com/api/mcp, identifying itself as "storefront-renderer" 0.1.0 on MCP protocol 2025-06-18. Five tools that answer anonymously end to end — search
  name: Off Grid Stores Storefront MCP Server
  slug: offgridstores-storefront-mcp
- description: 'Shopify Storefront GraphQL API served on the company''s own host at https://offgridstores.com/api/2025-10/graphql.json. Full introspection answers anonymously: 422 types, 34 query root fields and 41 mu'
  name: Off Grid Stores Storefront GraphQL API
  slug: offgridstores-storefront-graphql
- description: 'Anonymous read-only JSON over the storefront: /products.json and /collections.json for the catalog, /products/{handle}.json and /collections/{handle}/products.json for single resources, and /cart.js f'
  name: Off Grid Stores Storefront JSON Endpoints
  slug: offgridstores-storefront-json
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://offgridstores.com
- group: docs
  title: ''
  type: Documentation
  url: https://offgridstores.com/agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/llms/offgridstores-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/offgridstores-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/llms/offgridstores-agents.md
  title: ''
  type: AgentInstructions
  url: llms/offgridstores-agents.md
- group: company
  title: ''
  type: Blog
  url: https://offgridstores.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://offgridstores.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://offgridstores.com/pages/faqs
- group: start
  title: ''
  type: SignUp
  url: https://offgridstores.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offgridstores.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offgridstores.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://offgridstores.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://offgridstores.com/policies/shipping-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/well-known/offgridstores-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/offgridstores-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/authentication/offgridstores-authentication.yml
  title: ''
  type: Authentication
  url: authentication/offgridstores-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/scopes/offgridstores-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/offgridstores-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/conformance/offgridstores-conformance.yml
  title: ''
  type: Conformance
  url: conformance/offgridstores-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/lifecycle/offgridstores-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/offgridstores-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/conventions/offgridstores-conventions.yml
  title: ''
  type: Conventions
  url: conventions/offgridstores-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/conventions/offgridstores-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/offgridstores-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/errors/offgridstores-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/offgridstores-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/rate-limits/offgridstores-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/offgridstores-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/plans/offgridstores-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/offgridstores-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/data-model/offgridstores-data-model.yml
  title: ''
  type: DataModel
  url: data-model/offgridstores-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/mcp/offgridstores-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/offgridstores-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/mcp/offgridstores-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/offgridstores-mcp.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/graphql/offgridstores-storefront.graphql
  title: ''
  type: GraphQL
  url: graphql/offgridstores-storefront.graphql
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/security/offgridstores-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/offgridstores-domain-security.yml
created: '2026-08-26'
description: 'Off Grid Stores is a US direct-to-consumer retailer of off-grid solar equipment — solar generators and kits, portable and rigid panels, LiFePO4 battery banks, inverters, charge controllers and composting toilets — operating from offgridstores.com. It publishes no traditional developer program, but its Shopify-hosted storefront exposes a substantial, entirely anonymous machine surface on its own domain: an agents.md/llms.txt agent contract (indexed by a dedicated /sitemap_agentic_discovery.xml), a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp declaring UCP 2026-04-08, two live Model Context Protocol servers (a 13-tool UCP commerce server and a 5-tool Storefront MCP server), an anonymously introspectable Storefront GraphQL API of 422 types, and the storefront JSON endpoints for products, collections and cart.'
image: https://offgridstores.com/cdn/shop/files/Off_Grid_Stores_Logo_1204x630.png
layout: provider
mcp_servers:
- description: 'Off Grid Stores serves TWO live, remote Model Context Protocol servers from its own domain, both advertised in its /llms.txt and /agents.md. They are Shopify platform servers bound to this merchant''s '
  name: Off Grid Stores - All Things Off-Grid Solar MCP Server
  slug: off-grid-stores-all-things-off-grid-solar-mcp-server
modified: '2026-08-26'
name: Off Grid Stores - All Things Off-Grid Solar
nav: Providers
network: true
overview: 'Off Grid Stores - All Things Off-Grid Solar publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and off-grid solar.


  Off Grid Stores - All Things Off-Grid Solar''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Offgridstores Plans Pricing
  plan_count: 0
  slug: offgridstores-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Offgridstores Rate Limits
  slug: offgridstores-rate-limits
scopes:
- name: Offgridstores Scopes
  scope_count: 0
  slug: offgridstores-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 81.5
    operational_transparency: 0.0
  previous_composite: 38.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/offgridstores/refs/heads/main/screenshots/offgridstores-2026-09-02T150831.png
security:
- kind: authentication
  name: Offgridstores Authentication
  slug: offgridstores-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Offgridstores Domain Security
  slug: offgridstores-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: offgridstores
tags:
- Company
- Commerce
- E-Commerce
- Retail
- off-grid solar
- Renewable Energy
- Backup Power
- solar generators
- LiFePO4 batteries
- Inverters
- homesteading
- Agentic Commerce
- MCP
- GraphQL
- Universal Commerce Protocol
website: https://offgridstores.com
---
