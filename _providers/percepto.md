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
api_count: 1
apis:
- description: 'The HTTP API behind the Percepto AIM (Autonomous Inspection and Monitoring) console at drones.percepto.co. The application is a Django/Django-REST-Framework deployment: /api/schema/ and /api/docs/ are'
  name: Percepto AIM API
  slug: percepto-aim-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/percepto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://percepto.co/
- group: company
  title: ''
  type: Blog
  url: https://percepto.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/perceptoDrones
- group: operate
  title: ''
  type: Support
  url: https://percepto.co/contact/
- group: start
  title: ''
  type: SignUp
  url: https://drones.percepto.co/loginview/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://percepto.co/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://percepto.co/your-drone-inspection-data-is-secure/
- group: build
  title: ''
  type: Packages
  url: packages/percepto-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/percepto-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/percepto-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/percepto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/percepto-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/percepto-llms.txt
coverage:
  checked: '2026-08-26'
  detail: The Percepto AIM console at drones.percepto.co serves a Django-REST-Framework API whose own schema and docs routes are live but customer-only — GET /api/schema/ and GET /api/docs/ each return 302 to /loginview/?next=..., so the machine-readable contract exists and is simply not readable without a Percepto tenant login.
  evidence:
  - status: 302
    url: https://drones.percepto.co/api/schema/
  - status: 302
    url: https://drones.percepto.co/api/docs/
  - status: 404
    url: https://percepto.co/llms.txt
  - status: 404
    url: https://percepto.co/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: 'Percepto is an Israeli-founded industrial autonomy company (founded 2014, offices in Modi''in, Israel and the United States) that builds drone-in-a-box hardware and the software that runs it. Its hardware line includes the Percepto Air Max and Air Mobile drones and the Percepto Base docking station, and its software product is Percepto AIM (Autonomous Inspection and Monitoring), a platform that plans and launches autonomous missions, ingests visual, thermal, optical-gas-imaging and 3D data from Percepto drones as well as third-party DJI drones and fixed cameras, and applies AI-driven analytics to produce inspection, monitoring, emergency-response and security insights for oil and gas, mining, electric utilities, solar, ports and heavy industry sites. Percepto holds FAA beyond-visual-line-of-sight (BVLOS) authorizations for automated industrial inspections and has raised approximately $138.6M. The Percepto AIM console is served at drones.percepto.co and exposes an HTTP API under
  /api/, but the API schema and API documentation routes both redirect anonymous callers to a customer login: Percepto publishes no public developer portal, no OpenAPI document and no public API reference.'
image: https://percepto.co/wp-content/uploads/2020/11/Percepto-AIM-robotics-illustration.png
layout: provider
modified: '2026-08-26'
name: Percepto
nav: Providers
network: true
overview: 'Percepto publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Drones, Robotics, Industrial Inspection, Autonomous Systems, and Computer-Vision.


  Percepto''s developer surface includes engineering blog, support, signup flow, and 11 more developer resources.'
plans:
- name: Percepto Plans Pricing
  plan_count: 0
  slug: percepto-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Percepto Rate Limits
  slug: percepto-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/percepto/refs/heads/main/screenshots/percepto-2026-09-02T151035.png
security:
- kind: domain-security
  name: Percepto Domain Security
  slug: percepto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: percepto
tags:
- Drones
- Robotics
- Industrial Inspection
- Autonomous Systems
- Computer-Vision
- Asset Monitoring
- Energy
- Oil and Gas
- Mining
- Utilities
- Israel
website: https://percepto.co/
---
