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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The agent-callable commerce surface of the Evolved By Nature direct-to-consumer skincare store. A UCP 2026-04-08 MCP endpoint exposes 13 catalog, cart, checkout and order tools; a second Shopify store
  name: Evolved By Nature Skincare Store — Agentic Commerce API
  slug: evolved-by-nature-skincare-commerce
- description: The agent-callable commerce surface of the Evolved By Nature bioactives store, which sells Activated Silk ingredient grades to formulators. Same deployment as the skincare storefront — a UCP 2026-04-0
  name: Evolved By Nature Bioactives Store — Agentic Commerce API
  slug: evolved-by-nature-bioactives-commerce
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evolved-by-nature-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biotech.evolvedbynature.com
- group: company
  title: ''
  type: Blog
  url: https://biotech.evolvedbynature.com/news-media
- group: operate
  title: ''
  type: Support
  url: https://biotech.evolvedbynature.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biotech.evolvedbynature.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biotech.evolvedbynature.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Evolved-By-Nature
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/evolved-by-nature_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evolved-by-nature-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evolved-by-nature-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/evolved-by-nature-graphql.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evolved-by-nature-skincare-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evolved-by-nature-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/evolved-by-nature-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evolved-by-nature-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evolved-by-nature-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/evolved-by-nature-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evolved-by-nature-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evolved-by-nature-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/evolved-by-nature-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evolved-by-nature-rate-limits.yml
created: '2026-08-12'
description: 'Evolved By Nature is a Needham, Massachusetts biotechnology company — formerly Silk Therapeutics — that develops Activated Silk, a platform of liquid silk-derived molecules used as renewable bioactive ingredients and performance chemistries across personal care, skincare, leather finishing and textiles. The company sells physical product rather than software: there is no developer program, no OpenAPI and no API key issuance. Its only live machine-readable API surface is the agentic-commerce layer on its two Shopify storefronts, where UCP (Universal Commerce Protocol) and Shopify storefront MCP endpoints, a storefront GraphQL API, llms.txt and agents.md are served anonymously from evolvedbynature.com hosts.'
image: https://biotech.evolvedbynature.com/wp-content/themes/ebn/assets/images/cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: 'Evolved By Nature operates no developer program and publishes no OpenAPI. Its only live, machine-readable, callable API surface is the agentic-commerce layer on its two Shopify storefronts: a UCP (Uni'
  name: Evolved By Nature — MCP servers
  slug: evolved-by-nature-mcp-servers
modified: '2026-08-12'
name: Evolved By Nature
nav: Providers
network: true
overview: 'Evolved By Nature publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Materials Science, Sustainability, and Personal Care.


  Evolved By Nature''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Evolved By Nature Plans Pricing
  plan_count: 0
  slug: evolved-by-nature-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Evolved By Nature Rate Limits
  slug: evolved-by-nature-rate-limits
scopes:
- name: Evolved By Nature Scopes
  scope_count: 0
  slug: evolved-by-nature-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evolved-by-nature/refs/heads/main/screenshots/evolved-by-nature-2026-09-02T145440.png
security:
- kind: authentication
  name: Evolved By Nature Authentication
  slug: evolved-by-nature-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Evolved By Nature Domain Security
  slug: evolved-by-nature-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: evolved-by-nature
tags:
- Company
- Biotechnology
- Materials Science
- Sustainability
- Personal Care
- Cosmetics
- Specialty Chemicals
- Textiles
- E-Commerce
- Agentic Commerce
- MCP
- Universal Commerce Protocol
website: https://biotech.evolvedbynature.com
---
