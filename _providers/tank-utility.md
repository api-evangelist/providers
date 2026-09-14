---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://data.tankutility.com/api
  baseurl_source: declared
  description: Exchange account credentials for a short-lived API token.
  name: Tank Utility Authentication API
  slug: tank-utility-authentication-api
- baseURL: https://data.tankutility.com/api
  baseurl_source: declared
  description: List and read propane tank monitor devices.
  name: Tank Utility Devices API
  slug: tank-utility-devices-api
arazzos:
- description: Authenticate to the Tank Utility API, list the propane monitors on the account, and read the latest reading (fuel level %, temperature) for the first device.
  name: Tank Utility — read propane tank level
  slug: tank-utility-read-tank-level
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tank Utility Propane Monitor Authentication API
  slug: open-tank-utility-authentication-api
- collection_type: open
  name: Tank Utility Propane Monitor Authentication Devices API
  slug: open-tank-utility-devices-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tank-utility-mcp.yml
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


  Tank Utility''s developer surface includes authentication, CLI, support, engineering blog, and 16 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/tank-utility/refs/heads/main/screenshots/tank-utility-2026-09-02T162519.png
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
