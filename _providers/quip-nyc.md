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
  - rate-limits
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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Quip Nyc Agentic Access
  operation_count: 13
  slug: quip-nyc-agentic-access
  summary_line: 13 operations · 8 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: An anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service for the quip online store. Exposes thirteen tools covering catalog search and lookup, p
  name: quip UCP Commerce MCP API
  slug: quip-nyc-ucp-commerce-mcp
- description: The Shopify Storefront GraphQL API as deployed on the quip domain, version 2026-07. Schema introspection is open to anonymous callers and returns 415 types, 34 query root fields and 41 mutations cover
  name: quip Storefront GraphQL API
  slug: quip-nyc-storefront-graphql
- description: The read-only JSON surface the store documents for agents that only need to browse catalog data without transacting — product JSON by handle, collection product listings, product search and the sitema
  name: quip Storefront JSON Endpoints
  slug: quip-nyc-storefront-json
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/security/quip-nyc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quip-nyc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getquip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getquip.com/agents.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/llms/quip-nyc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quip-nyc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/well-known/quip-nyc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quip-nyc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/well-known/quip-nyc-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/quip-nyc-openid-configuration.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/authentication/quip-nyc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quip-nyc-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/scopes/quip-nyc-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/quip-nyc-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/conventions/quip-nyc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quip-nyc-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/conformance/quip-nyc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quip-nyc-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/errors/quip-nyc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quip-nyc-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/lifecycle/quip-nyc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quip-nyc-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/data-model/quip-nyc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quip-nyc-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/agentic-access/quip-nyc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quip-nyc-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/rate-limits/quip-nyc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quip-nyc-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/plans/quip-nyc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quip-nyc-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/packages/quip-nyc-packages.yml
  title: ''
  type: Packages
  url: packages/quip-nyc-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getquip.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.getquip.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.getquip.com/pages/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getquip
- group: start
  title: ''
  type: SignUp
  url: https://www.getquip.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getquip.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getquip.com/policies/privacy-policy
created: '2026-08-26'
description: 'quip NYC Inc. is a Brooklyn, New York oral care company founded in 2015 by Simon Enever and Bill May, selling dentist-designed electric toothbrushes, water flossers, refillable floss, toothpaste, mouthwash and whitening products direct to consumers on a recurring refill subscription. It has raised roughly $272M across its rounds and serves millions of subscribers. quip publishes no developer portal, API reference, OpenAPI specification or SDK of its own. Its entire machine-readable surface is its storefront: a Shopify-hosted commerce platform that serves agent-facing instructions at /agents.md and /llms.txt, a Universal Commerce Protocol merchant profile at /.well-known/ucp, an anonymous Model Context Protocol endpoint exposing thirteen catalog, cart, checkout and order tools, an openly introspectable Storefront GraphQL API, and a documented unauthenticated product JSON surface. The company''s published agent policy requires contemporaneous human approval before any agent completes
  a payment.'
image: https://www.getquip.com/cdn/shop/files/Screenshot_2025-04-16_at_6.12.36_PM.png?v=1744899824
jsonld:
- class_count: 0
  name: Quip Nyc Product Context
  property_count: 0
  slug: quip-nyc-product
layout: provider
mcp_servers:
- description: ''
  name: Quip NYC MCP Server
  slug: quip-nyc-mcp-server
modified: '2026-08-26'
name: Quip NYC
nav: Providers
network: true
overview: 'Quip NYC publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oral Care, Consumer Health, Personal Care, and Retail.


  The Quip NYC catalog on APIs.io includes 1 JSON-LD context.


  Quip NYC''s developer surface includes documentation, authentication, engineering blog, support, signup flow, and 20 more developer resources.'
plans:
- name: Quip Nyc Plans Pricing
  plan_count: 0
  slug: quip-nyc-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Quip Nyc Rate Limits
  slug: quip-nyc-rate-limits
scopes:
- name: Quip Nyc Scopes
  scope_count: 4
  slug: quip-nyc-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 30.4
    discoverability: 81.5
    operational_transparency: 2.6
  previous_composite: 40.4
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
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/quip-nyc/refs/heads/main/screenshots/quip-nyc-2026-09-02T152706.png
security:
- kind: authentication
  name: Quip Nyc Authentication
  slug: quip-nyc-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 7 schemes
- kind: domain-security
  name: Quip Nyc Domain Security
  slug: quip-nyc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quip-nyc
tags:
- Company
- Oral Care
- Consumer Health
- Personal Care
- Retail
- E-Commerce
- Direct to Consumer
- Subscription
- Agentic Commerce
- Shopify
website: https://www.getquip.com/
---
