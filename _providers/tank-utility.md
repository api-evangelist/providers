---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 39.4
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: Exchange account credentials for a short-lived API token.
  name: Tank Utility Authentication API
  slug: tank-utility-authentication-api
- description: List and read propane tank monitor devices.
  name: Tank Utility Devices API
  slug: tank-utility-devices-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Authenticate to the Tank Utility API, list the propane monitors on the account, and read the latest reading (fuel level %, temperature) for the first device.
  name: Tank Utility — read propane tank level
  slug: tank-utility-read-tank-level
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tank-utility-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tank-utility-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tank-utility-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tank-utility-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tank-utility-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tank-utility-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tank-utility-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/tank-utility-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tank-utility-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tank-utility-devices-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tank-utility-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/tank-utility-read-tank-level.yml
- group: operate
  title: ''
  type: Support
  url: https://support.tankutility.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://tankutility.com/blog/
- group: start
  title: ''
  type: Login
  url: https://portal.tankutility.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tankutility.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anova.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://tankutility.com
created: '2026-07-17'
description: Tank Utility makes LTE-connected propane tank monitors, mobile apps, and a read-only API that surface their data. Its sensors report tank fuel level, temperature, and battery state so homeowners get low-fuel alerts and fuel marketers can route deliveries by real consumption instead of guesswork — Tank Utility says this drops the same gallons in up to 40% fewer deliveries. The Tank Utility API lets an account exchange credentials (HTTP Basic) for a short-lived token, list the monitors on the account, and read each device's latest reading. Tank Utility is owned by Anova.
image: https://tankutility.com/wp-content/uploads/2025/06/logo_merge.png
layout: provider
modified: '2026-07-21'
name: Tank Utility
nav: Providers
network: true
overview: 'Tank Utility publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Devices API. Tagged areas include Propane, Tank Monitoring, IoT, Fuel Delivery, and Telemetry.


  Tank Utility''s developer surface includes authentication, CLI, support, engineering blog, and 15 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.9
    developer_ergonomics: 30.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 37.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Tank Utility Authentication
  slug: tank-utility-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tank Utility Domain Security
  slug: tank-utility-domain-security
  summary_line: TLSv1.3
slug: tank-utility
tags:
- Propane
- Tank Monitoring
- IoT
- Fuel Delivery
- Telemetry
- Energy
- Sensors
- Company
website: https://tankutility.com
---
