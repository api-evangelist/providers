---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: The agent-facing commerce surface for the UrbanStems store, implementing the Universal Commerce Protocol (dev.ucp.shopping) over MCP. Thirteen tools cover catalog search and lookup, product detail, ca
  name: UrbanStems Commerce MCP API
  slug: urbanstems-commerce-mcp-api
- description: The read-only storefront JSON endpoints UrbanStems documents for agents in its own /llms.txt and /agents.md — product JSON at /products/{handle}.json, collection product listings at /collections/{hand
  name: UrbanStems Storefront JSON API
  slug: urbanstems-storefront-json-api
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/security/urbanstems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urbanstems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urbanstems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://urbanstems.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.urbanstems.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://urbanstems.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://urbanstems.com/blogs/news.atom
- group: start
  title: ''
  type: SignUp
  url: https://urbanstems.com/account/register
- group: start
  title: ''
  type: Login
  url: https://urbanstems.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanstems.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanstems.com/policies/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbanstems
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/mcp/urbanstems-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/urbanstems-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/mcp/urbanstems-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/urbanstems-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/llms/urbanstems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/urbanstems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/well-known/urbanstems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/urbanstems-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/authentication/urbanstems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/urbanstems-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/scopes/urbanstems-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/urbanstems-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/conventions/urbanstems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/urbanstems-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/conventions/urbanstems-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/urbanstems-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/errors/urbanstems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/urbanstems-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/rate-limits/urbanstems-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/urbanstems-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/plans/urbanstems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/urbanstems-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/lifecycle/urbanstems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/urbanstems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/conformance/urbanstems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/urbanstems-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/data-model/urbanstems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/urbanstems-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/urbanstems/refs/heads/main/packages/urbanstems-packages.yml
  title: ''
  type: Packages
  url: packages/urbanstems-packages.yml
created: '2026-09-02'
description: 'UrbanStems is a direct-to-consumer flower and gifting company founded on Valentine''s Day 2014 in Washington, DC, selling modern bouquets, plants, gifts and centerpieces with same-day delivery in major US cities and next-day delivery nationwide, sourced through a vertically integrated supply chain that buys direct from Rainforest Alliance Certified farms. Its storefront runs on Shopify at urbanstems.com, and the company exposes a genuine agent-facing commerce surface rather than a developer API program: a published /llms.txt and /agents.md, a /.well-known/ucp merchant profile implementing the Universal Commerce Protocol (UCP 2026-08-25), and a live unauthenticated Model Context Protocol endpoint offering thirteen catalog, cart, checkout and order tools that lets an agent search the catalog and drive a buyer-approved purchase end to end.'
image: https://urbanstems.com/cdn/shop/t/637/assets/organization-image_large.png?v=133620255960512887901788204824
layout: provider
mcp_servers:
- description: ''
  name: UrbanStems Model Context Protocol servers
  slug: urbanstems-model-context-protocol-servers
modified: '2026-09-02'
name: UrbanStems
nav: Providers
network: true
overview: 'UrbanStems publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Flowers.


  UrbanStems'' developer surface includes documentation, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
plans:
- name: Urbanstems Plans Pricing
  plan_count: 0
  slug: urbanstems-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Urbanstems Rate Limits
  slug: urbanstems-rate-limits
scopes:
- name: Urbanstems Scopes
  scope_count: 0
  slug: urbanstems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    operational_transparency: 2.6
  previous_composite: 23.0
  provenance:
    conformance: first-party
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Urbanstems Authentication
  slug: urbanstems-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Urbanstems Domain Security
  slug: urbanstems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: urbanstems
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Flowers
- Gifting
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Direct to Consumer
website: https://urbanstems.com/
---
