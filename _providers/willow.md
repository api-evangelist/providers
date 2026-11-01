---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: Willow's storefront agent surface — a JSON-RPC 2.0 Model Context Protocol endpoint implementing the Universal Commerce Protocol 2026-08-25 shopping service. tools/list answers unauthenticated and retu
  name: Willow Pump UCP Commerce MCP
  slug: willow-pump-ucp-commerce-mcp
- description: Shopify Storefront GraphQL API served on Willow's own domain at onewillow.com/api/graphql. Anonymous introspection answered on 2026-10-20 (QueryRoot with 34 query fields, 41 mutations covering product
  name: Willow Storefront GraphQL
  slug: willow-storefront-graphql
- description: Shopify storefront MCP endpoint on Willow's domain at onewillow.com/api/mcp. tools/list answered anonymously on 2026-10-20 with one tool, search_shop_policies_and_faqs, which answers questions about W
  name: Willow Storefront MCP
  slug: willow-storefront-mcp
artifact_total: 12
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://shopify.dev/docs/agents/get-started/quickstart
- group: operate
  href: https://artifacts.apis.io/willow/lifecycle/willow-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/willow-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/willow/hosts/willow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/willow-hosts.yml
- group: other
  href: https://artifacts.apis.io/willow/vendors/willow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/willow-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://onewillow.com/blogs/all.atom
- group: auth
  href: https://artifacts.apis.io/willow/security/willow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/willow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onewillow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://onewillow.com/agents.md
- group: agent
  href: https://artifacts.apis.io/willow/llms/willow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/willow-llms.txt
- group: agent
  href: https://artifacts.apis.io/willow/mcp/willow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/willow-mcp.yml
- group: agent
  href: https://artifacts.apis.io/willow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/willow/well-known/willow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/willow-well-known.yml
- group: auth
  href: https://artifacts.apis.io/willow/authentication/willow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/willow-authentication.yml
- group: auth
  href: https://artifacts.apis.io/willow/scopes/willow-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/willow-scopes.yml
- group: design
  href: https://artifacts.apis.io/willow/conventions/willow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/willow-conventions.yml
- group: design
  href: https://artifacts.apis.io/willow/conventions/willow-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/willow-conventions.yml
- group: design
  href: https://artifacts.apis.io/willow/errors/willow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/willow-problem-types.yml
- group: design
  href: https://artifacts.apis.io/willow/conformance/willow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/willow-conformance.yml
- group: design
  href: https://artifacts.apis.io/willow/lifecycle/willow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/willow-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/willow/data-model/willow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/willow-data-model.yml
- group: operate
  href: https://artifacts.apis.io/willow/rate-limits/willow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/willow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/willow/plans/willow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/willow-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://help.onewillow.com/s
- group: operate
  title: ''
  type: HelpCenter
  url: https://onewillow.com/pages/willow-support
- group: company
  title: ''
  type: Blog
  url: https://onewillow.com/blogs/all
- group: start
  title: ''
  type: SignUp
  url: https://onewillow.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onewillow.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onewillow.com/policies/privacy-policy
created: '2026-09-04'
description: 'Willow Innovations, Inc. is a Mountain View, California consumer health-technology company founded in 2014 that makes wearable, in-bra breast pumps — the Willow 360, Willow Go and the Wave manual pump — sold direct to consumers at onewillow.com and paired with a mobile app that tracks output and controls suction. Willow publishes no developer programme, API keys or OpenAPI, but its storefront is an agent-callable surface: it serves a Universal Commerce Protocol merchant profile at /.well-known/ucp.json and a live, anonymous MCP endpoint at /api/ucp/mcp exposing 13 tools for catalog search, cart, checkout and order retrieval, alongside published agent instructions (agents.md, llms.txt) and OAuth 2.0/OIDC customer-account discovery documents.'
image: https://onewillow.com/cdn/shop/files/OG-Image_db607121-7a26-49c9-b231-3a1e572a0fca_1200x630.jpg?v=1716782735
layout: provider
mcp_servers:
- description: Willow's online store at onewillow.com exposes a live, anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service. An MCP client POSTs JSON-RPC to ht
  name: Willow Pump UCP Commerce MCP Server
  slug: willow-pump-ucp-commerce-mcp-server
- description: ''
  name: Willow MCP Server
  slug: willow-storefront-mcp-tools-list-json
modified: '2026-10-20'
name: Willow
nav: Providers
network: true
overview: 'Willow is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Health, Breast Pumps, Maternal Health, and Medical Devices.


  Willow''s developer surface includes getting-started guide, documentation, authentication, support, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Willow Plans Pricing
  plan_count: 0
  slug: willow-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Willow Rate Limits
  slug: willow-rate-limits
scopes:
- name: Willow Scopes
  scope_count: 4
  slug: willow-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 10.4
    developer_ergonomics: 42.3
    discoverability: 70.0
    operational_transparency: 28.9
  previous_composite: 33.9
  provenance:
    conformance: first-party
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/willow/willow-2026-10-11T194505.png
security:
- kind: authentication
  name: Willow Authentication
  slug: willow-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Willow Domain Security
  slug: willow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: willow-agentic-checkout
  slug: willow-agentic-checkout
- name: willow-catalog-discovery
  slug: willow-catalog-discovery
slug: willow
tags:
- Company
- Consumer Health
- Breast Pumps
- Maternal Health
- Medical Devices
- E-Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Agent-Native
- Shopify
website: https://onewillow.com/
---
