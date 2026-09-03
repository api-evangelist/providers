---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Device Specs Api Agentic Access
  operation_count: 4
  slug: device-specs-api-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://gsmarenaparser.p.rapidapi.com
  baseurl_source: declared
  description: The Values API from Device Specs API — 4 operation(s) for values.
  name: Device Specs API Values API
  slug: device-specs-api-values-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Device Specs Values API
  slug: open-device-specs-api-values-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
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
modified: '2026-08-09'
name: Device Specs API
nav: Providers
network: true
overview: 'Device Specs API publishes 1 API on the [APIs.io](https://apis.io/) network: Values API. Tagged areas include Mobile, Smartphones, Phone Specs, Chipsets, and Hardware.


  The Device Specs API catalog on APIs.io includes 1 Spectral governance ruleset.


  Device Specs API''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Device Specs Api Plans
  plan_count: 4
  slug: device-specs-api-plans
random_paper: 16
rate_limits:
- limit_count: 9
  name: Device Specs Api Rate Limits
  slug: device-specs-api-rate-limits
rules:
- effective_rule_count: 41
  extends:
  - spectral:oas
  name: Device Specs API API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: device-specs-api-spectral
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 49.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 51.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 34.2
  previous_composite: 57.2
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/device-specs-api/refs/heads/main/screenshots/device-specs-api-2026-08-17T080857.png
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
- Mobile
- Smartphones
- Phone Specs
- Chipsets
- Hardware
- mobile-specs
- Devices
- rapidapi
- gsmarena
- Reference Data
- Developer Tools
website: https://ds.gtgroup.dev/
---
