---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  score: 11.9
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The production Avarra API, served from api.avarra.ai behind an AWS application load balancer. Every path under /v1/ is protected and returns a JSON 401 envelope without a bearer token; tokens are issu
  name: Avarra API
  slug: avarra-api
artifact_total: 5
common:
- group: auth
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
- group: auth
  title: ''
  type: Authentication
  url: authentication/avarra-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avarra-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/avarra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/avarra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/avarra-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/avarra-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/avarra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/avarra-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avarra-llms.txt
created: '2026-07-17'
description: 'Avarra is an AI-powered sales training and enablement platform, operated by Ramp Systems, Inc., that helps revenue teams onboard, coach, and certify sales representatives at scale. The platform turns real sales conversations into AI-avatar role-play simulations delivered over Zoom, gives reps unlimited practice reps with instant coaching feedback, standardizes sales methodology across teams and regions, and reports certification and performance analytics through manager dashboards. Its workflow moves through five stages: Capture, Train, Practice, Certify, and Performance Insights, with the stated goal of cutting new-hire ramp time in half. Avarra is a Lightspeed Venture Partners portfolio company that exited stealth with $8M in seed funding. Avarra runs a production API at api.avarra.ai that publishes RFC 8414 OAuth 2.0 authorization server metadata and an RFC 7517 JWKS anonymously, but the entire /v1 resource surface is closed behind OAuth 2.0 client-credentials access and
  the company publishes no OpenAPI, developer portal, API reference, SDKs, or pricing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avarra.png
layout: provider
modified: '2026-08-14'
name: Avarra
nav: Providers
network: true
overview: 'Avarra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Enablement, Sales Training, Artificial Intelligence, and Coaching.


  Avarra''s developer surface includes signup flow, support, engineering blog, authentication, and 14 more developer resources.'
plans:
- name: Avarra Plans Pricing
  plan_count: 0
  slug: avarra-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Avarra Rate Limits
  slug: avarra-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avarra/refs/heads/main/screenshots/avarra-2026-07-25T201910.png
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
