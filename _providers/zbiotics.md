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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The anonymous Model Context Protocol endpoint ZBiotics serves on its own domain, implementing the Universal Commerce Protocol dev.ucp.shopping service at version 2026-08-25. tools/list answers without
  name: ZBiotics Universal Commerce MCP API
  slug: zbiotics-universal-commerce-mcp-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://zbiotics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zbiotics.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://zbiotics.com/pages/faqs
- group: company
  title: ''
  type: Blog
  url: https://zbiotics.com/blogs/journal
- group: company
  title: ''
  type: BlogRSS
  url: https://zbiotics.com/blogs/journal.atom
- group: commercial
  title: ''
  type: Pricing
  url: https://zbiotics.com/products/zbiotics
- group: start
  title: ''
  type: SignUp
  url: https://zbiotics.com/a/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zbiotics.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zbiotics.com/pages/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zbiotics-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zbiotics-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zbiotics-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zbiotics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zbiotics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zbiotics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zbiotics-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zbiotics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zbiotics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zbiotics-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zbiotics-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zbiotics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zbiotics-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zbiotics-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: 'ZBiotics is a San Francisco biotechnology company that makes the world''s first genetically engineered probiotics, sold direct to consumers - Pre-Alcohol, a drink containing the patented B. subtilis ZB183 strain engineered to break down acetaldehyde after drinking, and Sugar-to-Fiber, which converts dietary sugar into fiber in the gut. It publishes no developer program, no OpenAPI and no SDKs, but its storefront is a fully instrumented agentic-commerce surface: an anonymous Model Context Protocol server at zbiotics.com/api/ucp/mcp implementing the Universal Commerce Protocol dev.ucp.shopping service with 13 catalog, cart, checkout and order tools; a /.well-known/ucp.json merchant manifest; OIDC and RFC 9728 discovery documents for customer accounts; and a first-party /llms.txt and /agents.md that tell agents how to transact.'
image: https://zbiotics.com/cdn/shop/files/zbiotics-logo.svg?v=1714027569
layout: provider
mcp_servers:
- description: ''
  name: ZBiotics Universal Commerce (UCP) MCP Server
  slug: zbiotics-universal-commerce-ucp-mcp-server
modified: '2026-09-05'
name: ZBiotics
nav: Providers
network: true
overview: 'ZBiotics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Probiotics, Consumer Health, Direct to Consumer, and E-Commerce.


  ZBiotics'' developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: Zbiotics Plans Pricing
  plan_count: 0
  slug: zbiotics-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Zbiotics Rate Limits
  slug: zbiotics-rate-limits
scopes:
- name: Zbiotics Scopes
  scope_count: 0
  slug: zbiotics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
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
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Zbiotics Authentication
  slug: zbiotics-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Zbiotics Domain Security
  slug: zbiotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zbiotics
tags:
- Biotechnology
- Probiotics
- Consumer Health
- Direct to Consumer
- E-Commerce
- Agentic Commerce
- Model Context Protocol
- Universal Commerce Protocol
- Shopify
- Company
website: https://zbiotics.com/
---
