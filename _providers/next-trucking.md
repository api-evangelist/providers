---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The service gateway behind NEXT''s ATLAS transportation management system and its shipper, carrier and managed-carrier portals. Twenty-nine service paths were enumerated from the ATLAS web application '
  name: NEXT ATLAS Platform API
  slug: next-atlas-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://nexttrucking.com/
- group: company
  title: ''
  type: About
  url: https://nexttrucking.com/company/
- group: operate
  title: ''
  type: Support
  url: https://nexttrucking.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://nexttrucking.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nexttrucking.com/feed/
- group: company
  title: ''
  type: Press
  url: https://nexttrucking.com/press/
- group: start
  title: ''
  type: SignUp
  url: https://nexttrucking.com/sign-up-hub/
- group: start
  title: ''
  type: Login
  url: https://app.nexttrucking.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nexttrucking.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nexttrucking.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NextDeveloperTeam
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/next-trucking
- group: auth
  title: ''
  type: Authentication
  url: authentication/next-trucking-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/next-trucking-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/next-trucking-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/next-trucking-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/next-trucking-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/next-trucking-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/next-trucking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/next-trucking-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/next-trucking-llms.txt
coverage:
  checked: '2026-08-26'
  detail: NEXT's ATLAS service gateway is live and serves the springdoc Swagger UI shell for 22 services, but the OpenAPI documents that UI is configured to load (/<service>/v3/api-docs) are unrouted at the gateway and every service path returns nginx "401 Authorization Required" to an anonymous caller, so the contract is generated and then withheld behind a shipper/carrier agreement.
  evidence:
  - status: 200
    url: https://svcs.us-west-2.prod.aws.nexttrucking.com/shippers/swagger-ui/index.html
  - status: 404
    url: https://svcs.us-west-2.prod.aws.nexttrucking.com/shippers/v3/api-docs
  - status: 401
    url: https://svcs.us-west-2.prod.aws.nexttrucking.com/shippers
  - status: 404
    url: https://nexttrucking.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: 'NEXT Trucking (branded "NEXT") is a FreightTech company founded in 2015 and headquartered in the Los Angeles area, operating a digital freight marketplace focused on drayage at the Ports of Los Angeles and Long Beach, plus transloading, full-truckload over-the-road and expedited (NEXTpedited) service. Its technology core is ATLAS, a proprietary transportation management system that carries a container from delivery-order ingestion through job creation, dispatch, billing and payout, and that connects shippers, carriers, terminals, yards and chassis providers. The company markets EDI and API connectivity alongside its shipper/carrier portals and driver mobile apps, but publishes no developer portal, no API reference and no machine-readable contract: its service gateway answers every anonymous request with HTTP 401. NEXT was acquired by Chicago-based digital freight broker CDL 1000 in February 2024; the nexttrucking.com brand, marketplace and applications remain live. Backers
  before the acquisition included Sequoia Capital, Brookfield Growth, GLP Capital and Mucker Capital.'
image: https://nexttrucking.com/wp-content/uploads/2023/04/NEXT.svg
layout: provider
modified: '2026-08-26'
name: NEXT Trucking
nav: Providers
network: true
overview: 'NEXT Trucking publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, Trucking, and Drayage.


  NEXT Trucking''s developer surface includes support, engineering blog, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Next Trucking Plans Pricing
  plan_count: 0
  slug: next-trucking-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Next Trucking Rate Limits
  slug: next-trucking-rate-limits
scopes:
- name: Next Trucking Scopes
  scope_count: 0
  slug: next-trucking-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/next-trucking/refs/heads/main/screenshots/next-trucking-2026-09-02T150750.png
security:
- kind: authentication
  name: Next Trucking Authentication
  slug: next-trucking-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Next Trucking Domain Security
  slug: next-trucking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: next-trucking
tags:
- Company
- Logistics
- Freight
- Trucking
- Drayage
- Supply Chain
- Transportation
- Marketplace
- Transportation Management
- Shipping
website: https://nexttrucking.com/
---
