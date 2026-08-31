---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brelyon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brelyon.com/
- group: operate
  title: ''
  type: Support
  url: https://www.brelyon.com/support-2/support/
- group: company
  title: ''
  type: Blog
  url: https://www.brelyon.com/news/
- group: start
  title: ''
  type: SignUp
  url: https://www.brelyon.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://www.brelyon.com/log-in/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brelyon.com/order-page/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brelyon
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC9wRknKRClTLuYaEk-LeMmg
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brelyon-llms.txt
coverage:
  checked: '2026-08-08'
  detail: Brelyon sells headset-free display hardware plus end-user desktop software (Brelyon Suite, Focal Studio, Visual Engine) and publishes no developer surface at all — brelyon.com/api, /docs and /developers all 404, api./docs./developer./mcp.brelyon.com do not resolve, and the only machine-readable endpoint on the domain is the WordPress core + WooCommerce REST index at /wp-json/, which is the marketing CMS rather than a product API.
  evidence:
  - status: 404
    url: https://www.brelyon.com/developers
  - status: 404
    url: https://www.brelyon.com/api
  - status: 404
    url: https://www.brelyon.com/openapi.json
  - status: 404
    url: https://www.brelyon.com/.well-known/agent-card.json
  - status: 200
    url: https://www.brelyon.com/llms.txt
  - status: 200
    url: https://www.brelyon.com/wp-json/
  reason: no-developer-program
  state: none
created: '2026-08-08'
description: Brelyon is an MIT Media Lab spin-off building headset-free virtual displays — desktop monitors that use electro-optics and computational rendering to produce monocular image depth rather than autostereoscopic 3D. Its Ultra Reality line delivers a 122-inch virtual screen filling roughly 110 degrees of field of view, alongside Ultra Reality Extend (a multi-focal monitor that renders AI-generated overlays at different depths), Ultra Reality Mini, and experimental Hyper Displays. The company is headquartered in San Mateo, California with an international office in Taichung, Taiwan, and sells into enterprise simulation, training, teleoperation and medical visualization; prosumer flight simulation, gaming, trading and content production; and automotive in-vehicle HMI integration. Brelyon ships desktop software (Brelyon Suite, Focal Studio, Visual Engine, Stream Weaver) for distortion correction, monitor merging and multi-focal content creation, but publishes no public developer program,
  API, or SDK.
image: https://www.brelyon.com/wp-content/themes/brelyon-0430_2026/assets/images/blue-logo.svg
layout: provider
modified: '2026-08-08'
name: Brelyon
nav: Providers
network: true
overview: 'Brelyon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Displays, Hardware, Immersive Technology, and Virtual Reality.


  Brelyon''s developer surface includes support, engineering blog, signup flow, pricing, YouTube channel, and 5 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.9
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Brelyon Domain Security
  slug: brelyon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brelyon
tags:
- Company
- Displays
- Hardware
- Immersive Technology
- Virtual Reality
- Simulation and Training
- Automotive HMI
- Optics
- Visualization
website: https://www.brelyon.com/
---
