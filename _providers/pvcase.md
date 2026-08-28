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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Beta REST API for PVcase Prospect, published as the "Anderson Optimization API" (OpenAPI 3.0.3, version 1.0.0-beta) in the PVcase Prospect documentation. It exposes teams, companies, projects and geos
  name: PVcase Prospect API (Anderson Optimization API)
  slug: pvcase-prospect-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/pvcase-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pvcase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pvcase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pvcase-prospect.gitbook.io/pvcase-prospect-user-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://pvcase-prospect.gitbook.io/pvcase-prospect-user-documentation/prospect/advanced-tools/api-future-offering/api-reference-future-offering
- group: start
  title: ''
  type: GettingStarted
  url: https://pvcase-prospect.gitbook.io/pvcase-prospect-user-documentation/prospect/advanced-tools/api-future-offering/quick-start-future-offering
- group: operate
  title: ''
  type: Support
  url: https://help.pvcase.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.pvcase.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://pvcase.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pvcase.com/pricing-plans
- group: start
  title: ''
  type: SignUp
  url: https://prospect.pvcase.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pvcase.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://pvcase.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://pvcase.com/trust-center
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pvcase-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/pvcase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pvcase-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pvcase-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pvcase-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pvcase-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pvcase-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pvcase-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pvcase-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/pvcase-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pvcase-anderson-optimization-overlay.yaml
created: '2026-08-26'
description: 'PVcase is a Lithuanian solar engineering software company building an end-to-end platform for utility-scale and commercial photovoltaic project development, covering site prospecting, land and grid screening, ground-mount and roof-mount PV layout design, terrain-aware engineering and energy yield simulation. Its product family includes PVcase Prospect (site selection, parcel and landowner data, interconnection capacity and buildable-area analysis, built on the Anderson Optimization platform it acquired in June 2023), PVcase Ground Mount and Roof Mount (AutoCAD-based PV layout design), and PVcase Yield (energy simulation). The developer surface is narrow and early: a beta REST API for PVcase Prospect, documented under "Advanced tools" in the Prospect GitBook documentation as an Anderson Optimization API with an OpenAPI 3.0.3 description covering teams, projects and geospatial assets, offered to enterprise customers alongside a read-only WMS layer and SSO.'
image: https://pvcase.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: PVcase
nav: Providers
network: true
overview: 'PVcase publishes 1 API on the [APIs.io](https://apis.io/) network: Prospect API (Anderson Optimization API). Tagged areas include Solar, Energy, Renewable Energy, Photovoltaic, and Geospatial.


  PVcase''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Pvcase Plans Pricing
  plan_count: 3
  slug: pvcase-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Pvcase Rate Limits
  slug: pvcase-rate-limits
score:
  band: developing
  composite: 49.1
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 12.1
    contract_quality: 48.3
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 12.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 35.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Pvcase Authentication
  slug: pvcase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pvcase Domain Security
  slug: pvcase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pvcase Vulnerability Disclosure
  slug: pvcase-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Pvcase Trust Center
  slug: pvcase-trust-center
  summary_line: SOC 2 Type I, SOC 2 Type II, SOC 3
slug: pvcase
tags:
- Solar
- Energy
- Renewable Energy
- Photovoltaic
- Geospatial
- Site Selection
- Engineering Design
- Simulation
- Project Development
- CAD
website: https://pvcase.com/
---
