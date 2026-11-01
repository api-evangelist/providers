---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The GraphQL API is Knowde's recommended primary programmatic interface to the platform — anything possible in the REST API is intended to also be possible in GraphQL. The reference is generated from t
  name: Knowde GraphQL API
  slug: knowde-graphql-api
- description: The Knowde REST API is organized around RESTful resources with predictable resource-oriented URLs, JSON-encoded payloads and responses, and standard HTTP verbs and status codes. Resources include prod
  name: Knowde REST API
  slug: knowde-rest-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/knowde/rate-limits/knowde-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knowde-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/knowde/lifecycle/knowde-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/knowde-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/knowde/hosts/knowde-hosts.yml
  title: ''
  type: Hosts
  url: hosts/knowde-hosts.yml
- group: other
  href: https://artifacts.apis.io/knowde/vendors/knowde-vendors.yml
  title: ''
  type: Vendors
  url: vendors/knowde-vendors.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.knowde.com/feed/
- group: auth
  href: https://artifacts.apis.io/knowde/security/knowde-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knowde-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/knowde/security/knowde-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knowde-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.knowde.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.knowde.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.knowde.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.knowde.com/documentation/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.knowde.com/documentation/api_clients
- group: auth
  href: https://artifacts.apis.io/knowde/authentication/knowde-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knowde-authentication.yml
- group: design
  href: https://artifacts.apis.io/knowde/conventions/knowde-conventions.yml
  title: ''
  type: Conventions
  url: conventions/knowde-conventions.yml
- group: design
  href: https://artifacts.apis.io/knowde/conformance/knowde-conformance.yml
  title: ''
  type: Conformance
  url: conformance/knowde-conformance.yml
- group: design
  href: https://artifacts.apis.io/knowde/lifecycle/knowde-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/knowde-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/knowde/sandbox/knowde-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/knowde-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.knowde.com/documentation/rate_limits
- group: start
  title: ''
  type: SignUp
  url: https://www.knowde.com/sign-in
- group: start
  title: ''
  type: Login
  url: https://www.knowde.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privacy.knowde.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.knowde.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.knowde.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.knowde.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knowde
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knowde.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.knowde.com/
- group: operate
  href: https://artifacts.apis.io/knowde/changelog/knowde-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/knowde-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.knowde.com/resources/whats-new
- group: other
  title: ''
  type: Marketplace
  url: https://www.knowde.com/marketplace
- group: company
  title: ''
  type: Partners
  url: https://www.knowde.com/partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knowde/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/knowde
coverage:
  checked: '2026-10-19'
  detail: Knowde's GraphQL and REST references on developer.knowde.com now redirect to the www.knowde.com sign-in page, and developer-api.knowde.com answers 401/403 anonymously, so no contract can be read or generated; only the auth, API clients, PIMS filters and rate-limits pages remain public.
  evidence:
  - status: 403
    url: https://developer.knowde.com/documentation/rest
  - status: 401
    url: https://developer-api.knowde.com/graphql
  - status: 403
    url: https://developer-api.knowde.com/openapi.json
  - status: 200
    url: https://developer.knowde.com/documentation/rate_limits
  reason: customer-only-docs
  state: gated
created: '2026-08-01'
description: Knowde is an AI platform for industrial operations, built for the chemicals and ingredients industry. Knowde AI extracts, structures, harmonizes and enriches product data out of legacy systems and offline documents; Knowde MDM is the master data repository that data lands in; Knowde CXP launches supplier storefronts natively integrated with MDM; and the Knowde Marketplace is a network of 8,000+ chemical company storefronts. The Knowde API gives customers programmatic access to that platform through a GraphQL API (the recommended primary interface) and a RESTful JSON API, both served from developer-api.knowde.com behind OAuth 2.0 client credentials, with API Clients provisioned in the Developer Portal and a documented PIMS filter grammar for querying product, category and attribute data.
image: https://cdn.cxp.knowde.com/store/15d89a6e-1b0d-4b12-9ae9-06ae9d224a7b/knowde-logo_0b24070d06cb.svg
layout: provider
modified: '2026-10-06'
name: Knowde
nav: Providers
network: true
overview: 'Knowde is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemicals, Ingredients, Marketplace, and Master Data Management.


  Knowde''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, signup flow, support, and 26 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 1
  name: Knowde Rate Limits
  slug: knowde-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.1
    operational_transparency: 65.8
  previous_composite: 42.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/knowde/knowde-2026-08-07T171300.png
security:
- kind: authentication
  name: Knowde Authentication
  slug: knowde-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Knowde Domain Security
  slug: knowde-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Knowde Trust Center
  slug: knowde-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: knowde
tags:
- Company
- Chemicals
- Ingredients
- Marketplace
- Master Data Management
- Product Information Management
- Manufacturing
- Distribution
- B2B Commerce
- GraphQL
- Artificial Intelligence
website: https://www.knowde.com/
---
