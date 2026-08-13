---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Device Specs Api Agentic Access
  operation_count: 4
  slug: device-specs-api-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: The Values API from Device Specs API — 4 operation(s) for values.
  name: Device Specs API Values API
  slug: device-specs-api-values-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/device-specs-api-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/device-specs-api-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ds.gtgroup.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://ds.gtgroup.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ds.gtgroup.dev/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://ds.gtgroup.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://ds.gtgroup.dev/blogs
- group: operate
  title: ''
  type: Support
  url: mailto:kupatadze2000@outlook.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GranTurismo
- group: commercial
  title: ''
  type: Pricing
  url: https://ds.gtgroup.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/device-specs-api-plans.yml
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/controller2042000/api/gsmarenaparser
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rapidapi.com/privacy
- group: other
  title: ''
  type: APIsJSON
  url: https://ds.gtgroup.dev/apis.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/device-specs-api-spectral.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/device-specs-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/device-specs-api-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/device-specs-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/device-specs-api-packages.yml
- group: build
  title: ''
  type: .NET SDK
  url: https://www.nuget.org/packages/DeviceSpecs
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@granturismo/devicespecs
- group: auth
  title: ''
  type: Authentication
  url: authentication/device-specs-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/device-specs-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/device-specs-api-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/device-specs-api-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/device-specs-api-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/device-specs-api-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/device-specs-api-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/device-specs-api-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://ds.gtgroup.dev/playground
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/device-specs-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/device-specs-api-domain-security.yml
created: '2026-07-27'
description: A normalized mobile-device specifications REST API covering 12,000+ smartphones and 10,000+ models from 50+ manufacturers, delivering cleaned, strictly typed JSON for chipsets, display metrics (size, panel type, refresh rate, peak nits), CPU cores and clock speeds, RAM and storage options, battery capacity and charging, camera counts and resolutions, physical dimensions and IP rating, sound, connectivity, AnTuTu/Geekbench benchmarks, retail pricing in USD/EUR/GBP and EU energy-label data (energy class, battery endurance, repairability). Four read-only GET operations plus a documented deep query filter engine ({property}_{operator}={value}) supporting eq, contains, in, has, gt, gte, lt, lte and between across roughly 25 property aliases. Built and maintained by GranTurismo Engineering, distributed and metered through the RapidAPI marketplace with a free BASIC tier.
image: https://ds.gtgroup.dev/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: device-specs-api-mcp.yml
  slug: device-specs-api-mcpyml
modified: '2026-08-09'
name: Device Specs API
nav: Providers
network: true
overview: 'Device Specs API publishes 1 API on the [APIs.io](https://apis.io/) network: Values API. Tagged areas include mobile, smartphones, phone-specs, chipsets, and hardware.


  The Device Specs API catalog on APIs.io includes 1 Spectral governance ruleset.


  Device Specs API''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Device Specs Api Plans
  plan_count: 4
  slug: device-specs-api-plans
random_paper: 10
rate_limits:
- limit_count: 9
  name: Device Specs Api Rate Limits
  slug: device-specs-api-rate-limits
rules:
- name: Device Specs API API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: device-specs-api-spectral
score:
  band: strong
  composite: 57.7
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 54.5
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 21.9
    operational_transparency: 36.8
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Device Specs Api Authentication
  slug: device-specs-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Device Specs Api Domain Security
  slug: device-specs-api-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: device-specs-api
tags:
- mobile
- smartphones
- phone-specs
- chipsets
- hardware
- mobile-specs
- devices
- rapidapi
- gsmarena
- reference-data
- developer-tools
website: https://ds.gtgroup.dev/
---
