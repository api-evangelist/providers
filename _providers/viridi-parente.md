---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://vista.viridiparente.com
  baseurl_source: declared
  description: The REST API of ViSTA (Viridi Insights), Viridi's energy management and IIoT platform. ViSTA is a Viridi-operated deployment of the open-source ThingsBoard IoT platform (v3.7.0) served from vista.viri
  name: Viridi ViSTA Platform API
  slug: viridi-parente-vista
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/viridi-parente-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/viridi-parente-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://viridiparente.com/
- group: docs
  title: ''
  type: Documentation
  url: https://viridiparente.com/products/iiot-intelligent-solution/
- group: docs
  title: ''
  type: APIReference
  url: https://vista.viridiparente.com/swagger-ui/index.html
- group: start
  title: ''
  type: SignUp
  url: https://viridiparente.com/create-a-vista-account/
- group: company
  title: ''
  type: Blog
  url: https://viridiparente.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://viridiparente.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://viridiparente.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ViridiParente
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viridiparente.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viridiparente.com/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://viridiparente.com/faq/
- group: design
  title: ''
  type: Conventions
  url: conventions/viridi-parente-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/viridi-parente-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/viridi-parente-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/viridi-parente-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/viridi-parente-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/viridi-parente-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/viridi-parente-vista-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/viridi-parente-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/viridi-parente-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/viridi-parente-mcp.yml
created: '2026-09-04'
description: Viridi (Viridi Parente, Inc.) is a Buffalo, New York manufacturer of fail-safe, modular lithium-ion battery energy storage systems (RPS150, RPS50, RPSLink IN/EX, SBR30, FAVEO and the 1.2 MWh series) built around its Anti-Propagation technology for installation in occupied spaces. Its software side is ViSTA / Viridi Insights, an energy management and IIoT platform pairing a data-visualization engine with a Conductor edge computing platform, connecting behind-the-meter equipment over BACnet, Modbus, CANbus, DNP3 and serial links for remote monitoring, peak shaving and demand response. ViSTA runs a Viridi-branded ThingsBoard deployment at vista.viridiparente.com that serves an anonymously readable OpenAPI 3.1 contract and carries Viridi-authored controllers for SBR30 telemetry, generator and chiller data, CBRS device management and Moxion AEMP equipment telematics.
image: https://viridiparente.com/wp-content/uploads/viridi-featured-image-2023.jpg
layout: provider
modified: '2026-09-04'
name: Viridi
nav: Providers
network: true
overview: 'Viridi publishes 1 API on the [APIs.io](https://apis.io/) network: ViSTA Platform API. Tagged areas include Company, Energy, Energy Storage, Battery, and IoT.


  Viridi''s developer surface includes authentication, documentation, API reference, signup flow, engineering blog, support, FAQ, and 17 more developer resources.'
plans:
- name: Viridi Parente Plans Pricing
  plan_count: 0
  slug: viridi-parente-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Viridi Parente Rate Limits
  slug: viridi-parente-rate-limits
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.0
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Viridi Parente Authentication
  slug: viridi-parente-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Viridi Parente Domain Security
  slug: viridi-parente-domain-security
  summary_line: TLSv1.3 · DMARC
slug: viridi-parente
tags:
- Company
- Energy
- Energy Storage
- Battery
- IoT
- Industrial IoT
- Energy Management
- Manufacturing
- Telematics
- Microgrid
website: https://viridiparente.com/
---
