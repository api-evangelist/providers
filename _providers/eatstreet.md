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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The live EatStreet API, served under https://eatstreet.com/api/v2 and protected by OAuth 2.0 authorization code with PKCE. EatStreet publishes no reference, no OpenAPI and no developer portal for it; '
  name: EatStreet API v2
  slug: eatstreet-api-v2
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eatstreet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eatstreet.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/eatstreet_stock/
- group: operate
  title: ''
  type: Support
  url: https://help.eatstreet.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.eatstreet.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eatstreet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eatstreet.com/app/Legal.jsp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eatstreet
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eatstreet-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eatstreet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eatstreet-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eatstreet-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eatstreet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eatstreet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eatstreet-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/eatstreet-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eatstreet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eatstreet-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eatstreet-llms.txt
created: '2026-08-12'
description: 'EatStreet is a Madison, Wisconsin online food ordering and delivery marketplace, founded in 2010, that connects diners with local restaurants for takeout and delivery across US college towns and midsize metros, and sells restaurants an ordering, menu and point-of-sale integration platform on the merchant side. It once ran a documented public API — restaurant search, menus, order placement and tracking, and user management — at api.eatstreet.com/publicapi/v1, documented at developers.eatstreet.com. That surface is retired: the documentation host and every documented v1 path now return 404, though the company GitHub organization still points developers at the dead portal. What remains live is an OAuth 2.0 protected v2 API on the consumer host, whose only public, machine-readable contract is the RFC 8414 authorization server metadata EatStreet serves at /.well-known/oauth-authorization-server, advertising merchant_integration and customer scopes with PKCE.'
image: https://eatstreet.com/apple-touch-icon.png
layout: provider
modified: '2026-08-12'
name: EatStreet
nav: Providers
network: true
overview: 'EatStreet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Delivery, Restaurant, Online Ordering, and Marketplace.


  EatStreet''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Eatstreet Plans Pricing
  plan_count: 0
  slug: eatstreet-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Eatstreet Rate Limits
  slug: eatstreet-rate-limits
scopes:
- name: Eatstreet Scopes
  scope_count: 0
  slug: eatstreet-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 16.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eatstreet/refs/heads/main/screenshots/eatstreet-2026-09-02T145324.png
security:
- kind: authentication
  name: Eatstreet Authentication
  slug: eatstreet-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eatstreet Domain Security
  slug: eatstreet-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: eatstreet
tags:
- Company
- Food Delivery
- Restaurant
- Online Ordering
- Marketplace
- Local Commerce
- Consumer
- Point-of-Sale
- Authentication
website: https://eatstreet.com/
---
