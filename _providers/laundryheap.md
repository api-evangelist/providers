---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Laundryheap's primary product API. A single GraphQL endpoint serving the consumer web and mobile apps, covering ordering, recurring orders, addresses, timeslots, services, hotels, subscriptions, bundl
  name: Laundryheap GraphQL API
  slug: laundryheap-graphql-api
- description: A live, spec-clean OAuth 2.0 and OpenID Connect provider on Laundryheap's root host, discovered only by probing /.well-known/. It advertises the authorization_code (with PKCE) and client_credentials g
  name: Laundryheap OAuth 2.0 / OpenID Connect Authorization Server
  slug: laundryheap-oauth-20-openid-connect-authorization-server
- description: A small unauthenticated JSON endpoint under /api/v1 that returns the laundry and dry-cleaning services available at a given address, with each service's short code, description, minimum service durati
  name: Laundryheap Service Catalogue API
  slug: laundryheap-service-catalogue-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laundryheap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.laundryheap.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/laundryheap-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laundryheap-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laundryheap-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/laundryheap-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/laundryheap-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/laundryheap-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/laundryheap-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.laundryheap.com/en-gb/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.laundryheap.com/en-us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.laundryheap.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.laundryheap.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.laundryheap.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laundryheap
- group: start
  title: ''
  type: SignUp
  url: https://app.laundryheap.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/laundryheap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/laundryheap-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/laundryheap-openid-configuration.json
- group: docs
  title: ''
  type: GraphQL
  url: graphql/laundryheap-graphql.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/laundryheap-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/laundryheap-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/laundryheap-services-response.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laundryheap-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-23'
description: Laundryheap is a London-founded on-demand laundry and dry-cleaning company that collects, cleans and returns clothing within 24 hours, operating across the United Kingdom, United States, Ireland, the Netherlands, Sweden, Denmark, the UAE, Qatar, Kuwait, Bahrain and Singapore. It serves consumers directly through iOS, Android and web apps, and businesses through hotel-affiliate, commercial laundry and dry-cleaning partner programmes. Laundryheap operates no developer portal and publishes no API documentation, but it does run a real, live, standards-clean OAuth 2.0 and OpenID Connect authorization server on its own root host — complete with PKCE, token introspection, token revocation and open dynamic client registration — advertising an `orders.create` scope, alongside a production GraphQL API of 69 fields and a small unauthenticated JSON endpoint that returns its service catalogue. The API surface is real and substantial; what is missing is any documentation of it.
image: https://prod-cdn.laundryheap.com/images/static/og_image.jpg
layout: provider
modified: '2026-08-23'
name: Laundryheap
nav: Providers
network: true
overview: 'Laundryheap publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Laundry, Dry Cleaning, On-Demand Services, and Logistics.


  Laundryheap''s developer surface includes pricing, support, engineering blog, signup flow, authentication, code examples, and 19 more developer resources.'
plans:
- name: Laundryheap Plans Pricing
  plan_count: 0
  slug: laundryheap-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Laundryheap Rate Limits
  slug: laundryheap-rate-limits
scopes:
- name: Laundryheap Scopes
  scope_count: 0
  slug: laundryheap-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 20.8
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 22.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laundryheap/refs/heads/main/screenshots/laundryheap-2026-09-02T150223.png
security:
- kind: authentication
  name: Laundryheap Authentication
  slug: laundryheap-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Laundryheap Domain Security
  slug: laundryheap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laundryheap
tags:
- Company
- Laundry
- Dry Cleaning
- On-Demand Services
- Logistics
- Last Mile Delivery
- Consumer Services
- Hospitality
- Ordering
- GraphQL
- Authentication
website: https://www.laundryheap.com/
---
