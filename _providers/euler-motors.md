---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/euler-motors-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eulermotors.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.eulermotors.com/en/blogs/
- group: company
  title: ''
  type: News
  url: https://www.eulermotors.com/en/news/
- group: operate
  title: ''
  type: Support
  url: https://www.eulermotors.com/en/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eulermotors.com/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eulermotors.com/en/policy/
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.eulermotors.com/en/refund/
- group: company
  title: ''
  type: About
  url: https://www.eulermotors.com/en/about-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eulermotors/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/EulerMotors
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/euler-motors-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Euler Motors ships connected-vehicle software only as end-user products — the Shepherd Lite mobile app and the login-gated Shepherd Enterprise fleet console — and publishes no developer portal, API reference, OpenAPI/GraphQL/AsyncAPI specification, SDK or webhook catalog on any of its hosts; the Shepherd console's own backend is a private AWS API Gateway deployment that answers anonymous requests with 403 Forbidden.
  evidence:
  - status: 200
    url: https://www.eulermotors.com/en/vehicle-intelligence/
  - status: 404
    url: https://shepherd.eulermotors.com/openapi.json
  - status: 403
    url: https://www.eulermotors.com/.well-known/security.txt
  - status: 200
    url: https://www.eulermotors.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'Euler Motors is an Indian electric commercial vehicle manufacturer headquartered in New Delhi, building battery-electric cargo and light commercial vehicles for last-mile logistics — the HiLoad and Turbo electric three-wheelers and the Storm EV four-wheeler light commercial vehicle range. Alongside the vehicles the company operates Euler Shepherd, a connected-vehicle telematics platform delivered as two end-user products: Shepherd Lite (a mobile app for real-time vehicle location, battery state of charge, range, charging status and alerts) and Shepherd Enterprise (a browser-based fleet console with trip, utilization and operations reporting). Euler Motors publishes no public developer program: there is no developer portal, API reference, OpenAPI/AsyncAPI specification, SDK, webhook catalog or partner integration documentation on any host it controls. The Shepherd web console is a single-page application whose backend answers anonymous requests with 403, so the telematics data
  surface is reachable only to vehicle owners inside the product. The company does publish an llms.txt at its web root, directing AI crawlers to its product, service-network and blog pages.'
image: https://www.eulermotors.com/euler_white_logo.png
layout: provider
modified: '2026-08-12'
name: Euler Motors
nav: Providers
network: true
overview: 'Euler Motors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Electric Vehicles, Commercial Vehicles, and Logistics.


  Euler Motors'' developer surface includes engineering blog, product news, support, YouTube channel, and 8 more developer resources.'
plans:
- name: Euler Motors Plans Pricing
  plan_count: 0
  slug: euler-motors-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Euler Motors Rate Limits
  slug: euler-motors-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/euler-motors/refs/heads/main/screenshots/euler-motors-2026-09-02T145423.png
security:
- kind: domain-security
  name: Euler Motors Domain Security
  slug: euler-motors-domain-security
  summary_line: TLSv1.3 · DMARC
slug: euler-motors
tags:
- Company
- Automotive
- Electric Vehicles
- Commercial Vehicles
- Logistics
- Telematics
- Fleet Management
- Transportation
- Manufacturing
- India
website: https://www.eulermotors.com/en/
---
