---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The OK Capsule Core API V2 is a REST API that lets a brand programmatically create supplement orders, manage consumers and their addresses, browse the OK Capsule product formulary and its own client p
  name: OK Capsule Core API V2
  slug: ok-capsule-core-api-v2
- description: A production remote MCP server that exposes the OK Capsule platform — catalog, product intelligence, pack builder, recommendation validation, consumers, orders and fulfillments — as OAuth 2.1 scoped t
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://okcapsule.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.okcapsule.app/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.okcapsule.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api2-docs.okcapsule.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.okcapsule.app/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/ok-capsule-918b959a076c/en
- group: company
  title: ''
  type: Blog
  url: https://okcapsule.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/okcapsule
- group: commercial
  title: ''
  type: Pricing
  url: https://okcapsule.com/pricing/plans
- group: start
  title: ''
  type: SignUp
  url: https://portal.okcapsule.app/
- group: start
  title: ''
  type: Login
  url: https://portal.okcapsule.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://okcapsule.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://okcapsule.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: https://storefront.okcapsule.app/mcp
- group: build
  title: ''
  type: Packages
  url: packages/ok-capsule-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ok-capsule-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ok-capsule-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ok-capsule-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ok-capsule-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ok-capsule-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ok-capsule-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ok-capsule-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ok-capsule-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ok-capsule-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ok-capsule-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ok-capsule-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ok-capsule-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ok-capsule-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ok-capsule-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ok-capsule-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ok-capsule-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'OK Capsule is an on-demand, private-label supplement manufacturing and fulfillment platform. Health brands, telehealth providers, clinics and retailers use it to launch personalized daily vitamin packs without minimum order quantities, inventory or upfront deposits. The platform exposes its whole supply chain programmatically: a REST Core API V2 (199 operations across clients, consumers, orders, order lines, fulfillments, assemblies, batches, billings, product lines, pack builders and UPC codes) and a production remote MCP server that publishes the same catalog, pack-building, order and fulfillment surface as OAuth 2.1 scoped tools for Claude, ChatGPT, Gemini and other MCP hosts. Supplements are manufactured in cGMP-certified, FDA-registered facilities and lot-tested by ISO 17025 accredited third-party labs.'
image: https://okcapsule.com/og-preview.png
layout: provider
mcp_servers:
- description: A production remote MCP server that exposes the OK Capsule supplement platform — brands and catalog, product intelligence, the pack builder, recommendation validation, consumers, orders and fulfillmen
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server
- description: Production remote MCP server for catalog, pack building, consumers, orders and fulfillments, behind OAuth 2.1 + PKCE.
  name: OK Capsule MCP Server
  slug: ok-capsule-mcp-server-2
modified: '2026-08-26'
name: OK Capsule
nav: Providers
network: true
overview: 'OK Capsule publishes 1 API on the [APIs.io](https://apis.io/) network: Core API V2. Tagged areas include Supplements, Nutrition, Health, Manufacturing, and Fulfillment.


  OK Capsule''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Ok Capsule Plans Pricing
  plan_count: 3
  slug: ok-capsule-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ok Capsule Rate Limits
  slug: ok-capsule-rate-limits
scopes:
- name: Ok Capsule Scopes
  scope_count: 0
  slug: ok-capsule-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.6
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 53.5
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Ok Capsule Authentication
  slug: ok-capsule-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ok Capsule Domain Security
  slug: ok-capsule-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ok-capsule
tags:
- Supplements
- Nutrition
- Health
- Manufacturing
- Fulfillment
- Ecommerce
- Personalization
- Orders
- Shipping
- Agents
- MCP
- Telehealth
website: https://okcapsule.com/
---
