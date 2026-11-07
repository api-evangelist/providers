---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - authentication
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The production Avarra API, served from api.avarra.ai behind an AWS application load balancer. Every path under /v1/ is protected and returns a JSON 401 envelope without a bearer token; tokens are issu
  name: Avarra API
  slug: avarra-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/avarra/lifecycle/avarra-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/avarra-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/avarra/hosts/avarra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avarra-hosts.yml
- group: other
  href: https://artifacts.apis.io/avarra/vendors/avarra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avarra-vendors.yml
- group: auth
  href: https://artifacts.apis.io/avarra/security/avarra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avarra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avarra.ai
- group: start
  title: ''
  type: SignUp
  url: https://www.avarra.ai/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.avarra.ai/login
- group: operate
  title: ''
  type: Support
  url: mailto:support@avarra.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avarra.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.avarra.ai/product
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avarra.ai/msa
- group: company
  title: ''
  type: Blog
  url: https://www.avarra.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.avarra.ai
- group: agent
  href: https://artifacts.apis.io/avarra/well-known/avarra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avarra-well-known.yml
- group: design
  href: https://artifacts.apis.io/avarra/conventions/avarra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/avarra-conventions.yml
- group: design
  href: https://artifacts.apis.io/avarra/lifecycle/avarra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/avarra-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/avarra/conformance/avarra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avarra-conformance.yml
- group: operate
  href: https://artifacts.apis.io/avarra/rate-limits/avarra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avarra-rate-limits.yml
coverage:
  checked: '2026-10-20'
  detail: api.avarra.ai serves anonymous OAuth metadata and a JWKS, but every /v1 resource returns a JSON 401, no OpenAPI or docs are published, and access runs through the request-a-demo form.
  evidence:
  - status: 200
    url: https://api.avarra.ai/.well-known/oauth-authorization-server
  - status: 404
    url: https://www.avarra.ai/pricing
  - status: 200
    url: https://www.avarra.ai/request-a-demo
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'Avarra is an AI-powered sales training and enablement platform, operated by Ramp Systems, Inc., that helps revenue teams onboard, coach, and certify sales representatives at scale. The platform turns real sales conversations into AI-avatar role-play simulations delivered over Zoom, gives reps unlimited practice reps with instant coaching feedback, standardizes sales methodology across teams and regions, and reports certification and performance analytics through manager dashboards. Its workflow moves through five stages: Capture, Train, Practice, Certify, and Performance Insights, with the stated goal of cutting new-hire ramp time in half. Avarra is a Lightspeed Venture Partners portfolio company that exited stealth with $8M in seed funding. Avarra runs a production API at api.avarra.ai that publishes RFC 8414 OAuth 2.0 authorization server metadata and an RFC 7517 JWKS anonymously, but the entire /v1 resource surface is closed behind OAuth 2.0 client-credentials access and
  the company publishes no OpenAPI, developer portal, API reference, SDKs, or pricing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avarra.png
layout: provider
modified: '2026-08-14'
name: Avarra
nav: Providers
network: true
overview: 'Avarra is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Enablement, Sales Training, Artificial Intelligence, and Coaching.


  Avarra''s developer surface includes signup flow, support, engineering blog, and 15 more developer resources.'
plans:
- name: Avarra Plans Pricing
  plan_count: 0
  slug: avarra-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Avarra Rate Limits
  slug: avarra-rate-limits
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 66.1
    operational_transparency: 15.8
  previous_composite: 22.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/avarra/avarra-2026-07-25T201910.png
security:
- kind: authentication
  name: Avarra Authentication
  slug: avarra-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Avarra Domain Security
  slug: avarra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avarra
tags:
- Company
- Sales Enablement
- Sales Training
- Artificial Intelligence
- Coaching
- Role-Play Simulation
- Revenue Operations
- Onboarding
- Sales Readiness
- Conversation Intelligence
website: https://www.avarra.ai
---
