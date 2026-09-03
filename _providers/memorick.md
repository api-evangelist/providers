---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/memorick-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/memorick-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://memorick.com/register
- group: start
  title: ''
  type: Login
  url: https://memorick.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://memorick.com/terms
- group: company
  title: ''
  type: Website
  url: https://memorick.com
created: '2026-07-17'
description: Memorick is a 500 Global-backed company operating a live web application at memorick.com. Based on its observable application surface, it is a destination photography booking platform connecting customers with photographers across destinations, handling packages, orders, reviews, coupons, and messaging. The product is built on Laravel (Inertia.js single-page front end) and exposes an OAuth2 authorization server via Laravel Passport (authorize/token/clients/scopes plus personal access tokens), Sanctum first-party session auth, and optional two-factor authentication. It publishes no public API documentation, OpenAPI definition, SDKs, or developer portal at this time; the /api/* routes back the first-party application and are authentication-gated. This profile was enriched from live probing of the public surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/memorick.png
layout: provider
modified: '2026-07-20'
name: Memorick
nav: Providers
network: true
overview: 'Memorick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photography, Booking, Marketplace, and Travel.


  Memorick''s developer surface includes authentication, signup flow, and 4 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/memorick/refs/heads/main/screenshots/memorick-2026-08-07T172501.png
security:
- kind: authentication
  name: Memorick Authentication
  slug: memorick-authentication
  summary_line: oauth2/http · 4 schemes
- kind: domain-security
  name: Memorick Domain Security
  slug: memorick-domain-security
  summary_line: TLSv1.3
slug: memorick
tags:
- Company
- Photography
- Booking
- Marketplace
- Travel
- Photographers
- Authentication
- Laravel
website: https://memorick.com
---
