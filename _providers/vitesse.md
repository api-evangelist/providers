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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 4.7
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://vitesseautomation.com
- group: start
  title: ''
  type: SignUp
  url: https://app.vitesse.dev
- group: operate
  title: ''
  type: Support
  url: https://vitesseautomation.com/contact
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vitesse-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vitesse-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/vitesse-robots.txt
coverage:
  checked: '2026-08-17'
  detail: Vitesse ships its physical-AI automation platform only as an end-user product — a login-gated React application at app.vitesse.dev plus on-premise edge controllers — and its eight-URL sitemap contains no docs, API, developer or pricing page at all; the two product backends found in the app bundle (fleet.vitesse.dev, conversations.vitesse.dev) publish no specification and return the identical status for a nonsense control path as for every real one, so no developer API is marketed, documented, or provably present.
  evidence:
  - status: 404
    url: https://vitesseautomation.com/developers
  - status: 404
    url: https://vitesseautomation.com/docs
  - status: 200
    url: https://vitesseautomation.com/sitemap.xml
  - status: 404
    url: https://fleet.vitesse.dev/openapi.json
  - status: 401
    url: https://conversations.vitesse.dev/openapi.json
  - status: 404
    url: https://vitesseautomation.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Vitesse is a universal physical-AI platform for industrial machines, founded by the team behind Tesla's "Model 3 automation hell" fix alongside leaders from SpaceX, Siemens, and Safran. It connects any machine - Siemens, Allen-Bradley, Fanuc, KUKA, ABB, and legacy PLCs - through 135 native OT connectors, generates control logic from a natural-language description of a process (up to 15x faster than traditional PLC programming), and runs the full stack at the edge on purpose-built industrial controllers with no cloud required. The platform layers hardware, live data dashboards and SCADA views, interoperability, physical AI, and zero-trust OT/IT cybersecurity (NIS2 and NIST aligned) into one stack, with real-time browser-based monitoring across 800,000+ machine hours. The company traded as Full Speed Automation and renamed to Vitesse Automation after acquiring Niagara Tech; the legacy fullspeedautomation.com domain no longer resolves over TLS. Vitesse exposes a marketing website
  and a login-gated product application at app.vitesse.dev; as of August 2026 it publishes no public developer API, OpenAPI/AsyncAPI/GraphQL specification, SDK, webhooks, developer portal, or pricing page, and serves no /.well-known discovery documents.
image: https://vitesseautomation.com/images/og-image.jpg
layout: provider
modified: '2026-08-17'
name: Vitesse
nav: Providers
network: true
overview: 'Vitesse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Physical AI, Industrial Automation, Operational Technology, and Manufacturing.


  Vitesse''s developer surface includes signup flow, support, and 4 more developer resources.'
plans:
- name: Vitesse Plans Pricing
  plan_count: 0
  slug: vitesse-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Vitesse Rate Limits
  slug: vitesse-rate-limits
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Vitesse Domain Security
  slug: vitesse-domain-security
  summary_line: TLSv1.3
slug: vitesse
tags:
- Company
- Physical AI
- Industrial Automation
- Operational Technology
- Manufacturing
- IoT
- Edge Computing
- SCADA
- PLC
- Robotics
- Cybersecurity
- Interoperability
website: https://vitesseautomation.com
---
