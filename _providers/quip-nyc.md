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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-31'
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
artifact_total: 14
common:
- group: company
  title: ''
  type: Blog
  url: https://www.getquip.com/blogs/mouthoff-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.getquip.com/blogs/mouthoff-blog.atom
- group: auth
  href: https://artifacts.apis.io/quip-nyc/security/quip-nyc-domain-security.yml
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
  href: https://artifacts.apis.io/quip-nyc/llms/quip-nyc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quip-nyc-llms.txt
- group: agent
  href: https://artifacts.apis.io/quip-nyc/well-known/quip-nyc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quip-nyc-well-known.yml
- group: other
  href: https://artifacts.apis.io/quip-nyc/well-known/quip-nyc-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/quip-nyc-openid-configuration.json
- group: auth
  href: https://artifacts.apis.io/quip-nyc/authentication/quip-nyc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quip-nyc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/quip-nyc/scopes/quip-nyc-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/quip-nyc-scopes.yml
- group: design
  href: https://artifacts.apis.io/quip-nyc/conventions/quip-nyc-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quip-nyc-conventions.yml
- group: design
  href: https://artifacts.apis.io/quip-nyc/conformance/quip-nyc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quip-nyc-conformance.yml
- group: design
  href: https://artifacts.apis.io/quip-nyc/errors/quip-nyc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quip-nyc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/quip-nyc/lifecycle/quip-nyc-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/quip-nyc-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/quip-nyc/data-model/quip-nyc-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quip-nyc-data-model.yml
- group: agent
  href: https://artifacts.apis.io/quip-nyc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/quip-nyc/agentic-access/quip-nyc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quip-nyc-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/quip-nyc/rate-limits/quip-nyc-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quip-nyc-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/quip-nyc/plans/quip-nyc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quip-nyc-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/quip-nyc/packages/quip-nyc-packages.yml
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
- description: Remote MCP server at www.getquip.com over HTTP; 13 tools listed.
  name: Quip NYC MCP Server
  slug: universal-commerce
modified: '2026-10-06'
name: Quip NYC
nav: Providers
network: true
overview: 'Quip NYC is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oral Care, Consumer Health, Personal Care, and Retail.


  The Quip NYC catalog on APIs.io includes 1 JSON-LD context.


  Quip NYC''s developer surface includes engineering blog, documentation, authentication, support, signup flow, and 22 more developer resources.'
plans:
- name: Quip Nyc Plans Pricing
  plan_count: 0
  slug: quip-nyc-plans-pricing
random_paper: 6
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
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 15.7
    developer_ergonomics: 30.4
    discoverability: 61.7
    operational_transparency: 5.3
  previous_composite: 29.0
  provenance:
    agentic_access: first-party
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
screenshot: https://apis.io/screenshots/quip-nyc/quip-nyc-2026-09-02T152706.png
security:
- kind: authentication
  name: Quip Nyc Authentication
  slug: quip-nyc-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 7 schemes
- kind: domain-security
  name: Quip Nyc Domain Security
  slug: quip-nyc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Browse the quip catalog
  slug: quip-nyc-browse-catalog
- name: Build and maintain a quip cart
  slug: quip-nyc-build-cart
- name: Complete a quip checkout with buyer approval
  slug: quip-nyc-checkout-with-buyer-approval
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
