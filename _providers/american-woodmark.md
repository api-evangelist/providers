---
access_model:
  confidence: medium
  label: No public API access. Credentials for the identity provider and the Online Ordering portal are issued to dealers and trade customers out of band.
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://go.woodmark.com/onlineordering/orders
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: American Woodmark's OpenID Connect / OAuth 2.0 authorization server, an IdentityServer deployment that authenticates users of the company's dealer and customer applications including the Online Orderi
  name: American Woodmark Identity Provider
  slug: american-woodmark-identity
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.americanwoodmark.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-woodmark
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmericanWoodmark
- group: company
  title: ''
  type: Blog
  url: https://www.americanwoodmark.com/our-story/articles
- group: operate
  title: ''
  type: Support
  url: https://www.americanwoodmark.com/resources
- group: start
  title: ''
  type: Login
  url: https://go.woodmark.com/onlineordering/orders
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.americanwoodmark.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.americanwoodmark.com/terms-of-use
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/well-known/american-woodmark-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/american-woodmark-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/authentication/american-woodmark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/american-woodmark-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/scopes/american-woodmark-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/american-woodmark-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/conformance/american-woodmark-conformance.yml
  title: ''
  type: Conformance
  url: conformance/american-woodmark-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/packages/american-woodmark-packages.yml
  title: ''
  type: Packages
  url: packages/american-woodmark-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/llms/american-woodmark-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/american-woodmark-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/plans/american-woodmark-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/american-woodmark-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/rate-limits/american-woodmark-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/american-woodmark-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/finops/american-woodmark-finops.yml
  title: ''
  type: FinOps
  url: finops/american-woodmark-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/security/american-woodmark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-woodmark-domain-security.yml
created: '2026-04-19'
description: 'American Woodmark Corporation (NASDAQ: AMWD) is one of the largest manufacturers of kitchen, bath and home organization cabinetry in the United States, headquartered in Winchester, Virginia and operating manufacturing plants and service centers across the US and Mexico. It sells through home centers, homebuilders and independent dealers under brands including Timberlake, Waypoint Living Spaces, Shenandoah and 1951 Cabinetry. It is a manufacturer rather than a software vendor and runs no developer program: it publishes no API documentation, no OpenAPI, AsyncAPI, GraphQL or WSDL contract, and no SDKs. The only machine-readable contract it serves publicly is the OpenID Connect discovery document for its identity provider at id.woodmark.com, which fronts its dealer Online Ordering application. Trading-partner integration is conducted over ANSI ASC X12 EDI under bilateral trade agreements rather than through a public HTTP API.'
finops:
- name: American Woodmark Finops
  service_category: Building Products
  slug: american-woodmark-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-woodmark.png
layout: provider
modified: '2026-09-02'
name: American Woodmark
nav: Providers
network: true
overview: 'American Woodmark publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cabinetry, Home Products, Construction, Building Products, and Manufacturing.


  American Woodmark''s developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: American Woodmark Plans Pricing
  plan_count: 0
  slug: american-woodmark-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: American Woodmark Rate Limits
  slug: american-woodmark-rate-limits
scopes:
- name: American Woodmark Scopes
  scope_count: 0
  slug: american-woodmark-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/american-woodmark/refs/heads/main/screenshots/american-woodmark-2026-06-20T171920.png
security:
- kind: authentication
  name: American Woodmark Authentication
  slug: american-woodmark-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: American Woodmark Domain Security
  slug: american-woodmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: american-woodmark
tags:
- Cabinetry
- Home Products
- Construction
- Building Products
- Manufacturing
- Kitchen and Bath
- Home Improvement
- Identity
- EDI
- Supply Chain
website: https://www.americanwoodmark.com
---
