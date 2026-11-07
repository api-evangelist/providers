---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Teleship API provides cross‑border shipping, trade compliance, tracking, webhooks, and tax collection.
  name: Teleship API
  slug: teleship-api
artifact_total: 4
asyncapis:
- description: ''
  name: Teleship Webhooks
  slug: teleship-webhooks
common:
- group: design
  href: https://artifacts.apis.io/teleship/asyncapi/teleship-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/teleship-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/teleship/authentication/teleship-authentication.yml
  title: ''
  type: Authentication
  url: authentication/teleship-authentication.yml
- group: agent
  href: https://artifacts.apis.io/teleship/llms/teleship-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/teleship-llms.txt
- group: other
  href: https://artifacts.apis.io/teleship/a2a/teleship-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/teleship-a2a.yml
- group: agent
  href: https://artifacts.apis.io/teleship/well-known/teleship-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/teleship-well-known.yml
- group: other
  href: https://artifacts.apis.io/teleship/hosts/teleship-hosts.yml
  title: ''
  type: Hosts
  url: hosts/teleship-hosts.yml
- group: other
  href: https://artifacts.apis.io/teleship/vendors/teleship-vendors.yml
  title: ''
  type: Vendors
  url: vendors/teleship-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://teleship.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.teleship.com/signin
- group: docs
  title: ''
  type: Documentation
  url: https://developers.teleship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.teleship.com`
- group: docs
  title: ''
  type: APIReference
  url: https://developers.teleship.com/api-reference/authentication/authorize-app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Teleship
- group: auth
  href: https://artifacts.apis.io/teleship/security/teleship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/teleship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://teleship.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://teleship.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://teleship.com/blog
coverage:
  checked: '2026-10-28'
  detail: The developer portal provides documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is publicly available.
  evidence:
  - status: 404
    url: https://api.teleship.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Teleship provides a DDP (Delivered Duty Paid) shipping solution for e‑commerce merchants, enabling automatic calculation and collection of duties and taxes at checkout, and shipping duty‑paid to over 200 destinations. The platform integrates with Shopify, WooCommerce and other storefronts, offering a seamless checkout experience without surprise fees for customers.
image: https://teleship.com/teleship-og-1200.jpg
layout: provider
modified: '2026-10-28'
name: Teleship
nav: Providers
network: true
overview: 'Teleship is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, E-Commerce, DDP, Tax, and Integration.


  The Teleship catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Teleship''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 12 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 32.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Teleship Authentication
  slug: teleship-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Teleship Domain Security
  slug: teleship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: teleship
tags:
- Shipping
- E-Commerce
- DDP
- Tax
- Integration
- Company
website: https://teleship.com/
---
